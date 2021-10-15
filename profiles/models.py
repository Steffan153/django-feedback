from django.db.models.base import Model
from django.db.models.fields.files import ImageField


class UserProfile(Model):
    image = ImageField(upload_to="images")
