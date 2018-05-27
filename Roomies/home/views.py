from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from home.forms import ApplicationForm
from home.models import Post, Friend, Application

class ApplicationView(TemplateView):
    template_name = 'home/questions.html'

    def get(self, request):
        users = User.objects.exclude(id=request.user.id)
        ufirst_name = request.user.first_name
        ulast_name = request.user.last_name
        uemail = request.user.email

        try:
            friend = Friend.objects.get(current_user=request.user)
            friends = friend.users.all()
        except Friend.DoesNotExist:
            friends = None

        form = ApplicationForm(initial={'first_name':ufirst_name, 'last_name':ulast_name, 'email':uemail})
        try:
            application = Application.objects.filter(user=request.user)[:1]

            #print(request.user)
            #print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            #print(application.count())
            if application.count() > 0:
                #ubedtime = application.bedtime
                # ugraduating_class = application.graduating_class
                # umajor = application.major
                # form_filled = ApplicationForm(initial={
                #     'first_name':ufirst_name, 'last_name':ulast_name, 'email':uemail, 'bedtime': ubedtime,
                #     'graduating_class': ugraduating_class, 'major': umajor
                # })
                args = {
                    'form': None, 'users': users, 'friends': friends, 'bedtime': application,
                    'graduating_class': application, 'major': application
                }
                return render(request, self.template_name, args)
                #return render(request, self.template_name, {'form': form_filled, 'users': users, 'friends': friends})

            return render(request, self.template_name, {'form': form, 'users': users, 'friends': friends})

        except Application.DoesNotExist:
            application = None
            return render(request, self.template_name, {'form': form, 'users': users, 'friends': friends})

        #
        # application = Application.objects.filter(user=request.user)[:1]
        # if application.count() > 0:
        #     return render(request, self.template_name, {'form': None, 'users': users, 'friends': friends})
        # return render(request, self.template_name, {'form': form, 'users': users, 'friends': friends})

    def post(self, request):
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user
            post.save()
            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            bedtime = form.cleaned_data['bedtime']
            gclass = form.cleaned_data['graduating_class']
            major = form.cleaned_data['major']

            form.save()

            return render(request, 'home/questions.html')
        return render(request, self.template_name, {'form': form})

    # def get(self, request):
    #     form = ApplicationForm()
    #     posts = Post.objects.all().order_by('-created')
    #     users = User.objects.exclude(id=request.user.id)
    #
    #     args = {
    #         'form': form, 'posts': posts, 'users': users
    #     }
    #     return render(request, self.template_name, args)
    # def post(self, request):
    #     form = ApplicationForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.user = request.user
    #         post.save()
    #
    #         text = form.cleaned_data['post']
    #         form = ApplicationForm()
    #         return redirect('home:home')
    #     args = {'form': form, 'text': text}
    #     return render(request, self.template_name, args)


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        users = User.objects.exclude(id=request.user.id)
        try:
            friend = Friend.objects.get(current_user=request.user)
            friends = friend.users.all()
        except Friend.DoesNotExist:
            friends = None

        args = {
            'users': users, 'friends': friends
        }

        return render(request, self.template_name, args)



def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)

    return redirect('home:home')
