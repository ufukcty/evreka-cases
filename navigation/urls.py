from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('navigation/', include('navigation_record.urls')),
    path('collection/', include('collection_frequency.urls'))

]
