from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api_views

# Registrar las vistas
router = DefaultRouter()

urlpatterns = [
    path('barberia/<int:pk>/', api_views.BarberiaViewSet.as_view({'get': 'retrieve'}), name='barberia-detail'),
    path('barbero/<int:pk>/', api_views.BarberoViewSet.as_view({'get': 'retrieve'}), name='barbero-detail'),
    path('servicio/<int:pk>/', api_views.ServicioViewSet.as_view({'get': 'retrieve'}), name='servicio-detail'),
    path('catalogo-cortes/<int:pk>/', api_views.CatalogoCortesViewSet.as_view({'get': 'retrieve'}), name='catalogo-cortes-detail'),
    path('promocion/<int:pk>/', api_views.PromocionesViewSet.as_view({'get': 'retrieve'}), name='promocion-detail'),
    path('contabilidad/<int:pk>/', api_views.ContabilidadViewSet.as_view({'get': 'retrieve'}), name='contabilidad-detail'),
    path('cita/<int:pk>/', api_views.CitaViewSet.as_view({'get': 'retrieve'}), name='cita-detail'),
    
    # Incluye más rutas si lo necesitas
    path('', include(router.urls)),
]
