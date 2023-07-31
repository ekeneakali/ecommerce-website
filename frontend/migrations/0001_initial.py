# Generated by Django 3.2.18 on 2023-07-31 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyCoupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon', models.CharField(max_length=150)),
                ('upload', models.FileField(upload_to='profile_upload')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'BuyCoupon',
            },
        ),
        migrations.CreateModel(
            name='Buyers_Sellers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(blank=True, max_length=1000, null=True, verbose_name='company name(optional)')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='phonenumber (country code first)')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'BuyersAccount',
            },
        ),
        migrations.CreateModel(
            name='BuyersAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='phonenumber (country code first)')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'BuyersAccount',
            },
        ),
        migrations.CreateModel(
            name='CartCoupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon', models.CharField(max_length=150)),
                ('upload', models.FileField(upload_to='profile_upload')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'CartCoupon',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.FileField(upload_to='BLOG-COMMENT-IMAGE', verbose_name='upload personal image')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=700)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'NewsLetter',
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon', models.CharField(max_length=150)),
                ('upload', models.FileField(upload_to='profile_upload')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Coupon',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Delivery',
            },
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Detail',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Discount',
            },
        ),
        migrations.CreateModel(
            name='Estimate_Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=1000)),
                ('state', models.CharField(max_length=1000)),
                ('postal', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Estimate_Shipping',
            },
        ),
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'NewsLetter',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('created_by', models.CharField(max_length=50, verbose_name='last name')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='enter phonenumber(country code first)')),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=1000)),
                ('apartment', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name='select country')),
                ('post_code', models.IntegerField(verbose_name='zip postal code')),
                ('state', models.CharField(max_length=2000, verbose_name='regional state')),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Checkout',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Payment',
            },
        ),
        migrations.CreateModel(
            name='Post_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Post_Category',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('upload', models.FileField(upload_to='profile_upload')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Profile',
            },
        ),
        migrations.CreateModel(
            name='Select',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select', models.CharField(choices=[('select1', 'seller'), ('select2', 'buyer'), ('select3', 'seller/buyer')], max_length=1000, verbose_name='select account')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='phonenumber (country code first)')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Select',
            },
        ),
        migrations.CreateModel(
            name='Select_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Select Category',
            },
        ),
        migrations.CreateModel(
            name='SellersAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='sellersaccount/', verbose_name='upload your government id or business license')),
                ('business_name', models.CharField(blank=True, max_length=1000, null=True, verbose_name='company name(optional)')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='phonenumber (country code first)')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'SellersAccount',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.FileField(upload_to='BLOG-COMMENT-IMAGE', verbose_name='upload personal image')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='load', to='frontend.comment')),
            ],
            options={
                'verbose_name_plural': 'Reply',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('government', models.FileField(upload_to='government_id/', verbose_name='upload your government id or business license')),
                ('name', models.CharField(max_length=150, verbose_name='name of product')),
                ('price', models.IntegerField()),
                ('old', models.IntegerField(blank=True, null=True, verbose_name='old price(optional)')),
                ('new_price', models.CharField(max_length=1000)),
                ('old_price', models.CharField(blank=True, max_length=1000, null=True, verbose_name='old price(optional)')),
                ('created_by', models.CharField(max_length=50, verbose_name='company name')),
                ('supply', models.IntegerField(verbose_name='supply quantity')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='phonenumber (country code first)')),
                ('email', models.EmailField(max_length=254)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('size', models.IntegerField(default=0)),
                ('cost', models.IntegerField(default=0, verbose_name='shipping cost')),
                ('num_site', models.IntegerField(default=0, verbose_name='visited')),
                ('video', models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='upload a video(optional)')),
                ('description', models.TextField()),
                ('image', models.FileField(upload_to='upload/', verbose_name='upload a photo')),
                ('thumbnail', models.FileField(upload_to='thumbnail/', verbose_name='upload a photo')),
                ('multiple', models.FileField(upload_to='multiple/', verbose_name='upload a photo')),
                ('img_view', models.FileField(upload_to='img_view/', verbose_name='upload a photo')),
                ('img_slider', models.FileField(upload_to='img_slider/', verbose_name='upload a photo')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.category', verbose_name='select business type')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.delivery', verbose_name='select delivery time')),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.details', verbose_name='select packaging details')),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontend.discount', verbose_name='select discount(optional)')),
                ('favourite', models.ManyToManyField(blank=True, related_name='favourite', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.payment', verbose_name='select payment')),
                ('select_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.select_category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, unique=True)),
                ('created_by', models.CharField(max_length=100, verbose_name='author')),
                ('video', models.FileField(blank=True, null=True, upload_to='blog-video', verbose_name='upload a video(optional)')),
                ('num_site', models.IntegerField(default=0, verbose_name='visited')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='enter phonenumber(country code first)')),
                ('email', models.EmailField(max_length=254)),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name='select country')),
                ('description', models.TextField()),
                ('image', models.FileField(upload_to='blog-image', verbose_name='upload an image')),
                ('thumbnail', models.FileField(null=True, upload_to='thumbnail/', verbose_name='upload a photo')),
                ('multiple', models.FileField(upload_to='multiple/', verbose_name='upload a photo')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.post_category', verbose_name='select category')),
                ('favourite', models.ManyToManyField(blank=True, related_name='enough_favourite', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='enough_likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Order_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='frontend.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='frontend.product')),
            ],
            options={
                'verbose_name_plural': 'Order_Items',
            },
        ),
        migrations.CreateModel(
            name='Order2_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_detail', to='frontend.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='frontend.product')),
            ],
            options={
                'verbose_name_plural': 'Order2_Items',
            },
        ),
        migrations.CreateModel(
            name='Order2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('created_by', models.CharField(max_length=50, verbose_name='last name')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='enter phonenumber(country code first)')),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=1000)),
                ('apartment', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name='select country')),
                ('post_code', models.IntegerField(verbose_name='zip postal code')),
                ('state', models.CharField(max_length=2000, verbose_name='regional state')),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Order2',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.post'),
        ),
        migrations.CreateModel(
            name='Cart_Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select', models.CharField(choices=[('select1', 'international shipping|10-15 15-30 days'), ('select2', 'local shipping|1-3 2-5 days ')], max_length=1000, verbose_name='select shipping method')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Cart_Shipping',
            },
        ),
        migrations.CreateModel(
            name='Buy_Now_Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select', models.CharField(choices=[('select1', 'international shipping|10-15 15-30 days'), ('select2', 'local shipping|1-3 2-5 days ')], max_length=1000, verbose_name='select shipping method')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.order2')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Buy_Now_Shipping',
            },
        ),
        migrations.CreateModel(
            name='AddCoupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('active_on', models.DateField()),
                ('expire_on', models.DateField()),
                ('number', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.product')),
            ],
            options={
                'verbose_name_plural': 'AddCoupon',
            },
        ),
    ]
