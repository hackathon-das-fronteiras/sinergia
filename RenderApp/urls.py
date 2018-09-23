from django.urls import path
from RenderApp.views import home,cad_fornecedor,cad_empresa,consulta_residuos,demo_interesse

urlpatterns = [
    path('', home, name='home'),
    path('cadastro-fornecedor', cad_fornecedor, name='cad_fornecedor'),
    path('cadastro-empresa', cad_empresa, name='cad_empresa'),
    path('consulta-residuos', consulta_residuos, name='consulta_residuos'),
    path('demostrar-interesse/<int:pk>', demo_interesse, name='demo_interesse')
]