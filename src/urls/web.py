from django.urls import include, path
import sys
sys.path.append("src/views")
import home,post

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", home.index, name="home"),
    path("post", post.index, name="post"),
]
