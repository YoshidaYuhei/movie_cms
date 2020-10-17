from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from django.urls import path, include
from telephone_range import settings
from . import views
from .models import Genre


app_name = 'binty'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:content_id>/', views.DetailView.as_view(), name='detail'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('cast-autocomplete/', views.CastAutoComplete.as_view(), name='cast-autocomplete'),
    path('genre-autocomplete/', views.GenreAutoComplete.as_view(model=Genre), name='genre-autocomplete'),
    path('director-autocomplete/', views.DirectorAutoComplete.as_view(), name='director-autocomplete'),
    path('import/', views.ContentImport.as_view(), name='import'),
    path('castlist/<int:cast_id>/', views.CastListView.as_view(), name='castlist'),
    path('subform/', views.sub_form_view, name='subform'),
    path('mypage/<int:user_id>/', views.MyPageView.as_view(), name='mypage'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('ajax/', views.ajax, name='ajax'),
    # path('test/', views.samplefunc, name='test'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
