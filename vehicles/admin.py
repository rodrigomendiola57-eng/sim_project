from django.contrib import admin
from .models import Vehicle, Document, Maintenance

admin.site.register(Vehicle)
admin.site.register(Document)
admin.site.register(Maintenance)
