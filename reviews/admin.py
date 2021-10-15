from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from .models import Review

@register(Review)
class ReviewAdmin(ModelAdmin):
    pass