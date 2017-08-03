from __future__ import unicode_literals


from django.test import TestCase
from django.utils import timezone

from poll.models import Question


class QuestionModelTestCase(TestCase):

    def setUp(self):
        self.text = 'test'
        self.question = Question.objects.create(
            question_text=self.text, pub_date=timezone.now())

    def test_unicode(self):
        self.assertEqual(self.question.__unicode__(), self.text)
