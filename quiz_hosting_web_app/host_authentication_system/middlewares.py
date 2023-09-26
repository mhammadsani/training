from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from quiz_attempter_management.models import QuizAttempter


class UserIdentificatonMiddlewere:

    def __init__(self, get_response) -> None:
        self.get_response = get_response
        
        
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    
    # def process_view(self, request, *args, **kwargs): 
    #     user = request.user
    #     if user.is_authenticated:
    #         pass
    