from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlist", views.createlist, name="createlist"),
    path("listview/<int:item>", views.listview, name="listview"),
    path("watchlist/<int:list>/<int:remove>", views.watchlist, name="watchlist"),
    path("show_watchlist", views.show_watchlist, name="show_watchlist"),
    path("bid/<int:i>", views.bid, name="bid"),
    path("comment/<int:li>", views.comment, name="comment"),
    path("close/<int:list>", views.close, name="close"),
    path("category/<str:cat>", views.category, name="category")
]
