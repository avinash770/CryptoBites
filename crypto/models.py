from django.db import models


# Model used to show recommended cryptocurrencies
class Recommended(models.Model):
    coin = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    currentPrice = models.CharField(max_length=20)
    marketCapital = models.CharField(max_length=20)
    graphX = models.CharField(max_length=50, blank=True, default=0)
    graphY = models.CharField(max_length=50, blank=True, default=0)

    def __str__(self):
        return str(self.coin)


# Model used to show tutorial page
class Tutorial(models.Model):
    youtubeLink = models.URLField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.title)


# Model used to show testimonial page
class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    feedback = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.name)


# Model used to store all the coins name in DB
class Coin(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model used to buy coins
class BuyCoins(models.Model):
    customerName = models.CharField(max_length=100)
    qty = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    email = models.EmailField()
    name = models.ForeignKey(Coin, on_delete=models.CASCADE)

    def __str__(self):
        return self.customerName
