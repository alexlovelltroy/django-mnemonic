from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.edit import FormView
from django_mnemonic.forms import WordsForm
from django_mnemonic.mnemonic import random_word

class WordsFormView(FormView):
    template_name = 'base.html'
    form_class = WordsForm
    count = 2
    camelcase = False

    def get_context_data(self, **kwargs):
        if 'count' in self.kwargs:
            self.count = int(self.kwargs['count'])
        if 'camelcase' in self.kwargs:
            self.camelcase = self.kwargs['camelcase']
        context = super(WordsFormView, self).get_context_data(**kwargs)
        words = [random_word() for x in range(0,self.count)]
        if self.camelcase:
            headline = ''.join(words)
        else:
            headline = ' '.join(words)
        context['headline'] = headline
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        if form.cleaned_data['camelcase']:
            self.success_url = '/camel/%s' % form.cleaned_data['count']
        else:
            self.success_url = '/%s' % form.cleaned_data['count']
        return super(WordsFormView, self).form_valid(form)


class SimpleAPIView(View):
    count = 2
    def get(self, request, *args, **kwargs):
        words = [random_word() for x in range(0,self.count)]
        return HttpResponse(' '.join(words))

class CamelAPIView(View):
    count = 2
    def get(self, request, *args, **kwargs):
        words = [random_word() for x in range(0,self.count)]
        return HttpResponse(''.join(words))
