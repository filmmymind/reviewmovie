from django.shortcuts import render,get_object_or_404,redirect,HttpResponseRedirect
from webboard.models import *
from webpage.models import *
from webboard.forms import *
from django.contrib import messages


# Create your views here.
def Deletemoviecomment(request,id):
    comment = get_object_or_404(Comment,id=id)
    comment.delete()
    return redirect('/moviedetail/{}'.format(comment.movie.id))

def Deletemoviereply(request,id):
    reply = get_object_or_404(Comment,id=id)
    reply.delete()
    return redirect('/moviedetail/{}'.format(reply.movie.id))

def Deletewebboard(request,id):
    webboard = get_object_or_404(boardpost,id=id)
    webboard.delete()
    messages.success(request, 'Delete สำเร็จ')
    return redirect('board:webboard')

def Deletewebboardcomment(request,id):
    comment = get_object_or_404(Boardcomment,id=id)
    comment.delete()
    return redirect('board:boardcontent',comment.board.Slug)

def Editmovie(request,id):
    if request.method == 'POST':
        movie = get_object_or_404(Reviewmovie,id=id)
        movie.moviename = request.POST['moviename']
        movie.director = request.POST['direct']
        movie.actor = request.POST['actor']
        movie.review = request.POST['reviewarea']
        movie.movie_image = request.FILES.get('image', movie.movie_image)
        category = request.POST.getlist('category')
        movie.categorys.set(category)
        movie.save()
        print (movie.moviename)
        messages.success(request,'บันทึกสำเร็จ')
        return redirect('movie:moviedetail',id)
    else:
        movie = get_object_or_404(Reviewmovie,id=id)
        category = Category.objects.all().order_by('category')
        context={
            'movie':movie,
            'category':category
        }
        return render(request,'editmovie.html',context)

def EditmovieReply(request,id):
    reply = get_object_or_404(Comment,id=id)
    reply.comment = request.POST['replyedit']
    reply.save()
    print(reply.comment)
    return redirect('movie:moviedetail',reply.movie.id)

def EditmovieComment(request,id):
    comment = get_object_or_404(Comment,id=id)
    comment.comment = request.POST['commentedit']
    print(comment.comment)
    comment.save()
    return redirect('movie:moviedetail',comment.movie.id)

def EditWebboard(request,id):
    board = get_object_or_404(boardpost, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST,instance = board)
        if form.is_valid():
            post = form.save()
            post.save()
            messages.success(request,'บันทึกสำเร็จ')
            return redirect('board:boardcontent',board.Slug)
    else:
        forms = PostForm(instance = board)
        print(board.id)
        context = {
            "forms":forms,
            "board":board
        }
        return render(request,'editwebboard.html',context)

def EditWebboardComment(request,id):
    comment = get_object_or_404(Boardcomment, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST,instance = comment)
        if form.is_valid():
            post = form.save()
            post.comment = request.POST['editcomment']
            post.save()
            print(comment.id)
        return redirect('board:boardcontent', comment.board.Slug)
    else:
        return redirect('board:boardcontent',comment.board.Slug)

def EditWebboardReply(request,id):
    reply = get_object_or_404(Boardcomment,id=id)
    print(reply.id)
    print(reply.comment)
    if request.method == "POST":
        form = CommentForm(request.POST,instance=reply)
        if form.is_valid():
            post = form.save()
            post.comment = request.POST['editreply']
            post.save()
            return redirect('board:boardcontent',reply.board.Slug)
        else:
            return redirect('board:boardcontent',reply.board.Slug)

def EditStatus(request,id):
    userinformation = get_object_or_404(User,id=id)
    if userinformation.is_staff == True:
        userinformation.is_staff = False
    else:
        userinformation.is_staff = True
    userinformation.save()
    messages.success(request,'บันทึกการเปลี่ยนแปลงสำเร็จ')
    return redirect('report:userinformation',id)
