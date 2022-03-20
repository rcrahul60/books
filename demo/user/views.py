from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from django.http import HttpResponse
# Create your views here.




def bookWithAuthor(request):
  book_obj = Book.objects.all()
  for book in book_obj:
    print('"{}".{}'.format(book.title,book.author.name))

  for a in Author.objects.all():
    print('{} : {}'.format(a.name, a.author_book.all().values_list('title',flat=True)))

  for a in Author.objects.all():
    print('{} : {}'.format(a.name, a.author_book.count()))
  
  return HttpResponse(book_obj)