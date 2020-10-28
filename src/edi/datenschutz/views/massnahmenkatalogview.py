# -*- coding: utf-8 -*-

from edi.datenschutz import _
from Products.Five.browser import BrowserView

from plone.memoize import ram
from time import time

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Massnahmenkatalogview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('massnahmenkatalogview.pt')

    def __call__(self):
        self.msg = _(u'A small message')
        return self.index()

    @ram.cache(lambda *args: time() // (60 * 1))
    def get_folder_contents(self):
        contents = self.context.listFolderContents()
        print("Deutschland isch stabil")
        return contents

    def verfuegbarkeit(self):
        objects = []
        verfuegbarkeit = []

        objects = self.get_folder_contents()

        for i in objects:
            for object in i.zielerfuellung:
                if(object == 'verfuegbarkeit'):
                    verfuegbarkeit.append(i)
        
        return verfuegbarkeit

    def vertraulichkeit(self):
        objects = []
        vertraulichkeit = []

        for i in self.context.getFolderContents():
            iobject = i.getObject()
            objects.append(iobject)

        for i in objects:
            for object in i.zielerfuellung:
                if(object == 'vertraulichkeit'):
                    vertraulichkeit.append(i)
        
        return vertraulichkeit

    def datenintegritaet(self):
        objects = []
        datenintegritaet = []

        for i in self.context.getFolderContents():
            iobject = i.getObject()
            objects.append(iobject)

        for i in objects:
            for object in i.zielerfuellung:
                if(object == 'datenintegritaet'):
                    datenintegritaet.append(i)
        
        return datenintegritaet

    def datenminimierung(self):
        objects = []
        datenminimierung = []

        for i in self.context.getFolderContents():
            iobject = i.getObject()
            objects.append(iobject)

        for i in objects:
            for object in i.zielerfuellung:
                if(object == 'datenminimierung'):
                    datenminimierung.append(i)
        
        return datenminimierung

    def intervenierbarkeit(self):
        objects = []
        intervenierbarkeit = []

        for i in self.context.getFolderContents():
            iobject = i.getObject()
            objects.append(iobject)

        for i in objects:
            for object in i.zielerfuellung:
                if(object == 'intervenierbarkeit'):
                    intervenierbarkeit.append(i)
        
        return intervenierbarkeit

    def transparenz(self):
        objects = []
        transparenz = []

        for i in self.context.getFolderContents():
            iobject = i.getObject()
            objects.append(iobject)

        for i in objects:
            for object in i.zielerfuellung:
                if(object == 'transparenz'):
                    transparenz.append(i)
        
        return transparenz

    def nichtverkettung(self):
        objects = []
        nichtverkettung = []

        for i in self.context.getFolderContents():
            iobject = i.getObject()
            objects.append(iobject)

        for i in objects:
            for object in i.zielerfuellung:
                if(object == 'nichtverkettung'):
                    nichtverkettung.append(i)
        
        return nichtverkettung

    def konzeptionseinhaltung(self):
        objects = []
        konzeptionseinhaltung = []

        for i in self.context.getFolderContents():
            iobject = i.getObject()
            objects.append(iobject)

        for i in objects:
            for object in i.zielerfuellung:
                if(object == 'konzeptionseinhaltung'):
                    konzeptionseinhaltung.append(i)
        
        return konzeptionseinhaltung

    def richtigkeit(self):
        objects = []
        richtigkeit = []

        for i in self.context.getFolderContents():
            iobject = i.getObject()
            objects.append(iobject)

        for i in objects:
            for object in i.zielerfuellung:
                if(object == 'richtigkeit'):
                    richtigkeit.append(i)
        
        return richtigkeit