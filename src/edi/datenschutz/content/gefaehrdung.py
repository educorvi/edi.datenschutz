# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.supermodel import model
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from zope import schema
from zope.interface import implementer
from edi.datenschutz.interfaces import ziele, ampel
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.app.multilingual.browser.interfaces import make_relation_root_path

from edi.datenschutz import _


class IGefaehrdung(model.Schema):
    """ Marker interface and Dexterity Python Schema for Gefaehrdung
    """
    directives.widget("focus", CheckBoxFieldWidget)
    focus = schema.List(title="Fokus", value_type=schema.Choice(vocabulary=ziele))
    schwachstelle = schema.Text(title=u"Schwachstelle", required=True)
    quelle = schema.TextLine(title=u"Gefährdungsquelle", required=False)
    szenario = schema.Text(title=u"Gefährdungsszenario", required=False)
    grad_wahrscheinlichkeit = schema.Choice(title=u"Index Gefährdungsbewertung", vocabulary=ampel, required=True)
    wahrscheinlichkeit = schema.Text(title=u"Erläuterung zur Gefährdungsbewertung", required=False)
    massnahmen = RelationList(title=u"Maßnahmen zur Vermeidung oder Minimierung des Risikos",
                              value_type=RelationChoice(vocabulary='plone.app.vocabularies.Catalog'))
    erlaeuterung = schema.Text(title=u"Erläuterungen zu den Maßnahmen", required=False)

    directives.widget(
        "massnahmen",
        RelatedItemsFieldWidget,
        pattern_options={
            "selectableTypes": ["Massnahme"],
            "basePath": make_relation_root_path,
        },
    )


@implementer(IGefaehrdung)
class Gefaehrdung(Item):
    """
    """
