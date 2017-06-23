from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

from escuelas import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet)
router.register(r'escuelas', views.EscuelaViewSet)
router.register(r'contactos', views.ContactoViewSet)
router.register(r'eventos', views.EventoViewSet)
router.register(r'regiones', views.RegionViewSet)
router.register(r'perfiles', views.PerfilViewSet)
router.register(r'distritos', views.DistritoViewSet)
router.register(r'localidades', views.LocalidadViewSet)
router.register(r'programas', views.ProgramaViewSet)
router.register(r'tipos-de-financiamiento', views.TipoDeFinanciamientoViewSet)
router.register(r'tipos-de-gestion', views.TipoDeGestionViewSet)
router.register(r'areas', views.AreaViewSet)
router.register(r'niveles', views.NivelViewSet)
router.register(r'experiencias', views.ExperienciaViewSet)
router.register(r'cargos', views.CargoViewSet)
router.register(r'contratos', views.ContratoViewSet)

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
