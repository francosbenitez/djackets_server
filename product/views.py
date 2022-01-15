from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class LatestProductsList(APIView):

  ## This 'get' function overrides functionality
  def get(self, request, format=None):
    products = Product.objects.all()[0:4]

    ## Convert the 'products' using the serializer
    ## Many == True because we have more than one object
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)