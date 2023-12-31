from django.conf import settings
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Destination(models.Model):
    location = models.CharField(max_length=255, primary_key=True)
    details = models.TextField()
    country = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        default="staticfiles/img/dest/no_image.jpg", upload_to="static/img/dest/"
    )
    rating = models.IntegerField(
        default=3, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    numberReviews = models.IntegerField(default=1)

    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse("destination_detail", kwargs={"pk": self.pk})


class DestinationComment(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("destination_list")
