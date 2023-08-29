from django.db import models

from string import ascii_letters, digits
from random import choice


class URL(models.Model):
    original_url = models.URLField(unique=True, )
    short_url = models.CharField(unique=True, max_length=26, blank=True)

    def __str__(self):
        return f'{self.original_url} -> {self.short_url}'

    def save(self, *args, **kwargs):
        short_url = 'https://localhost/' + ''.join([choice(ascii_letters + digits) for _ in range(8)])
        if not self.short_url:
            self.short_url = short_url
            self.full_clean()
            super().save(*args, **kwargs)
