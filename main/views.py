from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# главная страница
def home(request):
    return render(request, 'home.html')

# страница с формой для подбора аналогов
def analogs(request):
    return render(request, 'analogs.html')

# страница входа
def login_view(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        # пока просто возвращаем на главную страницу
        return redirect('home')
    
    return render(request, 'login.html')

# страница результатов поиска
def find_analog(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_type = request.POST.get('product_type')
        product_composition = request.POST.get('product_composition')

        return render(request, 'result.html', {
            'name': product_name,
            'type': product_type,
            'composition': product_composition
        })

    return render(request, 'analog.html')

# страница избранных продуктов 
def favorites(request):
    return render(request, 'favorites.html')

