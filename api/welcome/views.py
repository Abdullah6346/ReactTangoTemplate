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
            "/welcome/info/": "This information."
        }
    }
    return Response(info)