"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#from homepage.views import homepage
from apps.pages_app.views import home
from apps.forum_app.views import forum_view
#from apps.forum_app.views import forum_view
from apps.pages_app.views import pais_e_profs
from apps.pages_app.views import videos

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('forum', forum_view, name='forum'),
    path('pais_e_profs', pais_e_profs, name='pais_profs'),
    path('videos', videos, name='videos')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
