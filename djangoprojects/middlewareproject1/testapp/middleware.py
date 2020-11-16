from django.http import HttpResponse


class ExecutionFlowMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('This line will printed at pre-processing of request')
        response = self.get_response(request)
        print('This line will printed at post-processing of request')
        return response


class AppMaintenanceMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return HttpResponse('<h1>Currently site is under maintenance....Please try after 2 days</h1>')


class ErrorMessageMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response=self.get_response(request)
        return response

    def process_exception(self, request, exception):
        s1 = '<h1>Currently we are facing some Technical issue, please try after some time....</h1>'
        s2 = '<h2>Exception:{}</h2>'.format(exception.__class__.__name__)
        s3 = '<h2>Exception Description/message:{}</h2>'.format(exception)
        return HttpResponse(s1+s2+s3)


class FirstMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print('This line is printed by FIRST middleware at pre processing of request')
        res=self.get_response(request)
        print('This line is printed by FIRST middleware at post processing of request')
        return res


class SecondMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print('This line is printed by SECOND middleware at pre processing of request')
        res=self.get_response(request)
        print('This line is printed by SECOND middleware at post processing of request')
        return res


class ThirdMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print('This line is printed by THIRD middleware at pre processing of request')
        res=self.get_response(request)
        print('This line is printed by THIRD middleware at post processing of request')
        return res
