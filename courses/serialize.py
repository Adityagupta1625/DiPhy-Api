from django.db.models import fields
from rest_framework import serializers
from .models import Courses
  
class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('id','title','description','created_at','updated_at','image','educator','content')