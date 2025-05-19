from django import template
register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def mul(value, arg):
    try:
        return float(value) * float(arg)
    except:
        return ''

@register.filter
def to_float(value):
    try:
        return float(value)
    except:
        return 0

@register.filter
def get_symbol_id(assets, symbol):
    symbol = str(symbol).strip().upper()
    for asset in assets:
        if asset.symbol.strip().upper() == symbol:
            return asset.id
    return None
