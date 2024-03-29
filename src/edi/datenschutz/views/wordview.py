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

        path = '/'.join(__file__.split('/')[:-1])
        path = path+"/VVT-Vorlage.docx"

        doc = DocxTemplate(path)

        personenlist = list()
        personen = self.context.beteiligte_personen_und_ihre_rollen
        if personen:
            for i in range(len(personen)):
                key='person%s' % str(i+1)
                personenlist.append((key, personen[i]))

        transformer = ITransformer(self.context)
        transformedValue = u''
        if self.context.beschreibung_massnahmen:
            transformedValue = transformer(self.context.beschreibung_massnahmen, 'text/plain')

        anmerkung = self.context.anmerkung_zum_status
        if not anmerkung:
            anmerkung = u''

        begruendung = self.context.begruendung
        if not begruendung:
            begruendung = u''

        erlaeuterung = self.context.datenschutz_erlaeuterung
        if not erlaeuterung:
            erlaeuterung = u''

        aktenzeichen = self.context.aktenzeichen
        if not aktenzeichen:
            aktenzeichen = u''

        datum = self.context.datumsangabe
        if datum:
            datum = datum.strftime('%d.%m.%Y')

        pruefdatum = self.context.pruefung_bis_wann
        if pruefdatum:
            pruefdatum = pruefdatum.strftime('%d.%m.%Y')

        context = {
            'title' : self.context.title,
            'document_id' : self.context.dokument_id,
            'aktenzeichen': aktenzeichen,
            'verantwortlicher': self.context.verantwortlicher,
            'angaben_zu_verantwortlichen': self.context.angaben_zu_verantwortlichen,
            'status': self.context.status,
            'anmerkung_zum_status': anmerkung,
            'datenschutzbeauftragter': self.context.datenschutzbeauftragter,
            'zwecke': self.context.zwecke,
            'rechtsgrundlagen_befugnis': self.context.rechtsgrundlagen_befugnis,
            'dienststelle_sachgebiet_abteilung': self.context.dienststelle_sachgebiet_abteilung,
            'datumsangabe': datum,
            'datenschutz_folgenabschatzung_erforderlich': self.context.datenschutz_folgenabschatzung_erforderlich,
            'pruefung_bis_wann': pruefdatum,
            'begruendung': begruendung,
            'vorliegen_stellungnahme': self.context.vorliegen_stellungnahme,
            'datenschutz_erlaeuterung': erlaeuterung,
            'beschreibung_massnahmen': transformedValue,
        }

        for i in personenlist:
            context[i[0]] = i[1]

        count = 0
        for i in self.context.kategorien_personen:
            key = 'kategorien_personen%s' %count
            context[key] = i['bezeichnung']
            count +=1

        count = 0
        for i in self.context.kategorien_daten:
            key = 'kategorien_daten%s' % count
            context[key] = i['bezeichnung']
            count += 1

        count = 0
        for i in self.context.kategorien_empfaenger:
            key1 = 'kategorien_empfaenger_emp%s' % count
            key2 = 'kategorien_empfaenger_offen%s' % count
            context[key1] = i['bezeichnung']
            context[key2] = i['anmerkung']
            count += 1

        count = 0
        for i in reversed(self.context.internationale_organisationen):
            key1 = 'uebermittlung_drittland%s' % count
            key2 = 'uebermittlung_garantien%s' % count
            context[key1] = i['bezeichnung']
            context[key2] = i['anmerkung']
            count += 1

        count = 0
        for i in self.context.loeschfristen:
            key = 'loeschung%s' % count
            context[key] = i['bezeichnung']
            count += 1

        count = 0
        for i in reversed(self.context.anlagen_beschreibung):
            key1 = 'anlagen_bezeichnung%s' % count
            key2 = 'anlagen_anmerkung%s' % count
            if not i.get('link'):
                context[key1] = i['bezeichnung']
            else:
                context[key1] = "%s (%s)" % (i['bezeichnung'], i['link'])
            context[key2] = i['anmerkung']
            count += 1

        count = 0
        for i in self.context.aenderungen:
            key1 = 'aenderungen_wann%s' % count
            key2 = 'aenderungen_wer%s' % count
            key3 = 'aenderungen_was%s' % count
            context[key1] = i['wann'].strftime("%d.%m.%Y")
            context[key2] = i['wer']
            context[key3] = i['was']
            count += 1

        doc.render(context)

        savepath = '/tmp/changed'
        doc.save(savepath)

        file = open(savepath, 'rb')
        file.seek(0)

        RESPONSE = self.request.response
        RESPONSE.setHeader('content-type', 'application/application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        RESPONSE.setHeader('content-disposition', 'attachment; filename=verarbeitungstaetigkeit.docx')
        return file.read()
