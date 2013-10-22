from django.contrib import admin
from appproyecto.models import usuario, relacionUsuario, calendario, instagram, soundcloud,youtube,album, comentario,meGusta, relacionComentario,relacionNotificacion, notificacion

admin.site.register(usuario)
admin.site.register(relacionUsuario)
admin.site.register(calendario)
admin.site.register(instagram)
admin.site.register(soundcloud)
admin.site.register(youtube)
admin.site.register(album)
admin.site.register(comentario)
admin.site.register(meGusta)
admin.site.register(notificacion)
admin.site.register(relacionNotificacion)
admin.site.register(relacionComentario)

