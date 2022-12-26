from  django import forms


class ContactForm(forms.Form):  # form of the E=mail feedback
    the_name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваше Имя', 'class': 'form-control valid'}
        )

    )

    e_mail = forms.CharField(
         widget=forms.EmailInput(
            attrs={'placeholder': 'Ваш  Email', 'class': 'form-control valid'}  # form of the E=mail feedback
        )

    )

    topic = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Тема', 'class': 'form-control valid'}
        )

    )

    message = forms.CharField(
        min_length=20,
        widget = forms.Textarea (
            attrs={'placeholder': 'Ваше сообщение', 'col': 30, 'rows': 9, 'class' : 'form-control w-100' }  # form of the E=mail feedback
        )

    )