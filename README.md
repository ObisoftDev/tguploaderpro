# tguploaderpro
Bot De Telegram : TGUploaderPro v7.0 Fixed , Descargador gratis de contenido desde internet a hacia moodles , nexcloud en cuba

# Deploy Usando Git Win Y Heroku Cli Desde PC
```
(CMD)
git clone https://github.com/ObisoftDev/tguploaderpro 
git init
git add .
git commit -m "OK"
heroku create myherokuapp
heroku git:remote myherokuapp
git push heroku master
```

# Comandos En El Bot (Usuarios Nomales)
```/start : Inicar Bot , Te Da La INfo
/tutorial : Te Da un tutorial basico de uso del bot q puedes echarle un ojo
/myuser : Obtiene la informacion del usuario q esta usando el bot
/zips : Configura el tamano de las partes comprimidas 7z
/account: COnfigura su cuenta de nube en el bot
/host : Configura el Host Al Cual ba a subir los archivos el bot x ejemplo https://moodle.uclv.edu.cu/ (Moodle o Nexcloud)
/repoid : EN EL caso de las moodles cada nube tiene su repoid q hay q saber extraerlo y configurarsel al bot para poder subir
/cloud : Alterna El tipo de subida a nubes ya sea cloud o moodle , en caso de cloud es nexcloud pero para simplificar se pone cloud
/tokenize_on : Enciende el modo tokenize , se recomienda no usar a no se q disponga de una de las apps oficiales de descarga del bot 
/tokenize_off : Apaga el modo tokenize
/uptype : Configure el modo de subir de moodle ya sea draft , evidence , blog y calendario
/proxy : Configura UN Proxy Para Las Subidas Del Bot , contactar en telegram a @obisoftdevel para contratar uno
/files : En caso de tener activa el uptype (evidence) este comando le da una lista de archivo q se encuentra en las evidencias de la nube
/delall : En caso de tener activa el uptype (evidence) este comando borra todos los archivos en la lista de evidencia de la nube
/dir : En caso de tener activo cloud configure el directorio base en la nexcloud donde se va a subir los archivos
```

# Comandos En El Bot (Administrador) 
```/adduser : permite un usuario de telegram tener acceso al bot
/banuser : quita acceso al bot de un usuario de telegram
/getdb : Obten la base de datos donde se almacenan la info de los usarios en el bot
```
# Deploy Directo (Heroku)
[![Heroku Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ObisoftDev/tguploaderpro)
