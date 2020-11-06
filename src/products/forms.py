from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title=forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'your title'}))
    email = forms.EmailField()
    description =forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'your description',
            'class':'new-class-name two',
            'id': 'my-id-for-text-area',
            'rows': 20,
            'cols': 120
            }))
    price=forms.DecimalField(required=False)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'email'
        ]

    def clean_title(self,*args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "a" in title:
            raise forms.ValidationError("this is not a valid title")
        return title

    def clean_email(self,*args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith('edu'):
            raise forms.ValidationError("this is not a valid email")
        return email

    def clean_price(self,*args, **kwargs):
        price = self.cleaned_data.get("price")
        if price < 100:
            raise forms.ValidationError("price too low")
        return price

class RawProductForm(forms.Form):
    title=forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'your title'}))
    description =forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'your description',
            'class':'new-class-name two',
            'id': 'my-id-for-text-area',
            'rows': 20,
            'cols': 120
            }))
    price=forms.DecimalField()
