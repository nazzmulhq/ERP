import django_filters
from django import forms
from productionplanning.models.ProductCenter import ProductCenter


class ProductCenterFilter(django_filters.FilterSet):
    product_center_name = django_filters.CharFilter(field_name='product_center_name', lookup_expr='icontains', label='Product Center Name',
                                   widget=forms.TextInput(
                                       attrs={'class': "form-control",
                                              'placeholder': 'Product Center Name'}))
    date = django_filters.DateFilter(field_name='date', lookup_expr='icontains',
                                     label='Date Time',
                                     widget=forms.DateInput(
                                         attrs={'class': "form-control",
                                                'type': 'date'
                                                }))

    class Meta:
        model = ProductCenter
        fields = ['product_center_name', 'date']
