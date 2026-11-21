from django.shortcuts import render, get_object_or_404
from .models import Movie, Genre, Advertisement


def home_view(request):
    query = request.GET.get('q')
    genre_id = request.GET.get('genre')

    movies = Movie.objects.all()

    if query:
        movies = movies.filter(title__icontains=query)
    if genre_id:
        movies = movies.filter(genres__id=genre_id)

    genres = Genre.objects.all()

    context = {
        'movies': movies,
        'genres': genres,
    }
    return render(request, 'movies/index.html', context)


def movie_detail_view(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    ad = Advertisement.objects.filter(is_active=True).order_by('?').first()

    context = {
        'movie': movie,
        'ad': ad,
    }
    return render(request, 'movies/detail.html', context)