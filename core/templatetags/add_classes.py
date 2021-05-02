from django.template import Library

register = Library()

@register.filter(name='class')
def addclass(field, class_attr):
    return field.as_widget(attrs={'class': class_attr})
