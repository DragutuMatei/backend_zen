from rest_framework import serializers
from .models import CustomUser, Another, YourModel
class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourModel
        fields = '__all__'

class AnotherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Another
        fields = '__all__'
        
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email',)
        