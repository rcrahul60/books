from django.urls import path
from .views import *

urlpatterns=[
     path('book_with_author/',bookWithAuthor,),
    #  path('login/',login,name="login")
]