from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from products.views import ProductsList, NewProduct, DetailProduct, DeleteProduct, UpdateProduct
from accounts.views import Login, Register, logout_view, ProfileDetails, ProfileUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductsList.as_view(), name= 'products_list'),
    path('new_product/', NewProduct.as_view(), name = 'new_product'),
    path('product/<int:pk>/', DetailProduct.as_view(), name = 'detail_product'),
    path('product/<int:pk>/delete', DeleteProduct.as_view(), name = 'delete_product'),
    path('product/<int:pk>/update', UpdateProduct.as_view(), name = 'update_product'),
    path('register/', Register.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileDetails.as_view(), name='profile_detail'),
    path('profile/<int:pk>/profile_edit', ProfileUpdate.as_view(), name='profile_update'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
