# -*- coding: utf-8 -*-

from edi.datenschutz import _
from Products.Five.browser import BrowserView
from plone import api as ploneapi
from edi.datenschutz.interfaces import ampel

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Verarbeitungstaetigkeitview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('verarbeitungstaetigkeitview.pt')

    def __call__(self):
        self.msg = _(u'A small message')
        return self.index()

    def get_todo(self):
        context = self.context
        todo = []
        if not context.beteiligte_personen_und_ihre_rollen:
            todo.append((1, u"Beteiligte Person(en) und ihre Rolle(n)"))
        if context.status == u"Sonstiges (Bitte  in Anmerkungen schreiben)" and not context.anmerkung_zum_status:
            todo.append((1, u"Anmerkung zum Status"))
        if not context.datumsangabe:
            todo.append((4, u"Zeitpunkt der Überprüfung"))
        if not context.zwecke or not context.rechtsgrundlagen_befugnis:
            todo.append((5, u"Zwecke und Rechtsgrundlagen der Verarbeitung"))
        if not context.kategorien_daten:
            todo.append((6, u"Kategorien der personenbezogenen Daten"))
        if not context.kategorien_personen:
            todo.append((7, u"Kategorien der personenbezogenen Personen"))
        if not context.kategorien_empfaenger:
            todo.append((8, u"Kategorien der Empfänger"))
        if not context.loeschfristen:
            todo.append((10, u"Fristen für die Löschung"))
        if not context.beschreibung_massnahmen:
            todo.append((11, u"Technische und Organisatorische Maßnahmen"))
        if not context.dienststelle_sachgebiet_abteilung:
            todo.append((12, u"Verantwortliche Organisationseinheit"))
        if not context.vorliegen_stellungnahme:
            todo.append((13, u"Stellungnahme des Datenschutzbeauftragten"))
        print(todo)
        print(len(todo))
        rest = len(todo)
        erfuellung = (11 - rest) / 11 * 100
        retdict = {'erfuellung': int(erfuellung),
                   'todo': todo}
        return retdict

    def get_documentid(self):
        docid = self.context.dokument_id
        result = "<p><strong>Dokument-ID:</strong> %s</p>" % docid
        return result

    def get_aktenzeichen(self):
        akz = self.context.aktenzeichen
        result = "<p><strong>Aktenzeichen:</strong> %s</p>" % akz
        return result

    def get_stand(self):
        stand = self.context.stand
        result = "<p><strong>Stand:</strong> %s</p>" % stand
        return result

    def get_beteiligtepersonen(self):
        personen = self.context.beteiligte_personen_und_ihre_rollen
        result = "Nachname, Vorname, Rolle: "+str(personen)
        return result

    def get_datenschutzfolgenabschaetzung(self):
        dsfa_ja = u'Datenschutz-Folgenabschätzung nach Art. 35 DSGVO <span class="badge badge-danger">ja</span>'
        dsfa_nein = u'Datenschutz-Folgenabschätzung nach Art. 35 DSGVO: <span class="badge badge-success">nein</span>'
        if self.context.datenschutz_folgenabschatzung_erforderlich == 'Ja':
            return '<h3 class="mt-3">%s</h3>' % dsfa_ja
        else:
            return '<h3 class="mt-3">%s</h3>' % dsfa_nein

    def get_pruefung_bis_wann(self):
        if self.context.pruefung_bis_wann:
            return self.context.pruefung_bis_wann.strftime('%d.%m.%Y')
        return u''

    def get_status(self):
        statusdict = {'in Bearbeitung': 'primary',
                      'Aktiviert': 'success',
                      'Deaktiviert': 'danger',
                      'Sonstiges (Bitte  in Anmerkungen schreiben)': 'warning'
                      }
        status = self.context.status
        statusclass = statusdict.get(status)
        if status == 'Sonstiges (Bitte  in Anmerkungen schreiben)':
            ret = ('Sonstiges', statusclass)
        else:
            ret = (status, statusclass)
        return ret

    def get_ueberpruefung(self):
        result = u'Es wurde noch kein Datum für die nächste routinemäßige Überprüfung festgelegt.'
        datum = self.context.datumsangabe
        if datum:
            result = datum.strftime("%d.%m.%Y")
        return result

    def get_dienststelle(self):
        dienststelle = self.context.dienststelle_sachgebiet_abteilung
        result = "Dienststelle / Sachgebiet / Abteilung: "+str(dienststelle)
        return result

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

    def is_redakteur(self):
        if ploneapi.user.is_anonymous():
            return False
        user = ploneapi.user.get_current()
        if ploneapi.user.has_permission("Add portal content", user=user, obj=self.context):
            return True
        return False

    def get_foldercontents(self):
        dsfatypes = [(u'Datenschutzfolgenabschaetzung',
                      u'DSFA'),
                     (u'Massnahmenkatalog',
                      u'Maßnahmenkatalog'),
                     (u'Risikomanagement',
                      u'Risikomanagement')]
        types = [(u'Massnahmenkatalog', u'Maßnahmenkatalog')]
        contents = []
        if self.context.datenschutz_folgenabschatzung_erforderlich == 'Ja':
            for i in dsfatypes:
                entry = dict()
                entry['title'] = i[1]
                content = self.context.listFolderContents(contentFilter={"portal_type": i[0]})
                if content:
                    obj = content[0]
                    entry['link'] = obj.absolute_url()
                    entry['add'] = False
                else:
                    if self.is_redakteur:
                        entry['link'] = self.context.absolute_url()+'/++add++%s' % i[0]
                    else:
                        entry['link'] = '#'
                    entry['add'] = True    
                contents.append(entry)
        else:
            for i in types:
                entry = dict()
                entry['title'] = i[1]
                content = self.context.listFolderContents(contentFilter={"portal_type": i[0]})
                if content:
                    obj = content[0]
                    entry['link'] = obj.absolute_url()
                    entry['add'] = False
                else:
                    if self.is_redakteur:
                        entry['link'] = self.context.absolute_url()+'/++add++%s' % i[0]
                    else:
                        entry['link'] = '#'
                    entry['add'] = True    
                contents.append(entry)
        return contents

    def get_zielelist(self):
        dsfa = self.context.listFolderContents(contentFilter={"portal_type": "Datenschutzfolgenabschaetzung"})
        ziele = []
        if dsfa:
            ziele.append(('Verfügbarkeit', dsfa[0].verfuegbarkeit, ampel.getTerm(dsfa[0].verfuegbarkeit).title))
            ziele.append(('Vertraulichkeit', dsfa[0].vertraulichkeit, ampel.getTerm(dsfa[0].vertraulichkeit).title))
            ziele.append(('Datenintegrität', dsfa[0].datenintegritaet, ampel.getTerm(dsfa[0].datenintegritaet).title))
            ziele.append(('Datenminimierung', dsfa[0].datenminimierung, ampel.getTerm(dsfa[0].datenminimierung).title))
            ziele.append(('Intervenierbarkeit', dsfa[0].intervenierbarkeit, ampel.getTerm(dsfa[0].intervenierbarkeit).title))
            ziele.append(('Transparenz', dsfa[0].transparenz, ampel.getTerm(dsfa[0].transparenz).title))
            ziele.append(('Nichtverkettung', dsfa[0].nichtverkettung, ampel.getTerm(dsfa[0].nichtverkettung).title))
            ziele.append(('Konzepteinhaltung', dsfa[0].konzeptionseinhaltung, ampel.getTerm(dsfa[0].konzeptionseinhaltung).title))
            ziele.append(('Richtigkeit', dsfa[0].richtigkeit, ampel.getTerm(dsfa[0].richtigkeit).title))
        return ziele
