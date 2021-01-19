from django.urls import path

from .views import (
    post_detail_view, 
    post_list_view,
    post_create_view,
    post_delete_view,
    # post_action_view
)

urlpatterns = [
    path('create-post', post_create_view),
    path('', post_list_view),
    path('<int:post_id>/', post_detail_view),
    path('<int:post_id>/delete/', post_delete_view),
    # path('action', post_action_view),
]