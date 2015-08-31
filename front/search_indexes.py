import datetime
from haystack import indexes
from front.models import Business

class BusinessIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    category = indexes.CharField(model_attr='category')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Business

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return Business.objects.filter(pub_date__lte=datetime.datetime.now())