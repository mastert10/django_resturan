from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from .models import Article
from django.core.paginator import Paginator

# Create your views here.
def Home(request):
    articles = Article.objects.all()
    
    paginator = Paginator(articles,3)
    page_number = request.GET.get('page')
    article_list = paginator.get_page(page_number)
    
    context = {
        "articles":article_list,       
    }
    return render(request,'blog/home.html',context )
    
def Detail(request, slug):
    article = get_object_or_404(Article , slug=slug)
    resents = Article.objects.all().order_by("created")[:3]
    
    context = {
        "article":article,
        "resents":resents,

    }
    return render(request, 'blog/detail.html', context)

def Search(request):
    if request.method == "GET":
        src = request.GET.get("search")
    article_list = Article.objects.filter(title__icontains=src)
    context = {
        "articles":article_list,
    }
    return render(request, "blog/home.html", context)


    