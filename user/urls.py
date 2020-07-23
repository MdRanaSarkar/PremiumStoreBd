from django.urls import path
from user.views import UserP,for_login,forlogout,forSignUp,ForUserProfile,user_update,user_password

urlpatterns=[
path('', UserP,name='UserProfile'),
path('login/', for_login,name='for_login'),
path('logout/', forlogout,name='forlogout'),
path('signup/', forSignUp,name="forSignUp"),
path('userprofile/', ForUserProfile,name='ForUserProfile'),
path('user_update/',user_update,name="user_update"),
path('password/',user_password,name="password"),
]