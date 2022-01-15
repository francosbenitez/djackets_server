from rest_framework import serializers

from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
  class Meta:

    ## We wanna use the product model to get information
    model = Product

    ## What fields we're going to use in the frontend
    fields = (
      "id",
      "name",
      "get_absolute_url",
      "description",
      "price",
      "get_image",
      "get_thumbnail"
    )

class CategorySerializer(serializers.ModelSerializer):

  ## To make sure that we get all the data
  ## connected to the product as well
  products = ProductSerializer(many=True)

  class Meta:
    model = Category

    ## All of the things connected to the categories
    fields = (
      "id",
      "name",
      # "slug",
      "get_absolute_url",
      "products"
    )