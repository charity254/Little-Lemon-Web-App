from django.contrib import admin
from .models import Menu
from.models import Booking

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'featured']
    list_filter = ['category', 'featured']
    fields = ['name', 'category', 'price', 'featured', 'menu_item_description', 'image']


class BookingAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date', 'time', 'guest_number']
    fields = ['first_name', 'last_name', 'date', 'time', 'guest_number', 'comment', 'special_requests']   

admin.site.register(Menu, MenuAdmin)
admin.site.register(Booking, BookingAdmin)