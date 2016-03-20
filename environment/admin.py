# -*- coding: utf-8 -*-

import urllib
import urllib2

from django.contrib import admin

from environment.models import Estatistica

class EstatisticaAdmin(admin.ModelAdmin):
    list_display = ('local', 'data', 'parametro', 'valor', 'unidade')
    list_filter = ['local', 'parametro']
    search_fields = ['local']
    date_hierarchy = 'data'
    
    def send_to_gae(self, request, queryset):
        ok = 0
        not_ok = 0
#        url = 'http://djctxenv.appspot.com/'
        url = 'http://localhost:8080/'
        for e in queryset.all():
            values = {"local": e.local,
                    "data": e.data,
                    "parametro": e.parametro,
                    "valor": e.valor,
                    "unidade": e.unidade}
            data = urllib.urlencode(valuerpz...s)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            the_page = response.read()
            if response.code==200:
                ok  += 1
            else:
                not_ok += 1
        self.message_user(request, "%s enviados com sucesso. %s falharam." % (ok, not_ok))
    send_to_gae.short_description = "Enviar para aplicação no GAE"
    actions = [send_to_gae]

admin.site.register(Estatistica, EstatisticaAdmin)
