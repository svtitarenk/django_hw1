from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    # переопределяем инициализацию формы, чтобы сделать форму с определенным стилем
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # необходимо сделать цикл, в котором будем изменять стили полей
        for field_name, field in self.fields.items():
            # можем сделать проверку
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        # fields = "__all__"
        exclude = ("owner",)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        check_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        if name in check_list:
            raise ValidationError('Это же шины, выберите подходящее имя для нее')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        check_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        if description in check_list:
            raise ValidationError('Это же шины, выберите подходящее описание, а не это вот всё')
        return description


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ("is_published", "description", "category",)


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = ('name', 'version_number', 'is_current',)
