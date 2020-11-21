# -*- coding: utf-8 -*-

from edi.datenschutz import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Verarbeitungstaetigkeitview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('verarbeitungstaetigkeitview.pt')

    def __call__(self):
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
        statusdict = {
                'in Bearbeitung':'badge badge-primary',
                'Aktiviert':'badge badge-success',
                'Deaktiviert':'badge badge-danger',
                'Sonstiges (Bitte  in Anmerkungen schreiben)':'badge badge-warning'}
        status = self.context.status
        if self.context.status == 'Sonstiges (Bitte  in Anmerkungen schreiben)':
            return ('Sonstiges', statusdict.get(self.context.status))
        else:
            return (self.context.status, statusdict.get(self.context.status))

    def get_ueberpruefung(self):
        datum = self.context.datumsangabe
        formatteddatum = datum.strftime("%d/%m/%Y")
        result = "Datumsangabe: "+str(formatteddatum)
        return result

    def get_dienststelle(self):
        dienststelle = self.context.dienststelle_sachgebiet_abteilung
        result = "Dienststelle / Sachgebiet / Abteilung: "+str(dienststelle)
        return result

    def get_foldercontents(self):
        return self.context.getFolderContents()
