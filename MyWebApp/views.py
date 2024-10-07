# Create your views here.
# function view
# class view

from django.shortcuts import render, HttpResponse
from django.views import View
from .forms import userform, djangoform, userModelForm
from .models import userModel, Product
from django.core.paginator import Paginator

def HomeView(request):
  return render(request, 'index.html')

def contact(request):
  return render(request, 'contact.html')

def blog(request):
  return render(request, 'blog-single.html')

def error(request):
  return render(request, '404.html')

def userForm(request):
  # method to get data from django form
  # if request.method == 'POST':
  #   form1 = userform(request.POST)
  #   if form1.is_valid():
  #     name = form1.cleaned_data['name']
  #     cont = form1.cleaned_data['contact']
  #     email = form1.cleaned_data['email']
  #     address = form1.cleaned_data['address']
  #     print('Name: ', name,'\nContact: ', cont,'\nEmail: ', email,'\nAddress: ', address)

  # method to get data from HTML form
  if request.method == 'POST':
    name=request.POST.get('name')
    cont=request.POST.get('contact')
    email=request.POST.get('email')
    print('Name: ', name,'\nContact: ', cont,'\nEmail: ', email)
  # form1 = userform()
  return render(request, 'userform.html')# {'form1':form1}

def djangoForm(request):
  if request.method == 'POST':
    print("Request method is POST")
    form = djangoform(request.POST, request.FILES)
    if form.is_valid():
      name = form.cleaned_data['name']
      # cont = form.cleaned_data['contact']
      # email = form.cleaned_data['email']
      # address = form.cleaned_data['address']
      # password = form.cleaned_data['password']
      uploaded_file = request.FILES['file']
      with open('uploaded_files/'+uploaded_file.name, "wb+") as destination:
        for chunk in uploaded_file.chunks():
          destination.write(chunk)

      print('Name: ', name) # '\nContact: ', cont,'\nEmail: ', email,'\nAddress: ', address,'\nPassword: ', password,'\nFile: ', file
  form = djangoform()
  return render(request, 'djangoform.html', {'form':form})

def register(request):
  form = userModelForm()
  if request.method == "POST":
    form = userModelForm(request.POST)
    if form.is_valid():
      form.save()
  return render(request, 'register.html', {'form':form})

def update(request, id):
  try:
    data = userModel.objects.get(pk=id)
    if request.method == "POST":
      form = userModelForm(request.POST, instance=data)
      if form.is_valid():
        form.save()
    else:
      form = userModelForm(instance=data)
    return render(request, 'register.html', {'form':form})
  except:
    return render(request, 'register.html')

def delete(request, id):
  try:
    data = userModel.objects.get(id=id)
    data.delete()
    return HttpResponse("Data Deleted")
  except:
    return HttpResponse("Data not found")


class About(View):
  def get(self, request):
    return HttpResponse("<h1 style='text-align: center'>About Us(Class view)</h1>")
  
def category(request):
  category_list = ["Electronics", "Fashion", "Books", "Furniture", "Groceries"]
  return render(request, 'category.html', {'item':category_list})

def contacts(request):
  return render(request, 'contacts.html')

def userdata(request, id):
  return HttpResponse(f"<h1 style='text-align: center'>Hello User with User <span style='text-transform: capitalize';>id - {id}</span>!!</h1>")

def user(request):
  detail = [
            {'name':'Whatever', 'contact':'918275947'},
            {'name':'Whatever', 'contact':'918275947'},
            {'name':'Whatever', 'contact':'918275947'},
            {'name':'Whatever', 'contact':'918275947'},
            {'name':'Whatever', 'contact':'918275947'},
           ]
  return render(request, 'user.html', {'userData':detail})

def alldata(request):
  data = userModel.objects.all()
  whatever = list(data.values())
  for i in whatever:
    print(i, end="\n")
  # print(whatever)
  return render(request, 'modeldata.html', {'data':whatever})

def products(request, page=1):
  prod = Product.objects.all()
  p = Paginator(prod,4)
  page_obj = p.get_page(page)
  # for i in list(prod.values()):
  #   print(i, end="\n")
  print(prod.values())
  return render(request, 'products.html', {'page_obj':page_obj})

