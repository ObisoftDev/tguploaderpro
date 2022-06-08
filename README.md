# TG-Uploader X

Sube archivos a Nextcloud y Moodles directamente desde Telegram.

- `1` - En Telegram inicia el bot [@BotFather](https://t.me/BotFather), crea un bot y copia el token.
- `2` - En el código abrir el archivo [main.py](/main.py).
- `3` - En la linea 243 rellenar (tl_admin_user = 'usuario de telegram sin el @').

## Desplegar en Heroku

[![Deploy on Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Comandos
Agregar en [@BotFather](https://t.me/BotFather)

    start - iniciar bot, te da la info.
    myuser - obtiene la información del usuario que está usando el bot.
    account - configura su cuenta de nube en el bot.
    host - configura el host al cuál va a subir los archivos el bot.
    repoid - en el caso de las moodles cada nube tiene su repoid que hay que saber extraerlo y configurarselo al bot para poder subir.
    cloud - alterna el tipo de subida a nubes ya sea cloud o moodle, en caso de cloud es nexcloud pero para simplificar se pone cloud.
    uptype - configure el modo de subir al moodle ya sea draft, evidence, blog o calendar.
    zips - configura el tamaño de las partes comprimidas 7z.
    proxy - configura un proxy para las subidas del bot.
    files - en caso de tener activo el uptype (evidence) este comando le da una lista de archivos que se encuentran en las evidencias de la nube.
    delall - en caso de tener activo el uptype (evidence) este comando borra todos los archivos en la lista de evidencia de la nube.
    dir - en caso de tener activo cloud configure el directorio base en la nexcloud donde se van a subir los archivos.
    adduser - permite un usuario de telegram tener acceso al bot.
    banuser - quita acceso al bot a un usuario de telegram.
    getdb - obtén la base de datos donde se almacenan la info de los usarios del bot.
    version - muestra la versión actual.