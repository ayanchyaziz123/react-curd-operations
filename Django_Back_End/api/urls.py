from .import views
from django.urls import path
from .views import UsersApiView, UsersApiNew, UsersAPIUpdate, UsersAPIDelete


urlpatterns = [
    path('', UsersApiView.as_view()),
    path('insert/', UsersApiNew.as_view()),
    path('update/<int:pk>/', UsersAPIUpdate.as_view()),
    path('delete/<int:pk>/', UsersAPIDelete.as_view()),
]