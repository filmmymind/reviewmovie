from webpage.models import Category,Comment,User,Reviewmovie
from webboard.models import boardpost

def Category_name(request):
    category_name = Category.objects.all().order_by('category')
    return {'Category_name':category_name}

def Count_user(request):
    count_user = User.objects.all().count()
    return{'count_user':count_user}
def Count_movie(request):
    count_movie = Reviewmovie.objects.all().count()
    return {'count_allmovie':count_movie}
def Count_webboard(request):
    count_board = boardpost.objects.all().count()
    return {'count_allboard':count_board}

