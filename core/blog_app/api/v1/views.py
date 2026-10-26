from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(['GET', 'POST'])
def postList(request):
    return Response('Ok')