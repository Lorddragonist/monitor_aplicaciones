from django.db import models


class ApiEndpoint(models.Model):
    name = models.CharField(max_length=255, help_text="Nombre del servicio o API")
    url = models.URLField(unique=True, help_text="URL del endpoint")
    last_checked = models.DateTimeField(
        null=True, blank=True, help_text="Última vez que se revisó"
    )
    status = models.BooleanField(default=True, help_text="Estado actual del servicio")

    def __str__(self):
        return self.name
