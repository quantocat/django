"""
Eigene Filter und Templatetags anlegen

Filter: |
Tag: {% %}
"""
from django import template 

register = template.Library()


@register.filter(name="has_group")
def has_group(user, group_name) -> bool:
    """Im Template prüfen, ob User einer Gruppe angehört. 
    
    Usage:
    {% if request.user|has_group('moderatoren') %}
        
    """
    return user.groups.filter(name=group_name).exists()