from django.urls import path
from .views import  get_solutions,fetchs, update_problema,fetchs_neuro, update_solucao, delete_problema, delete_solucao,persona_list,listar_solucoes, problema_solucoes, persona_create, sobre_page, persona_delete, persona_update,fetch_problems, criar_problema, criar_solucao, listar_problemas, main_page, persona_info, solution_detail
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
    path('solution_detail/<int:id>/', solution_detail, name='solution_detail'),
    path('fetch_problems/', fetch_problems, name='fetch_problems'),
    path('get-solutions/', get_solutions, name='get_solutions'),
    path('problem_solutions/<int:pk>/', problema_solucoes, name='problem_solutions'),

    #neurodivergencias
    path('fetchs/', fetchs, name='fetchs'),
    path('fetchs_neuro/', fetchs_neuro, name='fetchs'),
    path('criar_problema/', criar_problema, name='criar_problema'),
    path('criar_solucao/', criar_solucao, name='criar_solucao'),
    path('listar_problemas/', listar_problemas, name='listar_problemas'),
    path('listar_solucoes/', listar_solucoes, name='listar_solucoes'),
    path('editar_problema/<int:problema_id>/', update_problema, name='update_problema'),
    
    path('deletar_problema/<int:problema_id>/', delete_problema, name='delete_problema'),

    # URLs de Solução
    path('editar_solucao/<int:solucao_id>/', update_solucao, name='update_solucao'),
    path('deletar_solucao/<int:solucao_id>/', delete_solucao, name='delete_solucao'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
