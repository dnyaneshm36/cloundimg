
from django.shortcuts import render
from .models import Tree
# Create your views here.


def index(request):
    print(" --- check fine?")
    tres = Tree.objects.all()
    # for a in tres:
    #     print(a.image)
    return render(request, "index.html", {'trees': tres})






def about(request):

    # dests = Destination.objects.all()

    # return render(request, "index.html", {'dests': dests})
    print("thisi")
    return render(request, "about.html")


def contact(request):

    # dests = Destination.objects.all()

    # return render(request, "index.html", {'dests': dests})

    return render(request, "contact.html")









from .form import UploadImageForm
from django.shortcuts import render, redirect

def upload_file(request):
    form = UploadImageForm(request.POST, request.FILES)
    if form.is_valid():
        uploaded_img = form.save(commit=False)
        uploaded_img.image_data = form.cleaned_data['image'].file.read()
        
        uploaded_img.save()
        return redirect('/')
    else:
        form = UploadImageForm()
    return render(request, 'upload.html', {'form': form})