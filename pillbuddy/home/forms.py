from django import forms
from django.forms import EmailField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from dashboard.models import Drug


class UserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    email = EmailField(label=_("Email address"), required=True,
        help_text=_("Required."))
    

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("That user is already taken")
        return username

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.username = self.clean_username()
        if commit:
            user.save()
        return user
class SetUpDrugForm(forms.Form):
    Name = forms.CharField(max_length=30, required=True)
    Description = forms.CharField(max_length=30, required=True)
    MaxPerDay = forms.IntegerField(required = True)
    TakenToday = forms.IntegerField(required = True)
    Slot = forms.IntegerField(required = True)

    def clean_Name(self):
        data = self.cleaned_data['Name']
        return data
    def clean_Description(self):
        data = self.cleaned_data['Description']
        return data
    def clean_MaxPerDay(self):
        data = self.cleaned_data['MaxPerDay']
        return data
    def clean_TakenToday(self):
        data = self.cleaned_data['TakenToday']
        return data
    def clean_Slot(self):
        data = self.cleaned_data['Slot']
        return data


class SetUpSchedule(forms.Form):
    stuff=[(1,Drug.objects.get(slot=1).name),(2,Drug.objects.get(slot=2).name),(3,Drug.objects.get(slot=3).name)]
    Medicines = forms.MultipleChoiceField(choices=stuff, widget=forms.CheckboxSelectMultiple())
    Frequency = forms.ChoiceField(choices=[('Weekly','weekly'),('Daily','daily')])
    start_date = forms.DateField(widget=forms.SelectDateWidget())
    start_time = forms.TimeField()
    def clean_Medicines(self):
        data = self.cleaned_data['Medicines']
        return data
    def clean_Frequency(self):
        data = self.cleaned_data['Frequency']
        return data
    def clean_start_date(self):
        data = self.cleaned_data['start_date']
        return data
    def clean_start_time(self):
        data = self.cleaned_data['start_time']
        return data

