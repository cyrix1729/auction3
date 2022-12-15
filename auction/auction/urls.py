
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import home_view, login_view, logout_view, profile_view, reg_view, edit_profile_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("auctionApp.urls")),
    path('home/', home_view, name = 'home-view'),
    path('login', login_view, name= 'login'),
    path('logout/', logout_view, name= 'logout'),
    path('register/', reg_view, name= 'register'),
    path('editProfile/', edit_profile_view, name= 'editProfile'),
    path('profile/', profile_view, name= 'profile'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
