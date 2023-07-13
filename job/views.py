from django.urls import reverse
from django.shortcuts import redirect, render 
from .models import Job
from django.core.paginator import Paginator
from .form import Apply_form , Job_Form
# from django.http import HttpResponse


# Create your views here.


def job_list(request) :
     job_list =  Job.objects.all()
     paginator = Paginator(job_list, 3 )  # Show 25 contacts per page.

     page_number = request.GET.get("page")
     page_obj = paginator.get_page(page_number)


     context = {'jobs': page_obj}
     return render(request ,'job/job_list.html' , context )

# def job_image (request) :
#      job_image = Job.objects.
#      context ={'images': job_image}

#      return render(request,'job/job_list.html',context)

def job_detail(request, slug) :
    

    job_detail = Job.objects.get(slug=slug)

    if request.method == 'POST' :
     
         form = Apply_form(request.POST , request.FILES)
         
         if form.is_valid() :
          
             myform = form.save(commit=False)
          
             myform.job = job_detail
             
             myform.save()


    context = {'form': Apply_form(request.POST , request.FILES) ,'job': job_detail}
    return render(request,'job/job_detail.html',context)


def add_job(request):
     
      if request.method == 'POST' :
                form1 = Job_Form(request.POST , request.FILES)
                if form1.is_valid() :
                    myform = form1.save(commit=False)
                    myform.owner = request.user 
                    myform.save()
                    return redirect(reverse('jobs:job_list'))
     
     
     
      else:
          form1 = Job_Form()


      
      context = {'form1':form1}
     # context = {'post':add_job }
      return render(request ,'job/add_job.html' , context)
