"""core URL Configuration

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
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token # <-- NEW
from home.views import (count_day_sall_dartil,count_day_sall_snappshop,
                            count_monthly_sales_snappshop,
                            count_monthly_sales_dartil,
                            )

urlpatterns = [
    path('count_day_sall_dartil', count_day_sall_dartil),
    path('count_day_sall_snappshop', count_day_sall_snappshop),
    path('count_monthly_sales_snappshop', count_monthly_sales_snappshop),
    path('count_monthly_sales_dartil', count_monthly_sales_dartil),
    path("", admin.site.urls),
    path("", include('administrator.urls')),
    path('', include('django_dyn_dt.urls')), # <-- NEW: Dynamic_DT Routing   
]

# Lazy-load on routing is needed
# During the first build, API is not yet generated
try:
    urlpatterns.append( path("api/"      , include("api.urls"))    )
except:
    pass
