from django.db import models
from ckeditor.fields import RichTextField



class Vendor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Laptop(models.Model):

    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default="")

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField()
    parent = models.ForeignKey("Question", on_delete=models.PROTECT, null=True, blank=True)
    attachment_required = models.BooleanField(default=False)


class Answer(models.Model):
    comment = RichTextField(config_name='default')

    attachment = models.FileField(upload_to="report_attachments")
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
