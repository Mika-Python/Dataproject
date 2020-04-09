from django.shortcuts import render, redirect
from firstbook.forms import NewComment
from firstbook.models import Comment


def new_comment(request):
    if request.method == 'POST':
        form = NewComment(request.POST)
        form.save()


    else:
        form = NewComment()
    return render(request, "firstbook/new_comment.html", {'form': form})


def comment_list(request, study):
    comment = []
    for i in Comment.objects.filter(study__name=study):
        comment.append(i)

    return render(request, "firstbook/comment_list.html", {'list': comment, 'study': study})