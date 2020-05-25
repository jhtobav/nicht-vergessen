from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect, get_list_or_404, get_object_or_404
from django.utils import timezone
from django.urls import reverse

from .models import Rating


# Create your views here.
def ratings(request):
    ratings_list = Rating.objects.order_by("-rating_score")
    return render(request, 'ratings/ratings.html', {'ratings_list': ratings_list})


def rating_details(request, rating_id):
    rating = get_object_or_404(Rating, pk=rating_id)
    return HttpResponse(
        f"Rating id: {rating.id} Title Name: {rating.rating_title} Rating Score: {rating.rating_score}"
        f"Rating review: {rating.rating_review} Rating creation date: {rating.rating_creation_date}")


def rating_create(request):
    rating = Rating(rating_title=request.POST['rating_title'],
                    rating_type=request.POST['rating_type'],
                    rating_score=request.POST['rating_score'],
                    rating_review=request.POST['rating_review'],
                    rating_creation_date=timezone.now())
    rating.save()
    return HttpResponseRedirect(reverse('ratings:ratings'))
