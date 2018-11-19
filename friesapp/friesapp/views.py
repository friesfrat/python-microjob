from django.http import HttpResponse


def demo_response(request):

    if request.GET is not None:

        resp_msg = 'Turiiiiiii.... Bum Bum Bum Sakaia HEI HEI -> https://www.youtube.com/watch?v=NYeLG0wG--k'

        return HttpResponse(resp_msg)
