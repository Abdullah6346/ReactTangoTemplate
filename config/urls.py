from django.contrib import admin
from django.urls import path, include # re_path and TemplateView are no longer needed here for this purpose
# from django.views.generic import TemplateView # No longer needed for serving index.html
from django.conf import settings
from django.conf.urls.static import static

# Optional: A simple view to show at the root of the Django server
from django.http import HttpResponse
def api_root_view(request):
    # You can customize this to list API endpoints or show a welcome message
    return HttpResponse("<h1>Django API Backend is Running</h1><p>Access your frontend at its development server (e.g., http://localhost:5173).</p><p>Available API base: <a href='/api/'>/api/</a></p>")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), # Your API app's URLs

    # Optional: Add a view for the root of your Django server if you want one
    path('', api_root_view, name='api_root'),

    # COMMENT OUT OR DELETE THIS LINE:
    # re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]

if settings.DEBUG:
    if hasattr(settings, 'MEDIA_URL') and hasattr(settings, 'MEDIA_ROOT'):
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)