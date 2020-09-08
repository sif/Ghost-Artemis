"""Models for front page."""

from django.db import models

class Quotation(models.Model):
    """Quotation model that contains the name of the author and what was said."""
    quote = models.CharField(max_length=500)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.author
