from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from .models import Subscription
from .serializers import SubscriptionSerializer


# Create your views here.


class SubscriptionPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 50


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    pagination_class = SubscriptionPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title"]
    ordering_fields = ["id", "monthly_price", "title"]
