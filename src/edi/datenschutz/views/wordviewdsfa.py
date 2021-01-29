# -*- coding: utf-8 -*-

from edi.datenschutz import _
from Products.Five.browser import BrowserView
from plone.app.textfield.interfaces import ITransformer


from docxtpl import DocxTemplate

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Wordviewdsfa(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('wordviewdsfa.pt')

    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'A small message')

        doc = DocxTemplate("/Users/seppowalther/Dropbox/Arbeit/DSFA-Bericht-Vorlage.docx")

        context = {
            'dokument_id': self.context.dokument_id,
            'status': self.context.status_der_dsfa,
            'anmerkung_zum_status': self.context.anmerkung_zum_status,
            'kontaktdaten_datenschutzbeauftragter': self.context.kontaktdaten_datenschutzbeauftragter,
            'datumsangabe': self.context.datum,
            'dsfa_geplante_verarbeitung': self.context.dsfa_geplante_verarbeitung,
            'dsfa_zwecke_der_verarbeitung': self.context.dsfa_zwecke_der_verarbeitung,
            'dsfa_rechtsgrundlagen_der_verarbeitung': self.context.dsfa_rechtsgrundlagen_der_verarbeitung,
            'dsfa_einwilligung_der_betroffenen': self.context.dsfa_einwilligung_der_betroffenen,
            'normen_verarbeitung_relevant': self.context.normen_verarbeitung_relevant,
            'zustandigkeiten_fur_verarbeitung': self.context.zustandigkeiten_fur_verarbeitung,
            'verpflichtungen_der_auftragsverarbeiter': self.context.verpflichtungen_der_auftragsverarbeiter,
            'standpunkt_der_betroffenen_personen': self.context.standpunkt_der_betroffenen_personen,
            'anmerkung_begrundung': self.context.anmerkung_begrundung,
            'lebenszyklus_daten_prozesse': self.context.lebenszyklus_daten_prozesse,
            'betriebsmittel_fuer_datenverarbeitung': self.context.betriebsmittel_fuer_datenverarbeitung,
            'verarbeitung_verhaltnismassig': self.context.verarbeitung_verhaltnismassig,
            'warum_daten_erforderlich': self.context.warum_daten_erforderlich,
            'daten_auf_dem_neuesten_stand': self.context.daten_auf_dem_neuesten_stand,
            'speicherdauer_der_daten': self.context.speicherdauer_der_daten,
            'information_betroffener_personen': self.context.information_betroffener_personen,
            'recht_auf_auskunft_betroffener': self.context.recht_auf_auskunft_betroffener,
            'recht_auf_loschung': self.context.recht_auf_loschung,
            'recht_auf_berichtigung': self.context.recht_auf_berichtigung,
            'recht_auf_widerspruch': self.context.recht_auf_widerspruch,
            'recht_auf_datenubertragbarkeit': self.context.recht_auf_datenubertragbarkeit,
            'erfullung_datensicherheitsziele': self.context.erfullung_datensicherheitsziele,
            'erfullung_schutzbedarfsziele': self.context.erfullung_schutzbedarfsziele,
            'konsultation_aufsichtsbehorde': self.context.konsultation_aufsichtsbehorde,
            'begrundung': self.context.begrundung,
            'beschreibung_der_abstimmung': self.context.beschreibung_der_abstimmung,
            'dsfa_datenschutzmassnahmen': self.context.dsfa_datenschutzmassnahmen,
        }

        count = 0
        for i in reversed(self.context.dsfa_beteiligte_person):
            key = 'person%s' % count
            context[key] = i
            count += 1

        count = 0
        for i in reversed(self.context.anlagen_beschreibung):
            key1 = 'anlagen_bezeichnung%s' % count
            key2 = 'anlagen_anmerkung%s' % count
            context[key1] = i['bezeichnung']
            context[key2] = i['anmerkung']
            count += 1

        count = 0
        for i in reversed(self.context.aenderungen):
            key1 = 'aenderungen_wann%s' % count
            key2 = 'aenderungen_wer%s' % count
            key3 = 'aenderungen_was%s' % count
            context[key1] = i['wann'].strftime("%d/%m/%Y")
            context[key2] = i['wer']
            context[key3] = i['was']
            count += 1

        count = 0
        for i in reversed(self.context.kategorien_personenbezogener_daten):
            key1 = 'kategorie_bezeichnung%s' % count
            key2 = 'kategorie_anmerkung%s' % count
            context[key1] = i['bezeichnung']
            context[key2] = i['anmerkung']
            count += 1

        count = 0
        for i in reversed(self.context.kategorien_betroffener_personen):
            key1 = 'kategorie_personen%s' % count
            key2 = 'kategorie_personen_anmerkung%s' % count
            context[key1] = i['bezeichnung']
            context[key2] = i['anmerkung']
            count += 1

        count = 0
        for i in reversed(self.context.empfaenger_fuer_offenlegung):
            key1 = 'empfaenger%s' % count
            key2 = 'empfaenger_anlass%s' % count
            key3 = 'empfaenger_anmerkung%s' % count
            context[key1] = i['empfaenger']
            context[key2] = i['anlass']
            context[key3] = i['anmerkung']
            count += 1

        doc.render(context)

        doc.save("/Users/seppowalther/Dropbox/Arbeit/changeddsfa.docx")
