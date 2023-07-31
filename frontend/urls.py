
from django.urls import path
from frontend import views
from django.contrib.auth import views as auth_views



app_name = 'frontend'


urlpatterns = [
    path('two/<int:pst>/', views.two, name='two'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('activateEmail', views.activateEmail, name='activateEmail'),
    path('register', views.register, name='register'),
    path('select_account', views.select_account, name='select_account'),
    path('login', views.custom_login, name='custom_login'),
    path('logout', views.custom_logout, name='logout'),
    path('confirm_logout', views.confirm_logout, name='confirm_logout'),
    path('edit-profile', views.edit_profile, name='edit_profile'),
    path("password_change", views.password_change, name="password_change"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),
    path('news', views.news, name='news'),
     path('like_post/<int:pk>/', views.like_post, name='like_post'),
    path('profile', views.profile, name='profile'),

    #     PRODUCT CODE ENDS HERE
    path('add-post', views.add_post, name='add_post'),
    path('view-post', views.view_post, name='view_post'),
    path('delete_post/<int:pst_id>', views.delete_post, name='delete_post'),
    path('edit_post/<int:pst_id>', views.edit_post, name='edit_post'),
    path('favourite_post/<int:id>/', views.favourite_post, name='favourite_post'),
     path('post-list', views.post_list, name='post_list'),
     #path('error_404_view', views.error_404_view, name='error_404_view'),
     path('about', views.about, name='about'),
     
     path('contact-us', views.contact_us, name='contact_us'),
     path('contact', views.contact, name='contact'),
     path('newsletter', views.newsletter, name='newsletter'),
     path('shop', views.shop, name='shop'),
     path('about-us', views.about_us, name='about_us'),
     path('help_support', views.help_support, name='help_support'),
     path('privacy-policy', views.privacy_policy, name='privacy_policy'),
     path('terms-condition', views.terms_condition, name='terms_condition'),
     # PAYMENT METHOD STARTS HERE
     path('checkout', views.checkout, name='checkout'),
     path('buy_now/<int:pst>/', views.buy_now, name='buy_now'),
     # PAYMENT METHOD ENDS HERE
     
#     PRODUCT CODE ENDS HERE
    # CART STATRT HERE   
     path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail, name='cart_detail'),
     path('count-visit', views.count_visit, name='count_visit'),

    # CART END HERE

    #SEARCH BAR CODE
    path('search', views.search, name='search'),
          # BLOG PAGE STARTS HERE
     path('blog', views.blog, name='blog'),
     path('blog-two/<int:pst_id>/', views.blog_two, name='blog_two'),
     path('like-blog/<int:pk>/', views.like_blog, name='like_blog'),
     path('add-blog', views.add_blog, name='add_blog'),
     path('view-blog', views.view_blog, name='view_blog'),
     path('delete-blog/<str:pst_id>/', views.delete_blog, name='delete_blog'),
     path('edit-blog/<int:pst_id>/', views.edit_blog, name='edit_blog'),
     path('blog-post/<int:id>/', views.blog_post, name='blog_post'),
     path('blog-list', views.blog_list, name='blog_list'),
     path('result', views.result, name='result'),
     path('faqs', views.faqs, name='faqs'),
          # BLOG PAGE ENDS HERE

          # ORDER CODE START HERE

     path('customer-order', views.customer_order, name='customer_order'),
     path('orderby/<int:id>/', views.orderby, name='orderby'),
     path('buy_now_order', views.buy_now_order, name='buy_now_order'),
     path('buy_now_delete/<int:id>/', views.buy_now_delete, name='buy_now_delete'),
     path('order_history', views.order_history, name='order_history'),
     path('orders/<int:id>/', views.orders, name='orders'),
     path('orders-return', views.orders_return, name='orders_return'),
     
     


     
     # Comment REPLY START HERE
     path('comment-reply/<int:id>/', views.comment_reply, name='comment_reply'),
     
     # Comment REPLY ENDS HERE

          # ORDER CODE END HERE
     
     path('sellers_guideline', views.sellers_guideline, name='sellers_guideline'),
     path('currency', views.currency, name='currency'),
     path('sellers-profile/<int:id>/', views.sellers_profile, name='sellers_profile'),
     path('sellers-proof', views.sellers_proof, name='sellers_proof'),
     path('coupon', views.coupon, name='coupon'),
     path('buy-coupon', views.buy_coupon, name='buy_coupon'),          
     path('cart-coupon', views.cart_coupon, name='cart_coupon'),
     path('estimate-shipping', views.estimate_shipping, name='estimate_shipping'),
     path('advertisement', views.advertisement, name='advertisement'), 
     path('sellers-account', views.sellers_account, name='sellers_account'),
     path('buyers-account', views.buyers_account, name='buyers_account'),
     path('buyers-sellers-account', views.buyers_sellers_account, name='buyers_sellers_account'),
     path('account-type', views.account_type, name='account_type'),          
               
              
               
               
               
               
               
               
          
    ]
    
