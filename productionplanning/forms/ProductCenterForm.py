from django import forms
from productionplanning.models.ProductCenter import ProductCenter
from productionplanning.models.ProductCenter import CapacityScheduling




class ProductCenterForm(forms.ModelForm):
    class Meta:
        model = ProductCenter
        exclude = ['operationlist']

        widgets = {
            'product_center_name': forms.TextInput(attrs={'class': "form-control",
                                                          'required': "required",
                                                          'placeholder': "Product Center Name"

                                                          }),
            'division': forms.Select(attrs={'class': "form-control",
                                            'required': "required",
                                            }),

            'final_output': forms.Select(attrs={'class': "form-control",
                                                'required': "required"
                                                }),
            'm_by_c_or_tools': forms.TextInput(attrs={'class': "form-control",
                                                      'required': "required",
                                                      'placeholder': "M/C or Tools"
                                                      }),
            'responsible_per': forms.TextInput(attrs={'class': "form-control",
                                                      'required': "required",
                                                      'placeholder': "Enter Responsible Per"
                                                      }),
            'unit': forms.TextInput(attrs={'class': "form-control",
                                           'required': "required",
                                           'placeholder': "Enter Unit"
                                           }),
            'capacity_per_m_by_c': forms.NumberInput(attrs={'class': "form-control",
                                                            'required': "required",
                                                            'placeholder': "Enter  Capacity"
                                                            }),
            'NoOfMByC': forms.NumberInput(attrs={'class': "form-control",
                                                 'placeholder': "Enter no of MC",
                                                 'required': "required",
                                                 }),
            'total_capacity_by_day': forms.NumberInput(attrs={'class': "form-control",
                                                              'placeholder': "Enter total Capacity",

                                                              }),
            'm_by_c_per_operator': forms.TextInput(attrs={'class': "form-control",
                                                            'placeholder': "Enter M/C per Operator."
                                                            }),
            'total_opeartor_by_day': forms.NumberInput(attrs={'class': "form-control",
                                                              'placeholder': "Enter Total Operator/Day"
                                                              }),
            'exception_msg': forms.TextInput(attrs={'class': "form-control",
                                                    'placeholder': "Enter Exp Msg"
                                                    }),

        }



class CapacitySchedulingFormCRP(forms.ModelForm):
    class Meta:
        model = CapacityScheduling
        fields = '__all__'
        widgets = {
            'Date': forms.DateInput(attrs={
                "type": 'date',
                'class': "form-control",
                'required': "required"
            }),
            'AvalCapOrDay': forms.NumberInput(attrs={'class': "form-control ",
                                                     'required': "required",
                                                     'placeholder': "Enter Aval Cap/Day"

                                                     }),
            'CapALlloctdTo': forms.TextInput(attrs={'class': "form-control ",
                                                    'required': "required",
                                                    'placeholder': "Enter Cap Alloc To"

                                                    }),
            'AlloctdCap': forms.TextInput(attrs={'class': "form-control ",
                                                   'required': "required",
                                                   'placeholder': "Enter Allocated Cap"

                                                   }),
            'BalanceCap': forms.TextInput(attrs={'class': "form-control ",
                                                   'required': "required",
                                                   'placeholder': "Enter Balance Cap."

                                                   }),
            'AvalMcOrResHour': forms.TextInput(attrs={'class': "form-control ",
                                                        'required': "required",
                                                        'placeholder': "Enter Aval MC/Res Hour"

                                                        }),
            'ReqdMcOrResHour': forms.TextInput(attrs={'class': "form-control ",
                                                        'required': "required",
                                                        'placeholder': "Enter Req MC/Res Hour"

                                                        }),
            'BalMcOrHour': forms.TextInput(attrs={'class': "form-control ",
                                                    'required': "required",
                                                    'placeholder': "Enter Bal MC/Res Hour"

                                                    }),
            'StartTime': forms.TimeInput(attrs={'class': "form-control ",
                                                'type':'time',
                                                  'required': "required",
                                                  'placeholder': "Start Time"

                                                  }),
            'EndTime': forms.TimeInput(attrs={'class': "form-control ",
                                              'type': 'time',
                                                'required': "required",
                                                'placeholder': "End Time"

                                                }),
            'NoOfMCAlloctd': forms.NumberInput(attrs={'class': "form-control ",
                                                      'required': "required",
                                                      'placeholder': "No of MC Allocated"

                                                      }),

        }



class ViewProductCenterForm(forms.ModelForm):
    class Meta:
        model = ProductCenter
        exclude = ['operationlist']

        widgets = {
            'product_center_name': forms.TextInput(attrs={'class': "form-control",
                                                          'readonly': 'readonly'

                                                          }),
            'division': forms.TextInput(attrs={'class': "form-control",
                                            'readonly': 'readonly'}),

            'final_output': forms.TextInput(attrs={'class': "form-control",
                                                'readonly': 'readonly'
                                                }),
            'm_by_c_or_tools': forms.TextInput(attrs={'class': "form-control",
                                                      'readonly': 'readonly'
                                                      }),
            'responsible_per': forms.TextInput(attrs={'class': "form-control",
                                                      'readonly': 'readonly'
                                                      }),
            'unit': forms.TextInput(attrs={'class': "form-control",
                                           'readonly': 'readonly'
                                           }),
            'capacity_per_m_by_c': forms.NumberInput(attrs={'class': "form-control",
                                                            'readonly': 'readonly'
                                                            }),
            'NoOfMByC': forms.NumberInput(attrs={'class': "form-control",
                                                 'readonly': 'readonly'
                                                 }),
            'total_capacity_by_day': forms.NumberInput(attrs={'class': "form-control",
                                                              'readonly': 'readonly'
                                                              }),
            'm_by_c_per_operator': forms.TextInput(attrs={'class': "form-control",
                                                            'readonly': 'readonly'
                                                            }),
            'total_opeartor_by_day': forms.NumberInput(attrs={'class': "form-control",
                                                              'readonly': 'readonly'
                                                              }),
            'exception_msg': forms.TextInput(attrs={'class': "form-control",
                                                    'readonly': 'readonly'
                                                    }),

        }


class CapacitySchedulingForm(forms.ModelForm):
    class Meta:
        model = CapacityScheduling
        exclude = ['ProductCenterId']
        widgets = {
            'Date': forms.DateInput(attrs={
                "type": 'date',
                'class': "form-control",
                'required': "required"
            }),
            'AvalCapOrDay': forms.NumberInput(attrs={'class': "form-control ",
                                                     'required': "required",
                                                     'placeholder': "Enter Aval Cap/Day"

                                                     }),
            'CapALlloctdTo': forms.TextInput(attrs={'class': "form-control ",
                                                    'required': "required",
                                                    'placeholder': "Enter Cap Alloc To"

                                                    }),
            'AlloctdCap': forms.TextInput(attrs={'class': "form-control ",
                                                   'required': "required",
                                                   'placeholder': "Enter Allocated Cap"

                                                   }),
            'BalanceCap': forms.TextInput(attrs={'class': "form-control ",
                                                   'required': "required",
                                                   'placeholder': "Enter Balance Cap."

                                                   }),
            'AvalMcOrResHour': forms.TextInput(attrs={'class': "form-control ",
                                                        'required': "required",
                                                        'placeholder': "Enter Aval MC/Res Hour"

                                                        }),
            'ReqdMcOrResHour': forms.TextInput(attrs={'class': "form-control ",
                                                        'required': "required",
                                                        'placeholder': "Enter Req MC/Res Hour"

                                                        }),
            'BalMcOrHour': forms.TextInput(attrs={'class': "form-control ",
                                                    'required': "required",
                                                    'placeholder': "Enter Bal MC/Res Hour"

                                                    }),
            'StartTime': forms.TimeInput(attrs={'class': "form-control ",
                                                'type':'time',
                                                  'required': "required",
                                                  'placeholder': "Start Time"

                                                  }),
            'EndTime': forms.TimeInput(attrs={'class': "form-control ",
                                              'type': 'time',
                                                'required': "required",
                                                'placeholder': "End Time"

                                                }),
            'NoOfMCAlloctd': forms.NumberInput(attrs={'class': "form-control ",
                                                      'required': "required",
                                                      'placeholder': "No of MC Allocated"

                                                      }),

        }


class ViewCapacitySchedulingForm(forms.ModelForm):
    class Meta:
        model = CapacityScheduling
        exclude = ['ProductCenterId']
        widgets = {
            'Date': forms.TextInput(attrs={
                'class': "form-control",
                'readonly': 'readonly'
            }),
            'AvalCapOrDay': forms.NumberInput(attrs={'class': "form-control",
                                                     'readonly': 'readonly'

                                                     }),
            'CapALlloctdTo': forms.TextInput(attrs={'class': "form-control",
                                                    'readonly': 'readonly'

                                                    }),
            'AlloctdCap': forms.TextInput(attrs={'class': "form-control",
                                                   'readonly': 'readonly'

                                                   }),
            'BalanceCap': forms.TextInput(attrs={'class': "form-control",
                                                   'readonly': 'readonly'

                                                   }),
            'AvalMcOrResHour': forms.TextInput(attrs={'class': "form-control",
                                                        'readonly': 'readonly'

                                                        }),
            'ReqdMcOrResHour': forms.TextInput(attrs={'class': "form-control",
                                                        'readonly': 'readonly'

                                                        }),
            'BalMcOrHour': forms.TextInput(attrs={'class': "form-control",
                                                    'readonly': 'readonly'

                                                    }),
            'StartTime': forms.NumberInput(attrs={'class': "form-control",
                                                  'readonly': 'readonly'

                                                  }),
            'EndTime': forms.NumberInput(attrs={'class': "form-control",
                                                'readonly': 'readonly'

                                                }),
            'NoOfMCAlloctd': forms.NumberInput(attrs={'class': "form-control",
                                                      'readonly': 'readonly'

                                                      }),

        }
