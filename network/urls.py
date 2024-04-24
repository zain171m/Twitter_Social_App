
from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<int:user_id>", views.profile, name = "profile"),

    # API Routes
    path("post_update", views.post_update, name="post_update"),
    path("like_update", views.like_update, name ="like_update")
] 
