from django import forms
from datetime import date



            
class AdminAddMerbershipForm2(forms.Form):
    SEX_CHOICES = (
    ('M','Male'),
    ('F','Female'),
    )
    id = forms.CharField(required=True, label="Client ID", max_length=10, widget= forms.TextInput(attrs={'placeholder':'Id Client'}))
    last_name   = forms.CharField(required=True, label="Last Name", max_length=40, widget= forms.TextInput(attrs={'placeholder':'Last Name'}))
    first_name  = forms.CharField(required=True, label="First Name", max_length=20, widget= forms.TextInput(attrs={'placeholder':'First Name'}))
    phone       = forms.CharField(required=True, label="Phone", max_length=15, widget= forms.TextInput(attrs={'placeholder':'Phone'}))
    address     = forms.CharField(required=True, label="Address", max_length=120, widget= forms.TextInput(attrs={'placeholder':'Address'}))
    city        = forms.CharField(required=True, label="City", max_length=30, widget= forms.TextInput(attrs={'placeholder':'City'}))
    dmybir      = forms.DateField(required=True,label='Date Of Birth',widget=forms.TextInput(attrs={'class': 'form-control datepicker', 'type': 'date'}))
    sex         = forms.ChoiceField(required=True, choices= SEX_CHOICES)
    idorigin    = forms.CharField(required=True, label="ID Client Origin", max_length=30, widget= forms.TextInput(attrs={'placeholder':'ID Client Origin'}))
    dmyadm      = forms.DateField(required=True, label="Date of Admission",widget=forms.TextInput(attrs={'class': 'form-control datepicker', 'type': 'date'}))
    
    
    def __init__(self, *args, **kwargs):
        super(AdminAddMerbershipForm2, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })
        self.fields['dmyadm'].initial = date.today()
        
        
        
class CliGeoposAddForm(forms.Form):
    identification = forms.CharField(required=True, label='Identification', max_length=10, widget=forms.NumberInput(attrs={'placeholder': 'Identification'}))
    type = forms.ChoiceField(label = 'Tipo', required=True, choices= [('D', 'Dwelling'), ('N', 'Work')]) 
    latitude = forms.FloatField(required=True, label='Latitud', widget=forms.NumberInput(attrs={'placeholder': 'latitude'}))
    length = forms.FloatField(required=True, label='Longitud', widget=forms.NumberInput(attrs={'placeholder': 'length'}))
    observation = forms.CharField(required=True, label='Observacion', max_length=150, widget=forms.Textarea(attrs={'placeholder': 'Observation'}))

    def __init__(self, *args, **kwargs):
        super(CliGeoposAddForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control  input-sm',
                'style': 'float:left'
            })
        self.fields['observation'].widget.attrs['style'] = 'height: 60px;'
