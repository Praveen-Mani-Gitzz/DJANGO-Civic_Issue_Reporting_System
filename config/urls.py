"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from citygram import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Public landing (home) — shows Register/Login buttons for guests
    path('', views.home, name='home'),

    # Registration
    path('register/', views.register_view, name='register'),

    # Login / Logout (using Django auth views)
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    # App pages (protected inside views as needed)
    path('home/', views.home, name='home_logged'),   # optional alias if you used 'home' elsewhere
    path('complaint/new/', views.create_complaint, name='create_complaint'),
    path('my-complaints/', views.my_complaints, name='my_complaints'),

    # staff reply page (admin-only)
    path('reply/<int:complaint_id>/', views.reply_to_complaint, name='reply_to_complaint'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
