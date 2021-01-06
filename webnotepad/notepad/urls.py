from django.urls import path, include
from .views import memo_list, memo_write

urlpatterns = [
    path('', memo_list),
    path('write/', memo_write),
]
