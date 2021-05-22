from django.urls import path, include
from .views import TaskViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('tasks/', TaskList.as_view()),
#     path('tasks/<int:id>/', TaskDetails.as_view()),
# ]
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename="tasks")
router.register(r'users', UserViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]