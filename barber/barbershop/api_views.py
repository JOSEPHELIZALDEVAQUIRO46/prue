from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Barberia, Barbero, Servicio, CatalogoCortes, Promociones, Contabilidad, Cita
from .serializers import BarberiaSerializer, BarberoSerializer, ServicioSerializer, CatalogoCortesSerializer, PromocionesSerializer, ContabilidadSerializer, CitaSerializer

class BarberiaViewSet(viewsets.ModelViewSet):
    queryset = Barberia.objects.all()
    serializer_class = BarberiaSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            barberia = Barberia.objects.get(pk=pk)
        except Barberia.DoesNotExist:
            return Response({"detail": "No se encontró ninguna barbería."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(barberia)
        return Response(serializer.data)

class BarberoViewSet(viewsets.ModelViewSet):
    queryset = Barbero.objects.all()
    serializer_class = BarberoSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            barbero = Barbero.objects.get(pk=pk)
        except Barbero.DoesNotExist:
            return Response({"detail": "No se encontró ningún barbero."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(barbero)
        return Response(serializer.data)

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            servicio = Servicio.objects.get(pk=pk)
        except Servicio.DoesNotExist:
            return Response({"detail": "No se encontró ningún servicio."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(servicio)
        return Response(serializer.data)

class CatalogoCortesViewSet(viewsets.ModelViewSet):
    queryset = CatalogoCortes.objects.all()
    serializer_class = CatalogoCortesSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            catalogo_cortes = CatalogoCortes.objects.get(pk=pk)
        except CatalogoCortes.DoesNotExist:
            return Response({"detail": "No se encontró ningún corte."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(catalogo_cortes)
        return Response(serializer.data)

class PromocionesViewSet(viewsets.ModelViewSet):
    queryset = Promociones.objects.all()
    serializer_class = PromocionesSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            promocion = Promociones.objects.get(pk=pk)
        except Promociones.DoesNotExist:
            return Response({"detail": "No se encontró ninguna promoción."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(promocion)
        return Response(serializer.data)

class ContabilidadViewSet(viewsets.ModelViewSet):
    queryset = Contabilidad.objects.all()
    serializer_class = ContabilidadSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            contabilidad = Contabilidad.objects.get(pk=pk)
        except Contabilidad.DoesNotExist:
            return Response({"detail": "No se encontró ninguna contabilidad."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(contabilidad)
        return Response(serializer.data)

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            cita = Cita.objects.get(pk=pk)
        except Cita.DoesNotExist:
            return Response({"detail": "No se encontró ninguna cita."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(cita)
        return Response(serializer.data)
