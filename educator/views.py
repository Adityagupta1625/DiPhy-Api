from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Educator
from .serialize import EducatorSerializer
from rest_framework import serializers
from rest_framework import status
import json
from courses.models import Courses
from courses.models import Enrolled

@api_view(['GET'])

def ApiOverview(request):
    api_urls = {
        'signup':'/signup',
        'login':'/login',
        'list of students enrolled':'/show',
    }
  
    return Response(api_urls)

@api_view(['POST'])
def signup(request):
    edu=EducatorSerializer(data=request.data)
    
    email=request.data['email']
    
    if Educator.objects.filter(email=email).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    if edu.is_valid():
        edu.save()
        return Response(status=status.HTTP_200_OK)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def login(request):
    email=request.data['email']
    password=request.data['password']

    user=Educator.objects.filter(email=email).values()

    if not user.exists():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    user=json.dumps(list(user))
    user=json.loads(user)
    checkpassword=user[0]['password']

    if password!=checkpassword:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def show(request):
    id=request.data['id']
    
    enroll=Enrolled.objects.filter(courseid=id).all().values()
    enroll=list(enroll)
    
    student=[]

    for i in enroll:
        student.append(i['studentname'])

    return Response(status=status.HTTP_200_OK,data=student)
    