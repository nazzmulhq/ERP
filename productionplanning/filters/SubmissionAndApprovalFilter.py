import django_filters
from django import forms
from productionplanning.models.SubmissionAndApproval import SubmissionAndApproval


class SubmissionAndApprovalFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(field_name='id', lookup_expr='icontains', label='Submission & Approval ID',
                                   widget=forms.TextInput(
                                       attrs={'class': "form-control",
                                              'placeholder': 'Submission & Approval ID'}))
    data_of_submission = django_filters.DateFilter(field_name='data_of_submission', lookup_expr='icontains',
                                                   label='Date Time',
                                                   widget=forms.DateInput(
                                                       attrs={'class': "form-control",
                                                              'type': 'date'
                                                              }))
    r_and_d_order_ref_no = django_filters.CharFilter(field_name='r_and_d_order_ref_no', lookup_expr='icontains',
                                                     label='r_and_d_order_ref_no',
                                                     widget=forms.TextInput(
                                                         attrs={'class': "form-control",
                                                                'type': 'text',
                                                                'placeholder': "Enter R&D / Order Ref. No"
                                                                }))

    product_no = django_filters.CharFilter(field_name='product_no', lookup_expr='icontains',
                                           label='product_no',
                                           widget=forms.TextInput(
                                               attrs={'class': "form-control",
                                                      'type': 'text',
                                                      'placeholder': "Enter Product No."
                                                      }))
    item_ref_no = django_filters.CharFilter(field_name='item_ref_no', lookup_expr='icontains',
                                            label='item_ref_no',
                                            widget=forms.TextInput(
                                                attrs={'class': "form-control",
                                                       'type': 'text',
                                                       'placeholder': "Enter Item Ref No."
                                                       }))

    class Meta:
        model = SubmissionAndApproval
        fields = ['id', 'data_of_submission', 'r_and_d_order_ref_no', 'product_no', 'item_ref_no']
