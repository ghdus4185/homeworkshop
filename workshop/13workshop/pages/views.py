from django.shortcuts import render

# Create your views here.

def info(request):
    gjpy2 = [
            "고재형", "고태환", "공현아", "김규리",
            "김기범", "김상돈", "김선만", "김승연",
            "김혁준", "남선웅", "박선용", "박승규",
            "박승재", "박정우", "양선", "양예은",
            "윤서영", "윤준석", "정명한", "정윤선",
            "정은지", "정진주", "창호연", "최동호",
            "최수빈", "최화경",
            ]
    context = {
        'students': gjpy2,
    }
    return render(request, 'info.html', context)

def student(request, name):
    students = {'홍길동': 25, '김길동': 26, '박길동': 27}
    context = {
        'name': name,
        'age': students[name]
    }
    # student_age = students.get(name)
    # if student_age:
    #     message = '해당학생이 없습니다'
    # else:
    #     messge = f'{name}학생의 나이는 {student_age}입니다.'
    # context = {
    #     'message': message
    # }
    return render(request, 'student.html', context)