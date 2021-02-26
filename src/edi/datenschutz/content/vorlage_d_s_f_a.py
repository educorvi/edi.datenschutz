# -*- coding: utf-8 -*-
from plone.dexterity.content import Item
from plone.supermodel import model
from zope.interface import implementer


from edi.datenschutz import _


class IVorlageDSFA(model.Schema):
    """ Marker interface and Dexterity Python Schema for VorlageDSFA
    """

    model.load('vorlage_dsfa.xml')

@implementer(IVorlageDSFA)
class VorlageDSFA(Item):
    """
    """
