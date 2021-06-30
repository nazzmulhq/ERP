from django import forms
from productionplanning.models.OperationList import OperationList
from productionplanning.models.OperationSequence import OperationSequence


class ForDate(forms.DateInput):
    input_type = 'date'
    attrs = {
        'class': "form-control",
        'placeholder': "Enter purchase date",
        'required': "required"

    }


class ForTime(forms.TimeInput):
    input_type = 'time'
    attrs = {
        'class': "form-control",
        'placeholder': "Enter purchase date",
        'required': "required",
        'readonly': 'readonly'

    }


class OperationListForm(forms.ModelForm):
    class Meta:
        model = OperationList
        fields = "__all__"

        widgets = {
            'id': forms.TextInput(attrs={'class': "form-control",
                                                     }),
            'dataOfcreation': forms.TextInput(attrs={'class': "form-control",
                                                     "type": 'date',
                                                     'required': "required",
                                                     'placeholder': "Enter Date of creation",

                                                     }),
            'usage': forms.Select(attrs={'class': "form-control",
                                         'required': "required"
                                         }),
            'productioncategory': forms.Select(attrs={'class': "form-control",
                                                      'required': "required",
                                                      }),
            'productdescription': forms.TextInput(attrs={'class': "form-control",
                                                         'required': "required",
                                                         'placeholder': "Enter Product Description"
                                                         }),
            'responsibledept': forms.TextInput(attrs={'class': "form-control",
                                                      'required': "required",
                                                      'placeholder': "Enter Responsible Dept"
                                                      }),
            'previousref': forms.TextInput(attrs={'class': "form-control",
                                                  'placeholder': "Enter Previous Ref."
                                                  }),
            'orderref': forms.TextInput(attrs={'class': "form-control",
                                               'required': "required",
                                               'placeholder': "Enter Order Ref"
                                               }),

        }


class ViewOperationListForm(forms.ModelForm):
    class Meta:
        model = OperationList
        fields = "__all__"

        widgets = {
            'id': forms.TextInput(attrs={'class': "form-control",
                                         'readonly': 'readonly'
                                         }),
            'dataOfcreation': forms.TextInput(attrs={'class': "form-control",
                                                     'readonly': 'readonly'
                                                     }),
            'usage': forms.TextInput(attrs={'class': "form-control",
                                            'readonly': 'readonly'
                                            }),
            'productioncategory': forms.TextInput(attrs={'class': "form-control",
                                                         'readonly': 'readonly'
                                                         }),
            'productdescription': forms.TextInput(attrs={'class': "form-control",
                                                         'readonly': 'readonly'
                                                         }),
            'responsibledept': forms.TextInput(attrs={'class': "form-control",
                                                      'readonly': 'readonly'
                                                      }),
            'previousref': forms.TextInput(attrs={'class': "form-control",
                                                  'readonly': 'readonly'
                                                  }),
            'orderref': forms.TextInput(attrs={'class': "form-control",
                                               'readonly': 'readonly'
                                               }),
        }


class OperationSequenceForm(forms.ModelForm):
    class Meta:
        model = OperationSequence
        exclude = ["operation_list"]
        widgets = {
            'id': forms.TextInput(attrs={'class': "form-control",
                                         'required': "required",
                                         'placeholder': "Enter Date of creation",
                                         'type':'hidden'

                                         }),
            'operationSequence': forms.TextInput(attrs={'class': "form-control",
                                                        'required': "required",
                                                        'placeholder': "Enter Operation Sequence",

                                                        }),
            'production_center': forms.Select(attrs={'class': "form-control",
                                                        'required': "required",
                                                        'placeholder': "Enter Production Center",

                                                        }),

            'baseunit': forms.TextInput(attrs={'class': "form-control",
                                               'required': "required",
                                               'placeholder': "Enter Base unit",

                                               }),
            'reqdcapunit': forms.TextInput(attrs={'class': "form-control",
                                                  'required': "required",
                                                  'placeholder': "Enter Reqd Cap/Unit",

                                                  }),
            'standardtime': forms.TextInput(attrs={'class': "form-control",
                                                   'required': "required",
                                                   'placeholder': "Enter Standard time",

                                                   }),
            'allowancetime': forms.TextInput(attrs={'class': "form-control",
                                                    'required': "required",
                                                    'placeholder': "Enter Allowance time",

                                                    }),
            'totaltime': forms.TextInput(attrs={'class': "form-control",
                                                'required': "required",
                                                'placeholder': "Enter Total time",

                                                }),
            'componentsuser': forms.TextInput(attrs={'class': "form-control",
                                                     'required': "required",
                                                     'placeholder': "Enter Components user",

                                                     }),
            'toolsrequired': forms.TextInput(attrs={'class': "form-control",

                                                    'placeholder': "Enter Tools required",

                                                    }),
            'inspectioncenter': forms.TextInput(attrs={'class': "form-control",
                                                       'required': "required",
                                                       'placeholder': "Enter Inspection Center",

                                                       }),
            'exceptionmsg': forms.TextInput(attrs={'class': "form-control",

                                                   'placeholder': "Enter Exception msg",

                                                   })

        }

