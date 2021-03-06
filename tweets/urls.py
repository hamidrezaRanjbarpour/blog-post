from django.urls import path
from . import views

app_name = 'tweets'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_tweet/<int:post_id>/', views.delete_tweet, name='delete_tweet'),
    path('show_likes/<int:post_id>/', views.show_likes, name='show_likes'),
    path('ajax/like/', views.like_unlike_view, name='like_view'),
    path('ajax/retweet/', views.retweet_view, name='retweet_view'),
    path('register/', views.register_view, name='register'),
    path('post/', views.post, name='post'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user/<username>/', views.profile_view, name='profile'),
    path('hashtag/<hashtag>/', views.hashtag_view, name='hashtag'),
    path('comment/<int:post_id>', views.comment_view, name='comment'),

    path('user/<username>/follow', views.toggle_follow_view, name='follow'),
    path('user/<username>/edit_profile', views.edit_profile_view, name='edit_profile'),
    path('user/notification', views.notification_view, name='notification'),

]
