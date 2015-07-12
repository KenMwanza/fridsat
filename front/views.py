from django.shortcuts import render
from front.forms import BusinessForm
from front.models import Category, County
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def index(request):
    categories = Category.objects.all()
    counties = County.objects.all()
    return render(request, 'front/index.html',
        {
            'categories': categories,
            'counties': counties,
        }
    )

@login_required(login_url='/login/')
def publish(request):
    if request.method == "POST":
        form = BusinessForm(request.POST)
        if form.is_valid():
            business = form.save(commit=False)
            cd = form.cleaned_data
            business.name = cd['name']
            business.category = cd['category']
            business.county = cd['county']
            business.street_address = cd['street_address']
            business.email = cd['email']
            business.phone_number = cd['phone_number']
            business.description = cd['description']
            business.save()
            return HttpResponseRedirect('/home')
    else:
        form = BusinessForm()
    return render(request, 'front/post.html', {
        "form": form
        })
