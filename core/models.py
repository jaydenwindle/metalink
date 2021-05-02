from django.db import models
from django.utils.crypto import get_random_string


class Link(models.Model):
    url = models.URLField()
    slug = models.SlugField()
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField()

    def save(self, *args, **kwargs) -> None:
        if self.slug == "":
            self.slug = get_random_string(8)

        return super().save(*args, **kwargs)
