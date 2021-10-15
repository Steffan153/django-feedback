from django.forms.models import ModelForm
from django.forms.widgets import TextInput, Textarea, NumberInput

from .models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Review",
            "rating": "Your Rating",
        },
        error_messages = {
            "user_name": {
                "required": "Please enter your name.",
                "max_length": "Please enter no more than 50 letters for your name.",
                "min_length": "Please enter at least 2 characters for your name.",
            },
            "review_text": {
                "required": "Please enter your feedback.",
                "max_length": "Please enter no more than 200 letters for your feedback.",
                "min_length": "Please enter at least 10 characters for your feedback.",
            },
            "rating": {
                "required": "Please enter your rating.",
                "min_value": "1 is the minimum for the rating.",
                "max_value": "5 is the maximum for the rating."
            }
        }
        widgets = {
            "user_name": TextInput(attrs={'class': "form-control"}),
            "review_text": Textarea(attrs={'class': 'form-control'}),
            "rating": NumberInput(attrs={'class': 'form-control'})
        }
