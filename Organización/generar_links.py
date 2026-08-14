import urllib.parse

def make_gcal_link(title, start_iso_utc, end_iso_utc, details="", location="", recur=""):
    base = "https://calendar.google.com/calendar/render?action=TEMPLATE"
    params = {
        "text": title,
        "dates": f"{start_iso_utc}/{end_iso_utc}",
        "details": details,
        "location": location
    }
    if recur:
        params["recur"] = recur
    return base + "&" + urllib.parse.urlencode(params)

events = [
    {
        "name": "Clase Teórica - Modelos y Sistemas",
        "start": "20260814T210000Z",
        "end": "20260814T230000Z",
        "details": "Docentes: Guillermo La Mura - Diana Rubio\nHorario local: Viernes 18:00 - 20:00 hs",
        "recur": "RRULE:FREQ=WEEKLY;UNTIL=20261121T030000Z"
    },
    {
        "name": "Clase Práctica - Modelos y Sistemas",
        "start": "20260814T230000Z",
        "end": "20260815T010000Z",
        "details": "Docente: Paula Romina Soria\nHorario local: Viernes 20:00 - 22:00 hs",
        "recur": "RRULE:FREQ=WEEKLY;UNTIL=20261121T030000Z"
    },
    {
        "name": "Parcial Teórico-Práctico - Modelos y Sistemas",
        "start": "20261023T210000Z",
        "end": "20261024T010000Z",
        "details": "Parcial teórico-práctico de la materia.\nNota mínima de aprobación: 5.\nHorario local: Viernes 23/10 18:00 - 22:00 hs",
        "recur": ""
    },
    {
        "name": "Recuperatorio - Modelos y Sistemas",
        "start": "20261106T210000Z",
        "end": "20261107T010000Z",
        "details": "Fecha de recuperación del parcial.\nNota mínima de aprobación: 5.\nHorario local: Viernes 06/11 18:00 - 22:00 hs",
        "recur": ""
    },
    {
        "name": "ENTREGA LÍMITE: Trabajo Práctico Final",
        "start": "20261114T025900Z",
        "end": "20261114T025959Z",
        "details": "Fecha límite de entrega de informes TP Final (Grupos de 3 integrantes).\nHorario local límite: Viernes 13/11/2026 23:59h (Ajustado según instrucción del viernes previo a la fecha mal anotada).",
        "recur": ""
    },
    {
        "name": "Presentaciones TP Final - Modelos y Sistemas",
        "start": "20261120T210000Z",
        "end": "20261121T010000Z",
        "details": "Presentaciones de 15 minutos del Trabajo Práctico Final.\nHorario local: Viernes 20/11 18:00 - 22:00 hs",
        "recur": ""
    }
]

for ev in events:
    link = make_gcal_link(ev["name"], ev["start"], ev["end"], ev["details"], recur=ev["recur"])
    print(f"=== {ev['name']} ===")
    print(link)
    print()
