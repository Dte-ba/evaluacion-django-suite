from django.contrib import admin
import models
from django.contrib.auth.models import Permission
from dal import autocomplete
from django import forms

class CustomModelAdmin(admin.ModelAdmin):

    class Media:
         js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            )

class EscuelaForm(forms.ModelForm):

    class Meta:
        model = models.Escuela
        fields = ('__all__')
        widgets = {
            'localidad': autocomplete.ModelSelect2()
        }

class EscuelaAdmin(CustomModelAdmin):
    form = EscuelaForm
    model = models.Escuela
    list_display = ('id', 'cue', 'nombre', 'localidad', 'nivel', 'modalidad', 'numero_de_region', 'fecha_de_ultima_modificacion', 'perfil_de_ultima_modificacion')
    search_fields = ('cue', 'nombre')

class PerfilForm(forms.ModelForm):

    class Meta:
        model = models.Perfil
        fields = ('__all__')
        widgets = {
            'localidad': autocomplete.ModelSelect2(),
            'user': autocomplete.ModelSelect2()
        }

class PerfilAdmin(CustomModelAdmin):
    form = PerfilForm
    model = models.Perfil
    list_display = ('user', 'nombre', 'apellido', 'group', 'region', 'dni', 'email')
    search_fields = ('nombre', 'apellido', 'dni', 'aplicaciones__nombre')

class EventoAdmin(CustomModelAdmin):
    model = models.Evento
    list_display = ('id', 'region', 'titulo', 'fecha', 'inicio', 'fecha_fin', 'fin',  'responsable', 'escuela','fecha_de_creacion', 'fecha_de_ultima_modificacion')
    search_fields = ('id', 'titulo', 'legacy_id')

class EventoDeRoboticaAdmin(CustomModelAdmin):
    model = models.EventoDeRobotica
    list_display = ('id', 'fecha', 'inicio', 'fin', 'tallerista', 'fecha_de_creacion', 'fecha_de_ultima_modificacion')
    search_fields = ('id', 'tallerista')



class LocalidadForm(forms.ModelForm):

    class Meta:
        model = models.Localidad
        fields = ('__all__')
        widgets = {
            'distrito': autocomplete.ModelSelect2()
        }

class LocalidadAdmin(CustomModelAdmin):
    form = LocalidadForm
    model = models.Localidad
    list_display = ('id', 'nombre', 'distrito', 'cantidad_de_escuelas', 'numero_de_region', 'cantidad_de_perfiles_con_domicilio_vinculado')
    search_fields = ('id', 'nombre',)


class ComentarioDeTareaInline(admin.TabularInline):
    model = models.ComentarioDeTarea

class TareaAdmin(admin.ModelAdmin):
    inlines = [
        ComentarioDeTareaInline,
    ]


class ComentarioDeValidacionInline(admin.TabularInline):
    model = models.ComentarioDeValidacion

class ValidacionAdmin(admin.ModelAdmin):
    model = models.Validacion
    list_display = ('fecha_de_alta', 'fecha_de_modificacion', 'autor', 'cantidad_pedidas', 'cantidad_validadas', 'estado', 'observaciones', 'escuela')
    inlines = [
        ComentarioDeValidacionInline,
    ]


class CategoriaDeEventoAdmin(CustomModelAdmin):
    model = models.CategoriaDeEvento
    list_display = ('nombre', )

class TallerDeRoboticaAdmin(CustomModelAdmin):
    model = models.TallerDeRobotica
    list_display = ('nombre', "area")


class PisoAdmin(CustomModelAdmin):
    model = models.Piso
    list_display = ('servidor', 'serie', 'ups', 'rack', 'estado', 'llave')
    search_fields = ('id', 'servidor', 'serie', 'estado', 'llave')



class DistritoInline(admin.TabularInline):
    model = models.Distrito

class RegionAdmin(CustomModelAdmin):
    inlines = [
        DistritoInline,
    ]

class LocalidadInline(admin.TabularInline):
    model = models.Localidad

class DistritoAdmin(CustomModelAdmin):
    inlines = [
        LocalidadInline,
    ]
    list_display = ('id', 'nombre', 'cantidad_de_localidades', 'cantidad_de_escuelas', 'region', 'cantidad_de_perfiles_en_la_region')
    search_fields = ('id', 'nombre')

class PaqueteAdmin(CustomModelAdmin):
    model = models.Paquete
    list_display = (
        'legacy_id',
        'escuela',
        'fecha_pedido',
        'perfil_que_solicito_el_paquete',
        'ne',
        'id_hardware',
        'marca_de_arranque',
        'ma_hexa',
        'zip_paquete',
        'estado',
        'fecha_devolucion',
        'id_devolucion',
        'leido',
        'tpmdata'
    )
    search_fields = ('legacy_id', 'estado__nombre', 'escuela__cue', 'id_hardware')

class TrabajoAdmin(CustomModelAdmin):
    model = models.Trabajo
    list_display = (
        'fecha',
        'trabajo_id',
        'nombre',
        'archivo',
        'resultado',
        'progreso',
    )
    search_fields = ('trabajo_id', 'nombre')

class AplicacionAdmin(CustomModelAdmin):
    model = models.Aplicacion
    list_display = (
        'nombre',
        'identificador',
    )
    search_fields = ('nombre', 'identificador')

class DistribucionDePaqueteAdmin(CustomModelAdmin):
    model = models.DistribucionDePaquete
    list_display = (
        'fecha',
        'archivo',
    )


class ContactoAdmin(CustomModelAdmin):
    model = models.Contacto
    list_display = (
        'nombre',
        'escuela',
        'cargo',
        'telefono_particular',
        'telefono_celular',
        'email',
        'horario'
    )
    search_fields = ('nombre', 'cargo__nombre', 'escuela__nombre', 'email')

admin.site.register(Permission)
admin.site.register(models.Contacto, ContactoAdmin)
admin.site.register(models.Escuela, EscuelaAdmin)
admin.site.register(models.Evento, EventoAdmin)
admin.site.register(models.EventoDeRobotica, EventoDeRoboticaAdmin)
admin.site.register(models.Perfil, PerfilAdmin)

admin.site.register(models.MotivoDeConformacion)

admin.site.register(models.TipoDeFinanciamiento)
admin.site.register(models.Nivel)
admin.site.register(models.Modalidad)
admin.site.register(models.TipoDeGestion)
admin.site.register(models.Area)
admin.site.register(models.AreaDeRobotica)
admin.site.register(models.CursoDeRobotica)
admin.site.register(models.SeccionDeRobotica)
admin.site.register(models.EjeDeRobotica)
admin.site.register(models.Programa)
admin.site.register(models.Localidad, LocalidadAdmin)

admin.site.register(models.Experiencia)
admin.site.register(models.Cargo)
admin.site.register(models.RolEnRobotica)
admin.site.register(models.Contrato)

admin.site.register(models.Tarea, TareaAdmin)
admin.site.register(models.MotivoDeTarea)
admin.site.register(models.PrioridadDeTarea)
admin.site.register(models.EstadoDeTarea)
admin.site.register(models.ComentarioDeTarea)

admin.site.register(models.EstadoDeValidacion)
admin.site.register(models.EstadoDePaquete)
admin.site.register(models.Validacion, ValidacionAdmin)
admin.site.register(models.ComentarioDeValidacion)
admin.site.register(models.CategoriaDeEvento, CategoriaDeEventoAdmin)
admin.site.register(models.TallerDeRobotica, TallerDeRoboticaAdmin)
admin.site.register(models.Piso, PisoAdmin)
admin.site.register(models.Region, RegionAdmin)
admin.site.register(models.Distrito, DistritoAdmin)
admin.site.register(models.Paquete, PaqueteAdmin)
admin.site.register(models.Trabajo, TrabajoAdmin)
admin.site.register(models.DistribucionDePaquete, DistribucionDePaqueteAdmin)

admin.site.register(models.Aplicacion, AplicacionAdmin)
