from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('news', views.news, name='news'), # ZMIENIANNE Z SHOW NA NEWS
    path('show', views.show, name='show'),
    path('tutorial', views.tutorials, name='tutorial'),
    path('tutorial/<int:tutorial_id>',
         views.tutorials_szczegoly, name='tutorial_szczegoly'),
   
    path('blockchain', views.blockchains, name='blockchain'),
    path('blockchain/new', views.blockchain_nowy, name='blockchain_nowy'),
    path('blockchain/<int:blockchain_id>',
         views.blockchains_szczegoly, name='blockchain_szczegoly'),
    path('token', views.tokens, name='token'),
    
    path('token/new', views.token_nowy, name='token_nowy'),
    path('token/<int:token_id>',
         views.tokens_szczegoly, name='token_szczegoly'),
    path('cryptocurrencies', views.cryptocurrencies, name='cryptocurrencies'),
    path('basic', views.basics, name='basic'),
    path('basic/<int:basic_id>',
         views.basics_szczegoly, name='basics_szczegoly'),
    path('dict', views.dicts, name='dict'),
    path('dict/<int:dict_id>',
         views.dicts_szczegoly, name='dicts_szczegoly'),
    path('main', views.main, name='main'),   
    path('fake', views.cryptocurrencies, name='fake'),

         
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

