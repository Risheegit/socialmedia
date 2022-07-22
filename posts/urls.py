from django.urls import path, reverse_lazy
from . import views
from django.views.generic import RedirectView
from .views import PostDeleteView, PostDetailView, PostListView, PostUpdateView, PostCreateView
from .views import AddCommentView, AddLike, AddDislike, ReportView, CommentDeleteView

urlpatterns = [
    path ('', PostListView.as_view(), name ='home'),
	path('admin/', RedirectView.as_view(url=reverse_lazy('admin:index')), name = 'admin'),
	path ('posts/new/', PostCreateView.as_view(), name ='create'),
	path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
	path('post/<int:pk>/like', AddLike.as_view(), name='like'),
	path ('posts/<int:pk>/report/', ReportView.as_view(),  name ='report'),
    path ('posts/<pk>/', PostDetailView.as_view(), name ='detail'),
	path ('posts/<pk>/update/', PostUpdateView.as_view(), name ='update'),
	path ('posts/<pk>/delete/', PostDeleteView.as_view(), name ='delete'),
	path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
]