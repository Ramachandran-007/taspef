from django.db import models


class Magazine(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    pdf_file = models.FileField(upload_to='magazines/pdfs/')
    cover_image = models.ImageField(upload_to='magazines/covers/') 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
