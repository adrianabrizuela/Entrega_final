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
    fields = ["destino", "ciudad", "comentarios", "fecha",  "autor", "imagen"]
    context_object_name = "post"
    success_url = reverse_lazy("post-list")


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post/vbc/post_form.html"
    fields = ["destino", "ciudad", "comentarios", "fecha", "autor", "imagen"]
    success_url = reverse_lazy("post-list")



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
    
#-----------------------------------------------------------------
#                      acerca de mi
#-----------------------------------------------------------------


def about(request):
    # Aquí puedes definir la información sobre los dueños de la página
    owners_info = "Ésta es una página de recomendaciones para viajes."

    # Renderiza la plantilla "about.html" con la información de los dueños
    return render(request, 'about.html', {'owners_info': owners_info})
