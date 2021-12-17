from django.urls import path
from authy.views import UserProfile, Signup, PasswordChange, PasswordChangeDone, EditProfile

from django.contrib.auth import views as authViews


urlpatterns = [

    path('/user/profile/edit', EditProfile, name='edit-profile'),
    path('user/signup/', Signup, name='signup'),
    path('', authViews.LoginView.as_view(
        template_name='login.html'), name='login'),
    path('/user/logout/', authViews.LogoutView.as_view(),
         {'next_page': 'index'}, name='logout'),
    path('/user/changepassword/', PasswordChange, name='change_password'),
    path('/user/changepassword/done', PasswordChangeDone,
         name='change_password_done'),
    path('/user/passwordreset/',
         authViews.PasswordResetView.as_view(), name='password_reset'),
    path('/user/passwordreset/done',
         authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('/user/passwordreset/<uidb64>/<token>/',
         authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('/user/passwordreset/complete/',
         authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
