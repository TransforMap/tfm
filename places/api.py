
from places.models import Owner, MapInstance, MapObject
from rest_framework import filters, routers, serializers, viewsets



class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Owner
        fields = ('name', 'date_added', 'date_modified')


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


router = routers.DefaultRouter()
router.register('owners', OwnerViewSet)

