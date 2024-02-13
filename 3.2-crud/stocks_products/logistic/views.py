from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from django.core.paginator import Paginator

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']



class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [SearchFilter]
    search_fields = ['products__title', 'products__description']


def pagi(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(stock, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, context)