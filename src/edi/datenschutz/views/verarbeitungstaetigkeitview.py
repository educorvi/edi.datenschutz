# -*- coding: utf-8 -*-

from edi.datenschutz import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Verarbeitungstaetigkeitview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('verarbeitungstaetigkeitview.pt')

    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'A small message')
        return self.index()

    def get_documentid(self):
        id = self.context.dokument_id
        result = "Dokument-ID: "+str(id)
        return result

    def get_beteiligtepersonen(self):
        personen = self.context.beteiligte_personen_und_ihre_rollen
        result = "Nachname, Vorname, Rolle: "+str(personen)
        return result

    def get_status(self):
        status = self.context.status
        result = "Status: "+str(status)
        return result 

    def get_ueberpruefung(self):
        datum = self.context.datumsangabe
        formatteddatum = datum.strftime("%d/%m/%Y")
        result = "Datumsangabe: "+str(formatteddatum)
        return result
