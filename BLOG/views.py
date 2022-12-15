from django.shortcuts import render
from django.contrib.auth.decorators import login_required #vistas basadas en funciones
from .models import *
from .forms import *

# Create your views here.
def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="BLOG\media\avatares\avatarpordefecto.png"
    return imagen

@login_required
def aboutMe(request):
    return render (request, "chat/about.html", {"imagen":obtenerAvatar(request)})

@login_required
def profile(request):
    context = {
        "page":"profile",
    }
    return render(request,"chat/profile.html",context, {"imagen":obtenerAvatar(request)})

@login_required
def AgregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)#TRAE ARCHIVOS CON EL "FILES"
        if form.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)!=0:
                avatarViejo[0].delete()
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatar.save()
            return render(request, "chat\profile.html", {"mensaje":"Avatar agregado correctamente", "imagen":obtenerAvatar(request)})
        else:
            return render(request, "chat\profile.html", {"formulario":form, "usuario":request.user, "imagen":obtenerAvatar(request)})
    else:
        form=AvatarForm()
        return render(request, "chat\profile.html", {"formulario":form, "usuario":request.user, "imagen":obtenerAvatar(request)})
