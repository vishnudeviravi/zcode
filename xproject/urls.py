from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name ='home'),
    path('<int:id>', views.info, name='info'),
    path('accounts/', include('accounts.urls')),
    path('add/',views.add, name='add'),
    path('search',views.search,name='search'),
    path('<int:id>/upvote',views.upvote, name='upvote')
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)