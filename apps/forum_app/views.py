from django.shortcuts import render,redirect, get_object_or_404
from .forms import ForumForm, CommentForm
from .models import Comment,ForumPost
# Create your views here.


def forum_view(request):
    posts = ForumPost.objects.all().order_by('data_criacao')
    
    post_form = ForumForm()
    comment_form = CommentForm()

    if request.method == 'POST':

        
        if 'post_submit' in request.POST:
            post_form = ForumForm(request.POST)
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.save()
                return redirect('forum')
        
        elif 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                post_id = request.POST.get('post_id')
                post = get_object_or_404(ForumPost, id=post_id)
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()
                return redirect('forum')
        
    return render(request, 'pages_app/forum.html', {'posts': posts, 'post_form': post_form, 'comment_form': comment_form})
