from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import Image
from django.contrib.auth.decorators import login_required


@login_required(login_url='/register/')
def home(request):
    context = {
        'posts': Image.objects.all()
    }
    return render(request,'insta/home.html',context)

class ImageListView(ListView):
    model = Image 
    template_name = Imagecontect_name = 'insta/home.html'
    context_object_name = 'posts'
    ordering =['-date_created']


class ImageDetailView(DetailView): 
    model = Image
class ImageCreateView(LoginRequiredMixin,CreateView): 
    model = Image
    fields = ['image','caption']
    

    def form_valid(self, form):
        # form.instance.user = Image.objects.get(user=self.request.user)
        form.instance.user = self.request.user
        form.instance.name = self.request.user
        return super().form_valid(form)


class ImageUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): 
    model = Image
    fields = ['image','caption']
    

    def form_valid(self, form):
        # form.instance.user = Image.objects.get(user=self.request.user)
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        image = self.get_object()
        if self.request.user == image.user:
            return True
        return False    


def about(request):
    return render(request,'insta/about.html', {'title': 'About'})


def search_results(request):
    pass
