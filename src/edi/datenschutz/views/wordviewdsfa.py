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
        }

        doc.render(context)

        doc.save("/Users/seppowalther/Dropbox/Arbeit/changeddsfa.docx")
