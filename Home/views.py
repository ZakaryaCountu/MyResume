from django.http import request
from django.shortcuts import redirect, render
from .models import Profile,Skills,Sumary,Education,Experience,Experience_benefits,Project,Service,Info,TESTIMONIALS
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def Resume(request):
    #for about page ::
    info = Profile.objects.first()
    
    #for sills page ::
    skill = Skills.objects.all()


    #for resume page ::
    sumary = Sumary.objects.first()
    education =Education.objects.all()
    experience =Experience.objects.all()
    experience_bf = Experience_benefits.objects.all()
     
    #for portfolio page ::
    projects = Project.objects.all()
    

    #service page ::
    services = Service.objects.all()

    #Testimonials Page ::
    TestiM = TESTIMONIALS.objects.all()


    #Contact page ::
    myinfo = Info.objects.first()
   
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        
        
        send_mail(subject, message,email,['zakaryalaarrague@gmail.com'])
        return redirect('ResumePage:success')


    context = {'info':info, 'skill':skill,
            'sumary':sumary, 'education': education, 
            'experience':experience,
            'experience_bf':experience_bf ,
            'projects':projects,
            'services':services,
            'myinfo':myinfo,
            'TestiM': TestiM
             }


    return render(request,'index.html',context)
    


def Project_detail(request, slug):
    project_detail = Project.objects.get(slug=slug)
    return render(request, 'project-details.html',{'project_detail':project_detail})

def success(request):
    return render(request,'success.html',{})

   

