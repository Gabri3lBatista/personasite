from django.urls import path
from .views import persona_list, persona_create, persona_delete, persona_update, main_page, persona_info

app_name = 'persona'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('listar_personas/', persona_list, name='persona_list'),
    path('criar_persona/', persona_create, name='persona_create'),
    path('editar_persona/<int:pk>/', persona_update, name='persona_update'),
    path('deletar_persona/<int:pk>/', persona_delete, name='persona_delete'),
    path('info_persona/<int:pk>/', persona_info, name='persona_info')
]