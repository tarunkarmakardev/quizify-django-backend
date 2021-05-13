
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('api/', include('accounts.urls')),
    path('api/', include('quiz.urls')),
    path('', include('core.urls')),
    path('summernote/', include('django_summernote.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_title = "Quizify Admin"
admin.site.site_header = "Quizify Admin"
admin.site.index_title = "Quizify Admin"