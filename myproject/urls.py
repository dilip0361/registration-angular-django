"""myproject URL Configuration

e() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
     url(r'^admin/', admin.site.urls),
      url(r'^api/', include('myproject.api.urls'))
      ]