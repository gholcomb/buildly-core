from rest_framework import routers
from . import views


router = routers.SimpleRouter()

router.register(r'workflowlevel1', views.WorkflowLevel1ViewSet)
router.register(r'workflowlevel2', views.WorkflowLevel2ViewSet)
router.register(r'workflowlevel2sort', views.WorkflowLevel2SortViewSet)
router.register(r'workflowleveltype', views.WorkflowLevelTypeViewSet)
router.register(r'workflowlevelstatus', views.WorkflowLevelStatusViewSet)
router.register(r'workflowteam', views.WorkflowTeamViewSet)

urlpatterns = router.urls
