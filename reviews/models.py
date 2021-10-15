from django.core import validators
from django.db.models.base import Model
from django.db.models.fields import CharField, IntegerField
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

class Review(Model):
    user_name = CharField(max_length=50, validators=[MinLengthValidator(2)])
    review_text = CharField(max_length=200, validators=[MinLengthValidator(10)])
    rating = IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.user_name} ({self.rating})"