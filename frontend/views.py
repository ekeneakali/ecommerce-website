from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from . forms import *

from frontend.models import *

from django.contrib import messages

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

from .tokens import account_activation_token
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
import os
from .forms import SetPasswordForm
from .forms import PasswordResetForm

 
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import  ListView
from hitcount.views import HitCountDetailView
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin
from django.urls import reverse_lazy
from django.http.response import JsonResponse
from cart.cart import Cart
from django.core.paginator import Paginator
import copy
from django.conf import settings
import xlwt
import csv





# from django.contrib.auth.forms import authenticate, login



# Create your views here.


# PRODUCT CODE ENDS HERE
def home(request):
    auto = Product.objects.all().order_by('-created_at')
    store = Product.objects.all()[:3]
    fashion = Product.objects.all()[:3] 
    latest = Post.objects.all()[:2]
    
    page_num = request.GET.get('page', 1)
    paginator = Paginator(auto, 12)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'frontend/index.html', {'page_obj':page_obj, 'latest':latest, 'store':store, 'fashion':fashion})


def shop(request):
    auto = Product.objects.all().order_by('-created_at')
    late = Product.objects.all()[:3]
    cat_desc = Product.objects.all()[:2]
    page_num = request.GET.get('page', 1)
    paginator = Paginator(auto, 24)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'frontend/shop.html', {'page_obj':page_obj, 'late':late, 'cat_desc':cat_desc})

def two(request, pst):
    if not request.user.is_authenticated:
        messages.success(request, 'Login to Continue')
        return redirect('frontend:custom_login')
    
        
    race = Product.objects.get(pk=pst)
    race.num_site = race.num_site + 1
    race.save()
    product = Product.objects.all()[:3]
    
    is_liked = False
    is_favourite = False
    if race.likes.filter(id=request.user.id).exists():
        is_liked = True
    
    if race.favourite.filter(id=request.user.id).exists():
        is_favourite = True
    
    
    return render(request, 'frontend/detail-page.html', {'race':race, 'is_liked':is_liked, 'total_likes':race.total_likes, 'is_favourite':is_favourite, 'product':product})

def like_post(request, pk):
    post = get_object_or_404(Product, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
        messages.success(request, 'You dislike this product')
    else:

        post.likes.add(request.user)
        is_liked = True
        messages.success(request, 'thank you for liking this product')
            
    return HttpResponseRedirect(reverse('frontend:two', args=[str(pk)]))


def add_post(request):
    if not request.user.is_authenticated:
        return redirect('frontend:custom_login')

    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        image = request.FILES.getlist('image')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            for image in  image:
                messages.success(request, 'product added successfully ')
                return redirect('frontend:view_post')
    
    else:
        form = ProductForm()

    return render(request, 'frontend/addproduct.html', {'form':form})


def view_post(request):
    
    post = Product.objects.filter(user=request.user)

    post_item = Order_Items.objects.filter(product__user=request.user)



    return render(request, 'frontend/view-post.html', {'post':post, 'post_item':post_item})

def delete_post(request, pst_id):
    single_post = Product.objects.get(id=pst_id)
    single_post.delete()
    messages.success(request, 'file deleted successfully')

    return redirect('frontend:view_post')


def edit_post(request, pst_id):
    if not request.user.is_authenticated:
        return redirect('frontend:custom_lgin')

    edited = Product.objects.get(id=pst_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=edited)
        if form.is_valid():
            form.save()
            messages.success(request, 'product edited successfully')
    
    else:
        form = ProductForm(instance=edited)

    return render(request, 'frontend/edit-post.html', {'form':form})

def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        
        query_filter = Product.objects.filter(Q(name__icontains=search) | Q(description__icontains=search)  | Q(created_by__icontains=search)  | Q(select_category__select__icontains=search))
    
    return render(request, 'frontend/base.html', {'query':query_filter, 'search':search})

    # PRODUCT whishlist STARTS HERE

def favourite_post(request, id):
    if not request.user.is_authenticated:
        return redirect('frontend:custom_login')


    post = Product.objects.get(id=id)

    if post.favourite.filter(id=request.user.id).exists():
        post.favourite.remove(request.user)
        messages.success(request, 'product remove from whishlist succesfully!')


    else:
        post.favourite.add(request.user)
        messages.info(request, 'product added to whishlist successfully!')


    return HttpResponseRedirect(reverse('frontend:two', args=[str(id)]))

def post_list(request):
    if not request.user.is_authenticated:
        messages.success(request, 'Login to Continue')
        return redirect('frontend:custom_login')


    user = request.user

    favourite_post = user.favourite.all()

    return render(request, 'frontend/wishlist.html', {'favourite_post':favourite_post})

    # PRODUCT whishlist ENDS HERE

# PRODUCT CODE ENDS HERE

    # BLOG CODE START HERE

def blog(request):
    auto = Post.objects.all().order_by('-created_at')
    recent = Post.objects.all()[:2]
    comment = Comment.objects.all()[:3]
    page_num = request.GET.get('page', 1)
    paginator = Paginator(auto, 12)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'frontend/blog.html', {'page_obj':page_obj, 'recent':recent, 'comment':comment})

def blog_two(request, pst_id):

    race = Post.objects.get(id=pst_id)
    get_comment = Comment.objects.filter(post__id=pst_id)
    reply = Reply.objects.filter(name=request.user)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        Comment.objects.create(name=name, email=email, comment=comment, post=race)
        messages.success(request, 'comment created successfully!')

    recent = Post.objects.all()[:2]
    sample = Post.objects.all()[:5]
    trending = Product.objects.all()[:2]
    race.num_site = race.num_site + 1
    race.save()
    
    is_liked = False
    is_favourite = False
    if race.likes.filter(id=request.user.id).exists():
        is_liked = True
    
    if race.favourite.filter(id=request.user.id).exists():
        is_favourite = True



    return render(request, 'frontend/blog-article.html', {'race':race, 'comment':get_comment, 'is_liked':is_liked, 'total_likes':race.total_likes, 'is_favourite':is_favourite, 'recent':recent, 'trending':trending, 'sample':sample, 'reply':reply})

def like_blog(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
        messages.success(request, 'You have dislike this post')
    else:

        post.likes.add(request.user)
        is_liked = True
        messages.success(request, 'thank you for liking this post')
            
    return HttpResponseRedirect(reverse('frontend:blog_two', args=[str(pk)]))

    # BLOG FAVORITE STARTS HERE

# Comment REPLY START HERE

def comment_reply(request, id):

    get_reply = Comment.objects.get(pk=id)
    comment_reply = Reply.objects.filter(post__pk=id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        Reply.objects.create(name=name, email=email, comment=comment, post=get_reply)
        messages.success(request, 'thanks for replying!')
    
    return render(request, 'frontend/reply.html', {'get_reply':get_reply, 'reply':comment_reply})
   

# Comment REPLY ENDS HERE



def blog_post(request, id):
    if not request.user.is_authenticated:
        return redirect('frontend:custom_login')


    post = Post.objects.get(id=id)

    if post.favourite.filter(id=request.user.id).exists():
        post.favourite.remove(request.user)
        messages.success(request, 'product remove from favorite')


    else:
        post.favourite.add(request.user)
        messages.info(request, 'post added to favorite succesfully!')


    return HttpResponseRedirect(reverse('frontend:blog_two', args=[str(id)]))

def blog_list(request):
    if not request.user.is_authenticated:
        return redirect('frontend:custom_login')


    user = request.user

    post = user.enough_favourite.all()

    return render(request, 'frontend/favourite.html', {'post':post})

    # BLOG FAVORITE ENDS HERE



def add_blog(request):
    if not request.user.is_authenticated:
        return redirect('frontend:custom_login')

    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        image = request.FILES.getlist('image')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            for image in image:
                messages.success(request, 'Post added Successfully! ')
                return redirect('frontend:view_blog')
        
    else:
        form = PostForm()

    return render(request, 'frontend/addblog.html', {'form':form})


def view_blog(request):
    
    post = Post.objects.filter(user=request.user)

    return render(request, 'frontend/view-blog.html', {'post':post})

def delete_blog(request, pst_id):
    single_post = Post.objects.get(id=pst_id)
    single_post.delete()
    messages.success(request, 'file deleted successfully')

    return redirect('frontend:view_blog')


def edit_blog(request, pst_id):
    if not request.user.is_authenticated:
        return redirect('frontend:custom_lgin')

    edited = Post.objects.get(id=pst_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=edited)
        if form.is_valid():
            form.save()
            messages.success(request, 'post edited successfully')
    
    else:
        form = PostForm(instance=edited)

    return render(request, 'frontend/edit-blog.html', {'form':form})
def result(request):
    if request.method == 'GET':
        search = request.GET.get('q')
        
        query_filter = Post.objects.filter(Q(title__icontains=search) | Q(description__icontains=search) | Q(created_by__icontains=search))
    
    return render(request, 'frontend/blog-search.html', {'query':query_filter, 'search':search})


    # BLOG CODE END HERE


def select_account(request):
    
    
    if request.method == 'POST':
        form = SelectForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Continue Registration! ')
            return redirect('frontend:register')
        
            
                
    else:
        form = SelectForm()

    return render(request, 'frontend/select-account.html', {'form':form})

def register(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('frontend:register')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = Register()

    return render(request, "frontend/register.html", {"form": form}
        )
        


def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('frontend/account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to your email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')
def activate(request, uidb64, token):
    user = User()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('frontend:custom_login')
    else:
        messages.error(request, 'Activation link is invalid!')
    
    return redirect('home')

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello {user.username} You have been logged in")

                return redirect('home')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = AuthenticationForm() 
    
    return render(request, "frontend/login.html", {'form': form}
        )
# Same as in all places where we request some input from the user, we use the POST method; not an exception is the login function. We use the built-in Django Authentication form to receive the username and password from the user and check if it's valid. If the form is valid, we call the built-in Django authentication function that checks if such a 

def custom_logout(request):
    cart = copy.deepcopy(Cart(request).cart)
    logout(request)
    session = request.session
    session[settings.CART_SESSION_ID] = cart
    session.modified = True
    messages.success(request, 'Log out successfully!')
    return redirect('frontend:custom_login')

def confirm_logout(request):

    return render(request, 'frontend/confirm-logout.html')

def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('frontend:custom_login')

    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'profile edited successfully')
            return redirect('frontend:profile')
        else:
            messages.error(request, 'user not edited')
    else:
        form = EditProfile(instance=request.user)


    return render(request, 'frontend/edit-profile.html', {'form':form})


def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('frontend:custom_login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'frontend/password_reset_confirm.html', {'form': form})

def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = User.objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = "Password Reset request"
                message = render_to_string("frontend/reset.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[associated_user.email])
                if email.send():
                    messages.success(request,
                        """
                        <h2>Password reset sent</h2><hr>
                        <p>
                            We've emailed you instructions for setting your password, if an account exists with the email you entered. 
                            You should receive them shortly.<br>If you don't receive an email, please make sure you've entered the address 
                            you registered with, and check your spam folder.
                        </p>
                        """
                    )
                else:
                    messages.error(request, "Problem sending reset password email, <b>SERVER PROBLEM</b>")

            return redirect('home')

        for key, error in list(form.errors.items()):
            if key == 'captcha' and error[0] == 'This field is required.':
                messages.error(request, "You must pass the reCAPTCHA test")
                continue

    form = PasswordResetForm()
    return render(request, "frontend/password_reset.html", {"form": form}
        )
def passwordResetConfirm(request, uidb64, token):
    user = User()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been set. You may go ahead and <b>log in </b> now.")
                return redirect('frontend:custom_login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = SetPasswordForm(user)
        return render(request, 'frontend/password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "Link is expired")

    messages.error(request, 'Something went wrong, redirecting back to Homepage')
    return redirect("home")


def news(request):
    if request.method == "POST":
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            send_mail(
            name,
            email,
            'akaliekene42@gmail.com',
            ['waltrade42@gmail.com'],
            fail_silently=False,
            
        )

            
            # return redirect('frontend:base')
            messages.success(request, 'thanks for subscribing')

    else:
        form = NewsLetterForm()

    return render(request, "frontend/base.html", {"form": form}
        )

def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            description = form.cleaned_data.get('description')
            send_mail(
            email,
            description,
            'akaliekene42@gmail.com',
            ['waltrade42@gmail.com'],
            fail_silently=False,
            
        )

            messages.success(request, 'mail sent succesfully')
            return redirect('frontend:contact')

    else:
        form = ContactForm()

    return render(request, "frontend/contact-us.html", {"form": form}
        )



def BlogPostLike(request, pk):
    post = get_object_or_404(BlogPost, id=request.POST.get('blogpost_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('blogpost-detail', args=[str(pk)]))

# CART CODE STARTS HERE


def cart_add(request, id):
    if not request.user.is_authenticated:
        messages.success(request, 'Login to Continue')
        return redirect('frontend:custom_login')
    
        

    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    messages.success(request, 'product added to cart successfully')
    return redirect("frontend:cart_detail")
    # return HttpResponseRedirect(reverse('frontend:two', args=[str(id)]))




def item_clear(request, id):
    if not request.user.is_authenticated:
        return redirect('frontend:custom_login')

    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    messages.success(request, 'product deleted from cart successfully!')
    return redirect("frontend:cart_detail")



def item_increment(request, id):
    if not request.user.is_authenticated:
        return redirect('frontend:custom_login')

    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("frontend:cart_detail")

def item_decrement(request, id):
    if not request.user.is_authenticated:
        return redirect('frontend:custom_login')
    
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("frontend:cart_detail")

    
        

def cart_clear(request):
    if not request.user.is_authenticated:
        return redirect('frontend:custom_login')

    cart = Cart(request)
    cart.clear()
    return redirect("frontend:cart_detail")


def cart_detail(request):
    if not request.user.is_authenticated:
        messages.success(request, 'Login to view cart')
        return redirect('frontend:custom_login')

    cart = Cart(request)

    return render(request, 'frontend/cart_detail.html')


# CART CODE ENDS HERE

# PAYMENT METHOD STARTS HERE

def checkout(request):
    if not request.user.is_authenticated:
        return redirect('frontend:custom_login')

    cart = Cart(request)

    post = AddCoupon.objects.all()
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'payment made successfully ')
            return redirect('frontend:customer_order')
    
    else:
        form = OrderForm()
        cart_shipping = Cart_ShippingForm()

    return render(request, 'frontend/checkout.html', {'form':form, 'cart_shipping':cart_shipping, 'post':post})
    

def buy_now(request, pst):
    if not request.user.is_authenticated:
        return redirect('frontend:custom_login')

    race = Product.objects.get(pk=pst)

    post = AddCoupon.objects.all()
    
    if request.method == 'POST':
        form = Order2Form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'payment made successfully ')
            return HttpResponseRedirect(reverse('frontend:orderby', args=[str(pst)]))

    
    else:
        form = Order2Form()
        buy_now_shipping = Buy_Now_ShippingForm()

    return render(request, 'frontend/buy-now.html', {'form':form, 'race':race, 'post':post, 'buy_now_shipping':buy_now_shipping})


    # PAYMENT METHOD ENDS HERE

    # ORDER CODE START HERE



def orderby(request, id):

    race = Product.objects.get(pk=id)

    return render(request, 'frontend/orderby.html', {'race':race})

def customer_order(request):

    post = Order.objects.filter(user=request.user)

    return render(request, 'frontend/customer-order.html', {'post':post})

def buy_now_order(request):
    
    post = Order2.objects.filter(user=request.user)

    return render(request, 'frontend/buy-now-order.html', {'post':post})

def buy_now_delete(request, id):
    single_post = Order2.objects.get(pk=id)
    single_post.delete()
    messages.success(request, 'Order deleted successfully')
    return redirect('frontend:buy_now_order')




def order_history(request):
    
    post = Order.objects.filter(user=request.user)

    return render(request, 'frontend/order-history.html', {'post':post})

def orders(request, id):
    single_post = Order.objects.get(pk=id)
    single_post.delete()
    messages.success(request, 'Order deleted successfully')
    return redirect('frontend:order_history')



# ORDER CODE ENDS HERE

def about_us(request):

    return render(request, 'frontend/about-us.html')


def about(request):

    return render(request, 'frontend/about.html')

def privacy_policy(request):

    return render(request, 'frontend/privacy-policy.html')

def terms_condition(request):

    return render(request, 'frontend/terms-condition.html')

def orders_return(request):

    return render(request, 'frontend/orders-return.html')




def newsletter(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        messages.success(request, 'thanks for subscribing!')
        NewsLetter.objects.create(email=email)
        send_mail(
            email,
            email,
            'akaliekene42@gmail.com',
            ['waltrade42@gmail.com'],
            fail_silently=False,
            
        )

        
    return render(request, 'frontend/base.html')


def profile(request):
    
    
    return render(request, 'frontend/userprofile.html')

# ERROR HANDLING STARTS HERE

def error_400_view(request, exception):

    return render(request, 'frontend/400.html')

def error_403_view(request, exception):

    return render(request, 'frontend/403.html')

def error_404_view(request, exception):

    return render(request, 'frontend/404.html')

def error_500_view(request):

    return render(request, 'frontend/404.html')

# ERROR HANDLING ENDS HERE

    
def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'mail sent successfully ')
            return redirect('frontend:contact')
    
    else:
        form = ContactForm()

    return render(request, 'frontend/contact-us.html', {'form':form})


def faqs(request):

    return render(request, 'frontend/faqs.html')

def help_support(request):

    return render(request, 'frontend/help_support.html')


def count_visit(request):
    visit = request.session.get('visit', 0) + 1
    request.session['visit'] = visit
    return HttpResponse(f"Visit count:{request.session['visit']}")




def sellers_guideline(request):

    return render(request, 'frontend/sellers-guideline.html')

def currency(request):

    return render(request, 'frontend/currency.html')

def sellers_profile(request, id):

    post = Product.objects.get(pk=id)

    return render(request, 'frontend/sellers-profile.html', {'post':post})

def sellers_proof(request):

    
    return render(request, 'frontend/currency.html')

def coupon(request):

    if request.method == 'POST':
        coupon = request.POST.get('coupon')
        messages.success(request, 'coupon applied successfully!')
        Coupon.objects.create(coupon=coupon)
        
    return render(request, 'frontend/checkout.html')

def buy_coupon(request):

    if request.method == 'POST':
        coupon = request.POST.get('coupon')
        messages.success(request, 'coupon applied successfully!')
        BuyCoupon.objects.create(coupon=coupon)
        
    return render(request, 'frontend/buy-now.html')

def cart_coupon(request):

    if request.method == 'POST':
        coupon = request.POST.get('coupon')
        messages.success(request, 'coupon applied successfully!')
        CartCoupon.objects.create(coupon=coupon)
        
    return render(request, 'frontend/cart_detail.html')

def estimate_shipping(request):

    if request.method == 'POST':
        country = request.POST.get('country')
        state = request.POST.get('state')
        postal = request.POST.get('postal')
        messages.success(request, 'shipping estimated successfully!')
        Estimate_Shipping.objects.create(country=country, state=state, postal=postal)
        
    return render(request, 'frontend/cart_detail.html')

def advertisement(request):

   return render(request, 'frontend/advertisement.html')
 

def sellers_account(request):
    
    if request.method == 'POST':
        form = SellersAccountForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'continue registration')
            return redirect('frontend:register')

    
    else:
        form = SellersAccountForm()
        
    return render(request, 'frontend/sellers-account.html', {'form':form})

def buyers_account(request):
    
    if request.method == 'POST':
        form = BuyersAccountForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'continue registration')
            return redirect('frontend:register')

    
    else:
        form = BuyersAccountForm()
        
    return render(request, 'frontend/buyers-account.html', {'form':form})

def buyers_sellers_account(request):
    
    if request.method == 'POST':
        form = Buyers_sellersAccountForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'continue registration')
            return redirect('frontend:register')

    
    else:
        form = Buyers_sellersAccountForm()
        
    return render(request, 'frontend/hybrid-account.html', {'form':form})


def account_type(request):

   return render(request, 'frontend/account-type.html')





