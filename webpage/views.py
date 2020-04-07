from django.shortcuts import render , redirect, get_object_or_404, reverse,HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from webboard.models import boardpost
from accounts.models import Userprofile
# search.views.py
movieperpage= 16
# Create your views here.
def Index(request):
    movie = Reviewmovie.objects.all().order_by('-review_date')
    recom = Reviewmovie.objects.all().order_by('-score')[:6]
    # Page paginator
    paginator = Paginator(movie, movieperpage)
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
    context ={
        'movie':movie,
        'page_range':page_range,
        'items':items,
        'recom':recom
    }
    return render(request,'index.html',context)

def Movielist(request):
    movie = Reviewmovie.objects.all().order_by('-review_date')
    # Page paginator
    paginator = Paginator(movie, movieperpage)
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
        'movie':movie,
        'page_range':page_range,
        'items':items
    }
    return render(request,'movielist.html',context)

def Addmovie(request):
    category = Category.objects.all().order_by('category')
    if request.method == 'POST':
        moviename = request.POST['moviename']
        category = request.POST.getlist('category')
        director = request.POST['direct']
        actor = request.POST['actor']
        image = request.FILES['image']
        review = request.POST['reviewarea']
        score = request.POST['score']
        author = request.user
        post = Reviewmovie.objects.create(moviename=moviename,review=review,author=author,director=director,actor=actor,movie_image=image,score=score)
        rating = Ratingmovie.objects.create(movie=post,user=author,score=score)
        post.categorys.set(category)
        post.save()
        rating.save()
        return redirect('movie:addmovie')
    else:
     context ={
         'category':category
     }
     return render(request,'reviewmovie.html',context)

def Moviedetail(request, id):
    user = request.user
    movie = get_object_or_404(Reviewmovie, id = id)
    comment = Comment.objects.filter(movie=movie, reply=None)
    comment_count = Comment.objects.filter(movie=movie,reply=None).count()

    rate = Ratingmovie.objects.all().filter(movie=movie)
    if user.is_authenticated:
        checkrating = Ratingmovie.objects.filter(movie=movie, user=user)

    if request.method == 'POST':
        author = request.user
        score = request.POST.get('score',None)
        reply_id = request.POST.get('comment_id')
        movie.score = request.POST.get('allscore',1)
        movie.save()
        if reply_id:
            comment_qs=Comment.objects.get(id=reply_id)
            reply = request.POST['replytext']
            if reply == "":
                return redirect('movie:moviedetail',id=id)
            else:
                post = Comment.objects.create(comment=reply,author=author,movie=movie,reply=comment_qs)
                post.save()
                return HttpResponseRedirect('/moviedetail/{}'.format(movie.id))
        else:
            comment = request.POST['commenttext']
            post = Comment.objects.create(comment=comment,author=author,movie=movie)
            post.save()
            if score:
                calscore = Ratingmovie.objects.create(movie=movie,user=author,score=score)
                calscore.save()
            return HttpResponseRedirect('/moviedetail/{}'.format(movie.id))

    else:
        context = {
            'movie': movie,
            'comment': comment,
            'comment_count': comment_count,
            'rating': rate
        }
        if user.is_authenticated:
                context = {
                'movie': movie,
                'comment': comment,
                'comment_count': comment_count,
                'checkrating': checkrating,
                'rating': rate
            }

        return render(request,'moviedetail.html' ,context)

def Categorypage(request,id):
    movie = Reviewmovie.objects.all().filter(categorys=id).order_by('-review_date')
    category = Category.objects.get(id=id)
    # Page paginator
    paginator = Paginator(movie, movieperpage)
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
        'movie':movie,
        'page_range':page_range,
        'items':items,
        'category':category
    }

    return render(request,'categorypage.html',context)

def Dashboard(request,id):
    mymovie=Reviewmovie.objects.all().filter(author=id).order_by('-review_date')[:3]
    myboard= boardpost.objects.all().filter(Author=id).order_by('-Post_Date')[:3]
    allmymovie = Reviewmovie.objects.all().filter(author=id).order_by('-review_date')
    count_movie=Reviewmovie.objects.all().filter(author=id).count()
    count_webboard=boardpost.objects.all().filter(Author=id).count()
    movie = Reviewmovie.objects.all().order_by('-review_date')
    member = User.objects.all().order_by('-date_joined')
    webboard = boardpost.objects.all().order_by('-Post_Date')
    new_user = User.objects.all().order_by('-date_joined')[:3]
    new_movie = Reviewmovie.objects.all().order_by('-review_date')[:3]
    new_webboard = boardpost.objects.all().order_by('-Post_Date')[:3]
    category = Category.objects.all()
    context={
        'movie':movie,
        'member':member,
        'allmymovie':allmymovie,
        'webboard':webboard,
        'new_user':new_user,
        'new_movie':new_movie,
        'new_webboard':new_webboard,
        'category':category,
        'mymovie':mymovie,
        'count_movie':count_movie,
        'count_board':count_webboard,
        'myboard':myboard
    }
    return render(request,'dashboard.html',context)

def Profile(request,id):
    count_movie = Reviewmovie.objects.all().filter(author=id).count()
    count_webboard = boardpost.objects.all().filter(Author=id).count()
    context={
        'count_movie':count_movie,
        'count_board':count_webboard
    }
    return render(request,'editprofile.html',context)

def Search(request):
    movie = Reviewmovie.objects.all()
    webboard = boardpost.objects.all()
    query = request.GET.get('search')
    if query == "":
            return redirect("../")
    else:
        movie = movie.filter(moviename__icontains=query)
        webboard = webboard.filter(Title__icontains=query)
    context ={
        'movie':movie,
        'webboard':webboard
    }
    template = "search.html"
    return render(request,template,context)

def deletemovie(request,id):
    user=request.user.id
    movie = get_object_or_404(Reviewmovie,id=id)
    movie.delete()
    messages.success(request,'ลบข้อมูลสำเร็จ')
    return redirect('movie:dashboard',user)

def indexdeletemovie(request,id):
    movie = get_object_or_404(Reviewmovie,id=id)
    movie.delete()
    return redirect('movie:home')

def reportdeletemovie(request,id):
    movie = get_object_or_404(Reviewmovie,id=id)
    movie.delete()
    messages.success(request, 'ลบข้อมูลสำเร็จ')
    return redirect('report:report')



