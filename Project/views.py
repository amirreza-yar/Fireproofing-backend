from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Project, ProjectComment
from .forms import MakeComment as MakeCommentForm

def projects(request):
    
    projects = Project.objects.all()

    context = {
        "title": "پروژه ها",
        "is_index_page": False,
        "projects": projects,
    }

    return render(request, "projects.html", context=context)

def projectDetail(request, pk):

    project = get_object_or_404(Project, pk=pk)
    project_comments = ProjectComment.objects.all().filter(project=project)


    context = {
        "title": project.title,
        "is_index_page": project,
        "project": project,
        "project_comments": project_comments,
    }
    
    return render(request, "projectDetail.html", context=context)

@login_required(login_url='login')
@require_POST
def makeProjectComment(request, pk):
    # print("I'm running!")
    # print(request.POST)
    comment_form = MakeCommentForm(request.POST)
    # print(comment_form)
    if comment_form.is_valid():
        # print(comment_form['comment'].value())
        ProjectComment.objects.create(
            user=request.user,
            project=Project.objects.get(pk=pk),
            commenter_name=comment_form['commenter_name'].value(),
            commenter_email=comment_form['commenter_email'].value(),
            comment=comment_form['comment'].value(),
        )
        
        messages.success(request, "Commit sent!")
    
    else:
        messages.error(request, "Commit not sent!")

    return redirect('project', pk=pk)