from django.db.models import fields
from rest_framework import serializers
from .models import Educator
  
class EducatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educator
        fields = ('name','email','password')