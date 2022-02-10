from django.db import models

class Summary(models.Model):
    bioguide_id = models.CharField(max_length=7)
    office = models.CharField(max_length=500)
    program = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    year_to_date = models.DecimalField(max_digits=20, decimal_places=2)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    year = models.IntegerField()
    quarter = models.IntegerField()

class Detail(models.Model):
    bioguide_id = models.CharField(max_length=7)
    office = models.CharField(max_length=500)
    quarter = models.IntegerField()
    program = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    sort_sequence = models.CharField(max_length=500)
    date = models.DateField()
    transcode = models.CharField(max_length=15)
    recordid = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    purpose = models.CharField(max_length=500)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    year = models.IntegerField()
