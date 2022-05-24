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


# 공지사항
def announcement(request):
    context = {
        'banner_title':'공지사항'
    }
    return render(request, 'announcement.html', context=context)

def announcement_detail(request):
    context = {
        'banner_title':'공지사항'
    }
    return render(request, 'announcement_detail.html', context=context)


# 1:1문의
def inquiry(request):
    context = {
        'banner_title':'1:1문의'
    }
    return render(request, 'inquiry.html', context=context)

def inquiry_detail(request):
    context = {
        'banner_title':'1:1문의'
    }
    return render(request, 'inquiry_detail.html', context=context)


# 마이페이지
def mypage(request):
    context = {
        'banner_title':'마이페이지'
    }
    return render(request, 'mypage/mypage.html', context=context)

def mypage_order(request):
    context = {
        'banner_title':'마이페이지'
    }
    return render(request, 'mypage/mypage_order.html', context=context)

def mypage_delivery(request):
    context = {
        'banner_title':'마이페이지'
    }
    return render(request, 'mypage/mypage_delivery.html', context=context)