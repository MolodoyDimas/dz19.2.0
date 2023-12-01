from django import forms
from catalog.models import Product, Version

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name_product', 'description', 'image', 'category', 'purchase_price',)

    def clean_name_product(self):
        ban_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        cleaned_data = self.cleaned_data['name_product']

        if cleaned_data.lower() in ban_list:
            raise forms.ValidationError('Вы используете запрещенное слово')

        return cleaned_data


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

