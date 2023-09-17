from django.urls import path
from women.views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', categories)
]
