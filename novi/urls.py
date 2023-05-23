
from django.urls import path

from . import views
app_name='novi'
urlpatterns = [
    path('',views.homeView.as_view(),name='home'),
    path('register/',views.RegisterCreateView.as_view(),name='register'),
    path('login/',views.login.as_view(),name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('cart/<int:id>/',views.AddCartItems,name='cart'),
    path('cart/item/',views.CartView.as_view(),name='cartitem'),
    path('cart/delete/<int:cart_id>/item/<int:item_id>/',views.delete_cart_item,name="delete"),


    # db
    path('item/db/list/',views.ItemListView.as_view(),name='db-list'),
    path('item/db/create/',views.ItemCreateView.as_view(),name='create_items'),
    path('item/db/<pk>/update',views.ItemUpdateView.as_view(),name='update'),
    path('item/db/<int:id>/delete/',views.deleteItemView,name='Item_delete')

]