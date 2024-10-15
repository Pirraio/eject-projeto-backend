from django.shortcuts import render,redirect, get_object_or_404
from .forms import ForumForm
from .models import Comment,ForumPost
# Create your views here.

def post_list(request):
    posts = ForumPost.objects.all()
    form = ForumPost()
    if request.method == 'POST':
        form = ForumPost(request.POST)
        if form.is_valid():
            form.save()

            #TODO: Ajeitar caminho
            return redirect('post_list')
        
    return render(request, 'forum/post_list.html', {'posts': posts, 'form': form})

def post_comments(request,post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    comentarios = post.comentarios.all() #Utiliza o related_name do model para pegar os comentarios
    form = Comment()
    if request.method == 'POST':
        form = Comment(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post  # Associa o comentário ao post
            comentario.save()

            #TODO: Preencher com caminho para template
            return redirect('post_detail', post_id=post.id)
        
            #TODO: Preencher com caminho para template
    return render(request, 'forum/post_detail.html', {'post': post, 'comentarios': comentarios, 'form': form})