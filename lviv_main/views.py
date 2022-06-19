from django.contrib.auth.forms import AuthenticationForm
from django.http.response import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.urls.base import reverse_lazy

from django.core.paginator import Paginator

from django.contrib.auth import authenticate, login, logout

# from django.contrib.auth.forms import UserCreationForm

#from lviv_places.lviv_main.forms import AddPostForms
from django.views.generic import ListView, DetailView, CreateView 

from .models import *
from .forms import *

# Create your views here.
 


# menu = ["Про сайт", "Додати...", "Зворотній зв'язок", "Увійти"]

menu = [
    {'title': "Про сайт", 'url_name': 'about'},
    {'title': "Додати...", 'url_name': 'add_smth'},
    {'title': "Контакти", 'url_name': 'contact'},
    # {'title': "Увійти", 'url_name': 'login'},
]


# class WomenMain(ListView):
#     model = Women
#     template_name = 'lviv_main/index.html'
#     context_object_name = 'posts'

#     #extra_context = {'title': "Головна сторінка"}

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu'] = menu
#         context['title'] = "Головна сторінка"
#         context['cat_selected'] = 0
#         return context 

#     def get_queryset(self):
#         return Women.objects.filter(is_published = True)

def index(request):
    cats = Category.objects.all()

    content={
        'cats': cats,
        'menu': menu,
        'title': "Головна сторінка",

    }
    return render(request, 'lviv_main/index.html', context = content )

def all_categories(request):
    cats = Category.objects.all()
    

    content={
        
        'cats': cats,
        'menu': menu,
        'title': "Категорії",
        

    }
    return render(request, 'lviv_main/all_categories.html', context = content )



def about(request):
    cats = Category.objects.all()

    content={
        
        'cats': cats,
        'menu': menu,
        'title': "Про сайт",

    }

    return render(request, 'lviv_main/about.html', context = content) 



class AddSmth(CreateView):
    form_class = AddPostForm
    template_name = 'lviv_main/addsmth.html'
    success_url = reverse_lazy('main') 

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Додати..."
        context['menu'] = menu
        cats = Category.objects.all() 
        context['cats'] = cats
        return context


# def addsmth(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             # try: 
#             form.save()
#                 # Women.objects.create(**form.cleaned_data)
#             return redirect('main')
#             # except:
#             #     form.add_error(None, 'Помилка додавання')

#     else:
#         form = AddPostForm()

#     return render(request, 'lviv_main/addsmth.html', {'form': form, 'menu': menu, 'title': 'Додати...'})

#     #return HttpResponse ("Додати...")

def contact(request):
    cats = Category.objects.all()

    content  = {
        'cats': cats,
        'menu': menu,
        'title': "Контактна інформація",

    }

    return render(request, 'lviv_main/contact.html', context=content)



# def login(request):
#     cats = Category.objects.all()

#     content  = {
#         'cats': cats,
#         'menu': menu,
#         'title': "Вхід",

#     }

#     return render(request, 'lviv_main/login.html', context=content)

    



# def categories(request, catid):
#     #if (request.GET):
#          #print (request.GET)

#     #if (request.POST):
#         #print (request.POST) 
       
#     return HttpResponse (f"<h1>Статті за категоріями:</h1><p>{catid}</p>")

# def archive(request, year):
#     if int(year) > 2020:
#         return redirect('main', permanent = True)

#     return HttpResponse (f"<h1>Архів за роками</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінку не знайдено...</h1>')

def show_post(request, post_slug):
    post=get_object_or_404(Women, slug=post_slug)
    cats = Category.objects.all()


    content= {
        'post': post,
        'cats': cats,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,

    }

    return render(request, 'lviv_main/post.html', context=content)

    #return HttpResponse(f"Відображення допису з id = {post_id}")

# class ShowPost(DetailView):
#     model = Women
#     template_name = 'lviv_main/index.html'
#     slug_url_kwarg = 'post_slug'
#     context_object_name = 'post'

#     # pk_url_kwarg = 'post_pk'

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = context['post']
#         context['menu'] = menu
#         return context


# class WomenCategory(ListView):
#     model = Women
#     template_name = 'lviv_main/index.html'
#     context_object_name = 'posts'
#     allow_empty = False

#     def get_queryset(self):
#         return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

#     def get_context_data(self, *, object_list=None, **kwargs ):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Категорія - ' + str(context['posts'][0].cat)
#         context['menu'] = menu
#         context['cat_selected'] = context['posts'][0].cat_id
#         context['cats'] = Category.objects.all()
#         return context


def show_category(request, cat_id):
    posts=Women.objects.filter(cat_id=cat_id)
    cats=Category.objects.all()
    #cat_selected = Category.objects.get(slug=cat_slug)

    if len(posts) == 0:
        raise Http404()

    paginator = Paginator(posts, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    content={
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': "Досліджуй місто Лева з нами!",
        # 'cat_selected': cat_selected.cat_id,
        'cat_selected': cat_id,
        'page_obj': page_obj,

    }
    return render(request, 'lviv_main/show_category.html', context = content )


# class RegisterUser(request):
#     form_class = UserCreationForm
#     template_name = 'lviv_main/register.html'
#     success_url = reverse_lazy('login')

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Реєстрація")
#         return dict(list(context.items()) + list(c_def.items()))


def register_user(request):
    # form = UserCreationForm # UserCreationForm
    form = RegisterUserForm
    cats=Category.objects.all()
    
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')

    context = {
        'title': "Реєстрація",
        'menu': menu,
        'form': form,
        'cats': cats,
    }
    return render(request, 'lviv_main/register.html', context=context)



# class LoginUser(DataMixin, LoginView):
#     form_class = AuthenticationForm
#     template_name = 'lviv_main/login.html'

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Авторизація")
#         return dict(list(context.items()) + list(c_def.items()))


def login_user(request):
    # form = RegisterUserForm
    form = AuthenticationForm
    cats=Category.objects.all()

    if request.method == 'POST':
        # form = AuthenticationForm(request.POST)
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('all_cats')


    context = {
        'title': "Авторизація",
        'menu': menu,
        'form': form,
        'cats': cats,
    }
    return render(request, 'lviv_main/login.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('main')



