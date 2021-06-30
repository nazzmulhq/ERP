from django import forms
from productionplanning.models.Finished import Finished


class FinishedForm(forms.ModelForm):
    class Meta:
        model = Finished
        exclude = ['prod_center']

        widgets = {
            'operations_list': forms.Select(attrs={'class': "form-control", 'required': "required", }),
            'product_category': forms.Select(attrs={'class': "form-control",
                                                    'required': "required",

                                                    }),
            'product_description': forms.TextInput(attrs={'class': "form-control",
                                                          'required': "required",
                                                          'placeholder': "Enter Product Description",

                                                          }),
            'unit': forms.Select(attrs={'class': "form-control",
                                        'required': "required",
                                        }),
            'price': forms.TextInput(attrs={'class': "form-control",
                                            'required': "required",
                                            'placeholder': "Enter Product Price"
                                            }),
            'price_unit': forms.Select(attrs={'class': "form-control",
                                              'required': "required"
                                              }),
            'pur_or_prd': forms.Select(attrs={'class': "form-control",
                                              'required': "required"
                                              }),
            'date_0f_pur_or_prd': forms.DateInput(attrs={'class': "form-control",
                                                         'type': 'date',
                                                         'required': "required"
                                                         }),
            'time_0f_pur_or_prd': forms.TimeInput(attrs={'class': "form-control",
                                                         'type': 'time',
                                                         'required': "required"
                                                         }),
            'source': forms.Select(attrs={'class': "form-control",
                                          'required': "required"
                                          }),
            'previous_ref': forms.TextInput(attrs={'class': "form-control",
                                                   'placeholder': "Enter previous referance",
                                                   'required': "required",
                                                   }),
            'lead_time': forms.TextInput(attrs={'class': "form-control",
                                                'placeholder': "Enter lead Time"
                                                }),
            'responsible_dept': forms.TextInput(attrs={'class': "form-control",
                                                       'placeholder': "Enter Res Dept"
                                                       }),
            'usage_ref': forms.TextInput(attrs={'class': "form-control",
                                                'placeholder': "Enter Usage Ref"
                                                }),
            'mrp_responsible': forms.TextInput(attrs={'class': "form-control",
                                                      'required': "required",
                                                      'placeholder': "Enter Mrp Resp"
                                                      }),
            'lot_size': forms.TextInput(attrs={'class': "form-control",
                                               'placeholder': "Enter Lot size"
                                               }),
            'warehouse_location': forms.TextInput(attrs={'class': "form-control",
                                                         'required': "required",
                                                         'placeholder': "Enter Warehouse Location"
                                                         }),
            'shipping_unit': forms.TextInput(attrs={'class': "form-control",
                                                    'placeholder': "Enter Shipping unit"
                                                    }),
            'qty_or_unit': forms.TextInput(attrs={'class': "form-control",
                                                  'placeholder': "Enter Qty/Unit"
                                                  }),
            'gross_wt': forms.TextInput(attrs={'class': "form-control",
                                               'placeholder': "Enter Gross Weight"
                                               }),
            'net_wt': forms.TextInput(attrs={'class': "form-control",
                                             'placeholder': "Enter Net Weight"
                                             }),
            'bom_ref': forms.Select(attrs={'class': "form-control",
                                           'placeholder': "Enter Bom ref.",
                                           'required': "required",
                                           }),
            'product_resp': forms.TextInput(attrs={'class': "form-control",
                                                   'placeholder': "Enter Product Resp."
                                                   }),
            'inspection_ref': forms.TextInput(attrs={'class': "form-control",
                                                     'placeholder': "Enter Inspection Ref."
                                                     }),
            'old_operation_list_ref': forms.TextInput(attrs={'class': "form-control",
                                                             'placeholder': "Enter Old Operation List Ref."
                                                             }),
            'allowance': forms.TextInput(attrs={'class': "form-control",
                                                'placeholder': "Enter Allowance"
                                                }),
            'lab_ref': forms.TextInput(attrs={'class': "form-control",
                                              'placeholder': "Enter Lab Ref."
                                              }),
            'r_and_d_ref': forms.TextInput(attrs={'class': "form-control",
                                                  'placeholder': "Enter R & D Ref."
                                                  }),
            'packing_instruction': forms.TextInput(attrs={'class': "form-control",
                                                          'placeholder': "Enter Packing Instruction"
                                                          }),
            'storage_instruction': forms.TextInput(attrs={'class': "form-control",
                                                          'placeholder': "Enter Storage Instruction"
                                                          }),
        }


class ViewFinishedForm(forms.ModelForm):
    class Meta:
        model = Finished
        exclude = ['prod_center']

        widgets = {
            'operations_list': forms.Select(attrs={'class': "form-control",
                                                   'readonly': 'readonly'

                                                   }),
            'product_category': forms.TextInput(attrs={'class': "form-control",
                                                       'readonly': 'readonly'

                                                       }),
            'product_description': forms.TextInput(attrs={'class': "form-control",

                                                          'readonly': 'readonly'

                                                          }),
            'unit': forms.TextInput(attrs={'class': "form-control",
                                           'readonly': 'readonly'
                                           }),
            'price': forms.TextInput(attrs={'class': "form-control",
                                            'readonly': 'readonly'
                                            }),
            'price_unit': forms.TextInput(attrs={'class': "form-control",
                                                 'readonly': 'readonly'
                                                 }),
            'pur_or_prd': forms.TextInput(attrs={'class': "form-control",
                                                 'readonly': 'readonly'
                                                 }),
            'date_0f_pur_or_prd': forms.DateInput(attrs={'class': "form-control",
                                                         'type': 'date',
                                                         'required': "required",
                                                         'readonly': 'readonly'
                                                         }),
            'time_0f_pur_or_prd': forms.TimeInput(attrs={'class': "form-control",
                                                         'type': 'time',
                                                         'required': "required",
                                                         'readonly': 'readonly'
                                                         }),
            'source': forms.TextInput(attrs={'class': "form-control",
                                             'required': "required",
                                             'readonly': 'readonly'
                                             }),
            'previous_ref': forms.TextInput(attrs={'class': "form-control",

                                                   'readonly': 'readonly',
                                                   }),
            'lead_time': forms.TextInput(attrs={'class': "form-control",

                                                'readonly': 'readonly'
                                                }),
            'responsible_dept': forms.TextInput(attrs={'class': "form-control",
                                                       'readonly': 'readonly'
                                                       }),
            'usage_ref': forms.TextInput(attrs={'class': "form-control",
                                                'readonly': 'readonly'
                                                }),
            'mrp_responsible': forms.TextInput(attrs={'class': "form-control",
                                                      'readonly': 'readonly',
                                                      }),
            'lot_size': forms.TextInput(attrs={'class': "form-control",
                                               'readonly': 'readonly'
                                               }),
            'warehouse_location': forms.TextInput(attrs={'class': "form-control",
                                                         'readonly': 'readonly',
                                                         }),
            'shipping_unit': forms.TextInput(attrs={'class': "form-control",
                                                    'readonly': 'readonly'
                                                    }),
            'qty_or_unit': forms.TextInput(attrs={'class': "form-control",
                                                  'readonly': 'readonly'
                                                  }),
            'gross_wt': forms.TextInput(attrs={'class': "form-control",
                                               'readonly': 'readonly'
                                               }),
            'net_wt': forms.TextInput(attrs={'class': "form-control",
                                             'readonly': 'readonly'
                                             }),
            'bom_ref': forms.Select(attrs={'class': "form-control",
                                           'readonly': 'readonly'
                                           }),
            'product_resp': forms.Select(attrs={'class': "form-control",
                                                'readonly': 'readonly'
                                                }),
            'inspection_ref': forms.TextInput(attrs={'class': "form-control",
                                                     'readonly': 'readonly'
                                                     }),
            'old_operation_list_ref': forms.TextInput(attrs={'class': "form-control",
                                                             'readonly': 'readonly'
                                                             }),
            'allowance': forms.TextInput(attrs={'class': "form-control",
                                                'readonly': 'readonly'
                                                }),
            'lab_ref': forms.TextInput(attrs={'class': "form-control",
                                              'readonly': 'readonly'
                                              }),
            'r_and_d_ref': forms.TextInput(attrs={'class': "form-control",
                                                  'readonly': 'readonly'
                                                  }),
            'packing_instruction': forms.TextInput(attrs={'class': "form-control",
                                                          'readonly': 'readonly'
                                                          }),
            'storage_instruction': forms.TextInput(attrs={'class': "form-control",
                                                          'readonly': 'readonly'
                                                          }),
        }
