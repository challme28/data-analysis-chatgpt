import os

import magic
from django import forms
from django.conf import settings
# from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

from playground.models import FileData


def validate_is_csv(file):
    # Validate file's MIME type
    valid_mime_types = settings.VALID_MIME_TYPES
    file_mime_type = magic.from_buffer(file.read(2048), mime=True)
    if file_mime_type not in valid_mime_types:
        raise ValidationError('Unsupported file type.')
    valid_file_extension = ['.csv']
    # Validate the file extension. File's a csv but .pdf
    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in valid_file_extension:
        raise ValidationError('Unacceptable file extension.')


class FileDataForm(forms.ModelForm):
    file = forms.FileField(
        label="Please, choose a .csv file",
        # validators=[FileExtensionValidator(allowed_extensions=["csv"])],
        validators=[validate_is_csv],
        widget=forms.FileInput(attrs={'accept': '.csv'}),
    )
    input = forms.CharField(label="What is your query?", required=False,
                            widget=forms.TextInput(attrs={'placeholder': 'Give me an initial description of the data'}))

    class Meta:
        model = FileData
        fields = ['file', 'input']
