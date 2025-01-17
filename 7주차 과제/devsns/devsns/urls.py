"""devsns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from snsapp import views
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name = 'home'),
    path('postcreaate', views.postcreate,name = 'postcreate'),
    # /뒷부분을 post.id라는 값을 int형으로 인자로 넘겨주겠다.
    path('detail/<int>', views.detail,name = 'detail'),
    path('new_comment/<int>', views.new_comment,name = 'new_comment'),
    # 로그인하는 페이지
    path('login/', account_views.login,name = 'login'),
    # 로그아웃하는 페이지
    path('logout/', account_views.logout,name = 'logout'),
    # 회원가입하는 페이지
    path('signup/', account_views.signup,name = 'signup'),
    # 자유게사판 관련 url
    path('freehome/', views.freehome,name = 'freehome'),
    path('freepostcreate', views.freepostcreate,name = 'freepostcreate'),
    path('freedetail/<int:post_id>', views.freedetail,name = 'freedetail'),
    path('new_freecomment/<int:post_id>', views.new_freecomment,name = 'new_freecomment'),
    # 소셜로그인을 위한 것
    path('accounts/', include('allauth.urls')),
    

    


]
