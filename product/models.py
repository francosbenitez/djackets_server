## For images and resizing
from io import BytesIO
from PIL import Image

## To import files
from django.core.files import File

from django.db import models

# Create your models here.
class Category(models.Model):

   ## Category called 'name' with a max_length of 255
  name = models.CharField(max_length=255)

  ## Address for the name
  slug = models.SlugField()

  ## Options for the model ordering
  class Meta:

    ## A tuple with comma to be iterable for the backend
    ordering = ('name',)

  ## To avoid seeing an object in the backend
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return f'/{self.slug}/'

class Product(models.Model):

  ## A foreign key is an index in the database or a relation key
  cateogory = models.ForeignKey(
    Category, 
    related_name='products',

    ## If we delete one of the categories, 
    ## we also delete all of the products 
    ## connected to it
    on_delete=models.CASCADE
  )
  name = models.CharField(max_length=255)
  slug = models.SlugField()

  ## A field for the description
  description = models.TextField(

    ## It can be empty if one wants
    blank=True, 
    null=True
  )
  price = models.DecimalField(
    max_digits=6, 
    decimal_places=2
  )
  image = models.ImageField(
    upload_to='uploads/',
    blank=True,
    null=True
  )
  thumbnail = models.ImageField(
    upload_to='uploads/',
    blank=True,
    null=True
  )
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:

    ## In this case, we order by date
    ## And the '-' means 'in descending order'
    ordering = ('-date_added',)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return f'/{self.category.slug}/{self.slug}/'

  def get_image(self):
    if self.image:
      return 'http://127.0.0.1:8000' + self.image.url
    return ''
  
  def get_thumbnail(self):
    if self.thumbnail:
      return 'http://127.0.0.1:8000' + self.thumbnail.url
    else:
      if self.image:
        self.thumbnail = self.make_thumbnail(self.image)
        self.save()

        return 'http://127.0.0.1:8000' + self.thumbnail.url
      else:
        return ''

  def make_thumbnail(self, image, size=(300, 200)):
    img = Image.open(image)
    img.convert('RGB')
    img.thumbnail(size)
    thumb_io = BytesIO()
    img.save(thumb_io, 'JPEG', quality=85)
    thumbnail = File(thumb_io, name=image.name)
    return thumbnail


  