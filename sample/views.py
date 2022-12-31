from django.shortcuts import render
from sample.models import Sample
from django.core.files.storage import FileSystemStorage
from PIL import Image, ImageDraw
import json

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
        #post image

        #get api info
        text= {"detection_classes": ["tumor"],"detection_boxes": [["70.12711","170.55042","165.89742","260.38376"]],"detection_scores": ["0.80230874"]}
        data=json.loads(text)
        title=data["detection_classes"]
        i=title.index("tumor")
        if "tumor" in title:
            title="tumor"
        
        x1=float(data["detection_boxes"][i][3])
        y1=float(data["detection_boxes"][i][0])
        x2=float(data["detection_boxes"][i][2])
        y2=float(data["detection_boxes"][i][1])
        #create rectangle
        """img=Image.open(uploaded_file_url)
        draw=ImageDraw.Draw(img)
        draw.rectangle([(x1,y1),(x2,y2)],outline="green")
        uptadeimage=img.save(fs,"jpg")
        uptadeimage_url=s.url(uptadeimage)"""
        context=dict()
        #context["image"]=uptadeimage_url
        context["result"]=title
    return render(request, 'index.html', context)