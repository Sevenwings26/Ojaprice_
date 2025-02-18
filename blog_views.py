from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import CreateBlogForm

# Create
def create_blog(request):
    """
    Create blog function: Handles blog creation with form validation.
    """
    if request.method == "POST":
        form = CreateBlogForm(request.POST, request.FILES)  # request.FILES for image upload
        if form.is_valid():
            form.save()
            print("Form Saved")
            return redirect('blogs')  # Redirect to blog listing
        else:
            print("Form is not valid", form.errors)
    else:
        form = CreateBlogForm()

    return render(request, "pages/blogcreation.html", {"form": form})

# Read (Blog List & Detail)
def blog_list(request):
    """
    Retrieve and display all blog posts.
    """
    blogs = Blog.objects.all()
    return render(request, "pages/blog_list.html", {"blogs": blogs})

def blog_detail(request, pk):
    """
    Retrieve and display a single blog post.
    """
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, "pages/blog_detail.html", {"blog": blog})

# Update
def update_blog(request, pk):
    """
    Update an existing blog post.
    """
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = CreateBlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            print("Blog Updated")
            return redirect('blog_detail', pk=pk)  # Redirect to updated blog
        else:
            print("Form is not valid", form.errors)
    else:
        form = CreateBlogForm(instance=blog)

    return render(request, "pages/blog_update.html", {"form": form, "blog": blog})

# Delete
def delete_blog(request, pk):
    """
    Delete a blog post.
    """
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        blog.delete()
        print("Blog Deleted")
        return redirect('blogs')  # Redirect to blog list after deletion

    return render(request, "pages/blog_confirm_delete.html", {"blog": blog})



# Using slug 
from django.db import models
from django.utils.text import slugify


# Adjust models 
class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Generate slug from title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import CreateBlogForm

# Create
def create_blog(request):
    """
    Create a new blog post.
    """
    if request.method == "POST":
        form = CreateBlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.slug = slugify(blog.title)  # Generate slug before saving
            blog.save()
            print("Blog Created")
            return redirect('blog_detail', slug=blog.slug)
        else:
            print("Form is not valid", form.errors)
    else:
        form = CreateBlogForm()

    return render(request, "pages/blogcreation.html", {"form": form})

# Read (List & Detail)
def blog_list(request):
    """
    Retrieve and display all blog posts.
    """
    blogs = Blog.objects.all()
    return render(request, "pages/blog_list.html", {"blogs": blogs})

def blog_detail(request, slug):
    """
    Retrieve and display a single blog post using its slug.
    """
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, "pages/blog_detail.html", {"blog": blog})

# Update
def update_blog(request, slug):
    """
    Update an existing blog post using slug.
    """
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == "POST":
        form = CreateBlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            updated_blog = form.save(commit=False)
            updated_blog.slug = slugify(updated_blog.title)  # Update slug if title changes
            updated_blog.save()
            print("Blog Updated")
            return redirect('blog_detail', slug=updated_blog.slug)
        else:
            print("Form is not valid", form.errors)
    else:
        form = CreateBlogForm(instance=blog)

    return render(request, "pages/blog_update.html", {"form": form, "blog": blog})

# Delete
def delete_blog(request, slug):
    """
    Delete a blog post using slug.
    """
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == "POST":
        blog.delete()
        print("Blog Deleted")
        return redirect('blogs')

    return render(request, "pages/blog_confirm_delete.html", {"blog": blog})






from django.urls import path
from .views import create_blog, blog_list, blog_detail, update_blog, delete_blog

urlpatterns = [
    path('blogs/', blog_list, name='blogs'),
    path('blog/create/', create_blog, name='create_blog'),
    path('blog/<slug:slug>/', blog_detail, name='blog_detail'),
    path('blog/<slug:slug>/edit/', update_blog, name='update_blog'),
    path('blog/<slug:slug>/delete/', delete_blog, name='delete_blog'),
]
