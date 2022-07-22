from django.urls import path
from users.views import ProfileView, EditProfileView
from users.views import AddFollower, RemoveFollower, ListFollowers

urlpatterns = [
    path('profile/<int:pk>/', ProfileView.as_view(), name = 'profile'),
    path('profile/edit/<int:pk>/', EditProfileView.as_view(), name='profile-edit'),
    path('profile/<int:pk>/followers/', ListFollowers.as_view(), name='list-followers'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
]