# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from plone import api as ploneapi

class CreateDsfa(BrowserView):
    def __call__(self):
        folderuid = self.request.get('selectFolder')
        container = ploneapi.content.get(UID=folderuid)
        vorlagetitel = self.request.get('vorlagetitel')
        obj = ploneapi.content.create(
            type='Datenschutzfolgenabschaetzung',
            title=vorlagetitel,
            description = self.context.description,
            dsfa_beteiligte_person = self.context.dsfa_beteiligte_person,
            kontaktdaten_datenschutzbeauftragter = self.context.kontaktdaten_datenschutzbeauftragter,
            dsfa_zwecke_der_verarbeitung = self.context.dsfa_zwecke_der_verarbeitung,
            dsfa_rechtsgrundlagen_der_verarbeitung = self.context.dsfa_rechtsgrundlagen_der_verarbeitung,
            dsfa_einwilligung_der_betroffenen = self.context.dsfa_einwilligung_der_betroffenen,
            normen_verarbeitung_relevant = self.context.normen_verarbeitung_relevant,
            zustandigkeiten_fur_verarbeitung = self.context.zustandigkeiten_fur_verarbeitung,
            verpflichtungen_der_auftragsverarbeiter = self.context.verpflichtungen_der_auftragsverarbeiter,
            kategorien_personenbezogener_daten = self.context.kategorien_personenbezogener_daten,
            kategorien_betroffener_personen = self.context.kategorien_betroffener_personen,
            empfaenger_fuer_offenlegung = self.context.empfaenger_fuer_offenlegung,
            lebenszyklus_daten_prozesse = self.context.lebenszyklus_daten_prozesse,
            betriebsmittel_fuer_datenverarbeitung = self.context.betriebsmittel_fuer_datenverarbeitung,
            information_betroffener_personen = self.context.information_betroffener_personen,
            recht_auf_auskunft_betroffener = self.context.recht_auf_auskunft_betroffener,
            recht_auf_loschung = self.context.recht_auf_loschung,
            recht_auf_berichtigung = self.context.recht_auf_berichtigung,
            recht_auf_widerspruch = self.context.recht_auf_widerspruch,
            recht_auf_datenubertragbarkeit = self.context.recht_auf_datenubertragbarkeit,
            konsultation_aufsichtsbehorde = self.context.konsultation_aufsichtsbehorde,
            begrundung = self.context.begrundung,
            beschreibung_der_abstimmung = self.context.beschreibung_der_abstimmung,
            container=container)
        url = obj.absolute_url() + '/edit'
        return self.request.response.redirect(url)
