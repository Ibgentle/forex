from django.db import models

# Create your models here.

class Trade(models.Model):
    class TradeResult(models.TextChoices):
        WIN = 'Win', 'W'
        LOSS = 'Loss', 'L'

    class TradeType(models.TextChoices):
        UP = 'Up', 'U'
        DOWN = 'Down', 'D'

    class Meta:
        ordering = ['-date']

    date = models.DateField()
    type_of_trade = models.CharField(max_length=5,
            choices=TradeType.choices,
            default=TradeType.UP)
    result = models.CharField(max_length=5,
            choices=TradeResult.choices,
            default=TradeResult.WIN)
    currency_pair = models.CharField(max_length=50)
    analysis = models.TextField()
    broker = models.CharField(max_length=20)
    entry_time = models.TimeField()

    def __str__(self):
        return '%s, %s' % (self.type_of_trade, self.currency_pair)
