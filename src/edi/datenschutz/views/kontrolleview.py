# -*- coding: utf-8 -*-

from edi.datenschutz import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Kontrolleview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('kontrolleview.pt')

    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'A small message')
        return self.index()


    def get_kontrolle(self):
        kontrollen = self.context.art_der_kontrolle
        return kontrollen

    def get_datumsangabe(self):
        feld = self.context.datumsangabe
        formattedfeld = feld.strftime("%d/%m/%Y")
        return formattedfeld
