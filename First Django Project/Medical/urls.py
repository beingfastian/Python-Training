# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.patient_list, name='patient_list'),
#     path('create/', views.patient_create, name='patient_create'),
#     path('<int:id>/', views.patient_detail, name='patient_detail'),
#     path('<int:id>/edit/', views.patient_edit, name='patient_edit'),
#     path('<int:id>/delete/', views.patient_delete, name='patient_delete'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'patients', views.PatientViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]