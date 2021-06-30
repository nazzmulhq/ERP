import django_filters
from django import forms
from productionplanning.models.Finished import Finished


class FinishedFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(field_name='id', lookup_expr='icontains', label='Finished ID',
                                   widget=forms.TextInput(
                                       attrs={'class': "form-control",
                                              'placeholder': 'Finished ID'}))
    date = django_filters.DateFilter(field_name='date', lookup_expr='icontains',
                                     label='Date Time',
                                     widget=forms.DateInput(
                                         attrs={'class': "form-control",
                                                'type': 'date'
                                                }))

    class Meta:
        model = Finished
        fields = ['id', 'date']
