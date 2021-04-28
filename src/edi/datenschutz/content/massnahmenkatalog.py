# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer
from zope.schema.interfaces import IContextAwareDefaultFactory
from zope.interface import provider

from edi.datenschutz import _

@provider(IContextAwareDefaultFactory)
def get_title(context):
    title = u'Maßnahmenkatalog: %s' % context.title
    return title

class IMassnahmenkatalog(model.Schema):
    """ Marker interface and Dexterity Python Schema for Massnahmenkatalog
    """
    model.load('massnahmenkatalog.xml')


@implementer(IMassnahmenkatalog)
class Massnahmenkatalog(Container):
    """
    """
