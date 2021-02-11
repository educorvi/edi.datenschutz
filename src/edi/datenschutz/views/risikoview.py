# -*- coding: utf-8 -*-

from edi.datenschutz import _
from Products.Five.browser import BrowserView
from edi.datenschutz.interfaces import ziele
from edi.datenschutz.riskvocab import asset, threat, vulnerability

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Risikoview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('risikoview.pt')

    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'A small message')
        self.ziele = self.get_ziele()
        self.assets = self.get_assets()
        self.threat = self.get_threat()
        self.vulnerability = self.get_vulnerability()
        self.riskmatrix = self.get_riskmatrix()
        self.massnahmen = self.get_massnahmen()
        return self.index()

    def get_ziele(self):
        zielelist = []
        for ziel in self.context.focus:
            zielelist.append(ziele.getTerm(ziel).title)
        return zielelist

    def get_assets(self):
        assetlist = []
        for assetobj in self.context.asset_choice:
            assetlist.append(asset.getTerm(assetobj).title)    
        return ", ".join(assetlist)

    def get_threat(self):
        return threat.getTerm(self.context.quelle).title

    def get_vulnerability(self):
        return vulnerability.getTerm(self.context.schwachstelle_choice).title

    def get_riskmatrix(self):
        riskdict = dict()
        risiko = self.context.grad_wahrscheinlichkeit * self.context.grad_schwere
        riskdict['risiko'] = risiko
        riskdict['prozent'] = risiko/16 * 100
        if risiko < 3:
            riskdict['wertung'] = u'geringes Risiko'
            riskdict['class'] = 'success'
        elif 2 < risiko < 12:
            riskdict['wertung'] = u'Risiko'
            riskdict['class'] = 'warning'
        else:
            riskdict['wertung'] = u'hohes Risiko'
            riskdict['class'] = 'danger'
        return riskdict

    def get_massnahmen(self):
        massnahmen = []
        for massnahme in self.context.massnahmen:
            objmassnahme = massnahme.to_object
            massnahmendict = {}
            massnahmendict['title'] = objmassnahme.title
            massnahmendict['url'] = objmassnahme.absolute_url()
            massnahmendict['uid'] = 'edi'+objmassnahme.UID()
            massnahmen.append(massnahmendict)
        return massnahmen    
