from django import template

register = template.Library()

@register.filter
def cut(value,arg):
    """
    this cuts out all value of "arg" from the string!
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
