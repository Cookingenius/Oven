from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from recipes import views as recipe_views

# django rest framework router
router = routers.DefaultRouter()
router.register(r'recipes', recipe_views.RecipeViewSet)
# end of django rest framework router

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
