from django.urls import path

from . import views

app_name = 'polls' ##namespace url names

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
#Note that the name of the matched pattern in the path strings of the second and third patterns has changed from <question_id> to <pk>.






# ye jo hai generic view ke liye nahi hai 
#isme saare views ko hard code kiya hai
# upar jo hai wo generic view hai jisme 

# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),  
# #     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
# #     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
# #     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'), 
# ]