from django import template
register = template.Library()
#
#
# def truncate3(value):
#     return value[0:3]
#
#
# register.filter('truncate3', truncate3)
@register.filter(name='t_n')
def truncate_n(value,n):
    return value[0:n]
