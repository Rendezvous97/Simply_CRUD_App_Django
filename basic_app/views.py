from typing import Any
from django.shortcuts import render
from django.views.generic import (TemplateView,
                                ListView, DetailView,
                                CreateView, UpdateView,
                                DeleteView)
from django.http import HttpResponse
from basic_app import models
from django.urls import reverse_lazy


# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['injectme'] = "I've been injected!"

        return context


class SchoolListView(ListView):
    context_object_name = "schools"
    model = models.School



class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = "basic_app/school_detail.html"


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School
    # template_name = "TEMPLATE_NAME"

    
class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School
    # template_name = "TEMPLATE_NAME"

class SchoolDeleteView(DeleteView):
    model = models.School
    # template_name models.= ".html"
    success_url = reverse_lazy('basic_app:school_list')


# def index(request):
#     return render(request, "basic_app/index.html", {})



# class CBView(View):
#     def get(self, request):
#         return HttpResponse("Class based views are cool")
    
