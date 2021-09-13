from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt

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


