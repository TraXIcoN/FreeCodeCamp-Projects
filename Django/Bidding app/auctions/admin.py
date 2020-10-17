from django.contrib import admin
from .models import Listing, Bid, Comments
# Register your models here.

admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Comments)
