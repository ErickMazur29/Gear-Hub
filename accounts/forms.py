from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile

class RegisterForm(UserCreationForm):
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=Profile.GENDER_CHOICES)
    phone = forms.CharField(max_length=11)

    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit)

        Profile.objects.create(
            user=user,
            age=self.cleaned_data['age'],
            gender=self.cleaned_data['gender'],
            phone=self.cleaned_data['phone']
        )

        return user
    
class ProfileUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=100)

    class Meta:
        model = Profile
        fields = ['age', 'gender', 'phone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].initial = self.instance.user.username

    def save(self, commit=True):
        profile = super().save(commit)
        profile.user.username = self.cleaned_data['username']
        profile.user.save()
        return profile