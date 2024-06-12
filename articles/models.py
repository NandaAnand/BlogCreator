from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import bleach
from bleach.css_sanitizer import CSSSanitizer
from bs4 import BeautifulSoup
from django.core.exceptions import ValidationError

# Create your models here.


def validate_thumbnail(value):
    if not value:
        raise ValidationError("Thumbnail field is required.")


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = HTMLField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = thumb = models.ImageField(
        upload_to="thumbnails/", validators=[validate_thumbnail]
    )
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    article_image = models.ImageField(
        upload_to="article_images/", blank=True, null=True
    )

    def save(self, *args, **kwargs):
        # Your existing Bleach cleaning...

        # Extract image URLs from body and save to article_image field
        soup = BeautifulSoup(self.body, "html.parser")
        img_tags = soup.find_all("img")
        for img_tag in img_tags:
            img_url = img_tag.get("src")
            if img_url:
                self.article_image = img_url
                break  # Only save the first image URL found
        else:
            self.article_image = None  # No image found

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + "..."
