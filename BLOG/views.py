from django.shortcuts import render
from django.contrib.auth.decorators import login_required #vistas basadas en funciones
from .models import *
from .forms import *
from chat.models import *
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin #vistas basadas en clases
from django.urls import reverse_lazy


# Create your views here.
def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="BLOG/media/avatares/avatarpordefecto.png"
    return imagen

@login_required
def aboutMe(request):
    return render (request, "chat/about.html", {"imagen":obtenerAvatar(request)})

@login_required
def leerMas(request):
    return render (request, "chat/aboutLeermas.html", {"imagen":obtenerAvatar(request)})

@login_required
def profile(request):
    context = {
        "page":"profile",
        "imagen":obtenerAvatar(request),
    }
    return render(request,"chat/profile.html",context)

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
            return render(request, "chat\profile.html", {"mensaje":"Avatar agregado correctamente"})
        else:
            return render(request, "chat\profile.html", {"formulario":form, "usuario":request.user})
    else:
        form=AvatarForm()
        return render(request, "chat\profile.html", {"formulario":form, "usuario":request.user})

@login_required
def leerUsuarios(request):
    usuarios= User.objects.all()
    contexto= {"usuarios":usuarios, "imagen":obtenerAvatar(request)}
    return render(request, "chat/blogLeer.html", contexto)

"""def deleteComentario(request, id):
    comentario=comentarioM.objects.get(id=id)
    comentario.delete()
    comentario=comentarioM.objects.all()
    return render(request, "chat/blogList.html", {"comentario":comentario})
"""
class formularioComentario(LoginRequiredMixin, CreateView):
    model = comentarioM
    success_url = reverse_lazy("Crear")
    template_name = "chat/blogCrear.html"
    fields = ["nombre", "campo", "date_created", "imagen"]

class listComentario(LoginRequiredMixin, ListView):
    model= comentarioM
    template_name= "chat/blogList.html"

class deleteComentario(LoginRequiredMixin, DeleteView):
    model=comentarioM
    template_name = "chat/blogDelete.html"
    success_url= reverse_lazy("Lista")

class updateComentario(LoginRequiredMixin, UpdateView):
    model=comentarioM
    template_name= "chat/blogUpdate.html"
    success_url= reverse_lazy("Lista")
    fields =["campo"]