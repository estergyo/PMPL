# from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.
def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/lists/the-only-list-in-the-world/')

	items = Item.objects.all()

	if Item.objects.count() == 0:
		comment = 'yey, waktunya berlibur'
	elif Item.objects.count() < 5:
		comment = 'sibuk tapi santai'
	else:
		comment = 'oh tidak'

	return render(request, 'home.html', {'comment': comment})

def view_list(request):
	items = Item.objects.all()
	return render(request, 'list.html', {'items': items})
