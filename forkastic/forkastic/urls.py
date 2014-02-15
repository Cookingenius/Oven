from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# Rest framework router code --------------------
from rest_framework import routers

from accounts import views as account_views
from foods.views import FoodViewSet
from settings.views import GoalViewSet

router = routers.DefaultRouter()
router.register(r'foods', FoodViewSet)
router.register(r'users', account_views.AccountViewSet, base_name='account')
router.register(r'tokens', account_views.TokenViewSet, base_name='token')
# -----------------------------------------------

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
