from django.forms import TextInput


#Widget for calendar in Person edit form
class CalendarWidget(TextInput):
    class Media:
        jsp = '/site_media/js'
        css = {
            'all': ('/site_media/css/ui-lightness/jquery-ui-1.8.5.custom.css',)
        }
        js = ('%s/jquery-1.4.2.min.js' % jsp,
              '%s/jquery-ui-1.8.5.custom.min.js' % jsp,
              '%s/jquery.ui.datepicker-ru.js' % jsp,
              '%s/calendar_init.js' % jsp,
              '%s/jquery.form.js' % jsp,
              '%s/edit_form.js' % jsp,
        )

    def __init__(self, attrs={}):
        super(CalendarWidget, self).__init__(
                attrs={'class': 'datepicker'}
        )
