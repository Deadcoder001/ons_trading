
# ONS trading

**ONS Trading** is a web-based portfolio management tool designed for investors and traders who want to optimize their investments using AI-powered allocation and real-time market data.  
It allows users to:

- Add and manage assets from global stock markets and cryptocurrencies (using Yahoo Finance symbols).
- View live prices and historical performance.
- Automatically calculate and recommend optimal portfolio allocations using the Online Newton Step (ONS) algorithm.
- Effortlessly update prices and manage capital allocation.

**Who is it for?**  
This project is for individual investors, finance enthusiasts, and anyone interested in smarter, data-driven portfolio management with a simple, user-friendly interface.

---

## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/Deadcoder001/ons_trading/blob/main/LICENSE.txt)
[![GitHub release downloads](https://img.shields.io/github/downloads/Deadcoder001/ons_trading/latest/total.svg)](https://github.com/Deadcoder001/ons_trading/releases/latest)

## Deployment

You can deploy your Django ONS Trading app on any Linux server, cloud platform, or PaaS that supports Python. Hereâ€™s a basic guide for common deployment options:


```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```


# Roadmap

## 1. Core Features (Completed)
- [x] Add, view, and delete assets with name and symbol.
- [x] Fetch live prices using yfinance for stocks and crypto.
- [x] Display portfolio with real-time prices.
- [x] Run ONS (Online Newton Step) algorithm for optimal allocation.
- [x] Show recommended allocations and capital distribution.
- [x] Responsive, modern UI with Bootstrap.

## 2. Usability Improvements
- [x] Symbol lookup helper or autocomplete (link to Yahoo Finance or suggest format).
- [x] Asset edit functionality (change name/symbol).
- [x] Asset detail/history view (show price chart for each asset).
- [x]Improved error messages for invalid symbols or price fetch failures.

## 3. Advanced Features
- [x] Support for multiple exchanges (NSE, BSE, NASDAQ, etc.) with dropdown.
- [x] Import/export portfolio as CSV.
- [x] User authentication and personal portfolios.
- [x] Notifications for price changes or rebalancing suggestions.

## 4. Analytics & Visualization
- [x] Portfolio performance chart over time.
- [x] Asset allocation pie chart.
- [x] Risk/return analytics and historical backtesting.

## 5. Integrations & Automation
- [x] Scheduled price updates (via Celery or cron).
- [x] Integration with broker APIs for real trades (optional/advanced).
- [x] Mobile-friendly PWA or native app.

## 6. Documentation & Community
- [x] Complete user guide and FAQ.
- [x] Contribution guidelines for open source.
- [x] Demo video and deployment instructions.

---

**Suggestions and contributions are welcome!**
# Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
- **Database:** SQLite (default, can be switched to PostgreSQL/MySQL)
- **Live Price Data:** [yfinance](https://pypi.org/project/yfinance/) (Yahoo Finance Python API)
- **Numerical Computation:** NumPy
- **Deployment:** Linux server (compatible with Heroku, Render, DigitalOcean, etc.)
- **Version Control:** Git & GitHub
## Screenshots

![App Screenshot](https://github.com/Deadcoder001/ons_trading/blob/main/Screenshot%202025-05-25%20at%209.58.56%E2%80%AFPM.png?raw=true)


## Authors

- [@Deadcoder001](https://www.github.com/Deadcoder001)
