from django.urls import path
from kafedra_site.views import *

urlpatterns = [
    path('', edit_page, name = 'home'),
    path('article_cteate/', ArticleCreateView.as_view(), name = 'article_create'),
    path('relax-game/', page_app, name = 'relax'),

    path('logoin/',UserLoginViev.as_view(), name='login_page'),
    path('logout/',UserLogout.as_view(), name='logout_page'),

    path('profile/',ProfileListView.as_view(), name = 'profile'),
    path('profile-change/<int:pk>',ProfileUpdateView.as_view(), name = 'profile_update'),
    path('rating/',RatingListView.as_view(), name = 'rating'),
    path('groupmates/', GroupmatesListViews.as_view(), name = 'groupmates'),
]







