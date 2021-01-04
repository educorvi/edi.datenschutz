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
        todo = []
        if not self.context.beteiligte_personen_und_ihre_rollen:
            todo.append((1, u"Beteiligte Person(en) und ihre Rolle(n)"))
        if self.context.status == u"Sonstiges (Bitte  in Anmerkungen schreiben)" and not self.context.anmerkung_zum_status:
            todo.append((1, u"Anmerkung zum Status"))
        if not self.context.datumsangabe:
            todo.append((4, u"Zeitpunkt der Überprüfung"))
        if not self.context.zwecke or not self.context.rechtsgrundlagen_befugnis:
            todo.append((5, u"Zwecke und Rechtsgrundlagen der Verarbeitung"))
        if not self.context.kategorien_daten:
            todo.append((6, u"Kategorien der personenbezogenen Daten"))
        if not self.context.kategorien_personen:
            todo.append((7, u"Kategorien der personenbezogenen Personen"))
        if not self.context.kategorien_empfaenger:
            todo.append((8, u"Kategorien der Empfänger"))
        if not self.context.loeschfristen:
            todo.append((10, u"Fristen für die Löschung"))
        if not self.context.beschreibung_massnahmen:
            todo.append((11, u"Technische und Organisatorische Maßnahmen"))
        if not self.context.dienststelle_sachgebiet_abteilung:
            todo.append((12, u"Verantwortliche Organisationseinheit"))
        if not self.context.vorliegen_stellungnahme:
            todo.append((13, u"Stellungnahme des Datenschutzbeauftragten"))
        print(todo)
        print(len(todo))
        rest = len(todo)
        erfuellung = (11 - rest) / 11 * 100
        retdict = {'erfuellung':int(erfuellung),
                   'todo':todo}
        return retdict   

    def get_documentid(self):
        id = self.context.dokument_id
        result = "<p><strong>Dokument-ID:</strong> %s</p>" % id
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
        if self.context.datenschutz_folgenabschatzung_erforderlich == 'Ja':
            return '<h3 class="mt-3">Datenschutz-Folgenabschätzung nach Art. 35 DSGVO <span class="badge badge-danger">ja</span></h3>'
        else:
            return '<h3 class="mt-3">Datenschutz-Folgenabschätzung nach Art. 35 DSGVO <span class="badge badge-success">nein</span></h3>'

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
        result = u''
        datum = self.context.datumsangabe
        if datum:
            formatteddatum = datum.strftime("%d.%m.%Y")
            result = "Datumsangabe: "+str(formatteddatum)
        return result

    def get_dienststelle(self):
        dienststelle = self.context.dienststelle_sachgebiet_abteilung
        result = "Dienststelle / Sachgebiet / Abteilung: "+str(dienststelle)
        return result

    def get_anlagen(self):
        anlagen = self.context.listFolderContents(contentFilter={"portal_type" : "File"})
        counter = 1
        formatanlagen = []
        for i in anlagen:
            entry = {}
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
                entry = {}
                entry['title'] = i[1]
                content = self.context.listFolderContents(contentFilter={"portal_type": i[0]})
                if content:
                    obj = content[0]
                    entry['link'] = obj.absolute_url()
                else:
                    if self.is_redakteur:
                        entry['link'] = self.context.absolute_url()+'/++add++%s' % i[0]
                    else:
                        entry['link'] = '#'
                contents.append(entry)
        else:
            for i in types:
                entry = {}
                entry['title'] = i[1]
                content = self.context.listFolderContents(contentFilter={"portal_type": i[0]})
                if content:
                    obj = content[0]
                    entry['link'] = obj.absolute_url()
                else:
                    if self.is_redakteur:
                        entry['link'] = self.context.absolute_url()+'/++add++%s' % i[0]
                    else:
                        entry['link'] = '#'
                contents.append(entry)
        return contents

    def get_zielelist(self):
        dsfa = self.context.listFolderContents(contentFilter={"portal_type": "Datenschutzfolgenabschaetzung"})
        ziele = []
        if dsfa:
            ziele.append(('Verfügbarkeit:', dsfa[0].verfuegbarkeit, ampel.getTerm(dsfa[0].verfuegbarkeit).title))
            ziele.append(('Vertraulichkeit:', dsfa[0].vertraulichkeit, ampel.getTerm(dsfa[0].vertraulichkeit).title))
            ziele.append(('Datenintegrität:', dsfa[0].datenintegritaet, ampel.getTerm(dsfa[0].datenintegritaet).title))
            ziele.append(('Datenminimierung:', dsfa[0].datenminimierung, ampel.getTerm(dsfa[0].datenminimierung).title))
            ziele.append(('Intervenierbarkeit:', dsfa[0].intervenierbarkeit, ampel.getTerm(dsfa[0].intervenierbarkeit).title))
            ziele.append(('Transparenz:', dsfa[0].transparenz, ampel.getTerm(dsfa[0].transparenz).title))
            ziele.append(('Nichtverkettung:', dsfa[0].nichtverkettung, ampel.getTerm(dsfa[0].nichtverkettung).title))
            ziele.append(('Konzepteinhaltung:', dsfa[0].konzeptionseinhaltung, ampel.getTerm(dsfa[0].konzeptionseinhaltung).title))
            ziele.append(('Richtigkeit:', dsfa[0].richtigkeit, ampel.getTerm(dsfa[0].richtigkeit).title))
        return ziele
