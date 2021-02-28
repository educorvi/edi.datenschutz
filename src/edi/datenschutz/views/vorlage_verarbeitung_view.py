# -*- coding: utf-8 -*-
from edi.datenschutz import _
from Products.Five.browser import BrowserView
from plone import api as ploneapi

class VorlageVerarbeitungView(BrowserView):

    def get_folders(self):
        folders = ploneapi.content.find(context=self.context.aq_inner.aq_parent, portal_type='Folder')
        options = []
        for i in folders:
            entry = {}
            obj = i.getObject()
            entry['title'] = obj.title
            entry['uid'] = obj.UID()
            options.append(entry)
        return options

    def __call__(self):
        self.folders = self.get_folders()
        self.createurl = self.context.absolute_url()  + '/createVerarbeitung'
        return self.index()
