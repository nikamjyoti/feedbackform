from django.shortcuts import render
from .models import feedbackdata
from .forms import feedbackform
from django.http.response import HttpResponse
import datetime
date1= datetime.datetime.now()

# Create your views here.
def feedback_views(request):
    if request.method == "POST":
        fform = feedbackform(request.POST)
        if fform.is_valid():
            name = request.POST.get('name','')
            rating = request.POST.get('rating', '')
            feedback = request.POST.get('feedback', '')

            data = feedbackdata(name=name,
                                  rating = rating,
                                  feedback = feedback,
                                  date=date1)
            data.save()
            fform=feedbackform()
            fdata=feedbackdata.objects.all()
            return render(request,'feedback_form.html',{'fform':fform,'fdata':fdata})
        else:
            return HttpResponse("invalid data")
    else:
        fform=feedbackform()
        fdata=feedbackdata.objects.all()
        return render (request,'feedback_form.html',{'fform':fform,'fdata':fdata})



