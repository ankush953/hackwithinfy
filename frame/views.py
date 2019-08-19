from django.shortcuts import render
from django.http import HttpResponse
from frame.models import FrameModel
from frame.data_populate import populate
# Create your views here.
flag = False


def homepage(request):
    # global flag
    # if not flag:
    #     # populate2()
    #     # populate()

    #     flag = True
    return searchbycat(request, 'Danger')


def searchbycat(request, cat=None):
    # print(cat)
    catobj = FrameModel.objects.filter(image_type=cat)
    context = {
        'objects': catobj,
    }
    return render(request, 'homepage.html', context=context)
