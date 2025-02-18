from django.urls import path
from .views import blogs, create_blog, read_blog, update_blog, delete_blog

urlpatterns = [
    path("blogs/", blogs, name="blogs"),
    path("blog/create", create_blog, name="blog/create"),
    path("blog_read/<int:blog_id>", read_blog, name="blog/read"),
    path("blog_update/<blog_id>", update_blog, name="blog/update"),
    path("blog_delete/<blog_id>", delete_blog, name="blog/delete"),
]
