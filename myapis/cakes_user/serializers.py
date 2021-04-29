from cakes_user.models import *
from rest_framework import serializers


class UserDetailsSerializer(serializers.Serializer):
    class Meta:
        model = UserDetails
        fields = '__all__'

