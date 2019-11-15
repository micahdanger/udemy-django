from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context




# THIS IS THE OLD GHETTO WAY OF DOING THINGS
"""
def index(request):
    return render(request, 'index.html')
"""
