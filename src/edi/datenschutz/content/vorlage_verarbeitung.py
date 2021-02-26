# -*- coding: utf-8 -*-
from plone.dexterity.content import Item
from plone.supermodel import model
from zope.interface import implementer


from edi.datenschutz import _


class IVorlageVerarbeitung(model.Schema):
    """ Marker interface and Dexterity Python Schema for VorlageVerarbeitung
    """

    model.load('vorlage_verarbeitung.xml')


@implementer(IVorlageVerarbeitung)
class VorlageVerarbeitung(Item):
    """
    """
