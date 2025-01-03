from django.db import models
import re
from phonenumbers import parse, is_valid_number
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

"""
this is the model who manage the user. the authentification will be with email and password.
the clean method verify the data as phone number and email (@icloud, @gmail)
"""
class ManagementUser(AbstractUser):
    phone_number = models.CharField(max_length=18, unique=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  
    def clean(self):
        super().clean()
        try:
            phone_number_parsed = parse(self.phone_number)
            if not is_valid_number(phone_number_parsed):
                raise ValidationError("Your phone number is invalid!")
        except Exception as e:
            raise ValidationError(f"Invalid phone number: {str(e)}")
        email = self.email  
        if not email:
            raise ValidationError("The email cannot be empty.")
        if ManagementUser.objects.filter(email=email).exclude(id=self.id).exists():
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValidationError("Invalid email format. Email must contain '@' followed by a domain.")
"""
this is the informations of admin
email = floriandiangongo22@gmail.com
username = florian
password = florian
"""