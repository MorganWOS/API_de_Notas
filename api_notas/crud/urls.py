from django.urls import path
from .views import UserView, MateriaView, NotaView
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'crud'

urlpatterns = [

    # Usuario endpoints
    path('users/', UserView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserView.as_view(), name='user-detail'),
    path('materia/', MateriaView.as_view(), name='materia-list'),
    path('nota/', NotaView.as_view(), name='nota-list')
]

# Add support for format suffixes (.json, .api, etc.)
urlpatterns = format_suffix_patterns(urlpatterns)
