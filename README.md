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
    
    LOGIN AND REGISTRATION PAGE:>//
        login>>
        ![image](https://github.com/Mhdjaseer/Noviindus/assets/98450786/d3f0476f-997b-4772-bfc3-6f28e541721e)
        register:..
            ![image](https://github.com/Mhdjaseer/Noviindus/assets/98450786/198df9ac-6204-4afc-af65-998e0bcb1715)

    HOME PAGE:>
    ![image](https://github.com/Mhdjaseer/Noviindus/assets/98450786/503486ca-a701-48a8-87bf-db4ba50d0da7)
    CART PAGE :>
    ![image](https://github.com/Mhdjaseer/Noviindus/assets/98450786/5134483d-f80a-419b-b828-120f74e2ca1a)
    ____CRUD OPERATION PAGE:>_______
        DELETE FUNCTIONALITY IS AVAILBLE ON THE SAME PAGE :--
    ![image](https://github.com/Mhdjaseer/Noviindus/assets/98450786/a4ef5d82-cc6f-4540-9686-32a689001358)
        ADD ITEM TO DB:>//
            
            ![image](https://github.com/Mhdjaseer/Noviindus/assets/98450786/74952e49-2665-41c7-8e0a-8b9d9a6fe962)
        UPDATE ITEM :>//
            ![image](https://github.com/Mhdjaseer/Noviindus/assets/98450786/42947610-c1dc-4dd2-8980-634e725a938e)
