# -*- coding: utf-8 -*-

from edi.datenschutz import _
from Products.Five.browser import BrowserView
from edi.datenschutz.interfaces import ampel

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
        if not dsfa_beteiligte_person:
            todo.append((1, u"An DSFA beteiligte Person(en) und ihre Rolle(n)"))
        if context.status_der_dsfa == u"Sonstiges (Bitte  in Anmerkungen schreiben)" and not context.anmerkung_zum_status:
            todo.append((1, u"Anmerkung zum Status der DSFA"))
        if not context.datum:
            todo.append((4, u"Zeitpunkt der Überprüfung"))
        if not context.welche_verarbeitung_ist_geplant_:
            todo.append((5, u"Geplante Verarbeitung"))
        if not context.welche_zwecke_hat_die_verarbeitung_:
            todo.append((5, u"Zwecke der geplanten Verarbeitung"))
        if not context.welche_rechtsgrundlagen_befugnisse_fur_die_verarbeitung_gibt_es_:
            todo.append((5, u"Rechtsgrundlagen/Befugnisse der Verarbeitung"))
        if not context.wenn_anwendbar__wie_wird_die_einwilligung_der_betroffenen_personen_eingeholt_:
            todo.append((5, u"Einwilligung der betroffenen Personen"))
        if not context.normen_verarbeitung_relevant:
            todo.append((5, u"Normen und Standards"))
        print(todo)
        print(len(todo))
        rest = len(todo)
        erfuellung = (8 - rest) / 8 * 100
        retdict = {'erfuellung': int(erfuellung),
                   'todo': todo}
        return retdict

    def get_status(self):
        statusdict = {
                'in Bearbeitung':'badge badge-primary',
                'Aktiviert':'badge badge-success',
                'Deaktiviert':'badge badge-danger',
                'Sonstiges (Bitte  in Anmerkungen schreiben)':'badge badge-warning'}
        status = self.context.status_der_dsfa
        if self.context.status_der_dsfa == 'Sonstiges (Bitte  in Anmerkungen schreiben)':
            return ('Sonstiges', statusdict.get(self.context.status_der_dsfa))
        else:
            return (self.context.status_der_dsfa, statusdict.get(self.context.status_der_dsfa))

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
        print(formatanlagen)
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
        ziele.append(('Verfügbarkeit', dsfa.verfuegbarkeit, ampel.getTerm(dsfa.verfuegbarkeit).title))
        ziele.append(('Vertraulichkeit', dsfa.vertraulichkeit, ampel.getTerm(dsfa.vertraulichkeit).title))
        ziele.append(('Datenintegrität', dsfa.datenintegritaet, ampel.getTerm(dsfa.datenintegritaet).title))
        ziele.append(('Datenminimierung', dsfa.datenminimierung, ampel.getTerm(dsfa.datenminimierung).title))
        ziele.append(('Intervenierbarkeit', dsfa.intervenierbarkeit, ampel.getTerm(dsfa.intervenierbarkeit).title))
        ziele.append(('Transparenz', dsfa.transparenz, ampel.getTerm(dsfa.transparenz).title))
        ziele.append(('Nichtverkettung', dsfa.nichtverkettung, ampel.getTerm(dsfa.nichtverkettung).title))
        ziele.append(('Konzepteinhaltung', dsfa.konzeptionseinhaltung, ampel.getTerm(dsfa.konzeptionseinhaltung).title))
        ziele.append(('Richtigkeit', dsfa.richtigkeit, ampel.getTerm(dsfa.richtigkeit).title))
        return ziele
