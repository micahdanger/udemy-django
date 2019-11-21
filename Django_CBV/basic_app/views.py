from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView,
                                ListView, DetailView,
                                CreateView, UpdateView,
                                DeleteView)
from . import models

# Create your views here.

class SchoolListView(ListView):
    # this  is if you want to define your own context dictionary name
    context_object_name = 'schools'
    model = models.School
    # returns a list: schhol_list


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    """
    this is a security feature that allows only these fields to be added by a user
    """
    fields = ('name', 'principle', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    """
    what would we want to update about a school?
    name - maybe
    principle - certainly
    location - definitely not
    """
    fields = ('name', 'principle')
    model = models.School


class SchoolDeleteView(DeleteView):
    """
    referencing the model in HTML, use the lowercase version of it: school
    """
    model = models.School
    """
    this says that once a school is successfully deleted, go to this URL
    """
    success_url = reverse_lazy("basic_app:list")


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context

"""
# THIS IS THE OLD GHETTO WAY OF DOING THINGS

def index(request):
    return render(request, 'index.html')
"""
