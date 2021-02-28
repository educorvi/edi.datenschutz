# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from plone import api as ploneapi

class CreateVerarbeitung(BrowserView):
    def __call__(self):
        folderuid = self.request.get('selectFolder')
        container = ploneapi.content.get(UID=folderuid)
        vorlagetitel = self.request.get('vorlagetitel')
        import pdb;pdb.set_trace()
        obj = ploneapi.content.create(
            type='Verarbeitungstaetigkeit',
            title=vorlagetitel,
            description = self.context.description,
            verantwortlicher = self.context.verantwortlicher,
            angaben_zu_verantwortlichen = self.context.angaben_zu_verantwortlichen,
            datenschutzbeauftragter = self.context.datenschutzbeauftragter,
            beteiligte_personen_und_ihre_rollen = self.context.beteiligte_personen_und_ihre_rollen,
            zwecke = self.context.zwecke,
            rechtsgrundlagen_befugnis = self.context.rechtsgrundlagen_befugnis,
            kategorien_daten = self.context.kategorien_daten,
            kategorien_personen = self.context.kategorien_daten,
            loeschfristen = self.context.loeschfristen,
            dienststelle_sachgebiet_abteilung = self.context.dienststelle_sachgebiet_abteilung,
            vorliegen_stellungnahme = self.context.vorliegen_stellungnahme,
            datenschutz_erlaeuterung = self.context.datenschutz_erlaeuterung,
            container=container)
        url = obj.absolute_url() + '/edit'
        return self.request.response.redirect(url)
