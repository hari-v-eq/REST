from django.urls import path
from .views import ItemViews



urlpatterns=[
   
    path('items/', ItemViews.as_view()),
    path('items/<int:id>',ItemViews.as_view())
  
]