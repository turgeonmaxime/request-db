from __future__ import unicode_literals

from django.db import models

class Analyst(models.Model):
    # Attributes
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    phone_number = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Database(models.Model):
    # Attributes
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30)
    connection_details = models.CharField(max_length = 30)
    maintained_stakeholder = models.BooleanField()

    def __str__(self):
        return self.name

class Stakeholder(models.Model):
    # Attributes
    name = models.CharField(max_length = 30)
    title = models.CharField(max_length = 30)
    department = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    phone_number = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Request(models.Model):
    # Attributes
    title = models.CharField(max_length = 30)
    date_created = models.DateField()
    date_requested = models.DateField()
    date_released = models.DateField()
    stakeholder = models.ForeignKey(Stakeholder, on_delete = models.CASCADE)
    analysts = models.ManyToManyField(Analyst, through = 'Contribution')
    databases = models.ManyToManyField(Database)

    def __str__(self):
        return self.title

class Contribution(models.Model):
    # Attributes
    request = models.ForeignKey(Request, on_delete = models.CASCADE)
    analyst = models.ForeignKey(Analyst, on_delete = models.CASCADE)
    main_analyst = models.BooleanField()
