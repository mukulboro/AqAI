from django import forms
from .models import CustomUser

class SiteAdminUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "middle_name", "last_name", "is_municipal", "is_public")
        
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match.")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])  # hashes the password
        if commit:
            user.save()
        return user

class AdminLoginForm(forms.Form):
    email = forms.EmailField(max_length=256, widget=forms.EmailInput(attrs={
        "id": "Email",
        "class": "mt-0.5 w-full rounded border-gray-300 p-1 shadow-sm sm:text-sm"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "id": "Email",
        "class": "mt-0.5 w-full rounded border-gray-300 p-1 shadow-sm sm:text-sm"
    }))