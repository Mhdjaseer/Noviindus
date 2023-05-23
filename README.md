# Noviindus

# 1st task

1. Create a Registration and Login Page for users.
2. Users should be able to add things to the cart and On the Cart Page, each product image and amount should be displayed.
3. While adding each item on the cart the total Quantity should add up and on the deletion of an item from the cart it should be subtracted from the total.
4. A page to add, edit/update, and remove the item from the database is required.


all this functionalities are available in this project :


these are the paths  in this project:

    path('',views.homeView.as_view(),name='home'),
    path('register/',views.RegisterCreateView.as_view(),name='register'),
    path('login/',views.login.as_view(),name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('cart/<int:id>/',views.AddCartItems,name='cart'),
    path('cart/item/',views.CartView.as_view(),name='cartitem'),
    path('cart/delete/<int:cart_id>/item/<int:item_id>/',views.delete_cart_item,name="delete"),

    <!-- this section for the database CRUD OPERATION -->
    # db
    path('item/db/list/',views.ItemListView.as_view(),name='db-list'),
    path('item/db/create/',views.ItemCreateView.as_view(),name='create_items'),
    path('item/db/<pk>/update',views.ItemUpdateView.as_view(),name='update'),
    path('item/db/<int:id>/delete/',views.deleteItemView,name='Item_delete')