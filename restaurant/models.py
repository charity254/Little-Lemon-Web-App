from django.db import models


class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000, blank=True, default='')
   date = models.DateField(null=True, blank=True)
   time = models.TimeField(null=True, blank=True)
   special_requests = models.TextField(max_length=1000, blank=True, default='')

   def __str__(self):
      return self.first_name + ' ' + self.last_name


class Menu(models.Model):
   CATEGORY_CHOICES = [
      ('Starters', 'Starters'),
      ('Mains', 'Mains'),
      ('Desserts', 'Desserts'),
      ('Drinks', 'Drinks'),
   ]
   name = models.CharField(max_length=200)
   price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
   menu_item_description = models.TextField(max_length=1000, default='')
   category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Starters')
   featured = models.BooleanField(default=False)
   image = models.CharField(max_length=500, blank=True, default='')

   def __str__(self):
      return self.name