from django.db import models


class Notendur(models.Model):
    nafn = models.CharField(db_column='Nafn', primary_key=True, max_length=255)  
    bilnumer = models.CharField(db_column='Bilnumer', max_length=20, blank=True, null=True) 
    vandamal = models.TextField(db_column='Vandamal', blank=True, null=True)  
    stadsetning = models.CharField(db_column='Stadsetning', max_length=100, blank=True, null=True) 
    buid_til = models.DateTimeField(blank=True, null=True)
    kennitala = models.CharField(max_length=100, blank=True, null=True)
    simanumer = models.CharField(db_column='Simanumer', max_length=100, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'notendur'
