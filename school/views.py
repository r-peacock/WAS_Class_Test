from django.shortcuts import render
from django.http import HttpResponse
from school.models import SchoolNews

def index(request):
    school_news_list = SchoolNews.objects.all()

    context_dict = {}
    context_dict['news'] = school_news_list
    return render(request, 'school/index.html', context=context_dict)