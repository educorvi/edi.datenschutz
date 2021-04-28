# -*- coding: utf-8 -*-
from zope.interface import Interface
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from zope.interface import invariant, Invalid

from edi.datenschutz import _

class IVerarbeitungstaetigkeit(model.Schema):
    """ Marker interface and Dexterity Python Schema for Verarbeitungstaetigkeit
    """

    model.load('verarbeitungstaetigkeit.xml')

@implementer(IVerarbeitungstaetigkeit)
class Verarbeitungstaetigkeit(Container):
    """
    """
