from django.db import models

class Bill(models.Model):
    bill_no = models.AutoField(primary_key=True)
    bill_date = models.DateTimeField(auto_now_add=True)
    patient_name = models.CharField(max_length=200,  blank=True, null=True)
    patient_age = models.IntegerField( blank=True, null=True)
    address = models.CharField(max_length=2000, blank=True, null=True)
    item = models.CharField(max_length=500, blank=True, null=True)
    number_of_item =  models.IntegerField(default=1)
    amount_for_one = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    balance = models.FloatField(default=0)
