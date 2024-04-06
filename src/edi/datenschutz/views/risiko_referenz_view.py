# -*- coding: utf-8 -*-
from edi.datenschutz import _
from Products.Five.browser import BrowserView
from edi.datenschutz.interfaces import ziele
from edi.datenschutz.riskvocab import asset, threat, vulnerability

matrixrange = 4
low = 22
high = 22

def calculate_risk(value):
    erglist = []
    for i in range(1,matrixrange+1):
        for k in range(1,matrixrange+1):
            erg = i*k
            if erg not in erglist:
                erglist.append(erg)
    prozent = ((erglist.index(value)+1) / len(erglist)) * 100
    return int(prozent)

class RisikoReferenzView(BrowserView):

    def __call__(self):
        dstobj = self.context.risikoreferenz.to_object
        self.contextobj = dstobj
        self.msg = _(u'A small message')
        self.ziele = self.get_ziele(dstobj)
        self.assets = self.get_assets(dstobj)
        self.threat = self.get_threat(dstobj)
        self.vulnerability = self.get_vulnerability(dstobj)
        self.riskmatrix = self.get_riskmatrix(dstobj)
        self.massnahmen = self.get_massnahmen(dstobj)
        return self.index()

    def get_ziele(self, dstobj):
        zielelist = []
        for ziel in dstobj.focus:
            zielelist.append(ziele.getTerm(ziel).title)
        return zielelist

    def get_assets(self, dstobj):
        assetlist = []
        for assetobj in dstobj.asset_choice:
            assetlist.append(asset.getTerm(assetobj).title)    
        return ", ".join(assetlist)

    def get_threat(self, dstobj):
        return threat.getTerm(dstobj.quelle).title

    def get_vulnerability(self, dstobj):
        return vulnerability.getTerm(dstobj.schwachstelle_choice).title

    def get_riskmatrix(self, dstobj):
        riskdict = dict()
        risiko = dstobj.grad_wahrscheinlichkeit * dstobj.grad_schwere
        riskdict['risiko'] = risiko
        prozent = calculate_risk(risiko)
        riskdict['prozent'] = prozent
        riskmedium = 100 - (low+high)
        riskdict['low'] = low
        riskdict['high'] = high
        riskdict['medium'] = riskmedium
        if prozent < low:
            riskdict['wertung'] = u'geringes Risiko'
            riskdict['class'] = 'success'
        elif low < prozent < (low + riskmedium):
            riskdict['wertung'] = u'Risiko'
            riskdict['class'] = 'warning'
        else:
            riskdict['wertung'] = u'hohes Risiko'
            riskdict['class'] = 'danger'
        return riskdict

    def get_massnahmen(self, dstobj):
        massnahmen = []
        for massnahme in dstobj.massnahmen:
            objmassnahme = massnahme.to_object
            if objmassnahme:
                massnahmendict = {}
                massnahmendict['title'] = objmassnahme.title
                massnahmendict['url'] = objmassnahme.absolute_url()
                massnahmendict['uid'] = 'edi'+objmassnahme.UID()
                massnahmen.append(massnahmendict)
        return massnahmen    
