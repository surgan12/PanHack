from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import QueryImage
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import QueryImage
import logging
import json

def SaveImage(request):
    saved = False

    if request.method == "POST":
        # Get the posted form

        # print(request.POST['name'])
        MyProfileForm = ProfileForm(request.POST, request.FILES)
        # print(MyProfileForm.errors)
        if MyProfileForm.is_valid():
            # name = request.POST['name_image']

            image = QueryImage(query_image=request.FILES['picture'], name = request.POST['name'], long = request.POST['long'], lat = request.POST['lat'], aadhar = request.POST['aadhar'] )
            # image.uploaded_at = MyProfileForm.cleaned_data["uploaded_at"]

            image.save()
            # read_image = Image.open('/home/jatin/codes/PanHack/objectdetect/media/' + str(image.query_image))
            # _, _, image_type = predict(read_image)
            # print(read_image)
            # print("problem type is -> ", image_type)
            saved = True
    else:
        MyProfileForm = ProfileForm()

    return HttpResponse("success")
    # return render(request, 'object/saved.html', locals())

def upload(request):
    # documents = Document.objects.all()
    return render(request, 'object/upload_image.html')


def welcome(request):

    images = QueryImage.objects.all()
    print(images)
    return render(request, 'object/gov.html',
                    {
                    'user_data': list(images)
                    })
