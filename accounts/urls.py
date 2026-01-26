from django.urls import path
from . import views
from . import api_views

urlpatterns = [
	path('hello/', views.hello),
	path('profiles/', views.profiles, name = "profile"),
	path('add/',views.add_profile,name = 'profiles'),
	path("login/", views.login_view, name="login"),
	path("logout/",views.logout_view, name = "logout"),
	path("api/hello/",api_views.hello_api),
	path("api/profiles/", api_views.profile_list_api)

]
