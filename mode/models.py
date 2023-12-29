from django.db import models


class CarSpecs(models.Model):
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=100)
    production_year = models.CharField(max_length=10)
    car_body = models.CharField(max_length=100)
    car_engine_type = models.CharField(max_length=50)
    car_fuel = models.CharField(max_length=50)
    car_engine_cc = models.CharField(max_length=50)

    def __str__(self):
        return self.car_model
