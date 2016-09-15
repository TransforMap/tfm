from django.contrib import admin

from places.models import MapObject, MapInstance, Owner


admin.site.register(MapObject)
admin.site.register(MapInstance)
admin.site.register(Owner)

