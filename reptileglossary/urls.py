"""reptileglossary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from rest_framework import routers
from reptileglossaryapi.views.reptile import ReptileView
from reptileglossaryapi.views.reptilediet import ReptileDietView
from reptileglossaryapi.views.specialneedsreptile import SpecialNeedsReptileView
from reptileglossaryapi.views.reptileguide import ReptileGuideView
from reptileglossaryapi.views.dietguide import DietGuideView
from reptileglossaryapi.views.specialneedsguide import SpecialNeedsGuideView
from reptileglossaryapi.views import register_user, login_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'reptileguides', ReptileGuideView, 'reptileguide')
router.register(r'dietguides', DietGuideView, 'dietguide')
router.register(r'specialneedsguides', SpecialNeedsGuideView, 'specialneedsguide')
router.register(r'reptiles' ,ReptileView, "reptile")
router.register(r'reptilediets' ,ReptileDietView, "reptilediet")
router.register(r'specialneedsreptiles' ,SpecialNeedsReptileView, "specialneedsreptile")



urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
