from http import HTTPStatus

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    print("\n Enter the function --------------->;001")
    return render(request, 'bash.html')