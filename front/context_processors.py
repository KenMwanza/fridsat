from front.models import Category, County, Area

def categories_processor(request):
	categories = Category.objects.all()
	areas = Area.objects.all()
	counties = County.objects.all()     
 	return { 
 				'categories': categories,
 			 	'areas': areas,
 			 	'counties': counties
 			}