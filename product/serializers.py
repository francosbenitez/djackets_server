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