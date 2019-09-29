"""mydjango URL Configuration

The `urlpatterns` list routes URLs to utils. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function utils
    1. Add an import:  from my_app import utils
    2. Add a URL to urlpatterns:  path('', utils.home, name='home')
Class-based utils
    1. Add an import:  from other_app.utils import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('pophas.urls')),
    path('control/', admin.site.urls),
]
