from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

from .models import Article
from .forms import CommentForm
from django.views import View


class CommentGet(DetailView):
    model = Article
    template_name = "news/article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentPost(FormView):
    model = Article
    form_class = CommentForm
    template_name = "news/article_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article = self.get_object()
        return reverse("news:article_detail", kwargs={"pk": article.pk})


class ArticleListView(ListView):
    model = Article
    template_name = "news/article_list.html"


class ArticleDetailView(View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class ArticleUpdateView(UserPassesTestMixin, UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "news/article_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "news/article_delete.html"
    success_url = reverse_lazy("news:article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(CreateView):
    model = Article
    template_name = "news/article_new.html"
    fields = (
        "title",
        "body",
        "author",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
