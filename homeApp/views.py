from django.shortcuts import render
from django.views.generic import View
from .models import SlideModel, Skill


# Create your views here.
class HomeView(View):
    temp_name='homeApp/index.html'

    def get(self, request):
        slides = SlideModel.objects.all().order_by('-id')[:3]
        skills = Skill.objects.all().order_by('-id')
        
        context ={
            'slides': slides,
            'skills': skills
            
            }
        return render(request, self.temp_name, context)

    



