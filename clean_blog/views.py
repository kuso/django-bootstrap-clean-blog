from django.shortcuts import render
import markdown2


from .models import Post
# Create your views here.

def index(request):
    context = dict()
    posts = Post.objects.filter(is_public=True).all()
    context['posts'] = posts
    return render(request, 'index.html', context)


def about(request):
    context = dict()
    return render(request, 'about.html', context)


def contact(request):
    context = dict()
    return render(request, 'contact.html', context)


def post(request, post_id):
    classes_dict = {'table': 'table-responsive table-bordered table-striped my_table'}
    markdowner = markdown2.Markdown(extras={"tables": None,
                                            'fenced-code-blocks': None,
                                            "html-classes":classes_dict})
    context = dict()
    post = Post.objects.get(id=post_id)
    html_content = markdowner.convert(post.content)
    context['content'] = html_content
    context['post'] = post
    return render(request, 'post.html', context)

