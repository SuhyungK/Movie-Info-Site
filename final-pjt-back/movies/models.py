from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# 영화
class Movie(models.Model):
    # # TMDB latest
    # movieId = models.IntegerField() # id
    # title = models.CharField(max_length=100)
    # release_date = models.TextField()
    # runtime = models.IntegerField()
    # overview = models.TextField()
    # vote_average = models.FloatField()
    # poster_path = models.TextField()
    # ## 장르가 dictionary 형태로 들어옴
    # genre_id = models.IntegerField() #
    # genre_name = models.TextField() #



    # # TMDB credits '/movie/{movie_id}/credits'
    # actors = models.TextField() # 리스트형태 -> 제이슨
    # # director = 모든 제작진이 조회가 됨


    # # TMDB Videos '/movie/{movie_id}/videos'
    # youtubeKey = models.TextField() #

    # # TMDB Image '/movie/{movie_id}/images'
    # backgroundPost = models.TextField() # 제이
    # #  가격????

    
    movie_id = models.IntegerField()
    title = models.CharField(max_length=20)
    original_title = models.CharField(max_length=20)
    overview = models.TextField()
    # video = models.BooleanField()
    genres = models.TextField()
    release_date = models.CharField(max_length=20)
    poster_path = models.TextField()
    backdrop_path = models.TextField()
    trailer_path = models.TextField(default=False, null=True, blank=True)
    popularity = models.IntegerField()
    vote_average = models.FloatField()
    is_now_playing = models.BooleanField(default=False, null=True, blank=True)

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movie')

# 리뷰
class Review(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True, null=True)  # 별점
    isSpoiler = models.BooleanField(default=False)
    username = models.TextField()

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_review')

    # 이건 필요 없는...? 
    # from_review = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)


class Comment(models.Model):
    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.TextField()

# class Ticketing(models.Model):
#     date = models.TextField()
#     region = models.TextField()
#     number_of_people = models.IntegerField()
#     seat = models.TextField()

#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)



