from django.urls import path , include
from . import views
urlpatterns = [
    path("", views.index, name="index" ),
    path("post/<int:post_id>/", views.post_detail, name="post_detail" ),
    path("author/<int:author_id>/", views.author_detail, name="author_detail" ),
    
]