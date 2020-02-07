from django.shortcuts import render

posts = [
  {
    'author': 'me',
    'title': 'post 1',
    'content': 'first ever blog content',
    'date_posted': 'Feb 5',
  },
  {
    'author': 'me',
    'title': 'post 2',
    'content': 'more blog content',
    'date_posted': 'Feb 6',
  },
]

def home(request):
  context = { 'posts': posts }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', { 'title': 'About' })

