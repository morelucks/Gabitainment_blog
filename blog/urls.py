from django.urls import path
from . import views
urlpatterns=[
    path("login/", views.loginPage, name="login"),
    # path("admin-dashboard", views.adminDashboard, name="admin-dashboard"),
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.PostView.as_view(), name="posts-page"),
    path("createpost",views.createPost ,name="create-post"),

    path("create-author",views.CreateAuthor.as_view() ,name="create-author"),
    path("update-author/<str:pk>/",views.UpdateAuthor.as_view() ,name="update-author"),

    path("delete-comment/<str:pk>/", views.DeleteComment.as_view(), name="delete-comment"),
    
    path("updatepost/<str:pk>/",views.updatePost ,name="update-post"),
    path("deletepost/<str:pk>/",views.deletePost ,name="delete-post"),


    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="post-detail-page")
]