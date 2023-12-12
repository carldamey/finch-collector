from django.shortcuts import render

finches = [
  {'name': 'Birdtram', 'type': 'Saffron', 'description': 'he fly', 'age': 8},
  {'name': 'Birdley', 'type': 'Society', 'description': 'society lives in a him', 'age': 3},
  {'name': 'Birdolemew', 'type': 'Star', 'description': 'he squawk', 'age': 5},
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {
    'finches': finches
  })