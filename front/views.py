from django.shortcuts import render
from front.forms import PostDeviceForm, PublishForm
from front.models import Device, County
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'front/index.html')

@login_required(login_url='/login/')
def publish(request):
    devices = Device.objects.all()
    counties = County.objects.all()

    if request.method == "POST":
        pass
    else:
        form = PublishForm()
    return render(request, 'front/post.html', {
        "form": form,
        "devices": devices, 
        "counties": counties})
