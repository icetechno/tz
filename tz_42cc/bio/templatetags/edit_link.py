from django import template

register = template.Library()

#compilation function
def do_edit_link(parser, token):
    try:
        tag_name, target = token.split_contents()    #safe split
    except ValueError:
        msg = '%r tag requires a single argument' % token.contents[0]
        raise template.TemplateSyntaxError(msg)
    return EditLinkNode(target)

#template node
class EditLinkNode(template.Node):
    def __init__(self, target):
        self.target = target
        
    def render(self, context):
        return 'edit_link_test %s' % self.target
    
    
register.tag('edit_link', do_edit_link)    
    
    
    
    