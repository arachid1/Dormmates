from django import forms
from home.models import Post
from home.models import Application

class ApplicationForm(forms.ModelForm):
    # post = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Write a post'
    #     }
    # ))
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    email = forms.EmailField(label='Email', max_length=50)
    bedtime = forms.CharField(label="What time do you sleep")
    graduating_class = forms.ChoiceField(label='Graduating Class', choices=(('NA','NA'),('2018','2018'), ('2019','2019'), ('2020','2020'), ('2021+','2021+')))
    major = forms.CharField(label='Primary Major')


    class Meta:
        model = Post
        fields = ('first_name', 'last_name', 'email', 'bedtime', 'graduating_class', 'major')
        model = Application
