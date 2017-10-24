# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from models import Subject, Thread, Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from forms import ThreadForm, PostForm
from django.utils import timezone


def forum(request):
    # return the list of threads in descending order
    threads = Thread.objects.filter(created_at__lte=timezone.now()
                                ).order_by('-created_at')
    return render(request, "forum_main.html", {'threads': threads})


def forum_subjects(request):
    return render(request, 'forumsubjects.html', {'subjects': Subject.objects.all()})


def subject_threads(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'threads.html', {'subject': subject})


@login_required(login_url='/account/login/')
def new_thread(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    if request.method == "POST":
        thread_form = ThreadForm(request.POST)
        post_form = PostForm(request.POST)
        if thread_form.is_valid() and post_form.is_valid():
            thread = thread_form.save(False)
            thread.subject = subject
            thread.user = request.user
            thread.save()

            post = post_form.save(False)
            post.user = request.user
            post.thread = thread
            post.save()

            messages.success(request, "You have created a new thread!")

            return redirect(reverse('thread', args=[thread.pk]))
    else:
        thread_form = ThreadForm()
        post_form = PostForm()

    args = {
        'thread_form': thread_form,
        'post_form': post_form,
        'subject': subject,
    }
    args.update(csrf(request))

    return render(request, 'thread_form.html', args)


def thread(request, thread_id):
    thread_ = get_object_or_404(Thread, pk=thread_id)
    args = {'thread': thread_}
    args.update(csrf(request))
    return render(request, 'thread.html', args)


@login_required(login_url='/account/login/')
def new_post(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(False)
            post.thread = thread
            post.user = request.user
            post.save()

            messages.success(request, "Your post has been added to the thread!")

            return redirect(reverse('thread', args={thread.pk}))
    else:
        form = PostForm()

    args = {
        'form': form,
        'form_action': reverse('new_post', args={thread.id}),
        'button_text': 'Update Post'
    }
    args.update(csrf(request))

    return render(request, 'post_form.html', args)


@login_required
def edit_post(request, thread_id, post_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Your post has been updated!")

            return redirect(reverse('thread', args={thread.pk}))
    else:
        form = PostForm(instance=post)

    args = {
        'form': form,
        'form_action': reverse('edit_post', kwargs={"thread_id": thread.id, "post_id": post.id}),
        'button_text': 'Update Post'
    }
    args.update(csrf(request))

    return render(request, 'post_form.html', args)


@login_required
def delete_post(request, thread_id, post_id):
    post = get_object_or_404(Post, pk=post_id)
    thread_id = post.thread.id
    post.delete()

    messages.success(request, "Your post was deleted!")

    return redirect(reverse('thread', args={thread_id}))