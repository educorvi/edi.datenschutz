# -*- coding: utf-8 -*-

from edi.datenschutz import _
from Products.Five.browser import BrowserView

from plone.memoize import ram
from time import time

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from edi.datenschutz.views.risikomanagementview import Risikomanagementview

class Zielerfuellungsmanagementview(Risikomanagementview):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('zielerfuellungsmanagementview.pt')
    """
    """
