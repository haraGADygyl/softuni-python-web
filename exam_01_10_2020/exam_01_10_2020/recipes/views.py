from django.shortcuts import render, redirect

# Create your views here.
from exam_01_10_2020.recipes.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from exam_01_10_2020.recipes.models import Recipe


def show_index(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes
    }

    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateRecipeForm()

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditRecipeForm(instance=recipe)

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteRecipeForm(instance=recipe)

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, 'delete.html', context)


def details_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    ingredients_list = recipe.ingredients.split(', ')

    context = {
        'recipe': recipe,
        'ingredients_list': ingredients_list
    }
    return render(request, 'details.html', context)
