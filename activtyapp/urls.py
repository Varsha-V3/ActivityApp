from django.urls import path,include


# from rest_framework.urlpatterns import format_suffix_patterns
from activtyapp import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("Status",views.StatusAPI)
router.register("Members",views.MembersAPI)
router.register("ActivityPeriod",views.ActivityPeriodAPI)
router.register("User",views.UserAPI)

urlpatterns=[path('',include(router.urls))]