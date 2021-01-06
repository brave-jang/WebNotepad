from django.urls import path, include
from .views import memo_list, memo_write, memo_detail, memo_edit


app_name = "notepad"
urlpatterns = [
    path('', memo_list),
    path('write/', memo_write),
    path('<int:post_id>/', memo_detail, name="detail"),
    path('edit/<int:post_id>', memo_edit, name="edit")
]
