from django.contrib import admin
from django.urls import path,include
from blogg.views import frontpage,post_detail,addpost
from blogg import views


urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('addpost/', addpost, name='addpost'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls') ),
    path('admin/', admin.site.urls),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('<slug:slug>/delete_post',views.delete_post,name='delete_post'),
    path('<slug:slug>/update_post',views.update_post,name='update_post')

]
