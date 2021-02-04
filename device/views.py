from django.shortcuts import render
from django.shortcuts import render, redirect
from device.forms import DeviceForm
from device.models import Device
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging
# Create your views here.
def dev(request):
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/all')
            except:
                pass
    else:
        form = DeviceForm()
    return render(request,'index.html',{'form':form})
def show(request):
    devices = Device.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(devices, 10)
    try:
        devices = paginator.page(page)
    except PageNotAnInteger:
        devices = paginator.page(1)
    except EmptyPage:
        devices = paginator.page(paginator.num_pages)
    return render(request,"show.html",{'devices':devices})
def edit(request, name):
    device = Device.objects.get(name=name)
    return render(request,'edit.html', {'device':device})
def update(request, name):
    logger = logging.getLogger("mylogger")
    device = Device.objects.get(name=name)
    form = DeviceForm(request.POST, instance = device)
    logger.info(form.is_valid())
    if form.is_valid():
        form.save()
        return redirect("/all")
    return render(request, 'edit.html', {'device': device})
def destroy(request, name):
    device = Device.objects.get(name=name)
    device.delete()
    return redirect("/all")
def deleteAll(request):
    Device.objects.all().delete()
    return redirect("/all")
# Create your views here.
