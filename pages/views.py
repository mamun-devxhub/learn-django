""" pages/views.py """
from django.views.generic import TemplateView
# from django.shortcuts import render
# from django.http import HttpResponse

# def homePageView(request):
#     return HttpResponse('Hello, World!')


class HomePageView(TemplateView):
    """HomePageView"""
    template_name = 'home.html'


class AboutPageView(TemplateView):
    """AboutPageView"""
    template_name = 'about.html'
