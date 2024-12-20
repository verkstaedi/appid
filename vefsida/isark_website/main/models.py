# main/models.py
from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name

class Notendur(models.Model):
    tegund_okutaekis = models.CharField(max_length=100)
    framleidandi = models.CharField(max_length=100)
    gerd = models.CharField(max_length=100)
    nafn = models.CharField(max_length=100)
    simanumer = models.CharField(max_length=15)
    kennitala = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    lysing = models.TextField()
    buid_til = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nafn
