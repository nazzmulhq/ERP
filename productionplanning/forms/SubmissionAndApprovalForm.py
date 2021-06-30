from django import forms
from ..models.SubmissionAndApproval import SubmissionAndApproval


class SubmissionAndApprovalForm(forms.ModelForm):
    class Meta:
        model = SubmissionAndApproval
        fields = "__all__"
        widgets = {
            'data_of_submission': forms.DateInput(attrs={
                'class': "form-control",
                'type': 'date'
            }),
            'r_and_d_order_ref_no': forms.TextInput(attrs={'class': "form-control",
                                                           'placeholder': "R&D / Order Ref. No", }),
            'product_no': forms.TextInput(attrs={'class': "form-control",
                                                 'placeholder': "Enter Product No."}),
            'item_description': forms.TextInput(attrs={'class': "form-control",
                                                       'placeholder': "Enter Item Description", }),
            'color_per_variety': forms.TextInput(attrs={'class': "form-control",
                                                        'placeholder': "Color / Variety", }),
            'submission_product': forms.Select(attrs={'class': "form-control", }),
            'submission_type': forms.Select(attrs={'class': "form-control", }),
            'submission_item': forms.Select(attrs={'class': "form-control", }),
            'item_ref_no': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Enter Item Ref No.", }),
            'round_of_submission': forms.Select(
                attrs={'class': "form-control", 'placeholder': "Enter Round of Submission:"}),
            'pland_subm_date': forms.DateInput(attrs={
                'class': "form-control",
                'type': 'date',
            }),
            'submitted_date': forms.DateInput(attrs={
                'class': "form-control",
                'type': 'date'}),
            'result': forms.Select(attrs={'class': "form-control", 'placeholder': "Enter Result"
                                             }),
            'comment': forms.TextInput(attrs={'class': "form-control",
                                              'placeholder': "Enter Comment"}),
            'approval_or_rejection_date': forms.DateInput(attrs={'class': "form-control",
                                                                 'type': 'date',
                                                                 }),
        }
