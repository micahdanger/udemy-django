from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.replace(arg, '')

# the first 'cut' is the template tag, the second cut is the function reference
# register.filter('cut', cut)
