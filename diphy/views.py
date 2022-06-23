from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])

def ApiOverview(request):
    api_urls = {
        'courses releted functions':'/courses',
        'student releated functions':'/student',
        'educator related functions':'/educator',
    }
  
    return Response(api_urls)