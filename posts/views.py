from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from requests import request
from .models import Post, Comment, Report
from .forms import CommentForm
from django.core.mail import send_mail
from users.models import Profile

class PostListView (LoginRequiredMixin, ListView):
	model = Post
	template_name = 'posts/home.html'
	context_object_name = 'posts'
	ordering = ['-pub_date']


class PostDetailView (LoginRequiredMixin, DetailView):
	# model = Post
	# context_object_name = 'posts'

	def get (self, request, pk, *args, **kwargs):
		post = Post.objects.get(pk = pk)
		c_form = CommentForm()
		comments = Comment.objects.filter(post = post).order_by('-pub_date')
		context = {
			'post' : post,
			'c_form' : c_form,
			'comments' : comments
		}
		return render (request, 'posts/post_detail.html', context)
	#Adding comments 
	def post(self, request, pk, *args, **kwargs):
		post = Post.objects.get(pk = pk )
		c_form = CommentForm(request.POST)
		if c_form.is_valid():
			new_comment = c_form.save(commit=False)
			new_comment.author = request.user
			new_comment.post = post
			new_comment.save()
    
		comments = Comment.objects.filter(post=post).order_by('-pub_date')
		context = {
			'post': post,
			'c_form': c_form,
			'comments': comments,
		}

		return render(request, 'posts/post_detail.html', context)

#Make a ban if a user is bannde then he cannot post until dattime > 24 hrs
class PostCreateView (LoginRequiredMixin, CreateView):
	model = Post
	fields = ['image', 'caption']
	success_url = '/home'    

	def sendemail (self):
		from_user = self.request.user.email
		profile = Profile.objects.get(user = request.user)
		followers = profile.followers()
		for follower in followers :
			follower_email = follower.user.email
			if follower_email :
				send_mail ('New post', 'There has been a new post', from_user, follower_email, fail_silently=False)
	#To show that the logged in user is the author
	def form_valid(self, form):
		form.instance.op_name = self.request.user
		return super().form_valid(form)

#Update is not showing properly
class PostUpdateView (LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
	model = Post
	fields = ['caption', 'image']

	#To show that the logged in user is the author
	def form_valid(self, form):
		form.instance.op_name = self.request.user
		return super().form_valid(form)

	def test_func(self):
		posts = self.get_object()
		if self.request.user == posts.op_name:
			return True
		return False

	def get_success_url(self):
		pk = self.kwargs['pk']
		return reverse_lazy('detail', kwargs={'pk': pk})

class PostDeleteView (LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/home'
	def test_func(self):
		posts = self.get_object()
		if self.request.user == posts.op_name :
			return True
		return False

class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break
        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)
        if is_like:
            post.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class AddDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        is_like = False
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
        if is_like:
            post.likes.remove(request.user)

        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)
        if is_dislike:
            post.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class AddCommentView (LoginRequiredMixin, CreateView):
	model = Comment
	form_class = CommentForm
	# context_object_name = "all_comments"
	template_name = 'posts/post_detail.html'
	success_url = '/home'

	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		form.instance.username = self.request.user
		print ("Form validated")
		return super().form_valid(form)
	
	def get_context_data (self, **kwargs):
		context = super().get_context_data(**kwargs)
		reqdid = self.kwargs['pk']
		comments = Comment.objects.filter(post_id  =reqdid)
		context ['comments'] = comments
		context [reqdid] = reqdid
		print(comments)
		return context

class ReportView (LoginRequiredMixin, View):
	def post (self, request, pk, *args, **kwargs):
		post = Post.objects.get(pk = pk)
		#Even if user deletes post the content is stored
		if Report.objects.filter(post = post) :
			report =  Report.objects.filter(post = post).first()
			if report.reporter == request.user.username :
				pass
			else:
				reportcount += 1
		else : 
			report = Report.objects.create()
			report.post = post
			report.poster = post.op_name
			report.reporter = request.user.username
			report.image = post.image
			report.caption = post.caption
			report.reportcount = 1
			report.save()

		next = request.POST.get('next', '/')
		return HttpResponseRedirect(reverse('detail', args =  [post.pk] ))

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'posts/comment_delete.html'

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.usernmae

