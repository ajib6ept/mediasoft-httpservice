from django.contrib import admin

from mediasoft.httpservice.models import City, Shop, Street

admin.site.register(Shop)
admin.site.register(City)
admin.site.register(Street)
