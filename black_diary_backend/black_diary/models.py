from django.db import models


class NewPage(models.Model):
    title = models.CharField(max_length=250, blank=False)
    text = models.TextField()
    image = models.ImageField(upload_to="images/")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
