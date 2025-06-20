from django.shortcuts import render, redirect, get_object_or_404
from .models import Asset, Price, PortfolioWeight
from datetime import date
import numpy as np
import requests
import yfinance as yf

# API_KEY = 'c1dc02a0c7f64cca8608fb2b98abcea1'

# Show latest portfolio weights
def index(request):
    assets = Asset.objects.all()
    prices = {}
    today = date.today()
    for asset in assets:
        price_obj = Price.objects.filter(asset=asset, date=today).first()
        prices[asset.symbol] = price_obj.close if price_obj else None

    latest_weights = None

    # If the user submitted the capital form, run ONS and get new weights
    if request.GET.get('capital') and assets.count() > 1:
        # Gather historical prices for each asset
        price_lists = []
        for asset in assets:
            prices_qs = Price.objects.filter(asset=asset).order_by('date').values_list('close', flat=True)
            prices_list = list(prices_qs)
            price_lists.append(prices_list)

        # Make sure all assets have the same number of price points
        min_len = min(len(p) for p in price_lists)
        if min_len > 1:
            price_matrix = np.array([p[-min_len:] for p in price_lists]).T  # shape: (time, assets)
            returns = price_matrix[1:] / price_matrix[:-1]

            # ONS parameters
            n_assets = len(assets)
            eta = 0.5
            delta = 0.125
            w = np.ones(n_assets) / n_assets
            A = delta * np.identity(n_assets)

            # Run ONS across all return vectors
            for x in returns:
                grad = -x / np.dot(w, x)
                A += np.outer(grad, grad)
                w -= eta * np.linalg.inv(A).dot(grad)
                w = np.maximum(w, 0)
                w /= np.sum(w)  # Normalize

            # Use the weights for the current recommendation (do not save to DB)
            latest_weights = type('obj', (object,), {
                'weights': {asset.symbol: round(w[i], 4) for i, asset in enumerate(assets)}
            })()
    else:
        # Fallback: show latest saved weights if available
        latest_weights = PortfolioWeight.objects.order_by('-date').first()

    return render(request, 'onsapp/index.html', {
        'assets': assets,
        'prices': prices,
        'latest_weights': latest_weights,
    })


# Add new asset
def add_asset(request):
    if request.method == 'POST':
        name = request.POST['name']
        symbol = request.POST['symbol']
        asset = Asset.objects.create(name=name, symbol=symbol)
        
        # Fetch and save price
        price = fetch_price(symbol)
        if price:
            Price.objects.create(asset=asset, date=date.today(), close=price)
        
        return redirect('index')
    return render(request, 'onsapp/add_asset.html')


# Fetch live price for a given symbol
def fetch_price(symbol):
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d")
        if not data.empty:
            price = data['Close'].iloc[-1]
            print(f"Fetched price for {symbol}: {price}")
            return float(price)
        else:
            print(f"No price data for {symbol}")
            return None
    except Exception as e:
        print(f"Error fetching price for {symbol}: {e}")
        return None


# Update prices for all assets
def update_prices(request):
    today = date.today()
    for asset in Asset.objects.all():
        price = fetch_price(asset.symbol)
        if price:
            Price.objects.update_or_create(asset=asset, date=today, defaults={'close': price})
    return redirect('index')


# Execute ONS algorithm and store portfolio weights
def execute_ons(request):
    assets = list(Asset.objects.all())
    if not assets:
        return redirect('index')

    # Collect historical prices for each asset
    asset_prices = []
    for asset in assets:
        prices = list(Price.objects.filter(asset=asset).order_by('date').values_list('close', flat=True))
        if len(prices) < 2:
            return redirect('index')  # Require at least 2 data points
        asset_prices.append(prices)

    # Transpose so each row is a time step, each column an asset
    price_matrix = np.array(asset_prices).T

    # Calculate returns: r[t] = p[t] / p[t-1]
    returns = price_matrix[1:] / price_matrix[:-1]

    # ONS parameters
    n_assets = len(assets)
    eta = 0.5
    delta = 0.125
    w = np.ones(n_assets) / n_assets
    A = delta * np.identity(n_assets)

    # Run ONS across all return vectors
    for x in returns:
        grad = -x / np.dot(w, x)
        A += np.outer(grad, grad)
        w -= eta * np.linalg.inv(A).dot(grad)
        w = np.maximum(w, 0)
        w /= np.sum(w)  # Normalize

    # Save today's portfolio weights
    PortfolioWeight.objects.create(
        date=date.today(),
        weights={asset.symbol: round(w[i], 4) for i, asset in enumerate(assets)}
    )

    # Rebuild prices dict for today
    prices = {}
    today = date.today()
    for asset in assets:
        price_obj = Price.objects.filter(asset=asset, date=today).first()
        prices[asset.symbol] = price_obj.close if price_obj else None

    latest_weights = PortfolioWeight.objects.order_by('-date').first()
    return render(request, 'onsapp/index.html', {
        'assets': assets,
        'prices': prices,
        'latest_weights': latest_weights,
    })


# Delete an asset
def delete_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    if request.method == 'POST':
        asset.delete()
    return redirect('index')


# Clear all portfolio weight recommendations
def clear_recommendations(request):
    if request.method == 'POST':
        PortfolioWeight.objects.all().delete()
    return redirect('index')

