# -*- coding: utf-8 -*-

from edi.datenschutz import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Massnahmenkatalogview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('massnahmenkatalogview.pt')

    def __call__(self):
        self.msg = _(u'A small message')
        return self.index()

    def verfuegbarkeit(self):
        objects = []
        verfuegbarkeit_id = []

        for i in self.context.getFolderContents():
            iobject = i.getObject()
            objects.append(iobject)

        for i in objects:
            for object in i.zielerfuellung:
                if(object == 'verfuegbarkeit'):
                    verfuegbarkeit_id.append(i)
        
        return verfuegbarkeit_id
