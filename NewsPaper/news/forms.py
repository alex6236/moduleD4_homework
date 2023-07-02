from django import forms

class DateFilterForm(forms.Form):
    dataCreation__gt = forms.DateField(label='Дата создания', widget=forms.TextInput(attrs={
            'type': 'date',
            'name': 'date',
            'required': False,
        }))

class TitleFilterForm(forms.Form):
    title__icontains = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={
            'type': 'text',
            'name': 'title',
            'placeholder': 'Поиск по заголовку',
            'required': False,
        }))

class UsernameFilterForm(forms.Form):
    author__authorUser__username__icontains = forms.CharField(label='Автор', widget=forms.TextInput(attrs={
            'type': 'text',
            'name': 'username',
            'placeholder': 'Поиск по имени автора',
            'required': False,
        }))
    