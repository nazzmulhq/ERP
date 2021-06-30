from django import forms

from productionplanning.models.CRP import CRP, CRPTrack


class CRPTrackForm(forms.ModelForm):
    class Meta:
        model = CRPTrack
        fields = '__all__'


class AddCRPForm(forms.ModelForm):
    class Meta:
        model = CRP
        exclude = ['id', ]

        widgets = {
            'crp_track': forms.TextInput(attrs={'class': "form-control ",


                                                }),
            'operationSequence': forms.TextInput(attrs={'class': "form-control ",
                                                        'type': 'text',


                                                        }),
            'productioncneter': forms.TextInput(attrs={'class': "form-control ",
                                                       'type': 'text',


                                                       }),
            'AvalStartDate': forms.TextInput(attrs={'class': "form-control ",
                                                    'type': 'text',


                                                    }),
            'StartDate': forms.DateInput(attrs={'class': "form-control ",
                                                'type': 'date'

                                                }),
            'reqdcapunit': forms.TextInput(attrs={'class': "form-control ",
                                                  'type': 'text',


                                                  }),
            'ReqdMcHrByUnit': forms.TextInput(attrs={'class': "form-control ",
                                                     'type': 'text'

                                                     }),

            'AvalStartTime': forms.TextInput(attrs={'class': "form-control ",
                                                    'type': 'text',


                                                    }),
            'AvalMcHrOrDay': forms.TextInput(attrs={'class': "form-control ",
                                                    'type': 'text',


                                                    }),
            'NoOfMCByResAval': forms.TextInput(attrs={'class': "form-control ",
                                                      'type': 'text',


                                                      }),
            'AvalCAPByDay': forms.TextInput(attrs={'class': "form-control ",
                                                   'type': 'text',


                                                   }),

            'ReqdCAPByDay': forms.TextInput(attrs={'class': "form-control ",
                                                   'type': 'text'

                                                   }),
            'ReqdMcHour': forms.TextInput(attrs={'class': "form-control ",
                                                 'type': 'text'

                                                 }),

            'StartTime': forms.TimeInput(attrs={'class': "form-control ",
                                                'type': 'time'

                                                }),
            'EndTime': forms.TimeInput(attrs={'class': "form-control ",
                                              'type': 'time'

                                              }),
            'EndDate': forms.DateInput(attrs={'class': "form-control ",
                                              'type': 'date'

                                              }),
            'NoOfMcByRes': forms.TextInput(attrs={'class': "form-control ",
                                                  'type': 'text'

                                                  }),

            'mc_id_no': forms.TextInput(attrs={'class': "form-control ",
                                               'type': 'text'}),

        }


class UpdateCRPForm(forms.ModelForm):
    class Meta:
        model = CRP
        exclude = ['id', ]

        widgets = {
            'crp_track': forms.TextInput(attrs={'class': "form-control ",
                                                'type': 'hidden'

                                                }),
            'operationSequence': forms.TextInput(attrs={'class': "form-control ",
                                                        'type': 'text',
                                                        'readonly': 'readonly'

                                                        }),
            'productioncneter': forms.TextInput(attrs={'class': "form-control ",
                                                       'type': 'text',
                                                       'readonly': 'readonly'

                                                       }),
            'AvalStartDate': forms.TextInput(attrs={'class': "form-control ",
                                                    'type': 'text',
                                                    'readonly': 'readonly'

                                                    }),
            'StartDate': forms.DateInput(attrs={'class': "form-control ",
                                                'type': 'date'

                                                }),
            'reqdcapunit': forms.TextInput(attrs={'class': "form-control ",
                                                  'type': 'text',
                                                  'readonly': 'readonly'

                                                  }),
            'ReqdMcHrByUnit': forms.TextInput(attrs={'class': "form-control ",
                                                     'type': 'text'

                                                     }),

            'AvalStartTime': forms.TextInput(attrs={'class': "form-control ",
                                                    'type': 'text',
                                                    'readonly': 'readonly'

                                                    }),
            'AvalMcHrOrDay': forms.TextInput(attrs={'class': "form-control ",
                                                    'type': 'text',
                                                    'readonly': 'readonly'

                                                    }),
            'NoOfMCByResAval': forms.TextInput(attrs={'class': "form-control ",
                                                      'type': 'text',
                                                      'readonly': 'readonly'

                                                      }),
            'AvalCAPByDay': forms.TextInput(attrs={'class': "form-control ",
                                                   'type': 'text',
                                                   'readonly': 'readonly'

                                                   }),

            'ReqdCAPByDay': forms.TextInput(attrs={'class': "form-control ",
                                                   'type': 'text'

                                                   }),
            'ReqdMcHour': forms.TextInput(attrs={'class': "form-control ",
                                                 'type': 'text'

                                                 }),

            'StartTime': forms.TimeInput(attrs={'class': "form-control ",
                                                'type': 'time'

                                                }),
            'EndTime': forms.TimeInput(attrs={'class': "form-control ",
                                              'type': 'time'

                                              }),
            'EndDate': forms.DateInput(attrs={'class': "form-control ",
                                              'type': 'date'

                                              }),
            'NoOfMcByRes': forms.TextInput(attrs={'class': "form-control ",
                                                  'type': 'text'

                                                  }),

            'mc_id_no': forms.TextInput(attrs={'class': "form-control ",
                                               'type': 'text'}),

        }
