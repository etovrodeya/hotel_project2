from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from comments.models import Comment
from comments.forms import CommentReviewForm
from django.contrib import auth

def commentList(request):
    commentList=Comment.objects.all().order_by('-date')
    return render(request,'commentList.html',{'commentList':commentList})

def commentDetail(request,comment_id):
    commentDetail=get_object_or_404(Comment,pk=comment_id)
    return render(request, 'commentDetail.html', {'commentDetail': commentDetail})

@login_required
def commentReview(request):
    args={}
    error='Ошибка при заполнении формы'
    form=CommentReviewForm()
    if request.method == 'POST':
        form = CommentReviewForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.user = request.user
            response.save()
            return HttpResponseRedirect('/comments/')
        return render(request, 'commentReview.html', {'form': form,'error': error})
    return render(request, 'commentReview.html', {'form': form})
