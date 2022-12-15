from django.core.exceptions import ValidationError

def file_size(value):
    filessize = value.size
    if filessize > 100000000:
        raise ValidationError("Max size is 10 MB")
        