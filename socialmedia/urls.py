from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf import settings 
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from users import views as user_views
from users.views import UserSearch  
from django.contrib.auth import views as auth_views

# Fix the profile path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', RedirectView.as_view(url=reverse_lazy('admin:index')), name = 'admin'),
    path('accounts/', include('allauth.urls')),
    # path('',include("accounts.urls")),
    path('home/', include("posts.urls")),
    path ('posts/', include ("posts.urls")),
    # path ('profile/', user_views.profileupdate, name = 'profile'),
    path('register/', user_views.register, name = 'register'),
    path('search/', UserSearch.as_view(), name='search'),
    path('searchpage/', user_views.searchpage, name = 'searchpage'),
    path ('searchpage/export/', user_views.exportToExcel, name = 'export'),
    path('profile/', include("users.urls")),
    path('', auth_views.LoginView.as_view(template_name = 'users/login.html'),name = 'login'),
    path ('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'),name = 'login' ),
    path ('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'),name = 'logout' ),
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)