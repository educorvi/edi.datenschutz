# -*- coding: utf-8 -*-

from edi.datenschutz import _
from Products.Five.browser import BrowserView

from plone.memoize import ram
from time import time

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Risikomanagementview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('risikomanagementview.pt')

    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'A small message')
        return self.index()

    @ram.cache(lambda *args: time() // (60 * 1))
    def get_folder_contents(self):
        contents = self.context.listFolderContents()
        return contents

    def verfuegbarkeit(self):
        objects = []
        verfuegbarkeit = []

        objects = self.get_folder_contents()

        for i in objects:
            objdict = {}
            if 'verfuegbarkeit' in i.focus:
                objdict['obj'] = i
                objdict['refs'] = []
                for massnahme in i.massnahmen:
                    objmassnahme = massnahme.to_object
                    massnahmendict = {}
                    massnahmendict['title'] = objmassnahme.title
                    massnahmendict['url'] = objmassnahme.absolute_url()
                    objdict['refs'].append(massnahmendict)

                verfuegbarkeit.append(objdict)

        return verfuegbarkeit

    def vertraulichkeit(self):
        objects = []
        vertraulichkeit = []

        objects = self.get_folder_contents()

        for i in objects:
            objdict = {}
            if 'vertraulichkeit' in i.focus:
                objdict['obj'] = i
                objdict['refs'] = []
                for massnahme in i.massnahmen:
                    objmassnahme = massnahme.to_object
                    massnahmendict = {}
                    massnahmendict['title'] = objmassnahme.title
                    massnahmendict['url'] = objmassnahme.absolute_url()
                    objdict['refs'].append(massnahmendict)

                vertraulichkeit.append(objdict)

        return vertraulichkeit

    def datenintegritaet(self):
        objects = []
        datenintegritaet = []

        objects = self.get_folder_contents()

        for i in objects:
            objdict = {}
            if 'datenintegritaet' in i.focus:
                objdict['obj'] = i
                objdict['refs'] = []
                for massnahme in i.massnahmen:
                    objmassnahme = massnahme.to_object
                    massnahmendict = {}
                    massnahmendict['title'] = objmassnahme.title
                    massnahmendict['url'] = objmassnahme.absolute_url()
                    objdict['refs'].append(massnahmendict)

                datenintegritaet.append(objdict)

        return datenintegritaet

    def datenminimierung(self):
        objects = []
        datenminimierung = []

        objects = self.get_folder_contents()

        for i in objects:
            objdict = {}
            if 'datenminimierung' in i.focus:
                objdict['obj'] = i
                objdict['refs'] = []
                for massnahme in i.massnahmen:
                    objmassnahme = massnahme.to_object
                    massnahmendict = {}
                    massnahmendict['title'] = objmassnahme.title
                    massnahmendict['url'] = objmassnahme.absolute_url()
                    objdict['refs'].append(massnahmendict)

                datenminimierung.append(objdict)

        return datenminimierung

    def intervenierbarkeit(self):
        objects = []
        intervenierbarkeit = []

        objects = self.get_folder_contents()

        for i in objects:
            objdict = {}
            if 'intervenierbarkeit' in i.focus:
                objdict['obj'] = i
                objdict['refs'] = []
                for massnahme in i.massnahmen:
                    objmassnahme = massnahme.to_object
                    massnahmendict = {}
                    massnahmendict['title'] = objmassnahme.title
                    massnahmendict['url'] = objmassnahme.absolute_url()
                    objdict['refs'].append(massnahmendict)

                intervenierbarkeit.append(objdict)

        return intervenierbarkeit

    def transparenz(self):
        objects = []
        transparenz = []

        objects = self.get_folder_contents()

        for i in objects:
            objdict = {}
            if 'transparenz' in i.focus:
                objdict['obj'] = i
                objdict['refs'] = []
                for massnahme in i.massnahmen:
                    objmassnahme = massnahme.to_object
                    massnahmendict = {}
                    massnahmendict['title'] = objmassnahme.title
                    massnahmendict['url'] = objmassnahme.absolute_url()
                    objdict['refs'].append(massnahmendict)

                transparenz.append(objdict)

        return transparenz

    def nichtverkettung(self):
        objects = []
        nichtverkettung = []

        objects = self.get_folder_contents()

        for i in objects:
            objdict = {}
            if 'nichtverkettung' in i.focus:
                objdict['obj'] = i
                objdict['refs'] = []
                for massnahme in i.massnahmen:
                    objmassnahme = massnahme.to_object
                    massnahmendict = {}
                    massnahmendict['title'] = objmassnahme.title
                    massnahmendict['url'] = objmassnahme.absolute_url()
                    objdict['refs'].append(massnahmendict)

                nichtverkettung.append(objdict)

        return nichtverkettung

    def konzeptionseinhaltung(self):
        objects = []
        konzeptionseinhaltung = []

        objects = self.get_folder_contents()

        for i in objects:
            objdict = {}
            if 'konzeptionseinhaltung' in i.focus:
                objdict['obj'] = i
                objdict['refs'] = []
                for massnahme in i.massnahmen:
                    objmassnahme = massnahme.to_object
                    massnahmendict = {}
                    massnahmendict['title'] = objmassnahme.title
                    massnahmendict['url'] = objmassnahme.absolute_url()
                    objdict['refs'].append(massnahmendict)

                konzeptionseinhaltung.append(objdict)

        return konzeptionseinhaltung

    def richtigkeit(self):
        objects = []
        richtigkeit = []

        objects = self.get_folder_contents()

        for i in objects:
            objdict = {}
            if 'richtigkeit' in i.focus:
                objdict['obj'] = i
                objdict['refs'] = []
                for massnahme in i.massnahmen:
                    objmassnahme = massnahme.to_object
                    massnahmendict = {}
                    massnahmendict['title'] = objmassnahme.title
                    massnahmendict['url'] = objmassnahme.absolute_url()
                    objdict['refs'].append(massnahmendict)

                richtigkeit.append(objdict)

        return richtigkeit
