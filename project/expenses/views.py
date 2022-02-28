from django.shortcuts import render
from expenses.models import Summary, Detail

def index(request):
  total_summaries = Summary.objects.count()
  total_detail = Detail.objects.count()
  return render(request, 'expenses/index.html', context={'total_summaries': total_summaries, 'total_detail': total_detail})
