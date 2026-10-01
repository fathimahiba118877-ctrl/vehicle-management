from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers
from .models import ServiceRequest


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user


class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = '__all__'

    def validate_customer_name(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Customer name should not be empty.")
        return value

    def validate_vehicle_number(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Vehicle number should not be empty.")
        return value

    def validate_description(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Description should not be empty.")
        return value

    def validate_service_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Service date should not be in the past.")
        return value

    def validate_estimated_cost(self, value):
        if value <= 0:
            raise serializers.ValidationError("Estimated cost must be greater than 0.")
        return value