from __future__ import unicode_literals

import httplib as HTTP

from django.views.generic import TemplateView
from django.http import JsonResponse

from poll.forms import QuestionForm
from poll.models import Question


class HomeView(TemplateView):
    template_name = 'poll/home.html'
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            objects = Question.objects.values('question_text')
            return JsonResponse({'result': list(objects)})
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        kwargs['form'] = QuestionForm()
        return kwargs

    def post(self, request, *args, **kwargs):
        form = QuestionForm(request.POST)
        if not form.is_valid():
            return JsonResponse({}, status=HTTP.BAD_REQUEST)
        instance = form.save()
        return JsonResponse(
            {'question_text': instance.question_text}, status=HTTP.CREATED)
