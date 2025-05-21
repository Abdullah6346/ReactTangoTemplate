# DJANGO-REACT-SAMPLE/api/apps.py
import os
import importlib
from django.apps import AppConfig
from django.urls import path, include

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'  # This MUST match the app's directory name

    def ready(self):
        super().ready()
        try:
            from . import urls as root_api_urls # Relative import for api/urls.py
        except ImportError:
            print("ERROR: Could not import 'api.urls'. Ensure DJANGO-REACT-SAMPLE/api/urls.py exists.")
            # If api/urls.py is missing, you might need to create an empty one.
            # For now, let's assume it will exist.
            return

        api_app_dir = os.path.dirname(__file__) # This gives the path to 'DJANGO-REACT-SAMPLE/api/'
        print(f"ApiConfig: Scanning for sub-routes in: {api_app_dir}")

        for item_name in os.listdir(api_app_dir):
            item_path = os.path.join(api_app_dir, item_name)

            # Check if it's a directory, not a Python special dir, and not common app-level files/dirs
            if os.path.isdir(item_path) and \
               not item_name.startswith('__') and \
               item_name not in ['migrations', 'management', 'static', 'templates', 'tests', 'models']: # Added 'models' to exclusion for top-level models dir

                sub_module_name = f'{self.name}.{item_name}' # e.g., 'api.users'
                sub_urls_module_name = f'{sub_module_name}.urls' # e.g., 'api.users.urls'

                try:
                    importlib.import_module(sub_urls_module_name)
                    route_path_segment = f'{item_name}/' # e.g., 'users/'
                    new_url_pattern = path(route_path_segment, include(sub_urls_module_name))

                    # Prevent adding duplicate URL patterns if ready() is called multiple times
                    is_duplicate = any(
                        hasattr(p.pattern, 'regex') and hasattr(new_url_pattern.pattern, 'regex') and \
                        p.pattern.regex.pattern == new_url_pattern.pattern.regex.pattern
                        for p in root_api_urls.urlpatterns
                    )

                    if not is_duplicate:
                        root_api_urls.urlpatterns.append(new_url_pattern)
                        print(f"  -> Registered routes from {sub_urls_module_name} under api/{route_path_segment}")
                    # else:
                    #     print(f"  -> Routes from {sub_urls_module_name} already registered.")

                except ImportError as e:
                    if f"No module named '{sub_urls_module_name}'" in str(e):
                        # This is expected if a sub-directory doesn't have a urls.py
                        print(f"  -> No urls.py found in api/{item_name}. Skipping auto-route for this sub-directory.")
                    else:
                        # Other import error within the sub-module's urls.py or its dependencies
                        print(f"  -> Error importing from {sub_module_name} (likely {sub_urls_module_name}): {e}")
                except Exception as e:
                    print(f"  -> Unexpected error processing api/{item_name}: {e}")