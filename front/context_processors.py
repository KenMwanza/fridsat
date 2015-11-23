from front.models import Category, County, Area, CustomBusinessGroup

def categories_processor(request):
	categories = Category.objects.all()
	areas = Area.objects.all()
	custom_lists = CustomBusinessGroup.objects.all()
	counties = County.objects.all()     
 	return { 
 				'categories': categories,
 			 	'areas': areas,
 			 	'counties': counties,
 			 	"custom_lists": custom_lists,
 			}