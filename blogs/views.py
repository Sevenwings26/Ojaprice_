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
    return render(request, 'pages/blogs.html', context)


CRUD = ...
def create_blog(request):
    """
     Create blog function...
    """
    form = CreateBlogForm(request.POST, request.FILES)  # request.FILES is added for image upload
    if request.method == "POST":
        if form.is_valid():
            form.save()
            print("Form Saved")
            return redirect('blogs')
        else:
            print("Form is not valid", form.errors)
            return render(request, "pages/blogcreation.html", {"form":form})

    # form = CreateBlogForm() 
    return render(request, "pages/blogcreation.html", {"form":form})



def read_blog(request, blog_id):
    """
     Read blog function...
    """
    blog = get_object_or_404(Blog, pk=blog_id)
    # blog = Blog.objects.get(id=blog_id)
    context = {
        "blog":blog}
    return render(request, "pages/blogdetails.html", context)


def update_blog(request, blog_id):
    """
     Update blog function...
    """
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        form = CreateBlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            print("Updated Successfully")
            return redirect("blogs")
        else:
            print("Form is not valid", form.errors)
    else:
        form = CreateBlogForm(instance=blog)

    context = {
        "form": form,
        "blog": blog,
    }
    return render(request, "pages/blog_update.html", context)


def delete_blog(request, blog_id):
    """
    Delete a blog post.
    """
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        blog.delete()
        print("Blog Deleted")
        return redirect('blogs')  # Redirect to blog list after deletion
    return render(request, "pages/blog_delete.html", {"blog": blog})


 