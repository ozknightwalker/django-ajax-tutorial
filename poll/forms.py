from __future__ import unicode_literals

from django.forms import ModelForm
from django.utils import timezone

from poll.models import Question


class QuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = ['question_text']

    def save(self, commit=True):
        instance = super(QuestionForm, self).save(commit=False)
        instance.pub_date = timezone.now()
        if commit:
            instance.save()
        return instance
