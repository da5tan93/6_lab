from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import VisitorForm
from webapp.models import Visitor


def index_view(request, *args, **kwargs):
    visitors = Visitor.objects.filter(status='active').order_by('-created_at')
    return render(request, 'index.html', context={
        'visitors': visitors
    })


def visitor_view(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    return render(request, 'visitor.html', context={
        'visitor': visitor
    })


def visitor_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = VisitorForm()
        return render(request, 'create.html', context={'form': form})
    elif request.method == 'POST':
        form = VisitorForm(data=request.POST)
        if form.is_valid():
            visitor = Visitor.objects.create(
                author=form.cleaned_data['author'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text']
            )
            return redirect('visitor_view', pk=visitor.pk)
        else:
            return render(request, 'create.html', context={'form': form})


def visitor_update_view(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    if request.method == 'GET':
        form = VisitorForm(data={
            'author': visitor.author,
            'email': visitor.email,
            'text': visitor.text
        })
        return render(request, 'update.html', context={'form': form, 'visitor': visitor})
    elif request.method == 'POST':
        visitor.author = request.POST.get('author')
        visitor.email = request.POST.get('email')
        visitor.text = request.POST.get('text')

        errors = {}

        if not visitor.author:
            errors['author'] = 'author should not be empty!'
        elif len(visitor.author) > 40:
            errors['author'] = 'author should have length of 40 symbols or less!'

        if not visitor.email:
            errors['email'] = 'email should not be empty!'
        elif len(visitor.email) > 50:
            errors['email'] = 'email should have length of 40 symbols or less!'

        if not visitor.text:
            errors['text'] = 'Text should not be empty!'
        elif len(visitor.text) > 3000:
            errors['text'] = 'Text should have length of 3000 symbols or less!'

        if len(errors) > 0:
            return render(request, 'update.html', context={'errors': errors, 'visitor': visitor})

        visitor.save()
        return redirect('visitor_view', pk=visitor.pk)


def visitor_delete_view(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'visitor': visitor})
    elif request.method == 'POST':
        visitor.delete()
        return redirect('index')
