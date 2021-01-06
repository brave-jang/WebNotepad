from django.urls import path, include
from .views import memo_list, memo_write, memo_detail

urlpatterns = [
    path('', memo_list),
    path('write/', memo_write),
    path('<int:post_id>/', memo_detail),
]
