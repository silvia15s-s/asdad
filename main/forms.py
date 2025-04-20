from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'phone', 'address', 'profile_image',
                 'card_number', 'card_expiry', 'card_cvv', 'bank_name']
        
    def clean_card_number(self):
        card_number = self.cleaned_data.get('card_number')
        if card_number:
            # Удаляем все пробелы и нецифровые символы
            card_number = ''.join(c for c in card_number if c.isdigit())
        return card_number

class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=20, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password1', 'password2', 
                 'phone', 'address', 'profile_image')