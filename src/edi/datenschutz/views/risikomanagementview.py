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
            for object in i.focus:
                if (object == 'verfuegbarkeit'):
                    verfuegbarkeit.append(i)

        return verfuegbarkeit

