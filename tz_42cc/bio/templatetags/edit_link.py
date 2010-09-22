from django import template
from django.core.urlresolvers import reverse

register = template.Library()

#compilation function
def do_edit_link(parser, token):
    try:
        tag_name, target = token.split_contents()    #safe split
    except ValueError:
        msg = '%r tag requires a single argument' % token.contents[0]
        raise template.TemplateSyntaxError(msg)
    return EditLinkNode(target)

#return admin edit url for object
def url_to_edit_object(object):
    url = reverse('admin:%s_%s_change' %(object._meta.app_label,  object._meta.module_name),  args=[object.id] )
    return u'<a href="%s">Edit %s</a>' %(url,  object.__unicode__())

#template node
class EditLinkNode(template.Node):
    def __init__(self, target):
        self.target_variable = template.Variable(target)
        
    def render(self, context):
        try:
            actual_variable = self.target_variable.resolve(context)
            return url_to_edit_object(actual_variable)
        except template.VariableDoesNotExist:
            return 'render error'

#regiser tag in libray       
register.tag('edit_link', do_edit_link)    
    
    
    
    