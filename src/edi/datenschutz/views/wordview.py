# -*- coding: utf-8 -*-

from edi.datenschutz import _
from Products.Five.browser import BrowserView
from plone.app.textfield.interfaces import ITransformer


from docxtpl import DocxTemplate

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Wordview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('wordview.pt')

    def __call__(self):

        # Implement your own actions:

        #import pdb; pdb.set_trace()

        doc = DocxTemplate("/Users/seppowalther/Dropbox/Arbeit/VVT-Vorlage.docx")

        personen = self.context.beteiligte_personen_und_ihre_rollen

        transformer = ITransformer(self.context)
        transformedValue = transformer(self.context.beschreibung_massnahmen, 'text/plain')

        """

        if len(self.context.kategorien_daten) >= 1:
            kategorien_daten0 = self.context.kategorien_daten[(len(self.context.kategorien_daten)) - 1][
                                        'bezeichnung']
        else:
            kategorien_daten0 = ""

        if len(self.context.kategorien_daten) >= 2:
            kategorien_daten1 = self.context.kategorien_daten[(len(self.context.kategorien_daten)) - 2][
                                        'bezeichnung']
        else:
            kategorien_daten1 = ""

        if len(self.context.kategorien_daten) >= 3:
            kategorien_daten2 = self.context.kategorien_daten[(len(self.context.kategorien_daten)) - 3][
                                        'bezeichnung']
        else:
            kategorien_daten2 = ""

        if len(self.context.kategorien_daten) >= 4:
            kategorien_daten3 = self.context.kategorien_daten[(len(self.context.kategorien_daten)) - 4][
                                        'bezeichnung']
        else:
            kategorien_daten3 = ""

        if len(self.context.kategorien_daten) >= 5:
            kategorien_daten4 = self.context.kategorien_daten[(len(self.context.kategorien_daten)) - 5][
                                        'bezeichnung']
        else:
            kategorien_daten4 = ""

        """

        context = {
            'document_id' : self.context.dokument_id,
            'aktenzeichen': self.context.aktenzeichen,
            'verantwortlicher': self.context.verantwortlicher,
            'angaben_zu_verantwortlichen': self.context.angaben_zu_verantwortlichen,
            'status': self.context.status,
            'anmerkung_zum_status': self.context.anmerkung_zum_status,
            'datenschutzbeauftragter': self.context.datenschutzbeauftragter,
            'zwecke': self.context.zwecke,
            'rechtsgrundlagen_befugnis': self.context.rechtsgrundlagen_befugnis,
            'person1': personen[0],
            'person2': personen[1],
            'person3': personen[2],
            'person4': personen[3],
            'person5': personen[4],
            'beschreibung_massnahmen': self.context.beschreibung_massnahmen.output,
            'dienststelle_sachgebiet_abteilung': self.context.dienststelle_sachgebiet_abteilung,
            'datumsangabe': self.context.datumsangabe,
            'datenschutz_folgenabschatzung_erforderlich': self.context.datenschutz_folgenabschatzung_erforderlich,
            'pruefung_bis_wann': self.context.pruefung_bis_wann,
            'begruendung': self.context.begruendung,
            'vorliegen_stellungnahme': self.context.vorliegen_stellungnahme,
            'datenschutz_erlaeuterung': self.context.datenschutz_erlaeuterung,
            'beschreibung_massnahmen': transformedValue,

        }

        count = 0
        for i in reversed(self.context.kategorien_personen):
            key = 'kategorien_personen%s' %count
            context[key] = i['bezeichnung']
            count +=1

        count = 0
        for i in reversed(self.context.kategorien_daten):
            key = 'kategorien_daten%s' % count
            context[key] = i['bezeichnung']
            count += 1


        doc.render(context)

        doc.save("/Users/seppowalther/Dropbox/Arbeit/changed.docx")

        self.msg = _(u'A small message')
        return self.index()
