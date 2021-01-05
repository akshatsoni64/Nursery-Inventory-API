from rest_framework.serializers import *
from .models import *

class PlantSerializers(ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class ProfileSerializers(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class OrderSerializers(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'