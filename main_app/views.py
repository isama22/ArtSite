from django.shortcuts import render
from .models import Fiber
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Figurative
from .models import Digital
# Add the following import
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def contact(request):
  return render(request, 'contact.html')  
   
# def fibers_index(request):
#     return render(request, 'fibers/index.html', { 'fibers': fibers })    

def fibers_index(request):
  fibers = Fiber.objects.all()
  return render(request, 'fibers/index.html', { 'fibers': fibers })

def fibers_detail(request, fiber_id):
  fiber = Fiber.objects.get(id=fiber_id)
  return render(request, 'fibers/detail.html', { 'fiber': fiber })  

class FibersCreate(CreateView):
  model = Fiber
  fields = '__all__'
  success_url = '/fibers/'

class FiberUpdate(UpdateView):
  model = Fiber
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = '__all__'
  success_url = '/fibers/'

class FiberDelete(DeleteView):
  model = Fiber
  success_url = '/fibers/'

def figuratives_index(request):
  figuratives = Figurative.objects.all()
  return render(request, 'figuratives/index.html', { 'figuratives': figuratives })

def figuratives_detail(request, figurative_id):
  figurative = Figurative.objects.get(id=figurative_id)
  return render(request, 'figuratives/detail.html', { 'figurative': figurative }) 

class FigurativesCreate(CreateView):
  model = Figurative
  fields = '__all__'
  success_url = '/figuratives/'

class FigurativeUpdate(UpdateView):
  model = Figurative
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = '__all__'
  success_url = '/figuratives/'

class FigurativeDelete(DeleteView):
  model = Figurative
  success_url = '/figuratives/'

def digitals_index(request):
  digitals = Digital.objects.all()
  return render(request, 'digitals/index.html', { 'digitals': digitals })

def digitals_detail(request, digital_id):
  digital = Digital.objects.get(id=digital_id)
  return render(request, 'digitals/detail.html', { 'digital': digital }) 

class DigitalsCreate(CreateView):
  model = Digital
  fields = '__all__'
  success_url = '/digitals/'    

class DigitalUpdate(UpdateView):
  model = Digital
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = '__all__'
  success_url = '/digitals/'

class DigitalDelete(DeleteView):
  model = Digital
  success_url = '/digitals/'  