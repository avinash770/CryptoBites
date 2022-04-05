from django.contrib import admin

# Register your models here.
from .models import Tutorial, Testimonial, Recommended, Coin, BuyCoins

# Registering all the models
admin.site.register(Recommended)
admin.site.register(Tutorial)
admin.site.register(Testimonial)
admin.site.register(Coin)
admin.site.register(BuyCoins)
