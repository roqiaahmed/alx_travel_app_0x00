from django.db import models
from django.contrib.auth.models import AbstractUser


class Listing(models.Model):
    host_id = models.CharField(max_length=225)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    user_id = models.CharField(max_length=225)
    list_id = models.ForeignKey(Listing, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=50,
        choices=[
            ("confirmed", " CONFIRMED"),
            ("pending", "PENDING"),
            ("cancelled", "CANCELLED"),
        ],
    )


class Review(models.Model):
    user_id = models.CharField(max_length=225)
    list_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
