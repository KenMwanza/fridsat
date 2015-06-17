from django.shortcuts import render
from front.forms import PostDeviceForm
from front.models import Device, County
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'front/index.html')

@login_required(login_url='/login/')
def publish(request):
    devices = Device.objects.all()
    counties = County.objects.all()
    brands = []
    for device in devices:
        brands.append(device.brand)

    if request.method == "POST":
        pass
    else:
        form = PostDeviceForm()
    return render(request, 'front/post.html', {
        "devices": devices, 
        "brands": set(brands),
        "counties": counties})
