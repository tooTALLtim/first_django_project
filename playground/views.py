from django.core.cache import cache
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
import logging
import requests


logger = logging.getLogger(__name__)

class SayHelloView(APIView):
    def get(self, request):
        try:
            logger.info('Calling httpbin, hello?')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('I read you loud and clear!')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'hello.html', {'name': 'Timmmay!!'})


# class SayHelloView(APIView):
#     @method_decorator(cache_page(5 * 60))
#     def get(self, request):
#         response = requests.get('https://httpbin.org/delay/2')
#         data = response.json()
#         return render(request, 'hello.html', {'name': 'Timmmay!!'})



# @cache_page(5 * 60)
# def say_hello(request):
#     response = requests.get('https://httpbin.org/delay/2')
#     data = response.json()
#     return render(request, 'hello.html', {'name': data})


    # try:
    #     message = BaseEmailMessage(
    #         template_name='emails/hello_email.html',
    #         context={'name': 'the Grim Reaper'}
    #     )
    #     message.send(['thatguy@domain.com'])
        # message = EmailMessage(
        #             'subject: you have won!',
        #             'message: did you know that you could be worth $120,000?',
        #             'admin@domain.com',
        #             ['chumps@domain.com']
        # )
        # message.attach_file('playground/static/images/theearthisaman0.jpg')
        # message.send()
    # except BadHeaderError:
    #     pass