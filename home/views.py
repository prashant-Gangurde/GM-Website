from django.shortcuts import render,redirect
from home.models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')
def services(request):
    queryset = NewService.objects.all().values()
    context = {'queryset':queryset}
    return render(request, 'services.html',context)
def careers(request):
    return render(request, 'careers.html')
def about_us(request):
    return render(request, 'about_us.html')
def apply_page(request,id):
    if request.method == 'POST':
       name =request.POST.get('name')
       age =request.POST.get('age')
       gender =request.POST.get('gender')
       email =request.POST.get('email')
       mobile =request.POST.get('mobile')
       s1 =Applicant.objects.create(name = name,age =age,mobile=mobile,gender=gender,email_add= email)
       s1.save()
       redirect('services')
    return render(request, 'apply_page.html')