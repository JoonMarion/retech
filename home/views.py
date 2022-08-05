from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def home(request):
    return render(request, 'index.html')

@api_view(['GET'])
def healthcheck(request):
    try:
        return Response({"message": 'ok'}, status=200)
    except Exception:
        return Response({"message": "Error"}, status=400)