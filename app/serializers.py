from rest_framework import serializers

from app.models import user


class userserializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['email', 'is_verified']

class VerifyAccountSerialzer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length= 4)
