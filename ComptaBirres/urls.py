"""ComptaBirres URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from rest_framework import routers
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView
from ComptaBirres.views import *
from ComptaBirres import api
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
router.register(r'birres', api.BirresViewSet)

urlpatterns = [
    # Home
    url(r'^resum/', ComptaBirresView.as_view(), name='view'),
    url(r'^admin/', admin.site.urls),
    url(r'^client/', ComptaBirresClientView.as_view(), name='client'),
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^apiTirador/', ApiTiradorView.as_view(), name='apiTirador'),
    url(r'^$',RedirectView.as_view(url=r'resum/', permanent=False), name='view'),
    url(r'^api/totalBirres', ApiTotalBirresView.as_view(), name='api'),
    url(r'^api/dataBirres', DataBirresView.as_view()),
]

urlpatterns += staticfiles_urlpatterns()
