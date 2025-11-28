from django.urls import path
from .views import (
    LoginView,
    ProdutoListCreateView,
    ProdutoRetrieveUpdateDestroyView,
    MovimentacaoCreateView,
)

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("produtos/", ProdutoListCreateView.as_view(), name="produtos-list"),
    path("produtos/<int:pk>/", ProdutoRetrieveUpdateDestroyView.as_view(), name="produtos-rud"),
    path("movimentar/", MovimentacaoCreateView.as_view(), name="movimentar"),
]
