from django.shortcuts import render
from sample.models import Sample
from django.core.files.storage import FileSystemStorage
from PIL import Image, ImageDraw as D
# Create your views here.

"""
def index(request):

    context = dict()

    context['samples'] = Sample.objects.all() #SELECT * FROM sample

    return render(request, 'index.html', context)
"""

def image(request):
    if request.method == 'POST':
        uploaded_file=request.FILES["image"]
        fs=FileSystemStorage()
        filename=fs.save(uploaded_file.name, uploaded_file)
        uploaded_file_url = fs.url(filename)
        """img=Image.open(uploaded_file_url)
        draw=D.Draw(img)
        draw.rectangle([(50,50),(50,50)],outline="white")
        fs.save(((uploaded_file.name)+"1"),img)"""
    return render(request, 'index.html')