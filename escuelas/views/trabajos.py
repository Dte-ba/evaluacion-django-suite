# coding: utf-8
from __future__ import unicode_literals
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.decorators import list_route
from rest_framework.decorators import detail_route
from django.core.exceptions import ObjectDoesNotExist

from escuelas.models import Trabajo
from escuelas.models import DistribucionDePaquete
from escuelas import trabajos


class TrabajosViewSet(viewsets.ViewSet):

    @authentication_classes([])
    @permission_classes([])
    def list(self, request):
        queryset = Trabajo.objects

        return Response(Trabajo.obtener_trabajos_serializados())

    @list_route(methods=['get'])
    def sumar(self, request):
        job = trabajos.pruebas.sumar.delay(2, 2)

        return Response({
            'trabajo_id': job.id
        })

    @list_route(methods=['get'])
    def informe_de_perfil(self, request):
        desde = request.query_params['desde']
        hasta = request.query_params['hasta']
        perfil_id = request.query_params['perfil_id']
        aplicacion = request.query_params['aplicacion']

        job = trabajos.informes.generar_informe_de_perfil.delay(perfil_id, desde, hasta, aplicacion)

        return Response({
            'trabajo_id': job.id
        })

    @list_route(methods=['get'])
    def informe_de_perfil_por_region(self, request):
        desde = request.query_params['desde']
        hasta = request.query_params['hasta']
        region = request.query_params['region']
        aplicacion = request.query_params['aplicacion']
        job = trabajos.informes.generar_informe_de_region.delay(region, desde, hasta, aplicacion)

        return Response({
            'trabajo_id': job.id
        })

    @list_route(methods=['get'])
    def exportar_paquetes(self, request):
        inicio = request.query_params['inicio']
        fin = request.query_params['fin']
        estado = request.query_params['estado']

        trabajo = trabajos.paquetes.exportar_paquetes.delay(inicio, fin, estado)

        return Response({
            'trabajo_id': trabajo.id
        })

    @list_route(methods=['get'])
    def exportar_talleres_de_robotica(self, request):
        inicio = self.request.query_params.get('inicio', None)
        fin = self.request.query_params.get('fin', None)
        criterio = self.request.query_params.get('criterio', None)

        trabajo = trabajos.exportar_talleres_de_robotica.exportar_talleres.delay(inicio, fin, criterio)

        return Response({
            'trabajo_id': trabajo.id
        })

    @list_route(methods=['get'])
    def distribuir_paquetes(self, request):
        id = request.query_params['id']

        paquete = DistribucionDePaquete.objects.get(id=id)

        trabajo = trabajos.distribuir_paquetes.distribuir_paquetes.delay(paquete)

        return Response({
            'trabajo_id': trabajo.id
        })

    @detail_route(methods=['get'])
    def consultar(self, request, pk=None):
        try:
            trabajo = Trabajo.objects.get(trabajo_id=pk)
            url = ""

            if trabajo.archivo:
                url = request.build_absolute_uri(trabajo.archivo.url)

            return Response({
                'id': trabajo.id,
                'progreso': trabajo.progreso,
                'resultado': trabajo.resultado,
                'archivo': url,
                'error': trabajo.error,
                'detalle': trabajo.detalle.split("\n")
            })
        except ObjectDoesNotExist:
            return Response({
                'id': pk,
                'progreso': 0,
                'resultado':  None,
                'archivo': None,
                'detalle': []
            })
