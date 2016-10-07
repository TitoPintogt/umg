from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


from app.aldea.forms import AldeaForm
from app.aldea.models import Aldea


class AldeaList(ListView):
	model = Aldea
	template_name = 'aldea/aldea_list.html'

class AldeaCreate(CreateView):
	model = Aldea
	form_class = AldeaForm
	template_name = 'aldea/aldea_form.html'
	success_url = reverse_lazy('aldea:aldea_listar')

class AldeaUpdate(UpdateView):
	model = Aldea
	form_class = AldeaForm
	template_name = 'aldea/aldea_form.html'
	success_url = reverse_lazy('aldea:aldea_listar')

class AldeaDelete(DeleteView):
	model = Aldea
	template_name = 'aldea:aldea_delete.html'
	success_url = reverse_lazy('aldea:aldea_listar')
