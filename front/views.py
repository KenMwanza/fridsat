from django.shortcuts import render, get_object_or_404
from front.forms import BusinessForm
from front.models import Business, Category, County, Area, CustomBusinessGroup
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'front/index.html')

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    businesses = Business.objects.all().filter(category=category)
    return render(request, 'front/businesses.html',
        {
            'category': category,
            'businesses': businesses,
        }
    )

def business(request, slug):
    business = get_object_or_404(Business, slug=slug)
    category = Category.objects.get(name=business.category)
    county = County.objects.get(name=business.county)
    related_businesses = business.tags.similar_objects()[:5]
    return render(request, 'front/business.html',
        {
            'business': business,
            'category': category,
            'county': county,
            'related_businesses': related_businesses,
        }
    )

def county(request, slug):
    county = get_object_or_404(County, slug=slug)
    businesses = Business.objects.all().filter(county=county)
    return render(request, 'front/businesses.html',
        {
            'businesses': businesses,
            'county': county,
        }
    )

def area(request, county, area):
    county = get_object_or_404(County, slug=county)
    area = get_object_or_404(Area, slug=area)
    businesses = Business.objects.all().filter(county=county, area=area)
    return render(request, 'front/businesses.html',
        {
            'businesses': businesses,
            'area': area,
            'county': county,
        }
    )

def custom_business_group(request, slug):
    custom_business_group = get_object_or_404(CustomBusinessGroup, slug=slug)
    custom_business_group_tags = custom_business_group.tags.names()
    businesses = Business.objects.filter(tags__name__in=custom_business_group_tags).distinct()
    return render(request, 'front/businesses.html',
        {
            'custom_business_group': custom_business_group,
            'businesses': businesses,
        }
    )

def custom_business_groups(request):
    custom_business_groups = CustomBusinessGroup.objects.all()
    return render(request, 'front/custom_business_groups.html',
        {
            'custom_business_groups': custom_business_groups,
        }
    )

@login_required(login_url='/login/')
def add_business(request):
    if request.method == "POST":
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            cd = form.cleaned_data
            business.user = request.user
            business.name = cd['name']
            business.category = cd['category']
            business.county = cd['county']
            business.area = cd['area']
            business.street_address = cd['street_address']
            business.website = cd['website']
            business.email = cd['email']
            business.image = cd['image']
            tags = cd['tags']
            business.phone_number = cd['phone_number']
            business.description = cd['description']
            business.save()
            
            business.tags.add(*tags)
            return HttpResponseRedirect('/' + business.slug)
    else:
        form = BusinessForm()
    return render(request, 'front/post.html', {
        "form": form
        })
