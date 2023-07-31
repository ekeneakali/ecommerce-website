from django import forms

from.models import *

from django.core import validators

from django.contrib.auth.models import User

from django.contrib.auth.forms import (UserCreationForm, UserChangeForm)

from django.contrib.auth.forms import SetPasswordForm

from django.contrib.auth.forms import PasswordResetForm

from django.forms import ClearableFileInput





# CHOICE = [
#     ('select1', 'seller'),
#     ('select3', 'buyer'),
#     ('select3', 'buyer/seller'),

# ]

class Register(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter last name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'enter your email'}))
    # account = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'select account'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'enter password1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'enter password2'}))
    botfield = forms.CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])

    

    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']

        if commit:
            user.save()
        return user

class EditProfile(UserChangeForm):

    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']



class Info(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    date = forms.IntegerField()
    notify = forms.BooleanField(label='notify me when needed')
    botfield = forms.CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])


class ContactForm(forms.ModelForm):
    botfield = forms. CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])


    class Meta():
        model = Contact
        fields = '__all__'

class NewsLetterForm(forms.ModelForm):
    botfield = forms. CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])


    class Meta():
        model = NewsLetter
        fields = '__all__'
        exclude = ['name']



class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = User()
        fields = ['new_password1', 'new_password2']


class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


class SelectForm(forms.ModelForm):
    botfield = forms. CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])

    

    class Meta():
        model = Select
        fields = '__all__'
        exclude = ['country']

class SellersAccountForm(forms.ModelForm):
    botfield = forms. CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])

    

    class Meta():
        model = SellersAccount
        fields = '__all__'

class BuyersAccountForm(forms.ModelForm):
    botfield = forms. CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])

    

    class Meta():
        model = BuyersAccount
        fields = '__all__'

class Buyers_sellersAccountForm(forms.ModelForm):
    botfield = forms. CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])

    

    class Meta():
        model = Buyers_Sellers
        fields = '__all__'





        
        

class ProductForm(forms.ModelForm):
    botfield = forms. CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])

    

    class Meta():
        model = Product
        fields = '__all__'
        exclude = ['likes', 'favourite', 'num_site', 'user', 'old_price', 'new_price', 'cost', 'size', 'img_view', 'img_slider']
        # widgets = {
        #     'image': ClearableFileInput(attrs={'multiple': True}),
        # }

        

class Order2Form(forms.ModelForm):
    botfield = forms. CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])


    class Meta():
        model = Order2
        fields = '__all__'
        exclude = ['user']

class Buy_Now_ShippingForm(forms.ModelForm):
    botfield = forms. CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])


    class Meta():
        model = Buy_Now_Shipping
        fields = '__all__'
        exclude = ['user', 'category']

class OrderForm(forms.ModelForm):
    botfield = forms. CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])


    class Meta():
        model = Order
        fields = '__all__'
        exclude = ['user']

class Cart_ShippingForm(forms.ModelForm):
    botfield = forms. CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])


    class Meta():
        model = Cart_Shipping
        fields = '__all__'
        exclude = ['user', 'category']




class PostForm(forms.ModelForm):
    botfield = forms. CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])


    class Meta():
        model = Post
        fields = '__all__'
        exclude = ['slug', 'author',  'status', 'likes', 'favourite', 'num_site','user',
        'phone_number', 'email', 'country', 'thumbnail', 'multiple']
        widgets = {
            'image': ClearableFileInput(attrs={'multiple': True}),
        }



class ProfileForm(forms.ModelForm):
    botfield = forms. CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])


    class Meta():
        model = Profile
        fields = '__all__'
