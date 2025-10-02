from . import views
from django.urls import path

app_name = 'dama'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), #ok

    path('cadastro/', views.CadastroView.as_view(), name='cadastro'), #ok

    path('denuncia/', views.DenunciaView.as_view(), name='denuncia'), #ok

    path('mural/', views.MuralView.as_view(), name='mural'), #ok

    path('relato/', views.RelatoView.as_view(), name='relato'), #ok

    path('login/', views.LogarView.as_view(), name='login'), #ok

    path('logout/', views.LogoutView.as_view(), name='logout'), #ok

    path('perfil/', views.PerfilView.as_view(), name='perfil'), #ok

    path('material/', views.CadastroMaterialView.as_view(), name='material'), #ok

    path('material/<int:id>', views.MaterialDetailView, name='material-detail'), #ok

    path('materiais', views.MateriaisView.as_view(), name="materiais"), #ok
    
    path('editar/', views.EditarPerfilView.as_view(), name='editar'),

    path('delete/', views.DeletePerfilView.as_view(), name='delete'), #ok
]