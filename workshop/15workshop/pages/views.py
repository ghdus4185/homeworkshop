from django.shortcuts import render
# Create your views here.

def one(request):
    # number = request.GET.get('number')
    # num = Number(number=number)
    # num.save()

    # context = {
    #     'num':num,    
    # }
    return render(request, 'one.html')

def two(request):
    # number = request.GET.get('number')
    # num = Number(number=number)
    # num.save()

    # context = {
    #     'num':num,    
    # }
    return render(request, 'two.html')
