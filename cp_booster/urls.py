"""cp_booster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import *
from long import views as vlong
from cook_off import views as vcook
from lunch_time import views as vlunch

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="Homepage"),
    path('long/', vlong.long_challenges_view),
    path('long/division1/', vlong.long_div1_view),
    path('long/division2/', vlong.long_div2_view),
    path('long/division1/a/',vlong.div1A_view),
    path('long/division1/b/',vlong.div1B_view),
    path('long/division1/c/',vlong.div1C_view),
    path('long/division1/d/',vlong.div1D_view),
    path('long/division1/e/',vlong.div1E_view),
    path('long/division1/f/',vlong.div1F_view),
    path('long/division1/g/',vlong.div1G_view),
    path('long/division1/h/',vlong.div1H_view),
    path('long/division1/i/',vlong.div1I_view),
    path('long/division1/j/',vlong.div1J_view),
    path('long/division2/a/',vlong.div2A_view),
    path('long/division2/b/',vlong.div2B_view),
    path('long/division2/c/',vlong.div2C_view),
    path('long/division2/d/',vlong.div2D_view),
    path('long/division2/e/',vlong.div2E_view),
    path('long/division2/f/',vlong.div2F_view),
    path('long/division2/g/',vlong.div2G_view),
    path('long/division2/h/',vlong.div2H_view),
    path('long/division2/i/',vlong.div2I_view),
    path('long/division2/j/',vlong.div2J_view),

    path('cook_off/', vcook.cook_off_view),
    path('cook_off/division1', vcook.cook_div1_view),
    path('cook_off/division2', vcook.cook_div2_view),
    path('cook_off/division1/a/',vcook.div1A_view),
    path('cook_off/division1/b/',vcook.div1B_view),
    path('cook_off/division1/c/',vcook.div1C_view),
    path('cook_off/division1/d/',vcook.div1D_view),
    path('cook_off/division1/e/',vcook.div1E_view),
    path('cook_off/division1/f/',vcook.div1F_view),
    path('cook_off/division1/g/',vcook.div1G_view),
    path('cook_off/division2/a/',vcook.div2A_view),
    path('cook_off/division2/b/',vcook.div2B_view),
    path('cook_off/division2/c/',vcook.div2C_view),
    path('cook_off/division2/d/',vcook.div2D_view),
    path('cook_off/division2/e/',vcook.div2E_view),

    path('lunch_time/', vlunch.lunch_time_view),
    path('lunch_time/division1', vlunch.lunch_div1_view),
    path('lunch_time/division2', vlunch.lunch_div2_view),
    path('lunch_time/division1/a/',vlunch.div1A_view),
    path('lunch_time/division1/b/',vlunch.div1B_view),
    path('lunch_time/division1/c/',vlunch.div1C_view),
    path('lunch_time/division1/d/',vlunch.div1D_view),
    path('lunch_time/division1/e/',vlunch.div1E_view),
    path('lunch_time/division1/f/',vlunch.div1F_view),
    path('lunch_time/division1/g/',vlunch.div1G_view),
    path('lunch_time/division2/a/',vlunch.div2A_view),
    path('lunch_time/division2/b/',vlunch.div2B_view),
    path('lunch_time/division2/c/',vlunch.div2C_view),
    path('lunch_time/division2/d/',vlunch.div2D_view),
    path('lunch_time/division2/e/',vlunch.div2E_view),
    path('lunch_time/division2/f/',vlunch.div2F_view),
    path('lunch_time/division2/g/',vlunch.div2G_view),
]
