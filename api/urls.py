from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from engine.models import Space


def generate_serializer(in_model):
    # Serializers define the API representation.
    class XSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = in_model
            fields = '__all__'

    # ViewSets define the view behavior.
    class XViewSet(viewsets.ModelViewSet):
        queryset = in_model.objects.all()
        serializer_class = XSerializer

    return XViewSet


# Serializers define the API representation.
class SpaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Space
        fields = '__all__'

    actions = serializers.SerializerMethodField()

    def get_actions(self, obj):
        return obj.actions()

# ViewSets define the view behavior.
class SpaceViewSet(viewsets.ModelViewSet):
    queryset = Space.objects.all().select_subclasses()
    serializer_class = SpaceSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('Space', SpaceViewSet)


from django.apps import apps
models = apps.get_app_config('engine').get_models()
for model in models:
    if model.__name__ == 'Space':
        continue
    router.register(model.__name__, generate_serializer(model))

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
