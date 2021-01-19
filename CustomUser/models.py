from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    """
    Расширение встроеной модели юзера
    """
    email = models.EmailField(_('email address'), unique=True, null=False)

    country = models.ForeignKey('Country', null=True, blank=True, on_delete=models.SET_NULL)
    phone = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        if not CustomUser.objects.filter(email=self.email):
            super().save(*args, **kwargs)
        else:
            self.email = self.username
            super().save(*args, **kwargs)


class Country(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(blank=True, null=True, upload_to='Country')

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name
