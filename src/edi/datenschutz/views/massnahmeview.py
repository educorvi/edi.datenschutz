# -*- coding: utf-8 -*-

from edi.datenschutz import _
from edi.datenschutz import interfaces as interfaces
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Massnahmeview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('massnahmeview.pt')

    def __call__(self):
        self.msg = _(u'A small message')
        return self.index()

    def get_ziele(self):
        terms = self.context.zielerfuellung
        termtitles = [] 
        for i in terms:
            term = interfaces.ziele.getTerm(i)
            termtitle = term.title
            termtitles.append(termtitle)
        return ", ".join(termtitles)

    def get_massnahmenart(self):
        massnahmen = self.context.art_der_massnahme
        return massnahmen

    def get_datumsangabe(self):
        feld = self.context.datumsangabe
        formattedfeld = feld.strftime("%d/%m/%Y")
        return formattedfeld
