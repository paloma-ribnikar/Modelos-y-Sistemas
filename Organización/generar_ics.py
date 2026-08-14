ics_content = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Modelos y Sistemas//Cursada 2026//ES
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:Modelos y Sistemas - 2C 2026
X-WR-TIMEZONE:America/Argentina/Buenos_Aires
BEGIN:VTIMEZONE
TZID:America/Argentina/Buenos_Aires
X-LIC-LOCATION:America/Argentina/Buenos_Aires
BEGIN:STANDARD
TZOFFSETFROM:-0300
TZOFFSETTO:-0300
TZNAME:-03
DTSTART:19700101T000000
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
UID:teorica-modelos-sistemas-2026@local
DTSTAMP:20260811T120000Z
DTSTART;TZID=America/Argentina/Buenos_Aires:20260814T180000
DTEND;TZID=America/Argentina/Buenos_Aires:20260814T200000
RRULE:FREQ=WEEKLY;UNTIL=20261121T030000Z;BYDAY=FR
SUMMARY:Clase Teórica - Modelos y Sistemas
DESCRIPTION:Clase Teórica de Modelos y Sistemas.\\nDocentes: Guillermo La Mura - Diana Rubio\\nHorario: 18:00 a 20:00 hs.
LOCATION:Aula de Cursada
END:VEVENT
BEGIN:VEVENT
UID:practica-modelos-sistemas-2026@local
DTSTAMP:20260811T120000Z
DTSTART;TZID=America/Argentina/Buenos_Aires:20260814T200000
DTEND;TZID=America/Argentina/Buenos_Aires:20260814T220000
RRULE:FREQ=WEEKLY;UNTIL=20261121T030000Z;BYDAY=FR
SUMMARY:Clase Práctica - Modelos y Sistemas
DESCRIPTION:Clase Práctica de Modelos y Sistemas.\\nDocente: Paula Romina Soria\\nHorario: 20:00 a 22:00 hs.
LOCATION:Aula de Cursada
END:VEVENT
BEGIN:VEVENT
UID:parcial-modelos-sistemas-2026@local
DTSTAMP:20260811T120000Z
DTSTART;TZID=America/Argentina/Buenos_Aires:20261023T180000
DTEND;TZID=America/Argentina/Buenos_Aires:20261023T220000
SUMMARY:Parcial Teórico-Práctico - Modelos y Sistemas
DESCRIPTION:Parcial teórico-práctico de Modelos y Sistemas.\\nNota mínima de aprobación: 5.\\nHorario: 18:00 a 22:00 hs.
LOCATION:Aula de Cursada
END:VEVENT
BEGIN:VEVENT
UID:recuperatorio-modelos-sistemas-2026@local
DTSTAMP:20260811T120000Z
DTSTART;TZID=America/Argentina/Buenos_Aires:20261106T180000
DTEND;TZID=America/Argentina/Buenos_Aires:20261106T220000
SUMMARY:Recuperatorio - Modelos y Sistemas
DESCRIPTION:Examen de recuperación de Modelos y Sistemas.\\nNota mínima de aprobación: 5.\\nHorario: 18:00 a 22:00 hs.
LOCATION:Aula de Cursada
END:VEVENT
BEGIN:VEVENT
UID:entrega-tp-modelos-sistemas-2026@local
DTSTAMP:20260811T120000Z
DTSTART;TZID=America/Argentina/Buenos_Aires:20261113T235900
DTEND;TZID=America/Argentina/Buenos_Aires:20261113T235959
SUMMARY:ENTREGA LÍMITE: Trabajo Práctico Final - Modelos y Sistemas
DESCRIPTION:Fecha límite de entrega de informes TP Final (Grupos de 3 integrantes).\\nNota: En la diapositiva indicaba lunes 17/11 (que es martes), ajustado al viernes anterior 13/11/2026 a las 23:59h.
END:VEVENT
BEGIN:VEVENT
UID:presentaciones-tp-modelos-sistemas-2026@local
DTSTAMP:20260811T120000Z
DTSTART;TZID=America/Argentina/Buenos_Aires:20261120T180000
DTEND;TZID=America/Argentina/Buenos_Aires:20261120T220000
SUMMARY:Presentaciones TP Final - Modelos y Sistemas
DESCRIPTION:Presentaciones de 15 minutos del Trabajo Práctico Final.\\nGrupos de 3 integrantes.\\nHorario: 18:00 a 22:00 hs.
LOCATION:Aula de Cursada
END:VEVENT
END:VCALENDAR
"""

with open("modelos_y_sistemas_2026.ics", "w", encoding="utf-8") as f:
    f.write(ics_content.strip())

print("Clean ICS regenerated.")
