from django.db import models

class TraderData(models.Model):
    """ Model for trader data """
    
    timestamp = models.DateTimeField(auto_now_add=True)
    profit_loss = models.FloatField()
