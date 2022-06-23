from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from email.policy import HTTP
from .models import Courses
from rest_framework import status

@api_view(['GET'])

def ApiOverview(request):
    api_urls = {
        '':'/',
    }
  
    return Response(api_urls)

