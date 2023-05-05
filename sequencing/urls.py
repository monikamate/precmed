from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers


urlpatterns = [
    path('home/', views.load_reference_sequence),
    path('analyzefiles/', views.AnalyzeFilesView.as_view()),
]

router = DefaultRouter()
router.register('sequences',views.SequenceViewSet, basename='sequences')
router.register('references',views.ReferenceViewSet, basename='references')
router.register('analysisstatus',views.AnalysisStatusViewSet, basename='analysisstatus')

urlpatterns += router.urls