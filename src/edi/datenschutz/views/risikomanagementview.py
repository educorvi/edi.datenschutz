# -*- coding: utf-8 -*-

from edi.datenschutz import _
from Products.Five.browser import BrowserView
from edi.datenschutz.riskvocab import asset, vulnerability, threat

from plone.memoize import ram
from time import time

from plone import api

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Risikomanagementview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('risikomanagementview.pt')

    def __call__(self):
        return self.index()

    @ram.cache(lambda *args: time() // (60 * 1))
    def get_folder_contents(self):
        objekte = []
        contents = self.context.listFolderContents()
        for obj in contents:
            if obj.portal_type == "Risiko":
                objekte.append(obj)
            elif obj.portal_type == "Risikoreferenz":
                objekte.append(obj.risikoreferenz.to_object)
        return objekte

    def create_risk_entry(self, i):
        objdict = dict()
        objdict['obj'] = i
        objdict['asset'] = ", ".join([asset.getTerm(k).title for k in i.asset_choice])
        objdict['threat'] = threat.getTerm(i.quelle).title
        objdict['vul'] = vulnerability.getTerm(i.schwachstelle_choice).title
        risiko = i.grad_schwere * i.grad_wahrscheinlichkeit
        if risiko < 3:
            compurisk = ('success', u'geringes Risiko (%i)' % risiko)
        elif 2 < risiko < 12:
            compurisk = ('warning', u'Risiko (%i)' % risiko)
        else:
            compurisk = ('danger', u'hohes Risiko (%i)' % risiko)
        objdict['risiko'] = compurisk
        objdict['refs'] = []
        bewertung = ('light', 'keine Bewertung')
        if i.bewertung == 'success':
            bewertung = (i.bewertung, u'geringes Risiko')
        elif i.bewertung == 'warning':
            bewertung = (i.bewertung, u'Risiko')
        elif i.bewertung == 'danger':
            bewertung = (i.bewertung, u'hohes Risiko')
        objdict['bewertung'] = bewertung
        for massnahme in i.massnahmen:
            objmassnahme = massnahme.to_object
            if objmassnahme:
                massnahmendict = {}
                massnahmendict['title'] = objmassnahme.title
                massnahmendict['url'] = objmassnahme.absolute_url()
                massnahmendict['uid'] = 'edi'+objmassnahme.UID()
                rawview = api.content.get_view(
                    name='massnahmeraw',
                    context=objmassnahme,
                    request=self.request,
                )
                massnahmendict['view'] = rawview()
                objdict['refs'].append(massnahmendict)
        return objdict

    def massnahmen(self):
        uids = []
        massnahmen = []

        objects = self.get_folder_contents()

        for i in objects:
            for k in i.massnahmen:
                objmassnahme = k.to_object
                if objmassnahme:
                    if objmassnahme.UID() not in uids:
                        massdict = {}
                        uids.append(objmassnahme.UID())

                        rawview = api.content.get_view(
                            name='massnahmeraw',
                            context=objmassnahme,
                            request=self.request,
                        )
                        massdict['title'] = objmassnahme.title
                        massdict['uid'] = 'edi'+objmassnahme.UID()
                        massdict['rawview'] = rawview()
                        massnahmen.append(massdict)

        return massnahmen

    def get_zieldata(self, ziel):            
        data = []
        objects = self.get_folder_contents()
        for i in objects:
            if ziel in i.focus:
                ojdict = self.create_risk_entry(i)
                data.append(ojdict)
        return data

    def get_ziele(self):
        ziele = [
                {'title':u'Verfügbarkeit', 'data':self.get_zieldata('verfuegbarkeit')},
                {'title':u'Vertraulichkeit', 'data':self.get_zieldata('vertraulichkeit')},
                {'title':u'Datenintegrität', 'data':self.get_zieldata('datenintegritaet')},
                {'title':u'Datenminimierung', 'data':self.get_zieldata('datenminimierung')},
                {'title':u'Intervenierbarkeit', 'data':self.get_zieldata('intervenierbarkeit')},
                {'title':u'Transparenz', 'data':self.get_zieldata('transparenz')},
                {'title':u'Nichtverkettung', 'data':self.get_zieldata('nichtverkettung')},
                {'title':u'Konzeptionseinhaltung', 'data':self.get_zieldata('konzeptionseinhaltung')},
                {'title':u'Richtigkeit', 'data':self.get_zieldata('richtigkeit')},
                ]
        return ziele
