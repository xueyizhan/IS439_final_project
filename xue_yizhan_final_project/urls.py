from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
# from .views import redirect_root_view
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name = 'about_urlpattern', permanent = False)),
    # path('', redirect_root_view),
    path('admin/', admin.site.urls),
    path('', include('dentalinfo.urls')),
    path('about/', TemplateView.as_view(template_name = 'dentalinfo/about.html'), name = 'about_urlpattern'),
    path('login/', LoginView.as_view(template_name = 'dentalinfo/login.html'), name = 'login_urlpattern'),
    path('logout/', LogoutView.as_view(), name = 'logout_urlpattern'),
    path('contactus/', TemplateView.as_view(template_name = 'dentalinfo/contactus.html'),name = 'contactus_urlpattern'),
]
