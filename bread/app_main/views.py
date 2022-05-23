from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    context = {
        'banner_title':'회원가입'
    }
    return render(request, 'signup.html', context=context)

def signin(request):
    context = {
        'banner_title':'로그인'
    }
    return render(request, 'signin.html', context=context)
    
def find_info(request):
    context = {
        'banner_title':'아이디/비밀번호 찾기'
    }
    return render(request, 'find_info.html', context=context)