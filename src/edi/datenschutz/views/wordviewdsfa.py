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
        import pdb; pdb.set_trace()

        doc = DocxTemplate("/Users/seppowalther/Dropbox/Arbeit/DSFA-Bericht-Vorlage.docx")

        import pdb; pdb.set_trace()

        context = {
            'document_id': self.context.dokument_id,
            'status': self.context.status_der_dsfa,
            'anmerkung_zum_status': self.context.anmerkung_zum_status,
            'datumsangabe': self.context.datum,
            
        }

        count = 0
        for i in reversed(self.context.dsfa_beteiligte_person):
            key = 'person%s' % count
            context[key] = i['bezeichnung']
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

        doc.render(context)

        doc.save("/Users/seppowalther/Dropbox/Arbeit/changeddsfa.docx")
