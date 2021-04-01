from django.shortcuts import render,redirect
from .forms import DataForm,FilterForm
from .models import Data
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
# imports to visualize data
from io import BytesIO
import base64
import sys
import matplotlib
import matplotlib.pyplot as plt
# import tkinter
import numpy as np


# Create your views here.
def index(request):
    if request.method=='POST':
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            applicant_mail = form.cleaned_data["email"]
            messages.success(request,"Request send successfully and an email has been send! ")

            subject="Request - Confirmation mail"
            message ="Thank you for showing your interest in joining."
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [applicant_mail,]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('index')
    form = DataForm()
    return render(request,'myapp/index.html',{'form':form})

def details(request):
    if request.method == 'POST':
        status=request.POST.get('current_status')
        filter_form = FilterForm(request.POST)
        if filter_form.is_valid():
            applicants = Data.objects.filter(current_status = status)
            return render(request,'myapp/details.html',{'applicants':applicants,'filter_form':filter_form})
    filter_form = FilterForm()
    applicants = Data.objects.all()
    return render(request,'myapp/details.html',{'applicants':applicants,'filter_form':filter_form})

def visualize(request):
    pending_data = Data.objects.filter(current_status="pending").count()
    approved_data = Data.objects.filter(current_status="approved").count()
    rejected_data = Data.objects.filter(current_status="rejected").count()
    # matplotlib.use('Agg')

    y = np.array([pending_data, approved_data, rejected_data])
    mylabels = ["Pending", "Approved", "Rejected"]

    plt.pie(y,labels=mylabels)
    plt.show() 

    #Two  lines to make our compiler able to draw:
    buffer = BytesIO()
    plt.savefig(buffer, format='png')

    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    # # sys.stdout.flush()
    return render(request,'myapp/graphic.html',{'graphic':graphic})
    # return render(request,'myapp/graphic.html')