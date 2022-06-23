from email.policy import HTTP
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serialize import StudentSerializer
from rest_framework import status
import json
from courses.models import Courses,Enrolled

@api_view(['GET'])

def ApiOverview(request):
    api_urls = {
        'signup':'/signup',
        'login':'/login',
        'show all courses':'/show',
        'enroll in course':'/enroll',
        'course info':'/info',
    }
  
    return Response(api_urls)

@api_view(['POST'])
def signup(request):
    user=StudentSerializer(data=request.data)
    
    username=request.data['username']
    email=request.data['email']
    
    if Student.objects.filter(username=username).exists() or Student.objects.filter(email=email).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    if user.is_valid():
        user.save()
        return Response(status=status.HTTP_200_OK)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def login(request):
    username=request.data['username']
    password=request.data['password']

    user=Student.objects.filter(username=username).values()

    if not user.exists():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    user=json.dumps(list(user))
    user=json.loads(user)
    checkpassword=user[0]['password']

    if password!=checkpassword:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def show(request):
    course=Courses.objects.all().values()
    course=list(course)

    return Response(status=status.HTTP_200_OK,data=course)

@api_view(['POST'])
def info(request):
    id=request.data['id']
    course=Courses.objects.filter(id=id).values()
    course=list(course)

    return Response(status=status.HTTP_200_OK,data=course[0])

@api_view(['POST'])
def enroll(request):
    id=request.data['id']
    username=request.data['username']
    
    course=Courses.objects.all().values()
    course=list(course)
    
    ispresnt=False

    for i in course:
        if i['id']==id:
            ispresnt=True
    
    if not ispresnt:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    enroll=Enrolled.objects.filter(courseid=id).all().values()
    enroll=list(enroll)

    if len(enroll)==0:
        enroll=Enrolled(courseid=id,studentname=username)
        enroll.save()

    else:
        for i in enroll:
            if i['studentname']==username:
                return Response(data={'message':'already enrolled'},status=status.HTTP_400_BAD_REQUEST)

        enroll=Enrolled(courseid=id,studentname=username)
        enroll.save()

    return Response(status=status.HTTP_200_OK)