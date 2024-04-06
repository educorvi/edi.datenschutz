# -*- coding: utf-8 -*-

from edi.datenschutz import _
from Products.Five.browser import BrowserView
from edi.datenschutz.interfaces import ampel
from edi.datenschutz.helpers import check_value

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class Dsfaview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('dsfaview.pt')

    def __call__(self):
        return self.index()

    def get_todo(self):
        context = self.context
        todo = []
        if not context.dsfa_beteiligte_person:
            todo.append((1, u"An DSFA beteiligte Person(en) und ihre Rolle(n)"))
        if context.status_der_dsfa == u"Sonstiges (Bitte  in Anmerkungen schreiben)" and not context.anmerkung_zum_status:
            todo.append((1, u"Anmerkung zum Status der DSFA"))
        if not context.datum:
            todo.append((4, u"Zeitpunkt der Überprüfung"))
        if not context.dsfa_geplante_verarbeitung:
            todo.append((5, u"Geplante Verarbeitung"))
        if not context.dsfa_zwecke_der_verarbeitung:
            todo.append((5, u"Zwecke der geplanten Verarbeitung"))
        if not context.dsfa_rechtsgrundlagen_der_verarbeitung:
            todo.append((5, u"Rechtsgrundlagen der Verarbeitung"))
        if not context.dsfa_einwilligung_der_betroffenen:
            todo.append((5, u"Einwilligung betroffenener Personen"))
        if not context.normen_verarbeitung_relevant:
            todo.append((5, u"Normen und Standards"))
        if not context.zustandigkeiten_fur_verarbeitung:
            todo.append((5, u"Zuständigkeiten für Verarbeitung"))
        if not context.verpflichtungen_der_auftragsverarbeiter:
            todo.append((5, u"Verpflichtungen Auftragsverarbeiter"))
        if not context.standpunkt_der_betroffenen_personen:
            todo.append((5, u"Standpunkt betroffene Personen"))
        if not context.kategorien_personenbezogener_daten:
            todo.append((6, u"Kategorien von Daten"))
        if not context.kategorien_betroffener_personen:
            todo.append((6, "Kategorien betroffner Personen"))
        if not context.empfaenger_fuer_offenlegung:
            todo.append((6, u"Empfänger offengeleter Daten"))
        if not context.lebenszyklus_daten_prozesse:
            todo.append((6, u"Lebenszyklus Daten und Prozesse"))
        if not context.betriebsmittel_fuer_datenverarbeitung:
            todo.append((7, u"Betriebsmittel Datenverarbeitung"))
        if not context.verarbeitung_verhaltnismassig:
            todo.append((7, u"Verhältnismäßigkeit der Verarbeitung" ))
        if not context.warum_daten_erforderlich:
            todo.append((7, u"Erfordernis der Daten"))
        if not context.daten_auf_dem_neuesten_stand:
            todo.append((7, u"Aktualität der Daten"))
        if not context.speicherdauer_der_daten:
            todo.append((7, u"Speicherdauer der Daten"))
        if not context.information_betroffener_personen:
            todo.append((8, u"Information betroffener Personen"))
        if not context.recht_auf_auskunft_betroffener:
            todo.append((8, u"Möglichkeiten für Auskunft"))
        if not context.recht_auf_loschung:
            todo.append((8, u"Recht auf Löschung"))
        if not context.recht_auf_berichtigung:
            todo.append((8, u"Recht auf Berichtigung"))
        if not context.recht_auf_widerspruch:
            todo.append((8, u"Recht auf Widerspruch"))
        if not context.recht_auf_datenubertragbarkeit:
            todo.append((8, u"Recht auf Übertragbarkeit"))
        if not context.erfullung_datensicherheitsziele:
            todo.append((9, u"Erfüllung Datensicherheitsziele"))
        if not context.erfullung_schutzbedarfsziele:
            todo.append((10, u"Erfüllung Schutzbedarfsziele"))
        if not context.konsultation_aufsichtsbehorde:
            todo.append((12, u"Konsultation Aufsichtsbehörde"))
        if not context.dsfa_datenschutzmassnahmen:
            todo.append((13, u"Datenschutzmaßnahmen"))

        rest = len(todo)
        erfuellung = (30 - rest) / 30 * 100
        retdict = {'erfuellung': int(erfuellung),
                   'todo': todo}
        return retdict

    def get_status(self):
        statusdict = {
                'in Bearbeitung':'primary',
                'Aktiviert':'success',
                'Deaktiviert':'danger',
                'Sonstiges (Bitte  in Anmerkungen schreiben)':'warning'}
        status = self.context.status_der_dsfa
        statusclass = statusdict.get(status)
        if self.context.status_der_dsfa == 'Sonstiges (Bitte  in Anmerkungen schreiben)':
            return ('Sonstiges', statusclass)
        else:
            return (self.context.status_der_dsfa, statusclass)

    def get_anlagen(self):
        anlagen = self.context.listFolderContents(contentFilter={"portal_type": "File"})
        counter = 1
        formatanlagen = []
        for i in anlagen:
            entry = dict()
            entry['nr'] = counter
            entry['title'] = i.title
            entry['link'] = i.absolute_url()
            entry['anmerkung'] = i.description
            formatanlagen.append(entry)
            counter += 1
        return formatanlagen

    def get_ueberpruefung(self):
        result = u'Es wurde noch kein Datum für die nächste routinemäßige Überprüfung festgelegt.'
        datum = self.context.datum
        if datum:
            result = datum.strftime("%d.%m.%Y")
        return result

    def get_zielelist(self):
        dsfa = self.context
        ziele = list()
        ziele.append(('Verfügbarkeit', dsfa.verfuegbarkeit, ampel.getTerm(check_value(dsfa.verfuegbarkeit)).title))
        ziele.append(('Vertraulichkeit', dsfa.vertraulichkeit, ampel.getTerm(check_value(dsfa.vertraulichkeit)).title))
        ziele.append(('Datenintegrität', dsfa.datenintegritaet, ampel.getTerm(check_value(dsfa.datenintegritaet)).title))
        ziele.append(('Datenminimierung', dsfa.datenminimierung, ampel.getTerm(check_value(dsfa.datenminimierung)).title))
        ziele.append(('Intervenierbarkeit', dsfa.intervenierbarkeit, ampel.getTerm(check_value(dsfa.intervenierbarkeit)).title))
        ziele.append(('Transparenz', dsfa.transparenz, ampel.getTerm(check_value(dsfa.transparenz)).title))
        ziele.append(('Nichtverkettung', dsfa.nichtverkettung, ampel.getTerm(check_value(dsfa.nichtverkettung)).title))
        ziele.append(('Konzepteinhaltung', dsfa.konzeptionseinhaltung, ampel.getTerm(check_value(dsfa.konzeptionseinhaltung)).title))
        ziele.append(('Richtigkeit', dsfa.richtigkeit, ampel.getTerm(check_value(dsfa.richtigkeit)).title))
        return ziele
