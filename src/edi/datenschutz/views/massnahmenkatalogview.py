# -*- coding: utf-8 -*-

from edi.datenschutz import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Massnahmenkatalogview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('massnahmenkatalogview.pt')

    def __call__(self):
        # Implement your own actions:
        objects = []

        verfuegbarkeit_id = []
        verfuegbarkeit_title = []
        verfuegbarkeit_orgatechnisch = []
        verfuegbarkeit_ansprechpartner = []

        vertraulichkeit_id = []
        vertraulichkeit_title = []
        vertraulichkeit_orgatechnisch = []
        vertraulichkeit_ansprechpartner = []

        datenintegritaet_id = []
        datenintegritaet_title = []
        datenintegritaet_orgatechnisch = []
        datenintegritaet_ansprechpartner = []

        verfuegbarkeit_id = []
        verfuegbarkeit_title = []
        verfuegbarkeit_orgatechnisch = []
        verfuegbarkeit_ansprechpartner = []

        verfuegbarkeit_id = []
        verfuegbarkeit_title = []
        verfuegbarkeit_orgatechnisch = []
        verfuegbarkeit_ansprechpartner = []

        verfuegbarkeit_id = []
        verfuegbarkeit_title = []
        verfuegbarkeit_orgatechnisch = []
        verfuegbarkeit_ansprechpartner = []

        for i in self.context.getFolderContents():
            iobject = i.getObject()
            objects.append(iobject)
        import pdb; pdb.set_trace()

        for i in objects:
            for object in i.zielerfuellung:
                if(object == 'verfuegbarkeit'):
                    verfuegbarkeit_id.append(i.id_massnahme)
                    verfuegbarkeit_title.append(i.title)
                    verfuegbarkeit_orgatechnisch.append(i.art_der_massnahme)
                    verfuegbarkeit_ansprechpartner.append(i.ausfuehrender)

        import pdb; pdb.set_trace()

        self.msg = _(u'A small message')
        return self.index()
