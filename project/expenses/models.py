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

    def __str__(self):
        return self.category

class Detail(models.Model):
    bioguide_id = models.CharField(max_length=7)
    office = models.CharField(max_length=500)
    quarter = models.CharField(max_length=1)
    program = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    sort_sequence = models.CharField(max_length=500)
    date = models.DateField(blank=True, null=True)
    transcode = models.CharField(max_length=15)
    recordid = models.CharField(max_length=500, blank=True, null=True)
    payee = models.CharField(max_length=500)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    purpose = models.CharField(max_length=500)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    year = models.IntegerField()

    def __str__(self):
        return self.payee
