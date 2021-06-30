from django import forms
from productionplanning.models.BOM import BOM
from productionplanning.models.BomAndRawMaterial import BomAndRowMaterial
from productionplanning.models.RawMaterial import RawMaterial


class ForDate(forms.DateInput):
    input_type = 'date'
    attrs = {
        'class': "form-control",
        'placeholder': "Enter purchase date",
        'required': "required"

    }


class ForText(forms.TextInput):
    attrs = {
        'type': 'text',
        'class': "form-control",
        'readonly': 'readonly'

    }


class BOMForm(forms.ModelForm):
    class Meta:
        model = BOM
        fields = '__all__'

        widgets = {
            'productcenter': forms.Select(attrs={'class': "form-control", }),
            'material': forms.SelectMultiple(attrs={'class': "form-control",

                                                    'placeholder': "Enter Product Description",

                                                    }),
            'id': forms.Select(attrs={'class': "form-control",
                                      'required': "required",
                                      }),
            'purpose_of_bom': forms.Select(attrs={'class': "form-control",
                                                  'required': "required"
                                                  }),
            'final_product': forms.TextInput(attrs={'class': "form-control",
                                                    'required': "required",
                                                    'placeholder': "Enter Final Product",
                                                    }),

            'unit_of_meas': forms.TextInput(attrs={'class': "form-control",
                                                   'required': "required",
                                                   'placeholder': "Enter Unit Of Meas",
                                                   }),
            'order_ref': forms.TextInput(attrs={'class': "form-control",
                                                'placeholder': "Enter previous referance",
                                                'required': "required"
                                                }),

            'responsible_dept': forms.TextInput(attrs={'class': "form-control",
                                                       'placeholder': "Enter Res Dept"
                                                       }),
            'options_or_old_bom': forms.TextInput(attrs={'class': "form-control",
                                                         'placeholder': "Enter Options / Old Bom"
                                                         }),
            'valid_from': forms.DateInput(attrs={'class': "form-control",
                                                 'type': 'date'}),
            'valid_to': forms.DateInput(attrs={'class': "form-control",
                                               'type': 'date'}),
            'labref': forms.TextInput(attrs={'class': "form-control",
                                             'required': "required",
                                             'placeholder': "Enter Lab Ref."
                                             }),

        }


class BOMForm2(forms.ModelForm):
    class Meta:
        model = BOM
        fields = '__all__'

        widgets = {
            'valid_from': forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}),
            'valid_to': forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class ViewBOMForm(forms.ModelForm):
    class Meta:
        model = BOM
        exclude = '__all__'

        widgets = {
            'productcenter': forms.TextInput(attrs={
                'type': 'text',
                'class': "form-control",
                'readonly': 'readonly'

            }),
            'material': ForText(),
            'id': ForText(),
            'purpose_of_bom': forms.TextInput(attrs={
                'type': 'text',
                'class': "form-control",
                'readonly': 'readonly'

            }),
            'final_product': forms.TextInput(attrs={
                'type': 'text',
                'class': "form-control",
                'readonly': 'readonly'

            }),
            'unit_of_meas': forms.TextInput(attrs={
                'type': 'text',
                'class': "form-control",
                'readonly': 'readonly'

            }),
            'order_ref': forms.TextInput(attrs={
                'type': 'text',
                'class': "form-control",
                'readonly': 'readonly'

            }),
            'responsible_dept': forms.TextInput(attrs={
                'type': 'text',
                'class': "form-control",
                'readonly': 'readonly'

            }),
            'options_or_old_bom': forms.TextInput(attrs={
                'type': 'text',
                'class': "form-control",
                'readonly': 'readonly'

            }),
            'valid_from': forms.TextInput(attrs={
                'type': 'text',
                'class': "form-control",
                'readonly': 'readonly'

            }),
            'valid_to': forms.TextInput(attrs={
                'type': 'text',
                'class': "form-control",
                'readonly': 'readonly'

            }),
            'labref': forms.TextInput(attrs={
                'type': 'text',
                'class': "form-control",
                'readonly': 'readonly'

            }),

        }


class BomAndRowMaterialForm(forms.ModelForm):
    class Meta:
        model = BomAndRowMaterial
        exclude = ['bom']

        widgets = {
            'product_category': forms.Select(attrs={'class': "form-control",
                                                    'required': "required",
                                                    'readonly': 'readonly'

                                                    }),
            'product_description': forms.TextInput(attrs={'class': "form-control",
                                                          'required': "required",
                                                          'placeholder': "Enter Product Description",
                                                          'readonly': 'readonly'
                                                          }),
            'unit': forms.Select(attrs={'class': "form-control",
                                        'readonly': 'readonly'
                                        }),
            'qty_required': forms.TextInput(attrs={'class': "form-control",
                                                   'required': "required",
                                                   'placeholder': "Enter Product Description",

                                                   }),
            'assigned_stroe': forms.TextInput(attrs={'class': "form-control",
                                                     'required': "required",
                                                     'placeholder': "Enter Assigned Store"
                                                     }),
            'status': forms.TextInput(attrs={'class': "form-control",
                                             'required': "required",
                                             'placeholder': "Enter Product Price"
                                             }),
            'raw_material': forms.TextInput(attrs={'class': "form-control",
                                                   'placeholder': "Enter Raw Material ID",
                                                   'readonly': 'readonly',
                                                   'type': 'hidden'
                                                   }),

        }


class BomAndRowMaterialForm2(forms.ModelForm):
    class Meta:
        model = BomAndRowMaterial
        exclude = ['bom']

        widgets = {
            'product_category': forms.Select(attrs={'class': "form-control product_category",
                                                    'required': "required",
                                                    'readonly': 'readonly'
                                                    }),
            'product_description': forms.TextInput(attrs={'class': "form-control product_description",
                                                          'required': "required",
                                                          'placeholder': "Enter Product Description",
                                                          'readonly': 'readonly'
                                                          }),
            'unit': forms.Select(attrs={'class': "form-control unit",
                                        'readonly': 'readonly'
                                        }),
            'qty_required': forms.TextInput(attrs={'class': "form-control ",
                                                   'required': "required",
                                                   'placeholder': "Enter Product Description",

                                                   }),
            'assigned_stroe': forms.TextInput(attrs={'class': "form-control",
                                                     'required': "required",
                                                     'placeholder': "Enter Assigned Store"
                                                     }),
            'status': forms.TextInput(attrs={'class': "form-control",
                                             'required': "required",
                                             'placeholder': "Enter Product Price"
                                             }),
            'raw_material': forms.TextInput(attrs={'class': "form-control",
                                                   'placeholder': "Enter Raw Material ID",
                                                   'readonly': 'readonly',
                                                   }),

        }


class BomAndRowMaterialForm3(forms.ModelForm):
    class Meta:
        model = BomAndRowMaterial
        exclude = ['bom']

        widgets = {
            'product_category': forms.Select(attrs={'class': "form-control product_category3",
                                                    'required': "required",
                                                    'readonly': 'readonly'
                                                    }),
            'product_description': forms.TextInput(attrs={'class': "form-control product_description3",
                                                          'required': "required",
                                                          'placeholder': "Enter Product Description",
                                                          'readonly': 'readonly'
                                                          }),
            'unit': forms.Select(attrs={'class': "form-control unit3",
                                        'readonly': 'readonly'
                                        }),
            'qty_required': forms.TextInput(attrs={'class': "form-control ",
                                                   'required': "required",
                                                   'placeholder': "Enter Product Description",

                                                   }),
            'assigned_stroe': forms.TextInput(attrs={'class': "form-control",
                                                     'required': "required",
                                                     'placeholder': "Enter Assigned Store"
                                                     }),
            'status': forms.TextInput(attrs={'class': "form-control",
                                             'required': "required",
                                             'placeholder': "Enter Product Price"
                                             }),
            'raw_material': forms.TextInput(attrs={'class': "form-control",
                                                   'placeholder': "Enter Raw Material ID",
                                                   'type': "hidden"
                                                   }),

        }
