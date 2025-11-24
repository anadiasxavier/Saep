from django.urls import path
from .views import (
    LoginView,
    ProdutoListCreateView,
    ProdutoRetrieveUpdateDestroyView,
    MovimentacaoCreateView
)

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path('produtos/', ProdutoListCreateView.as_view()),
    path('produtos/<int:pk>/', ProdutoRetrieveUpdateDestroyView.as_view()),
    path('movimentar/', MovimentacaoCreateView.as_view()),
]
