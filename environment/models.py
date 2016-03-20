from django.db import models

from datetime import datetime

# Create your models here.

class Estatistica(models.Model):
    local = models.CharField(max_length=200)
    data = models.DateTimeField(default=datetime.now())
    unidade = models.CharField(max_length=5, blank=True)
    valor = models.CharField(max_length=10)
    parametro = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.local + ' ' + str(self.data) + ' ' + self.parametro + ' ' + \
            self.valor + self.unidade
