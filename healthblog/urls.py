from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    # path("post", views.posts, name="all-post"),
    # path("post/<slug:slug>", views.post_details, name="post-details-page")
]

