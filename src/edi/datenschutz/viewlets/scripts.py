# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import ViewletBase

class BootstrapScripts(ViewletBase):

    def render(self):
        """ 
        Don't load bootstrap-resources in editors environment
        """
        requrl = self.request.URL
        exclude = [
                '++add++',
                '@@resourceregistry-controlpanel'
                ]
        endswith = [
                'edit',
                'folder_contents',
                ]

        for i in exclude:
            if i in requrl:
                return ""

        for i in endswith:
            if requrl.endswith(i):
                return ""

        return super(BootstrapScripts, self).render()

