from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, FileField, CharField

from laptops.models import Laptop, Answer


class LaptopForm(ModelForm):

    model = Laptop


class AnswerForm(ModelForm):

    attachment = FileField(required=False)
    comment = CharField(widget=CKEditorWidget())


    class Meta:
        model = Answer
        fields = ["comment", "attachment", "question"]
