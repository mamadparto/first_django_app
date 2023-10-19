from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Posts
from . import forms


class PostListView(generic.ListView):
    template_name = "weblog/posts_lists.html"
    context_object_name = "all_posts"

    def get_queryset(self):
        return Posts.objects.filter(status="pub").order_by("-datetime_update")


class PostDetailView(generic.DetailView):
    model = Posts
    template_name = "weblog/post_detail.html"
    context_object_name = "post"


class PostCreateView(generic.CreateView):
    form_class = forms.NewPostForm
    template_name = "weblog/post_new_post.html"
    # context_object_name = "form"


class PostUpdateView(generic.UpdateView):
    model = Posts
    form_class = forms.NewPostForm
    template_name = "weblog/post_new_post.html"


class PostDeleteView(generic.DeleteView):
    model = Posts
    template_name = "weblog/post_delete.html"
    success_url = reverse_lazy("list_of_post")

# def list_of_post(request):
#     all_posts = Posts.objects.filter(status="pub").order_by("-datetime_update")
#     return render(request, "weblog/posts_lists.html", {"all_posts": all_posts})

# def post_detail(request, pk):
#     post = get_object_or_404(Posts, pk=pk)
#     return render(request, "weblog/post_detail.html", {'post': post})


# def create_post(request):
#     if request.method == "POST":
#         form = forms.NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("list_of_post")
#
#     else:
#         form = forms.NewPostForm()
#
#     return render(request, "weblog/post_new_post.html", context={"new_post_form": form})

# def update_post(request, pk):
#     post = get_object_or_404(Posts, pk=pk)
#     form = forms.NewPostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect("list_of_post")
#
#     return render(request, "weblog/post_new_post.html", context={"form": form})

# def delete_post(request, pk):
#     post = get_object_or_404(Posts, pk=pk)
#
#     if request.method == 'POST':
#         post.delete()
#         return redirect("list_of_post")
#
#     return render(request, "weblog/post_delete.html", context={"post": post})
