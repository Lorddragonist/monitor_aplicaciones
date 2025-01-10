from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(
        unique=True,
        validators=[EmailValidator(message="Debe ser un correo válido de Claro (@claro.com.co)")],
        error_messages={
            'unique': "Ya existe un usuario con este correo."
        },
    )

    def save(self, *args, **kwargs):
        if not self.email.endswith('@claro.com.co'):
            raise ValueError("El correo debe terminar en @claro.com.co")
        super().save(*args, **kwargs)
