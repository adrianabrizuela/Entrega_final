from django.urls import path
from . import views
from .views import (
    home_view,
    PostListView,
    PostDetailView,
    PostDeleteView,
    PostUpdateView,
    PostCreateView,
    user_login_view,
    user_logout_view,
    user_creation_view,
    UserUpdateView,
    #post_search_view,
   )

urlpatterns = [
    path("", home_view, name= 'home'),
    path("post/list/", PostListView.as_view(), name="post-list"),
    path("post/create/", PostCreateView.as_view(),name= "post-create"),
    path("post/<int:pk>/detail/", PostDetailView.as_view(), name= "post-detail"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name= "post-delete"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name= "post-update"),
    #path("post/buscar/", post_search_view, name= 'sala-buscar'),
    path("login/", user_login_view, name="login"),
    path("logout/", user_logout_view, name="logout"),
    path("crear-usuario/", user_creation_view, name="crear-usuario"),
    path("editar-perfil/", UserUpdateView.as_view(), name= 'editar-perfil'),
    path('about/', views.about, name='about'),
    
]


