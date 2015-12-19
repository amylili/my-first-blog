from django.shortcuts import render

# Create your views here.
def post_lsit(request):
	return render(request, 'blog/post_list.htmll', {})
	