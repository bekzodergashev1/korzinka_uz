import django_filters
from django_filters import DateFilter
from .models import *


class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='data_created', lookup_expr="gte")
    end_date = DateFilter(field_name='data_created', lookup_expr="lte")

    class Meta:
        model = Order
        fields = '__all__'
        # olib tashlidi
        exclude = ['customer', 'date_created']