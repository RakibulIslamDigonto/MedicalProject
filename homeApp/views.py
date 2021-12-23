from django.shortcuts import render
from django.views.generic import View
from .models import SlideModel


# Create your views here.
class HomeView(View):
    temp_name='homeApp/index.html'

    def get(self, request):
        slides = SlideModel.objects.all()[:3]
        return render(request, self.temp_name, context={'slides':slides})



