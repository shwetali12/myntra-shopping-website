from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app1 .models import CustomUser,Category,Product,Brand,Size,Color,Cart,Wishlist,Order
from django.http import Http404
from app1.forms import OrderForm
from django.db import transaction
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    brands = Brand.objects.all()  # Fetch all brands
    categorys = Category.objects.all()
    brand_products = {}  # Dictionary to store products for each brand
    category_products ={}

    # Loop through each brand and fetch its products
    for category in categorys:
        category_products[category] = Product.objects.filter(category=category)[:6]
    
    for brand in brands:
        brand_products[brand] = Product.objects.filter(brand=brand)[:6]

    return render(request, 'index.html', {'brand_products': brand_products,'category_products':category_products})



def men(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    brand = Brand.objects.all()
    size = Size.objects.all()
    color = Color.objects.all()

    menswear_products = products.filter(category__name__in=['T-shirt', 'Shirt'])

    category_id = request.GET.get('categories')
    brand_id = request.GET.get('brand')
    sizes = request.GET.getlist('size')
    price_id = request.GET.get('price')
    color_id = request.GET.get('color')

    if category_id:
        menswear_products = menswear_products.filter(category_id=category_id)

    if brand_id:
        menswear_products = menswear_products.filter(brand_id=brand_id)

    if sizes:
        menswear_products = menswear_products.filter(size__in=sizes)

    if color_id:
        menswear_products = menswear_products.filter(color_id=color_id)

    if price_id:
        if price_id == 'under-500':
            menswear_products = menswear_products.filter(price__lte=500)
        elif price_id == '500-2000':
            menswear_products = menswear_products.filter(price__gte=500, price__lte=2000)
        elif price_id == '2000-5000':
            menswear_products = menswear_products.filter(price__gte=2000, price__lte=5000)
        elif price_id == '5000':
            menswear_products = menswear_products.filter(price__gte=5000)

    product_counts = menswear_products.count()

    return render(request, 'men.html', {'products': products, 'menswear_products': menswear_products, 'product_counts': product_counts,'brand':brand,'size':size,'color':color,'categories':categories})




def women(request):
    # Retrieve all products and categories
    products = Product.objects.all()
    categories = Category.objects.all()
    brand = Brand.objects.all()
    size = Size.objects.all()
    color = Color.objects.all()
    # Filter products for women's wear categories by names
    womenswear_products = products.filter(category__name__in=['Saree', 'Dress'])

    # Apply additional filters
    brand_id = request.GET.get('brand')
    sizes = request.GET.getlist('size')  # Get list of selected sizes
    price_id = request.GET.get('price')
    color_id = request.GET.get('color')
    category_id = request.GET.get('categories')

    if category_id:
        womenswear_products = womenswear_products.filter(category_id=category_id)


    if brand_id:
        womenswear_products = womenswear_products.filter(brand_id=brand_id)

    if sizes:
        womenswear_products = womenswear_products.filter(size__in=sizes)

    if color_id:
        womenswear_products = womenswear_products.filter(color_id=color_id)

    if price_id:
        if price_id == 'under-500':
            womenswear_products = womenswear_products.filter(price__lte=500)
        elif price_id == '500-2000':
            womenswear_products = womenswear_products.filter(price__gte=500, price__lte=2000)
        elif price_id == '2000-5000':
            womenswear_products = womenswear_products.filter(price__gte=2000, price__lte=5000)
        elif price_id == '5000':
            womenswear_products = womenswear_products.filter(price__gte=5000)

    # Count the number of women's products after filtering
    product_counts = womenswear_products.count()

    return render(request, 'women.html', {'womenswear_products': womenswear_products, 'product_counts': product_counts, 'categories': categories,'brand':brand,'color':color,'size':size})


def kids(request):
    # Retrieve all products and categories
    products = Product.objects.all()
    categories = Category.objects.all()
    brand = Brand.objects.all()
    size = Size.objects.all()
    color = Color.objects.all()
    # Filter products for women's wear categories by names
    kidswear_products = products.filter(category__name__in=['Boy', 'Girl'])

    # Apply additional filters
    brand_id = request.GET.get('brand')
    sizes = request.GET.getlist('size')  # Get list of selected sizes
    price_id = request.GET.get('price')
    color_id = request.GET.get('color')
    category_id = request.GET.get('categories')

    if category_id:
        kidswear_products = kidswear_products.filter(category_id=category_id)


    if brand_id:
        kidswear_products = kidswear_products.filter(brand_id=brand_id)

    if sizes:
        kidswear_products = kidswear_products.filter(size__in=sizes)

    if color_id:
        kidswear_products = kidswear_products.filter(color_id=color_id)

    if price_id:
        if price_id == 'under-500':
            kidswear_products = kidswear_products.filter(price__lte=500)
        elif price_id == '500-2000':
            kidswear_products = kidswear_products.filter(price__gte=500, price__lte=2000)
        elif price_id == '2000-5000':
            kidswear_products = kidswear_products.filter(price__gte=2000, price__lte=5000)
        elif price_id == '5000':
            kidswear_products = kidswear_products.filter(price__gte=5000)

    # Count the number of women's products after filtering
    kids_product_counts = kidswear_products.count()

    return render(request, 'kids.html', {'kidswear_products': kidswear_products, 'kids_product_counts': kids_product_counts, 'categories': categories,'brand':brand,'color':color,'size':size})

def cart(request):
    product = Cart.objects.all()
    total_price = sum(item.product.price * item.quantity for item in product)
    return render(request,'cart.html',{'product':product, 'total_price':total_price})

def product_search(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    products = Product.objects.all()  # Get all products by default

    if query:
        # Filter products by name, brand, or category
        products = products.filter(name__icontains=query) | \
                   products.filter(brand__name__icontains=query) | \
                   products.filter(category__name__icontains=query)

    return render(request, 'product_search.html', {'products': products, 'query': query})
   
def add_to_cart(request, id):
    product = get_object_or_404(Product, pk=id)
    
    # Get or create the cart object for the current user and product
    cart, created = Cart.objects.get_or_create(user=request.user, product=product)

    # Increase the quantity of the product in the cart
    cart.quantity += 1
    cart.save()

    return redirect('cart')

def wishlist(request):
    product = Wishlist.objects.all()
    return render(request, 'wishlist.html', {'product': product})

def add_to_cart_from_wishlist(request, id):
    # Get the product object from the wishlist
    wishlist_item = get_object_or_404(Wishlist, pk=id, user=request.user)
    product = wishlist_item.product
    
    # Get or create the cart object for the current user
    cart, created = Cart.objects.get_or_create(user=request.user, product=product)

    # Increase the quantity of the product in the cart
    cart.quantity += 1
    cart.save()

    # Remove the product from the wishlist
    wishlist_item.delete()

    return redirect('wishlist')
    
    # Remove the product from the wishlist
   

def add_to_wishlist(request, id):
    product = get_object_or_404(Product, pk=id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user,product=product)
    item_created = False  # Initialize the variable before its usage

    if not item_created:
        product.quantity += 1
        product.save()
    
    return redirect('wishlist')

def remove_from_cart(request,id):
    product = get_object_or_404(Cart, pk=id)
    if product.quantity > 1:
        product.quantity -= 1
        product.save()
    else:
        # If the quantity is 1 or less, delete the product from the cart
        product.delete()
    return redirect('cart')
   



def details(request,id):
    
    product = get_object_or_404(Product, pk=id)
    print(id)
    return render(request,'details.html',{'product': product})

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email') 
        password1 = request.POST.get('pass1')
        user = authenticate(request, email=email, password=password1)
        if user is not None:
            login(request, user) 
            return redirect('index')
        else:
            return HttpResponse('incorrect username pass')

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirm_password')

        # Check if user with the same email already exists
        existing_user = CustomUser.objects.filter(email=email).first()
        if existing_user:
            return HttpResponse("User with this email already exists!")

        if pass1 == pass2:
            User = get_user_model()
            my_user = User.objects.create_user(email=email, password=pass1, name=uname)
            return HttpResponse("You have Signed up Successfully!")
        else:
            return HttpResponse("Password not matching...")

    else:
        return render(request, 'signup.html')

def logoutpage(request):
    logout(request)
    return redirect('index')




@login_required
def place_order(request, id):
    product = get_object_or_404(Product, id=id)
    cart_item = get_object_or_404(Cart, product=product, user=request.user)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        
        if form.is_valid():
            user = request.user
            address = form.cleaned_data['address']
            zipcode = form.cleaned_data['zipcode']
            phone_number = form.cleaned_data['phone_number']
            country = form.cleaned_data['country']
            state = form.cleaned_data['state']
            quantity = form.cleaned_data['quantity']
            total_price = product.price * quantity

            # Create an order for the current user and product
            Order.objects.create(
                product=product,
                user=user,
                address=address,
                zipcode=zipcode,
                phone_number=phone_number,
                country=country,
                state=state,
                quantity=quantity,
                total_price=total_price
            )
            cart_item.delete()
           
           
            return redirect('cart')  # Redirect to a confirmation page
        else:
            # Print form errors for debugging
            print(form.errors)
    else:
        # If it's a GET request, initialize the form with initial data
        initial_data = {
            'email': 'example@example.com',  # Example initial email
            'address': '123 Main Street',     # Example initial address
            'zipcode': '12345',               # Example initial zipcode
            'phone': '555-1234',              # Example initial phone number
            'country': 'Your Country',        # Example initial country
            'state': 'Your State',            # Example initial state
            'quantity': 1,                    # Example initial quantity
            # Add other initial values as needed
        }
        form = OrderForm(initial=initial_data)

    return render(request, 'place_order.html', {'form': form})

def order(request):
    products = Order.objects.filter(user=request.user)
    return render(request,'order.html',{'products':products})