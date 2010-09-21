from tz_42cc.bio.models import HttpRequestData

class LogHttpRequest:
    def process_request(self, request):
        request_data = ''
        if request.method == 'GET':
            request_data = unicode(request.GET)
        elif request.method == 'POST':
            request_data = unicode(request.POST)
        
        log_instance = HttpRequestData(path = request.path,
                                       method = request.method,
                                       request = request_data,
                                       cookies = unicode(request.cookies) if hasattr(request, 'cookies') else '',
                                       meta = request.META,
                                       user = u'is_authenticated' if request.user.is_authenticated() else u'not_authenticated')                                       
        log_instance.save()
