from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
import re


def validate_full_name(value):
    if len(value.strip()) < 3:
        raise ValidationError("Full name must be at least 3 characters.")

    if not re.fullmatch(r"[A-Za-z ]+", value):
        raise ValidationError("Full name can contain only letters and spaces.")


def validate_gmail(value):
    if not re.fullmatch(r"[A-Za-z0-9._%+-]+@gmail\.com", value):
        raise ValidationError("Enter a valid Gmail address.")


def validate_mobile(value):
    if not re.fullmatch(r"[6-9]\d{9}", value):
        raise ValidationError(
            "Mobile number must contain exactly 10 digits and start with 6, 7, 8, or 9."
        )


def validate_password(value):

    if len(value) < 8:
        raise ValidationError("Password must be at least 8 characters.")

    if not re.search(r"[A-Z]", value):
        raise ValidationError("Password must contain at least one uppercase letter.")

    if not re.search(r"[a-z]", value):
        raise ValidationError("Password must contain at least one lowercase letter.")

    if not re.search(r"\d", value):
        raise ValidationError("Password must contain at least one number.")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
        raise ValidationError("Password must contain at least one special character.")


class User(models.Model):

    full_name = models.CharField(
        max_length=100,
        validators=[validate_full_name]
    )

    username = models.CharField(
        max_length=30,
        unique=True
    )

    email = models.EmailField(
        unique=True,
        validators=[validate_gmail]
    )

    mobile = models.CharField(
        max_length=10,
        unique=True,
        validators=[validate_mobile]
        
    )

    password = models.CharField(
        max_length=255,
        validators=[validate_password]
    )
    otp= models.CharField(default='', max_length=6)  # Field to store OTP
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name