from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
import csv
import codecs
from uploader.models import Upload
import logging
import os
from django.conf import settings
from device.models import Device
from django.db import connection
from ftplib import FTP
from django.contrib import messages

class UploadView(CreateView):
   model = Upload
   fields = ['upload_file', ]
   success_url = reverse_lazy('fileupload')

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['documents'] = Upload.objects.all()
       return context

def upload(request,name):
    logger = logging.getLogger("mylogger")
    # ftp = FTP(host='10.235.65.24',user='task', passwd = 'task!123!')
    # ftp.login()
    # ftp.cwd('/home/task')
    # filename = 'task.csv'
    # localfile = open(filename, 'wb')
    # ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    # ftp.quit()
    # with open(localfile,encoding = 'cp850') as csv_file:
    try:
        with open(os.path.join(settings.MEDIA_ROOT,name),encoding = 'cp850') as csv_file:
            next(csv_file)
            csv_reader = csv.reader(csv_file,delimiter=',')
            all_devices= []
            for row in csv_reader:
                str1 =row[1].replace("O/L","Online")
                str2=str1.replace("CEASING","Offline")
                all_devices.append(Device(name=row[0],status=str2,chassis_type=row[2],service_type=row[3],device_type=row[4],toposite_name=row[5],site_name=row[6],ico01=row[7]))
        Device.objects.bulk_create(all_devices);
        return redirect("/all")
    except:
       messages.info(request, 'Wrong file format, please choose a .csv file!')
       return redirect('/')

