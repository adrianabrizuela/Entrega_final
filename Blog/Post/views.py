from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import PostSearchForm


def home_view(request):
    return render(request, "post/home.html")





#-----------------------------------------------------------------
#                      CRUD POST
#-----------------------------------------------------------------

# List

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "post/vbc/post_list.html"
    context_object_name = "ADRIANDARGELOS"


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post/vbc/post_detail.html"
    context_object_name = "GUSTAVOCERATI"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "post/vbc/post_confirm_delete.html"
    success_url = reverse_lazy("post-list")


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "post/vbc/post_form.html"
    fields = ["titulo", "subtitulo", "contenido", "fecha",  "autor"]
    context_object_name = "post"
    success_url = reverse_lazy("post-list")


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post/vbc/post_form.html"
    fields = ["titulo", "subtitulo", "contenido", "fecha", "autor"]
    success_url = reverse_lazy("post-list")



# def sala_search_view(request):
#     if request.method == "GET":
#         form = PostSearchForm()
#         return render(
#             request, "bookings/form_search.html", context={"search_form": form}
#         )
#     elif request.method == "POST":
#         #  devolverle a "chrome" la lista de reservas encontrada o avisar que no se encontró nada
#         form = SalaSearchForm(request.POST)
#         if form.is_valid():
#             nombre_de_sala = form.cleaned_data["nombre"]
#             salas_encontradas = Sala.objects.filter(nombre= nombre_de_sala).all()
#             contexto_dict = {"ADRIANDARGELOS": salas_encontradas}
#             return render(request, "bookings/vbc/sala_list.html", contexto_dict)
#         else: 
#             return render(
#             request, "bookings/form_search.html", context={"search_form": form}
#         )

#-----------------------------------------------------------------
#                      login/logout
#-----------------------------------------------------------------


from django.contrib.auth import logout,login
from django.contrib.auth.forms import AuthenticationForm


def user_login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.user_cache
            if user is not None:
                login(request, user)
                return redirect("home")

    return render(request, "post/login.html", {"MICHAELSTIPE": form})

def user_logout_view(request):
    logout(request)
    return redirect("login")


#-----------------------------------------------------------------
#                      crear usuario
#-----------------------------------------------------------------

from django.contrib.auth.forms import UserCreationForm


def user_creation_view(request):
    if request.method == "GET":
        form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

    return render(request, "post/crear-usuario.html", {"form": form})



#-----------------------------------------------------------------
#                      editar usuario
#-----------------------------------------------------------------

from django.contrib.auth.models import User
from .forms import UserEditForm

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'post/user_edit_form.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user