from api.views import PersonaViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('persona', PersonaViewset)