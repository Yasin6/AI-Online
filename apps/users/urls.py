# coding=utf-8
_author_ = 'Yasin'
_date_ = '2018-04-19 22:03'
from django.conf.urls import url, include
from .views import UserInfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView, MyCourseView, MyFavOrgView, MyFavTeacherView, MyFavCourseView, MyMessageView


urlpatterns = [
    url(r'^info/$', UserInfoView.as_view(), name="user_info"),  # 用户信息
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),  # 用户头像上传
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),  # 用户个人中心修改密码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),  # 发送邮箱验证码
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),  # 修改邮箱
    url(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"),  # 我的课程
    url(r'^myfav/org/$', MyFavOrgView.as_view(), name="myfav_org"),  # 我收藏的课程机构
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name="myfav_teacher"),  # 我收藏的老师
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name="myfav_course"),  # 我收藏的课程
    url(r'^mymessage/$', MyMessageView.as_view(), name="mymessage"),  # 我的消息

]

