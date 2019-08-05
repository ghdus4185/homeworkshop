from django.shortcuts import render

# Create your views here.

def info(request):
    # class_mate = ['홍길동', '김길동', '박길동']
    # context = {
    #     'name': name
    # }
    return render(request, 'info.html')

def student(request, name):
    age = {'홍길동': 25, '김길동': 26, '박길동': 27}
    context = {
        'name': name,
        'age': age[name]
    }
    return render(request, 'student.html', context)