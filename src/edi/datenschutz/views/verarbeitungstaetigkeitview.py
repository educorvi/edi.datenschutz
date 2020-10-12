# -*- coding: utf-8 -*-

from edi.datenschutz import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Verarbeitungstaetigkeitview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('verarbeitungstaetigkeitview.pt')

    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'A small message')
        import pdb; pdb.set_trace()
        return self.index()
