from django.urls import path
from django.urls.conf import re_path

from .views import *

urlpatterns = [
    # path('', WomenMain.as_view(), name = 'main'), 
    path('', index, name = 'main'), #http://127.0.0.1:8000/ 
    path('about/', about, name = 'about'),
    path('allcategories/', all_categories, name='all_cats'),
    path('addsmth/', AddSmth.as_view(), name = 'add_smth'),
    path('contact/', contact, name = 'contact'),
    path('login/', login_user, name = 'login'),
    path('register/', register_user, name = 'register'),
    path('logout/', logout_user, name = 'logout'),
    # path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    # path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
    #path('category/<slug:cat_slug>/', show_category, name='category'),
    path('category/<int:cat_id>/', show_category, name='category'),
    



    
    
    # path('category/<int:catid>/', categories), #http://127.0.0.1:8000/category/
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]
 