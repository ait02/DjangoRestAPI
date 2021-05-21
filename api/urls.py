from django.urls import path, include
from .views import TaskViewSet
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('tasks/', TaskList.as_view()),
#     path('tasks/<int:id>/', TaskDetails.as_view()),
# ]
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename="tasks")
urlpatterns = router.urls