from django.shortcuts import render
from front.forms import BusinessForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'front/index.html')

@login_required(login_url='/login/')
def publish(request):

    if request.method == "POST":
        pass
    else:
        form = BusinessForm()
    return render(request, 'front/post.html', {
        "form": form
        })
