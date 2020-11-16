from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import EmailSendForm, WhatsappSendForm, CommentForm
from django.core.mail import send_mail
from taggit.models import Tag


# Create your views here.
def post_display_view(request, tag_slug=None):
    post_list = Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page')
    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = Paginator.page(paginator.num_pages)
    return render(request, 'blog/post_list.html', {'post_list': post_list, 'tag': tag})


class PostListView(ListView):
    model = Post
    paginate_by = 2


def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year, publish__month=month, publish__day=day)

    comments = post.comments.filter(active=True)
    csubmit = False
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            csubmit = True
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form, 'csubmit': csubmit, 'comments': comments})


def mail_send_view(request, id):
    post = get_object_or_404(Post, id=id, status='published')
    sent = False
    if request.method == 'POST':
        form = EmailSendForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = '{} ({}) recommends you to read "{}"'.format(
                cd['sender_name'], cd['sender_email'], post.title)
            post_url = request.build_absolute_uri(post.get_absolute_url())
            message = 'Read post at:\n{}\n\n{}\'s Comment:\n{}'.format(
                post_url, cd['sender_name'], cd['comments'])
            send_mail(subject, message, 'rahul@blog.com', [cd['receiver_email']])
            sent = True
    else:
        form = EmailSendForm()
    return render(request, 'blog/sharebymail.html', {'form': form, 'post': post, 'sent': sent})


def whatsapp_send_view(request, id):
    post = get_object_or_404(Post, id=id, status='published')
    sent = False
    if request.method == 'POST':
        form = WhatsappSendForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            whatsapp_data(cd['receiver_mobile_number'], cd['comments'])
            sent = True
    else:
        form = WhatsappSendForm()
    return render(request, 'blog/sharebywhatsapp.html', {'form': form, 'post': post})


def whatsapp_data(phone, message):
    import time
    import webbrowser as web
    import pyautogui as pg
    phone_number = "+91" + str(phone)
    web.open('https://web.whatsapp.com/send?' +
             phone_number + '&text=' + message)
    time.sleep(30)
    pg.write(str(phone))
    time.sleep(2)
    pg.press('enter')
