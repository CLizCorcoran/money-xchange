from django.urls import path
from store import views
from store.models import Transactions


#home_list_view = views.HomeListView.as_view(
#    queryset=Transactions.objects.order_by("-log_date")[:5], # :5 limits the results to the five most recent
#    context_object_name="transaction_list",
#    template_name="store/home.html"
#)

urlpatterns = [
    path("", views.home, name="home"),
    #path("", home_list_view, name="home"),
    path("stock/<name>", views.stock_info, name="stock_info"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('log/', views.log_transaction, name="log"),
    path('transactions/', views.TransactionsByUserListView.as_view(), name='my-transactions'),
]