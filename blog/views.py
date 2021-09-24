from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(render, 'blog.html', {})
