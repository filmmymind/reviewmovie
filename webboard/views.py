from django.shortcuts import render, redirect, get_object_or_404,HttpResponseRedirect,reverse
from django.contrib.auth.models import User
from .models import boardpost,Boardcomment
from .forms import PostForm,CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.contrib import messages

postperpage = 10
# Create your views here.
def webboard(request):
    posts = boardpost.objects.all().order_by('-Post_Date')
    # Page paginator
    paginator = Paginator(posts, postperpage)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]
    # end Page Paginator
    context = {
        'page_range': page_range,
        'items': items,

    }
    return render(request,'webboard.html', context)

def createwebboard(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Author = request.user
            post.save()
            return redirect('../webboard')
    else:
        form = PostForm()
        return render(request,'createwebboard.html' , {'form':form})

def boarddetail (request, slug):
    post = get_object_or_404(boardpost , Slug=slug)
    boardcomment = Boardcomment.objects.all().filter(board=post,reply=None)
    comment_count=Boardcomment.objects.all().filter(board=post,reply=None).count()
    form = CommentForm

    if request.method=="POST":
        form = CommentForm(request.POST)
        reply_id = request.POST.get('comment_id')

        if reply_id:
            if form.is_valid():
                addreply = form.save(commit=False)
                comment_qs = Boardcomment.objects.get(id=reply_id)
                reply = request.POST['replytext']
                addreply.author = request.user
                addreply.board = post
                addreply.reply = comment_qs
                addreply.comment = reply
                addreply.save()
                return HttpResponseRedirect("/webboard/content/{}".format(post.Slug))
        elif form.is_valid():
            addcomment=form.save(commit=False)
            addcomment.author = request.user
            addcomment.board = post
            addcomment.save()
            return HttpResponseRedirect("/webboard/content/{}".format(post.Slug))
    context = {
        'post':post,
        'form':form,
        'boardcomment':boardcomment,
        'count':comment_count,
    }
    return render (request, 'boardcontent.html',context)

def deletewebboardreport (request,id):
    webboard = get_object_or_404(boardpost,id=id)
    webboard.delete()
    reverse('report:report')
    messages.success(request, 'ลบข้อมูลสำเร็จ')
    return redirect('report:report')

def deletewebboarddashboard (request,id):
    webboard = get_object_or_404(boardpost,id=id)
    webboard.delete()
    messages.success(request, 'ลบข้อมูลสำเร็จ')
    return redirect('/dashboard/{}'.format(webboard.Author.id))