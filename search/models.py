from django.db import models
import json

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    menu = models.JSONField()

    def __str__(self):
        return self.menu
    
    def get_menu_as_dict(self):
        return json.loads(self.menu)