from django.shortcuts import render
from .models import *

def Home(request):
    qidiruv = request.GET.get("searched")
    togri = Togri.objects.filter(soz=qidiruv)
    if len(togri) == 0:
        notogri = Natogri.objects.filter(soz=qidiruv)
        if len(notogri) == 0:
            togri = "Bunaqa soz bazada yoq"
            notogri = ""
        else:
            togri = notogri[0].t_soz
            notogri = Natogri.objects.filter(t_soz = togri)
    else:
        togri = togri[0]
        notogri = Natogri.objects.filter(t_soz__soz=togri)


    content = {
           "t": togri,
           "n": notogri
       }
    return render(request, 'result.html', content)
# Create your views here.
