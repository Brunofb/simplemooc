"""Summary
"""
from django.shortcuts import render


def home(request):
    """Summary
    Args:
        request (TYPE): Description
    Returns:
        TYPE: Description
    """
    return render(request, 'home.html', {"usuario": "Bruno Fonseca Barbosa"})


def contact(request):
    """Summary
    Args:
        request (TYPE): Description
    Returns:
        TYPE: Description
    """
    return render(request, 'contact.html')
