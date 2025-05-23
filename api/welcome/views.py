# api/welcome/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status # Keep for potential future use, though not strictly needed for these examples

@api_view(['GET'])
def general_welcome(request):
    """
    A general welcome message for the API.
    """
    return Response({"message": "Welcome to our Awesome API!"})

@api_view(['GET'])
def personalized_welcome(request, name):
    """
    A personalized welcome message.
    """
    if not name: # Should not happen with URL config, but good for robustness
        return Response({"error": "Name cannot be empty"}, status=status.HTTP_400_BAD_REQUEST)
    
    # You could add more logic here, e.g., check for known names, etc.
    return Response({"message": f"Hello, {name}! Welcome aboard."})

# Example of a more complex welcome that could show API info
@api_view(['GET'])
def api_info(request):
    """
    Provides some basic information about the API.
    """
    info = {
        "api_name": "My Welcome API",
        "version": "1.0.0",
        "description": "An API to provide warm welcomes.",
        "endpoints": {
            "/welcome/": "General welcome message.",
            "/welcome/{name}/": "Personalized welcome for a given name.",
            "/welcome/info/": "This information."
        }
    }
    return Response(info)