# -*- coding: utf-8 -*-

from edi.datenschutz import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Dsfaview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('dsfaview.pt')

    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'A small message')
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

    def get_ueberpruefung(self):
        datum = self.context.datum
        formatteddatum = datum.strftime("%d.%m.%Y")
        result = "Datumsangabe: "+str(formatteddatum)
        return result
