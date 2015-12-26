from django.core.management.base import BaseCommand, CommandError
from front.models import Business

class Command(BaseCommand):
    help = 'Fetches four random businesses to be featured'


    def handle(self, *args, **options):

        featured = []

        featured_businesses = Business.objects.order_by('?')[:4]
        for featured_business in featured_businesses:
            featured.append(featured_business.pk)

        with open('featured.txt','w') as f:
            f.write('\n'.join(str(e) for e in featured))
