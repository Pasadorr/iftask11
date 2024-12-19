from django.shortcuts import render

def platform(request):
    return render(request, 'third_task/platform.html')

def games(request):
    game_list = {
        'games': [
            {'name': 'Atomic Heart', 'button': 'Купить'},
            {'name': 'Cyberpunk 2077', 'button': 'Купить'},
            {'name': 'PayDay 2', 'button': 'Купить'},
        ]
    }
    return render(request, 'third_task/games.html', game_list)

def cart(request):
    return render(request, 'third_task/cart.html')