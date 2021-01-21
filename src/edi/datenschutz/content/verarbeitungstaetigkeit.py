# -*- coding: utf-8 -*-
from zope.interface import Interface
# from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from zope.interface import invariant, Invalid


from edi.datenschutz import _

fehler_datum = _(u"Bei Erforderlichkeit einer Datenschutzfolgenabschätzung muss ein Datum für die Fertigstellung oder Überprüfung angegeben werden.")

class DSFADatum(Invalid):
    __doc__ = fehler_datum

class IVerarbeitungstaetigkeit(model.Schema):
    """ Marker interface and Dexterity Python Schema for Verarbeitungstaetigkeit
    """

    model.load('verarbeitungstaetigkeit.xml')

    @invariant
    def validateDatum(data):
        if data.datenschutz_folgenabschatzung_erforderlich == 'Ja':
            if not data.pruefung_bis_wann:
                raise DSFADatum(fehler_datum)


@implementer(IVerarbeitungstaetigkeit)
class Verarbeitungstaetigkeit(Container):
    """
    """
