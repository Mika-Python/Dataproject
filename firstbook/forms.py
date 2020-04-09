from django import forms
from firstbook.models import Study, Comment


class NewStudy(forms.ModelForm):
    class Meta:
        model = Study
        fields = '__all__'


class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

