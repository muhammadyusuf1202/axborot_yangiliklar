"""
URL configuration for axborot_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from news import views
from news.views import search_view
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.conf import settings



urlpatterns = [
    # path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path("search/", search_view, name="search"),
    # DRF
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("admin1/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

# urlpatterns += i18n_patterns(
    # path('', include('axborot_site.urls')),  # sizning appingiz
# )

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
