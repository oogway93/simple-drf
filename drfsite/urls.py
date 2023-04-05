from django.contrib import admin
from django.urls import path, include
from logic.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'person', PersonViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    # path('api/v1/person/', PersonAPIList.as_view()),
    # path('api/v1/person/<int:pk>/', PersonAPIUpdate.as_view()),
    # path('api/v1/persondetail/<int:pk>/', PersonAPIDestroy.as_view()),
]
