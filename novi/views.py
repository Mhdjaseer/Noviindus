from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import redirect,get_object_or_404,render
from django.views.generic import TemplateView,View,CreateView,ListView,UpdateView
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import logout
from .models import Item,Cart

# Create your views here.


class homeView(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] =self.request.user
        context['item']=Item.objects.all()
        cart=Cart.objects.filter(user=self.request.user).first()
        context['cart_count'] = cart.items.count()
        return context
    


class login(LoginView):
    template_name='login.html'
    redirect_authenticated_user=True
    
    def get_success_url(self):
        return reverse_lazy('novi:home')
    
    def form_invalid(self,form):
        return self.render_to_response(self.get_context_data(form=form))


class RegisterCreateView(CreateView):
    form_class=SignUpForm
    success_url=reverse_lazy('novi:login')
    template_name = 'registration.html'

def logout_view(request):
    logout(request)
    messages.info(request,"Logged out successfully !!")
    return redirect('novi:login')



def AddCartItems(request, id):
    item = get_object_or_404(Item, id=id)
    print(item)
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)
    cart.items.add(item)
    return redirect('novi:home')


class CartView(ListView):
    template_name = 'cartItems.html'
    model = Cart

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.filter(user=self.request.user).first()
        if cart:
            cart_items = cart.items.all()
            total_price=sum(item.price for item in cart_items)
        else:
            cart_items = []
            total_price=0
        context['cartItems'] = cart_items
        context['total_price']=total_price
        context['cart']=cart
        context['cart_count'] = cart.items.count()
        return context

def delete_cart_item(request,cart_id,item_id):
    cart=get_object_or_404(Cart,id=cart_id, user=request.user)
    item=get_object_or_404(Item,id=item_id)
    cart.items.remove(item)
    return redirect('novi:cartitem')



# addItem,edit,delete,update

class ItemListView(ListView):
    template_name='db/list.html'
    model=Item
    context_object_name='items'

   
class ItemCreateView(CreateView):
    model = Item
    template_name = 'db/create.html'
    fields='__all__'
    success_url=reverse_lazy('novi:db-list')

class ItemUpdateView(UpdateView):
    model=Item
    fields='__all__'
    success_url=reverse_lazy('novi:db-list')
    template_name='db/update.html'


def deleteItemView(request,id):
    obj=get_object_or_404(Item, id=id)
    obj.delete()
    return redirect('novi:db-list')