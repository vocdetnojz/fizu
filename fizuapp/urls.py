from django.urls import path

from . import views

urlpatterns = [
    path('blank.html', views.blank, name='blank'),
    path('buttons.html', views.buttons, name='buttons'),
    path('cards.html', views.cards, name='cards'),
    path('charts.html', views.charts, name='charts'),
    path('forgot-password.html', views.forgot_password, name='forgot_password'),
    path('login.html', views.login, name='login'),
    path('register.html', views.register, name='register'),
    path('tables.html', views.tables, name='tables'),
    path('utilities-animation.html', views.utilities_animation, name='utilities_animation'),
    path('utilities-border.html', views.utilities_border, name='utilities_border'),
    path('utilities-color.html', views.utilities_color, name='utilities_color'),
    path('utilities-other.html', views.utilities_other, name='utilities_other'),

    path('blank', views.blank, name='blank'),
    path('buttons', views.buttons, name='buttons'),
    path('cards', views.cards, name='cards'),
    path('charts', views.charts, name='charts'),
    path('forgot-password', views.forgot_password, name='forgot_password'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('tables', views.tables, name='tables'),
    path('utilities-animation', views.utilities_animation, name='utilities_animation'),
    path('utilities-border', views.utilities_border, name='utilities_border'),
    path('utilities-color', views.utilities_color, name='utilities_color'),
    path('utilities-other', views.utilities_other, name='utilities_other'),

    path('', views.index, name='home'),
    path('index', views.index, name='home'),
    path('index.html', views.index, name='home'),
    path('generate', views.generate, name='generate'),
    path('delete', views.delete, name='delete'),
]
