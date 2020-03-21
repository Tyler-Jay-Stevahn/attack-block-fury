from django.shortcuts import render

# Create your views here.


def landing_page(request):
    context = {
        "greeting": "heylo"
    }
    return render(request, 'landingpage.html', context)
