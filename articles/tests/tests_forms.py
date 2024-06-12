from django.test import TestCase

from django_blog import settings
from ..forms import CreateArticle
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from PIL import Image
import io
import os


class ArticleFormsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.test_image_path = None

    def tearDown(self):
        # Clean up any test files created during testing
        media_dir = os.path.join(settings.MEDIA_ROOT, "thumbnails")
        for file_name in os.listdir("media/thumbnails"):

            if file_name.startswith("test_picture"):
                file_path = os.path.join(media_dir, file_name)
                os.remove(file_path)

        super().tearDown()

    def create_test_image(self):
        # Create an image in memory
        image = Image.new("RGB", (100, 100), color=(73, 109, 137))
        byte_arr = io.BytesIO()
        image.save(byte_arr, format="JPEG")  # Save image to bytes
        test_image_path = "test_picture.jpg"
        with open(test_image_path, "wb") as f:
            f.write(byte_arr.getvalue())

        return byte_arr.getvalue(), test_image_path

    def test_article_form_valid(self):
        # Create a SimpleUploadedFile instance for the thumb field
        test_image_content, test_image_path = self.create_test_image()

        # Initialize the form with data and files separately
        form = CreateArticle(
            data={
                "title": "TestTitle",
                "slug": "test-article",
                "body": "This is test article body",
                "author": self.user.id,  # Ensure author is provided if required by the form
            },
            files={
                "thumb": SimpleUploadedFile(
                    name="test_picture.jpg",
                    content=test_image_content,
                    content_type="image/jpeg",
                ),
            },
        )

        # Check if the form is valid
        self.assertTrue(form.is_valid(), form.errors)

        # Save the form and check the created article
        article = form.save(commit=False)
        article.author = self.user  # Ensure you set an author if required
        article.save()

        self.assertEqual(article.title, "TestTitle")
        self.assertEqual(article.body, "This is test article body")
        self.assertEqual(article.slug, "test-article")
        self.assertTrue(article.thumb)  # Check that the thumb field has a file

    def test_article_form_invalid(self):
        form = CreateArticle(data={"title": "", "body": "", "slug": "", "thumb": ""})
        self.assertFalse(form.is_valid())
