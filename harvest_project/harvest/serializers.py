from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Harvest
from decimal import Decimal

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user

class HarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harvest
        fields = ['id', 'user', 'title', 'description', 'date', 'location', 'quantity_in_tons', 'seed_type', 'fertilizer']
        read_only_fields = ['user', 'date']  # A data será gerada automaticamente

    def validate_quantity_in_tons(self, value):
        if isinstance(value, str):
            try:
                value = Decimal(value)
            except ValueError:
                raise serializers.ValidationError("O campo 'quantity_in_tons' deve ser um número válido.")
        elif not isinstance(value, Decimal):
            raise serializers.ValidationError("O campo 'quantity_in_tons' deve ser um número decimal.")
        return value

    def create(self, validated_data):
        validated_data['date'] = validated_data.get('date', None) or timezone.now()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['date'] = validated_data.get('date', instance.date)
        return super().update(instance, validated_data)
