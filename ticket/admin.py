from django.contrib import admin
from .models import Ticket, Item, Category


admin.site.register(Ticket)
admin.site.register(Item)
admin.site.register(Category)

# Register your models here.
