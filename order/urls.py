# from django.urls import path  

# from order import views 

# urlpatterns = [
#   # path('checkout/', views.checkout, name='checkout')
#   path('checkout/', views.checkout),

#   path('orders/', views.OrdersList.as_view())
# ]
from django.urls import path

from order import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('orders/', views.OrdersList.as_view()),  
]