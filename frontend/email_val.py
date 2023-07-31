def clean_email(self):
        email_val = self.cleaned_data.get('email')
        if User.objects.filter(email=email_val).exists():
            raise forms.ValidationError('email already exist')
        return email_val
    