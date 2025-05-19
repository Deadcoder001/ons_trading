from django.contrib import admin
from .models import Asset, Price, PortfolioWeight

admin.site.register(Asset)
admin.site.register(Price)
admin.site.register(PortfolioWeight)
