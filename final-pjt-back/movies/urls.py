from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tmp_list/', views.tmpList),
    path('tmp_reviewC/<int:movie_pk>/', views.tmpReviewCeate),
    path('like/<int:movie_pk>/', views.likeMovie),  #영화 좋아요
    path('like-list/', views.likeList),
    path('like-list-Detail/', views.likeListDetail),
    path('algorithm/', views.algorithm),
    path('my-review/', views.reviewcount), # 사용자가 쓴 리뷰 
    path('reviews/<int:movie_pk>/', views.movieReviews), # 특정영화에 대한 리뷰 목록가져오기
    path('like-review/<int:review_pk>/', views.likeReview),  #리뷰 좋아요
    path('like-reviews-list/', views.likeReviewList), # 내가 좋아요한 리뷰 리스트 뽑기
    path('search/', views.searchMovie),

    

]