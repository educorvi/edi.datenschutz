# -*- coding: utf-8 -*-
from plone.app.multilingual.browser.interfaces import make_relation_root_path
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from zope import schema
from zope.interface import implementer

from edi.datenschutz import _

class IRisikoreferenz(model.Schema):
    """ Marker interface and Dexterity Python Schema for Risikoreferenz
    """

    title = schema.TextLine(title=u"Titel", default=u"Risikoreferenz", required=True)

    id = schema.TextLine(title=u"ID des Risikos", required=True)

    risikoreferenz = RelationChoice(
        title=u"Risikoverweis",
        description=u"Bitte wählen Sie ein Risiko auf das Sie verweisen wollen.",
        vocabulary='plone.app.vocabularies.Catalog',
        required=False,
    )

    directives.widget(
        "risikoreferenz",
        RelatedItemsFieldWidget,
        pattern_options={
            "selectableTypes": ["Risiko"],
            "basePath": make_relation_root_path,
        },
    )

@implementer(IRisikoreferenz)
class Risikoreferenz(Item):
    """
    """
