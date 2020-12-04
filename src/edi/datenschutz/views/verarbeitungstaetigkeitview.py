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
        formatteddatum = datum.strftime("%d.%m.%Y")
        result = "Datumsangabe: "+str(formatteddatum)
        return result

    def get_dienststelle(self):
        dienststelle = self.context.dienststelle_sachgebiet_abteilung
        result = "Dienststelle / Sachgebiet / Abteilung: "+str(dienststelle)
        return result

    def get_foldercontents(self):
        return self.context.getFolderContents()


    """
    def get_verfuegbarkeit(dsfa):
        verfuegbarkeit = dsfa[0].verfuegbarkeit
        return verfuegbarkeit

    def get_vertraulichkeit(dsfa):
        vertraulichkeit = dsfa[0].vertraulichkeit
        return vertraulichkeit

    def get_datenintegritaet(dsfa):
        datenintegritaet = dsfa[0].datenintegritaet
        return datenintegritaet

    def get_datenminimierung(dsfa):
        datenminimierung = dsfa[0].datenminimierung
        return datenminimierung

    def get_intervenierbarkeit(dsfa):
        intervenierbarkeit = dsfa[0].intervenierbarkeit
        return intervenierbarkeit

    def get_transparenz(dsfa):
        transparenz = dsfa[0].transparenz
        return transparenz

    def get_nichtverkettung(dsfa):
        nichtverkettung = dsfa[0].nichtverkettung
        return nichtverkettung

    def get_konzeptionseinhaltung(dsfa):
        konzeptionseinhaltung = dsfa[0].konzeptionseinhaltung
        return konzeptionseinhaltung

    def get_richtigkeit(dsfa):
        richtigkeit = dsfa[0].richtigkeit
        return richtigkeit

    """
    def get_zielelist(self):

        dsfa = self.context.listFolderContents(contentFilter={"portal_type": "Datenschutzfolgenabschaetzung"})

        ziele = []
        ziele.append(('Verfügbarkeit:', dsfa[0].verfuegbarkeit))
        ziele.append(('Vertraulichkeit:', dsfa[0].vertraulichkeit))
        ziele.append(('Datenintegrität:', dsfa[0].datenintegritaet))
        ziele.append(('Datenminimierung:', dsfa[0].datenminimierung))
        ziele.append(('Intervenierbarkeit:', dsfa[0].intervenierbarkeit))
        ziele.append(('Transparenz:', dsfa[0].transparenz))
        ziele.append(('Nichtverkettung:', dsfa[0].nichtverkettung))
        ziele.append(('Konzeptionseinhaltung:', dsfa[0].konzeptionseinhaltung))
        ziele.append(('Richtigkeit:', dsfa[0].richtigkeit))


        return ziele
