from django.urls import path

from .views import IndexView, DisciplinaView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('disciplina/<int:id>', DisciplinaView.as_view(), name='disciplina'),
]
