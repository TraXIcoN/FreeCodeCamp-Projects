from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.forms import ModelForm
from .models import User, Listing, Bid, Comments
from .forms import ListingForm


def index(request):
    if( User.objects.filter(username=request.user.username).exists()):
        list = Listing.objects.all()
        amt=[]
        for item in list:
            if(Bid.objects.filter(bid=item).exists()):
                currentbid = Bid.objects.get(bid=item)
                amt.append(currentbid.amount)
            else:
                amt.append(item.startbid)
        List= zip(list,amt)
        return render(request, "auctions/index.html", {'List':List})
    else:
        return render(request, "auctions/index.html", {'present':0, 'amt':" "})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def createlist(request):
    if request.method == "GET":
        form = ListingForm()
        return render(request, "auctions/list.html", {'form':form, 'error':False})
    else:
        l = Listing(user=User.objects.get(username=request.user.username))
        form = ListingForm(request.POST, instance=l)
        if form.is_valid():
            form.save()
        else:
            form = ListingForm()
            return render(request, "auctions/list.html", {'form':form, 'error':True})
        return index(request)

def listview(request,item):
    it = Listing.objects.get(id=item)
    u = User.objects.get(username=request.user.username)
    wl = User.objects.get(username=request.user.username).watchlist.all()
    if(Bid.objects.filter(bid=it).exists()):
        currentbid = Bid.objects.get(bid=it)
        amt = currentbid.amount
        if(u.id == currentbid.bidder.id):
            result = True
        else:
            result = False
    else:
        amt = it.startbid
        result = False
    cmt = Comments.objects.filter(rlist=it)

    own = u.owner.all()


    if it in wl:
        return render(request, 'auctions/listing.html' ,{'listing':it, 'wlist':True, 'amount':amt, 'comments':cmt, 'own':own, 'r':result})
    else:
        return render(request, 'auctions/listing.html' ,{'listing':it, 'wlist':False, 'amount':amt, 'comments':cmt, 'own':own, 'r':result})

def watchlist(request,list,remove):
    if remove==0:
        user = User.objects.get(username=request.user.username)
        user.watchlist.add(Listing.objects.get(id=list))
    else:
        user = User.objects.get(username=request.user.username)
        user.watchlist.remove(Listing.objects.get(id=list))
    return show_watchlist(request)

def show_watchlist(request):
    user = User.objects.get(username=request.user.username)
    list = user.watchlist.all()
    amt=[]
    for item in list:
        if(Bid.objects.filter(bid=item).exists()):
             currentbid = Bid.objects.get(bid=item)
             amt.append(currentbid.amount)
        else:
            amt = item.startbid
    if(len(list) == 0):
        return render(request, "auctions/watchlist.html", {'present':0, 'amt':" "})
    else:
        List= zip(list,amt)
        return render(request, "auctions/watchlist.html", {'List':List})
def bid(request, i):
    userr = User.objects.get(username=request.user.username)
    if (Bid.objects.filter(bid=Listing.objects.get(id=i)).exists()):
        currentbid = Bid.objects.get(bid=Listing.objects.get(id=i))
        currentbid.amount = request.POST['quantity']
        currentbid.bidder = userr
        currentbid.save()
        return listview(request, i)

    else:
        b = Bid(bid=Listing.objects.get(id=i),bidder=userr,amount=request.POST['quantity'])
        b.save()
        return listview(request, i)

def comment(request,li):
    c = Comments(rlist=Listing.objects.get(id=li), commenter=User.objects.get(username=request.user.username), comment=request.POST['name'])
    c.save()
    return listview(request,li)

def close(request,list):
    c = Listing.objects.get(id=list)
    c.closed = True
    c.save()
    return listview(request,list)

def category(request,cat):
    if cat == " ":
        return render(request, "auctions/category.html", {'clist':['Electronics','Fashion','Homedecor','Automobiles','Sports equipment','Music equipment','Books','Miscallenous']})
    else:
        if(Listing.objects.filter(category=cat).exists()):
            l = Listing.objects.filter(category=cat)
            amt=[]
            for item in l:
                if(Bid.objects.filter(bid=item).exists()):
                    currentbid = Bid.objects.get(bid=item)
                    amt.append(currentbid.amount)
                else:
                    amt.append(item.startbid)
            List= zip(l,amt)
            return render(request, "auctions/index.html", {'List':List})
        else:
            return render(request, "auctions/index.html", {'present':0, 'amt':" "})
