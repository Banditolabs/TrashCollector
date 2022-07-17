from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Trash
from .forms import FeedingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
    return HttpResponse('<h1>Garbage! Om nom nom<h1>')

def about(request):
    return render(request, 'about.html')

def landfill(request):
  trash = Trash.objects.all()
  return render(request, 'trash/index.html', { 'trash': trash })

def trash_detail(request, trash_id):
  ## Get the the individual trash
  trash = Trash.objects.get(id=trash_id)
  feeding_form = FeedingForm()
  ## render template, pass it the trash
  return render(request, 'trash/detail.html', { 
    'trash': trash, 'feeding_form': feeding_form

    })

def add_feeding(request, trash_id):
  # create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the trash_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.trash_id = trash_id
    new_feeding.save()
  return redirect('detail', trash_id=trash_id)

class TrashCreate(CreateView):
  model = Trash
  fields = '__all__'
  success_url = '/landfill/'

class TrashUpdate(UpdateView):
  model = Trash
  # Let's disallow the renaming of a trash by excluding the name field!
  fields = '__all__'

class TrashDelete(DeleteView):
  model = Trash
  success_url = '/landfill/'


