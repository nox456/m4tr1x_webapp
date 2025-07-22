from django.http import HttpResponse

count = 1

def index(_):
    global count
    if count > 5:
        # Max iterations reached
        return HttpResponse(b"STOP!!")
    count += 1
    return HttpResponse(bytes(str(count), 'utf-8'))
