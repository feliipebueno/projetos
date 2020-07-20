from django.urls import include, path
from rest_framework import routers
from .views import *
from . import views

handler404 = views.handler404
handler500 = views.handler500


router = routers.DefaultRouter()
router.register(r'forma', FormaViewSet)
router.register(r'materia', MateriaViewSet)
router.register(r'processo', ProcessoViewSet)
router.register(r'tipoprocesso', TipoProcessoViewSet)



urlpatterns = [

    #index
    path('', index, name='index'),

    #Forma
    path('forma/', forma, name='forma'),
    path('forma/new', forma_new, name='forma/new'),
    path('forma/edit/<int:id>', forma_edit, name='forma/edit/'),
    path('forma/delete/<int:id>', forma_delete, name='forma/delete/'),
    #Matéria
    path('materia/', materia, name='materia'),
    path('materia/new', materia_new, name='materia/new'),
    path('materia/edit/<int:id>', materia_edit, name='materia/edit/'),
    path('materia/delete/<int:id>', materia_delete, name='materia/delete/'),

    #Tipo Processo
    path('tipo_processo/', tipo_processo, name='tipo_processo'),
    path('tipo_processo/new', tipo_processo_new, name='tipo_processo/new'),
    path('tipo_processo/edit/<int:id>', tipo_processo_edit, name='tipo_processo/edit/'),
    path('tipo_processo/delete/<int:id>', tipo_processo_delete, name='tipo_processo/delete/'),

    #Processo
    path('processo/', processo, name='processo'),
    path('processo/new', processo_new, name='processo/new'),
    path('processo/edit/<int:id>', processo_edit, name='processo/edit/'),
    path('processo/delete/<int:id>', processo_delete, name='processo/delete/'),

    #Django rest Framework
    path('api/', include(router.urls)),

]