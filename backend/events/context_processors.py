# from .models import Event

def event_types(request):
    return {'event_types': ('CINEMA', 'PLAYS', 'BOOKS', 'THEATER'), }
