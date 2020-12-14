from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .models import (
    CityData, 
    Address, 
    StateData, 
    Visitors, 
    Files, 
    Messages, 
    WebCounter, 
    MiniLocation, 
    Category, 
    Resources,
    )

@api_view(['GET'])
@permission_classes((AllowAny,))
def all_categories(request):
    categories = Category.objects.all()
    json_format = serializers.serialize('json', categories)
    return Response(json_format)