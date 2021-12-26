from django.shortcuts import redirect, render
from django.views.generic import View
from .models import Clint_feedback, Department, Department_galary, SlideModel, Skill, Services, Appoinment, Schedule, Doctor, Clint_feedback, ServicesCount
from .forms import AppoinmentForm
from django.contrib import messages


# Create your views here.
class HomeView(View):
    temp_name='homeApp/index.html'

    def get(self, request):
        slides = SlideModel.objects.all().order_by('-id')[:3]
        skills = Skill.objects.all().order_by('-id')
        services = Services.objects.all().order_by('-id')
        departments = Department.objects.all()
        department_gals = Department_galary.objects.filter(department__in=departments)
        appoinment = AppoinmentForm
        doctor = Doctor.objects.prefetch_related('doc_schedule').all()
        cli_feedback = Clint_feedback.objects.all()
        services_count = ServicesCount.objects.all()

        context ={
            'slides': slides,
            'skills': skills,
            'services': services,
            'appoinment': appoinment,
            'departments': departments,
            'department_gals': department_gals,
            'doctors': doctor,
            'Clint_feedbacks': cli_feedback,
            'services_counts': services_count
            }
        return render(request, self.temp_name, context)


    def post(self, request):
        appoinment = AppoinmentForm(request.POST)
        if appoinment.is_valid():
            appoinment.save()
            messages.success(request, 'Profile details updated.')
            return redirect('homeApp:home')
        return render(request, self.temp_name, {'appoinment': appoinment})





