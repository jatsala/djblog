from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Categoria, Post
from django.db.models import Q
from django.core.paginator import Paginator


def buscar(request, var):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact=var)
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact=var)
        ).distinct()

    return posts


def paginacion(request, posts):
    paginator = Paginator(posts, 1)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return posts


def home(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado=True)

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset)
        ).distinct()

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'index.html', {'posts': posts})


def detallePost(request, slug):
    # post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'post.html', {'detalle_post': post})

    # try:
    #     post = Post.objects.get(slug=slug)
    #     return render(request, 'post.html', {'detalle_post': post})
    # except Post.DoesNotExist:
    #     raise Http404


def generales(request):
    try:
        posts = buscar(request, 'General')
        posts = paginacion(request, posts)

        return render(request, 'generales.html', {'posts': posts})
    except Post.DoesNotExist:
        raise Http404
    # except Exception as e:
    #     print(f'Ocurrio un problema: {e}')


def programacion(request):
    try:
        posts = buscar(request, 'Programación')
        posts = paginacion(request, posts)
        return render(request, 'programacion.html', {'posts': posts})
    except Post.DoesNotExist:
        raise Http404


def tutoriales(request):
    try:
        posts = buscar(request, 'Tutoriales')
        posts = paginacion(request, posts)

        return render(request, 'tutoriales.html', {'posts': posts})
    except Post.DoesNotExist:
        raise Http404


def tecnologia(request):
    try:
        posts = buscar(request, 'Tecnología')
        posts = paginacion(request, posts)

        return render(request, 'tecnologia.html', {'posts': posts})
    except Post.DoesNotExist:
        raise Http404


def videojuegos(request):
    try:
        posts = buscar(request, 'Videojuegos')
        posts = paginacion(request, posts)

        return render(request, 'videojuegos.html', {'posts': posts})
    except Post.DoesNotExist:
        raise Http404
