from django.shortcuts import render, get_object_or_404

from .models import Posts

# Create your views here.
def post_list(request):
    queryset = Posts.objects.all()
    context = {
        "object_list": queryset,
        "title": "Статьи",
    }
    return render(request, "post_list.html", context)


def post_detail(request, id=None):
    instance = get_object_or_404(Posts, id=id)
    context = {
        "object": instance,
        "title": instance.title,
    }
    return render(request, "post_detail.html", context)