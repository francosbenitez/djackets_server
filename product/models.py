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

  