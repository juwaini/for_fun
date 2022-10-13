from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=30)


class State(models.Model):
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=30)


class District(models.Model):
    state = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=30)
