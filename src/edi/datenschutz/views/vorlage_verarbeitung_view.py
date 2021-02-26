# -*- coding: utf-8 -*-
from edi.datenschutz import _
from Products.Five.browser import BrowserView
from plone import api as ploneapi

class VorlageVerarbeitungView(BrowserView):

    def get_folders(self):
        folders = api.content.find(context=self.context, portal_type='Folder')
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
        return self.index()
