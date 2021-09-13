from django.shortcuts import render, redirect,  render_to_response, HttpResponseRedirect
from django.conf import settings
# from .forms import NewImagePost, CreateComment, UpdateProfile
from .models import Image, Comment, Profile, User
import datetime as dt
from django.http import HttpResponse, Http404
from django.templatetags.static import static

# Create your views here.


def index(request):
    date = dt.date.today()
    images = Image.get_images()
    comments = Comment.get_comment()

    current_user = request.user
    if request.method == 'POST':
        form = NewCommentForm(request.POST, auto_id=False)
        img_id = request.POST['image_id']
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = current_user
            image = Image.get_image(img_id)
            comment.image = image
            comment.save()
        return redirect(f'/#{img_id}',)
    else:
        form = NewCommentForm(auto_id=False)


    return render(request, 'index.html')


