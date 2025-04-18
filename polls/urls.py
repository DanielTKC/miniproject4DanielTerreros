from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import AboutView, UpcomingEventsView

app_name = 'polls'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),

    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path("login/", auth_views.LoginView.as_view(template_name="polls/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="polls:index"), name="logout"),

    path("about/", AboutView.as_view(), name="about"),

    path("events/", UpcomingEventsView.as_view(), name="events"),

]
