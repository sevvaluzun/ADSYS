"""
URL configuration for adsys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.core.management import call_command
admin.site.site_header = "ADSYS Yönetim Paneli"
admin.site.site_title = "ADSYS"
admin.site.index_title = "Yönetim Ana Sayfası"

def run_seed_data(request):
    if request.GET.get("key") != "adsys2026":
        return HttpResponse("Yetkisiz işlem", status=403)

    call_command("seed_data")
    return HttpResponse("Seed data başarıyla çalıştı.")
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('products.urls')),
    path('sepetim/', include('cart.urls')),
    path('panel/', include('dashboard.urls')),

    path('hesap/', include('accounts.urls')),
    path('hesap/', include('django.contrib.auth.urls')),
     path('bagis/', include('donations.urls')),
     path("run-seed-data/", run_seed_data),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

import os
from django.core.management import call_command

if os.environ.get("RUN_SEED_DATA") == "1":
    try:
        call_command("seed_data")
    except Exception as e:
        print("Seed data error:", e)