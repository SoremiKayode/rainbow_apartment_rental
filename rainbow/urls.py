from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home_page, name="home"),
    path("about", views.about_page, name="about"),
    path("contact", views.contact_page, name="contact"),
    path("all-properties", views.all_properties_page, name="all-properties"),
    path("single-property", views.single_properties_page, name="single-property"),
    path("profie", views.profile_page, name="profile"),
    path("login", views.login_user, name="login"),
    path("signup", views.signup, name="signup"),
    path("admin-dashboard", views.admin_dashboard, name="admin-dashboard"),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
