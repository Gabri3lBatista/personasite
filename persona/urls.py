from django.urls import path
from .views import  get_solutions, persona_list, persona_create, sobre_page, persona_delete, persona_update,fetch_problems, main_page, persona_info, solution_detail, generate_pdf
from django.conf import settings
from django.conf.urls.static import static

app_name = 'persona'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('sobre/', sobre_page, name='sobre_page'),
    path('listar_personas/', persona_list, name='persona_list'),
    path('criar_persona/', persona_create, name='persona_create'),
    path('editar_persona/<int:pk>/', persona_update, name='persona_update'),
    path('deletar_persona/<int:pk>/', persona_delete, name='persona_delete'),
    path('info_persona/<int:pk>/', persona_info, name='persona_info'),
    path('solution_detail/', solution_detail, name='solution_detail'),
    path('fetch_problems/', fetch_problems, name='fetch_problems'),
   # path('info_persona/<int:persona_id>/pdf/', generate_pdf, name='generate_pdf'),
    path('get-solutions/', get_solutions, name='get_solutions'),


]

