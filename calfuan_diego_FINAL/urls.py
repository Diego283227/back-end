
from django.contrib import admin
from django.urls import path
from calfuan_diego_FINAL_APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('listar/', views.listar_Inscripciones,name='listar'),
    path('agregar/', views.agregar_inscripcion,name='agregar'),
    path('eliminar/<int:id>', views.eliminar_inscripcion,name='eliminar'),
    path('actualizar/<int:id>', views.actualizar_inscripcion,name='editar'),
    path('inscritos/<int:pk>', views.InscripcionDetalle.as_view()),
    path('FBW/',views.InstitucionLista),
    path('FBW/<int:pk>',views.InstitucionDetalle),
    path('inscritos/', views.InscritosLista.as_view()),
    path('ver/', views.verinscripcion),
    path('instituciones/', views.agregarinstituciones),
    path('autor/', views.AutorDetalleView.as_view()),

]