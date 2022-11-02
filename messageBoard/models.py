from django.db import models

# Create your models here.
from django.db import models


class MessageBoard(models.Model):
    text = models.TextField()

    def __str__(self):
        # Just trying something fun. if the text entry is "Hello, World!" then it changes the title in the admin console
        # if you're reading this Arana Fireheart, then hello!
        if self.text[:13] == "Hello, World!":
            return "Typical Hello World Message smh..."
        else:
            return self.text[:50]
