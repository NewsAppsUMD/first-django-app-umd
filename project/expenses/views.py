from django.shortcuts import render, get_object_or_404
from expenses.models import Summary, Detail, Category

def index(request):
  total_summaries = Summary.objects.count()
  total_detail = Detail.objects.count()
  return render(request, 'expenses/index.html', context={'total_summaries': total_summaries, 'total_detail': total_detail})

def summary(request, summary_id):
  summary = Summary.objects.get(id=summary_id)
  return render(request, 'expenses/summary.html', {'summary': summary})

def categories(request):
  categories = Category.objects.all().order_by('name')
  return render(request, 'expenses/categories.html', {'categories': categories})

def category_detail(request, slug):
  category = get_object_or_404(Category, slug=slug)
  category_summary = Summary.objects.filter(category=category.name).count()
  category_detail = Detail.objects.filter(category=category.name).count()
  return render(request, 'expenses/category_detail.html', {'category': category, 'category_summary': category_summary, 'category_detail': category_detail})
