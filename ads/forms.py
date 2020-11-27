from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile

from ads.models import Ad
from ads.humanize import natural_size


class CreateForm(forms.ModelForm):

    # 2 MB max picture size
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = natural_size(max_upload_limit)


    # Call this 'picture' so it gets copied from the form to the in-memory model
    # It will not be the "bytes", it will be the "InMemoryUploadedFile"
    # because we need  to pull out things like content_type
    picture = forms.FileField(required=False, label='File to Upload <= ' + max_upload_limit_text)
    upload_field_name = 'picture'


    class Meta:
        model = Ad
        fields = ['title', 'price', 'text', 'picture'] # Picture is manual


    # Validate the size of the picture
    def clean(self):
        cleaned_data = super().clean()
        pic = cleaned_data.get('picture')

        if pic is None:
            return
        if len(pic) > self.max_upload_limit:
            self.add_error('picture', "File must be < " + self.max_upload_limit_text + " bytes")


    def save(self, commit=True):
        instance = super(CreateForm, self).save(commit=False)

        # We only need to adjust picture if it is a freshly uploaded file
        f = instance.picture # make a copy

        if isinstance(f, InMemoryUploadedFile): # Extract data from the form to the model
            byte_arr = f.read()
            instance.content_type = f.content_type
            instance.picture = byte_arr # Overwrite withe the actual image data


        if commit:
            instance.save()

        return instance



# https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/
# https://stackoverflow.com/questions/2472422/django-file-upload-size-limit
# https://stackoverflow.com/questions/32007311/how-to-change-data-in-django-modelform
# https://docs.djangoproject.com/en/3.0/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other



# strip means to remove whitespace from the begining and the end before storing the column
class CommentForm(forms.Form):
    comment = forms.CharField(required=True, max_length=500, min_length=3, strip=True)