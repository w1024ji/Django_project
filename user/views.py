from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from post.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


# Create your views here.

# 회원 가입
def signup(request):
    if request.method == 'POST':
        # 필수 입력값이 누락되었는지 확인
        required_fields = ['nickname', 'username', 'password', 'confirm']
        for field in required_fields:
            if not request.POST.get(field):
                error_message = f"{field}을(를) 입력해주세요."
                if field == 'nickname':
                    error_message = "닉네임을 입력해주세요."
                elif field == 'username':
                    error_message = "아이디를 입력해주세요."
                elif field == 'password':
                    error_message = "비밀번호를 입력해주세요."
                elif field == 'confirm':
                    error_message = "비밀번호를 한번 더 입력해주세요."
                return render(request, 'user/signup.html', {'error': error_message})


        # 비밀번호와 비밀번호 확인이 일치하는지 확인
        if request.POST['password'] != request.POST['confirm']:
            error_message = "비밀번호가 일치하지 않습니다."
            return render(request, 'user/signup.html', {'error': error_message})

        # 이미 가입된 아이디인지 확인
        if User.objects.filter(username=request.POST['username']).exists():
            error_message = "이미 가입된 아이디입니다."
            return render(request, 'user/signup.html', {'error': error_message})

        # 아이디가 최소 4글자 이상인지 확인
        if len(request.POST['username']) < 4:
            error_message = "아이디는 최소 4자 이상이어야 합니다."
            return render(request, 'user/signup.html', {'error': error_message})

        # 비밀번호가 조건을 충족하는지 확인
        password = request.POST['password']
        if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
            error_message = "비밀번호는 영문과 숫자를 포함하여 8자 이상이어야 합니다."
            return render(request, 'user/signup.html', {'error': error_message})

        # 비밀번호가 조건을 충족하고, 아이디가 최소 4글자 이상이며 이미 가입되지 않은 경우에 새로운 유저를 만들고 로그인
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
        auth.login(request, user)
        return redirect('/')

    return render(request, 'user/signup.html')

# 로그인
def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST['username']
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)

        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
        # 존재하지 않는다면
        else:
            error_message = '아이디 또는 비밀번호가 일치하지 않습니다.'
            return render(request, 'user/login.html', {'error': error_message})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, 'user/login.html')


# 로그 아웃
# def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    # if request.method == 'POST':
    #     auth.logout(request)
    #     return redirect('/')

    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    # return render(request, 'user/login.html')

# 로그 아웃
def logout(request):
    auth.logout(request)
    return redirect('/')

#@login_required
def mypage(request):

    return render(request, 'user/mypage.html')
# @login_required
# def my_postList(request):
#     username=request.user.username
#     user_posts = Post.objects.filter(author=request.user)
#     return render(request, 'user/my_post_list.html', {'username': username})




class MyPostsListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'user/my_post_list.html'  # 적절한 템플릿 이름으로 변경하세요.
    context_object_name = 'posts'
    ordering = ['-created_at']

    def get_queryset(self):
        # 현재 로그인한 사용자의 게시글만 필터링
        return Post.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 현재 로그인한 사용자의 username을 context에 추가
        context['username'] = self.request.user.username
        return context