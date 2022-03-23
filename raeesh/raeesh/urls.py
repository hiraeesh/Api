
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('studentapi', views.Born_To_Be_A_Programmer, basename='student')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

] 
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
