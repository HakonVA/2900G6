from django import template
register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class":css})

@register.filter(name='addid')
def addid(field,css_id):
    return field.as_widget(attrs={"id":css_id})