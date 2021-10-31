from rest_framework import serializers
from .models import places
from .models import user
from .models import feedback
from .models import slider
from .models import Employee
from .models import gallery
from .models import reels
from .models import popular
from .models import history
from .models import review


from django.contrib.auth.models import User


class placesSerializer(serializers.ModelSerializer):
    class Meta:
        model = places
        fields = '__all__'


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'


class feedbackSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    feedback = serializers.CharField(max_length=400)

    class Meta:
        model = feedback
        fields = '__all__'


class sliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = slider
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class gallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = gallery
        fields = '__all__'


class reelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = reels
        fields = '__all__'


class popularSerializer(serializers.ModelSerializer):
    class Meta:
        model = popular
        fields = '__all__'


class historySerializer(serializers.ModelSerializer):
    class Meta:
        model = history
        fields = '__all__'


class reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = '__all__'


