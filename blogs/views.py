from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import CreateBlogForm

# Create your views here.
# def index  

def blogs(request):
    blogs = Blog.objects.all()
    context = {
        "blogs":blogs
    }
    return render(request, 'pages/blogs/blogs.html', context)


CRUD = ...
# def create_blog(request):
#     form = CreateBlogForm(request.POST, request.FILES)
#     if request.method == "POST":
#         if form.is_valid():
#             blog = form.save(commit=False)
#             if not blog.slug:
#                 blog.slug = slugify(blog.title)  # Ensure slug is set
#             blog.save()
#             return redirect('blog/read', slug=blog.slug)
#     return render(request, "pages/blogs/blogcreation.html", {"form": form})

def create_blog(request):
    """
     Create blog function...
    """
    form = CreateBlogForm(request.POST, request.FILES)  # request.FILES is added for image upload
    if request.method == "POST":
        if form.is_valid():
            form.save()
            print("Form Saved")
            return redirect('blog/read')
        else:
            print("Form is not valid", form.errors)
            return render(request, "pages/blogs/blogcreation.html", {"form":form})
    # form = CreateBlogForm() 
    return render(request, "pages/blogs/blogcreation.html", {"form":form})


def read_blog(request, slug):
    """
     Read blog function...
    """
    blog = get_object_or_404(Blog, slug=slug)
    # blog = Blog.objects.get(id=blog_id)
    context = {
        "blog":blog}
    return render(request, "pages/blogs/blogdetails.html", context)


def update_blog(request, slug):
    """
    Update an existing blog post using slug.
    """
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == "POST":
        form = CreateBlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            updated_blog = form.save(commit=False)
            # updated_blog.slug = slugify(updated_blog.title)  # Update slug if title changes
            updated_blog.save()
            print("Blog Updated")
            return redirect('blog/read', slug=updated_blog.slug)
        else:
            print("Form is not valid", form.errors)
    else:
        form = CreateBlogForm(instance=blog)
    return render(request, "pages/blogs/blog_update.html", {"form": form, "blog": blog})


def delete_blog(request, blog_id):
    """
    Delete a blog post.
    """
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == "POST":
        blog.delete()
        print("Blog Deleted")
        return redirect('blogs')  # Redirect to blog list after deletion
    return render(request, "pages/blogs/blog_delete.html", {"blog": blog})

