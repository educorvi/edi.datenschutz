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
