from django.urls import include, path

from .views import users, professors, administratives

urlpatterns = [
    path('', users.home, name='home'),

    path('professors/', include(([
        path('', professors.HomeView, name='professors_home'),
    ], 'users'), namespace='professors')),

    path('administratives/', include(([
        path('', administratives.HomeView, name='administratives_home'),
    ], 'users'), namespace='administratives')),
]
