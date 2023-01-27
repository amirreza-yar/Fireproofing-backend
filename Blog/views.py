from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Blog, BlogComment
from .forms import MakeComment as MakeCommentForm

def blogs(request):
    
    blogs = Blog.objects.all()

    context = {
        "title": "بلاگ",
        "is_index_page": False,
        "blogs": blogs,
    }

    return render(request, "blogs.html", context=context)

def blogDetail(request, pk):

    blog = get_object_or_404(Blog, pk=pk)
    blog_comments = BlogComment.objects.all().filter(blog=blog)


    context = {
        "title": blog.title,
        "is_index_page": False,
        "blog": blog,
        "blog_comments": blog_comments,
    }
    
    return render(request, "blogDetail.html", context=context)

@login_required(login_url='login')
@require_POST
def makeBlogComment(request, pk):
    # print("I'm running!")
    # print(request.POST)
    comment_form = MakeCommentForm(request.POST)
    # print(comment_form)
    if comment_form.is_valid():
        # print(comment_form['comment'].value())
        BlogComment.objects.create(
            user=request.user,
            blog=Blog.objects.get(pk=pk),
            commenter_name=comment_form['commenter_name'].value(),
            commenter_email=comment_form['commenter_email'].value(),
            comment=comment_form['comment'].value(),
        )
        
        messages.success(request, "Commit sent!")
    
    else:
        messages.error(request, "Commit not sent!")

    return redirect('blog', pk=pk)