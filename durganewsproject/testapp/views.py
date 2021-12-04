from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'testapp/index.html')
def movie_view(request):
    head_msg='DURGA MOVIE NEWS'
    m1='OTT is the result of covid'
    m2='RRR ready to release and will give left and right'
    m3='Cheating case filed on Salman and his sister'
    m4='Love story is ready to release'
    m5='Real life of screen actors is very horrible'
    type='movies'
    my_dict={'head_msg':head_msg,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'type':type}
    return render(request,'testapp/news.html',my_dict)
def sports_view(request):
    head_msg='DURGA Sports NEWS'
    m1='OTT is the result of covid'
    m2='RRR ready to release and will give left and right'
    m3='Cheating case filed on Salman and his sister'
    m4='Love story is ready to release'
    m5='Real life of screen actors is very horrible'
    type='sports'
    my_dict={'head_msg':head_msg,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'type':type}
    return render(request,'testapp/news.html',my_dict)
def politics_view(request):
    head_msg='DURGA Politics NEWS'
    m1='OTT is the result of covid'
    m2='RRR ready to release and will give left and right'
    m3='Cheating case filed on Salman and his sister'
    m4='Love story is ready to release'
    m5='Real life of screen actors is very horrible'
    type='politics'
    my_dict={'head_msg':head_msg,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'type':type}
    return render(request,'testapp/news.html',my_dict)
