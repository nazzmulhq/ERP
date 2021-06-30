from django import forms
from ..models.MRP import MRPGeneralData, MRP


class MREGenetalForm(forms.ModelForm):
    class Meta:
        model = MRPGeneralData
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'class': "form-control",
                                           'type': 'date', }),
            'order_ref': forms.TextInput(attrs={'class': "form-control",
                                                'placeholder': "Enter Order Ref.",
                                                }),
            'mrp_purpose': forms.Select(attrs={'class': "form-control",

                                               'placeholder': "Enter Product Description",

                                               }),
            'responsible_dept': forms.Select(attrs={'class': "form-control",
                                                    'required': "required",
                                                    }),
            'final_prod_no': forms.TextInput(attrs={'class': "form-control",
                                                    'required': "required",
                                                    'placeholder': "Enter Finished Product No."
                                                    }),
            'final_prod_des': forms.TextInput(attrs={'class': "form-control",
                                                     'required': "required",
                                                     'placeholder': "Enter Finished Product Des."
                                                     }),
            'bom_ref_no': forms.TextInput(attrs={'class': "form-control",
                                                 'required': "required",
                                                 'placeholder': "Enter BOM Ref.",
                                                 }),
        }


class MRPForm(forms.ModelForm):
    class Meta:
        model = MRP
        fields = '__all__'
        widgets = {
            'mrp_general_data': forms.TextInput(attrs={'class': "form-control",
                                                       }),
            'raw_material': forms.TextInput(attrs={'class': "form-control",

                                             }),
            'product_description': forms.TextInput(attrs={'class': "form-control",
                                                       'placeholder': "Enter Product Description",
                                                       }),
            'unit': forms.TextInput(attrs={'class': "form-control",
                                           }),
            'qty_required': forms.TextInput(attrs={'class': "form-control",
                                                   'placeholder': "Enter REQUIRED QTY"
                                                   }),
            'total_reqd_qty': forms.TextInput(attrs={'class': "form-control",
                                                     'placeholder': "Enter TOTAL REQD QTY"
                                                     }),
            'required_date': forms.DateInput(attrs={'class': "form-control",
                                                    'type': 'date',
                                                    'placeholder': "Enter TOTAL REQD QTY"
                                                    }),
            'source': forms.Select(attrs={'class': "form-control",
                                          'placeholder': "Enter Required Date",
                                          }),
            'source_name': forms.TextInput(attrs={'class': "form-control",
                                                  'placeholder': "Enter SOURCE NAME",
                                                  }),
            'action_required': forms.Select(attrs={'class': "form-control",
                                                      'placeholder': "Enter ACTION REQUIRED",
                                                      }),
            'status_s': forms.TextInput(attrs={'class': "form-control",
                                             'placeholder': "Enter Status",
                                             }),
            'time_to_get': forms.TextInput(attrs={'class': "form-control",
                                                  'placeholder': "Enter TIME TO GET",
                                                  })
        }


class UpdateMRPForm(forms.ModelForm):
    class Meta:
        model = MRP
        exclude = ['mrp_general_data']
        widgets = {
            'raw_id': forms.TextInput(attrs={'class': "form-control",
                                                   'readonly': 'readonly'
                                             }),

            'product_description': forms.TextInput(attrs={'class': "form-control",
                                                          'readonly': 'readonly',
                                                       'placeholder': "Enter Product Description",
                                                       }),
            'unit': forms.TextInput(attrs={'class': "form-control",
                                           'readonly': 'readonly'
                                           }),
            'qty_required': forms.TextInput(attrs={'class': "form-control",
                                                   'placeholder': "Enter REQUIRED QTY",
                                                   'readonly': 'readonly'
                                                   }),
            'total_reqd_qty': forms.TextInput(attrs={'class': "form-control",
                                                     'placeholder': "Enter TOTAL REQD QTY"
                                                     }),
            'required_date': forms.DateInput(attrs={'class': "form-control",
                                                    'type': 'date',
                                                    'placeholder': "Enter TOTAL REQD QTY"
                                                    }),
            'source': forms.Select(attrs={'class': "form-control",
                                          'placeholder': "Enter Required Date",
                                          }),
            'source_name': forms.TextInput(attrs={'class': "form-control",
                                                  'placeholder': "Enter SOURCE NAME",
                                                  }),
            'action_required': forms.Select(attrs={'class': "form-control",
                                                      'placeholder': "Enter ACTION REQUIRED",
                                                      }),
            'status_s': forms.TextInput(attrs={'class': "form-control",
                                             'placeholder': "Enter Status",
                                             }),
            'time_to_get': forms.TextInput(attrs={'class': "form-control",
                                                  'placeholder': "Enter TIME TO GET",
                                                  })
        }