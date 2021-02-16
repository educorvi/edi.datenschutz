# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.supermodel import model
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from edi.datenschutz.interfaces import ziele, grad, ampel
from edi.datenschutz.riskvocab import asset, vulnerability, threat
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.app.multilingual.browser.interfaces import make_relation_root_path
from zope.interface import Invalid

from edi.datenschutz import _


def checkbox_constraint(value):
    if value == []:
        raise Invalid(u"Bitte treffen Sie eine Auswahl")
    return True


class IRisiko(model.Schema):
    """ Marker interface and Dexterity Python Schema for Risiko
    """
    directives.widget("focus", CheckBoxFieldWidget)
    focus = schema.List(title="Auswahl der Gewährleistungsziele, die durch das Risiko kompromittiert werden", constraint=checkbox_constraint, value_type=schema.Choice(vocabulary=ziele))

    directives.widget("asset_choice", CheckBoxFieldWidget)
    asset_choice = schema.List(title=u"Art des Vermögensgegenstands", constraint=checkbox_constraint, value_type=schema.Choice(vocabulary=asset))

    asset = schema.Text(title=u"Optional: Nähere Erläuterung / Anmerkung zum Vermögensgegenstand", required=False)

    quelle = schema.Choice(title=u"Art der Bedrohung bzw. Quelle des Risikos", description=u"Treffen Sie eine Auswahl.", default="intern_employee", 
            vocabulary=threat)

    szenario = schema.Text(title=u"Optional: Nähere Erläuterung zur Bedrohung bzw. zur Quelle des Risikos", required=False)

    schwachstelle_choice = schema.Choice(title=u"Art der Schwachstelle (Vulnerability)", description=u"Treffen Sie eine Auswahl.", vocabulary=vulnerability)

    schwachstelle = schema.Text(title=u"Optional: Nähere Erläuterung zur Schwachstelle (Vulnerability)", required=False)

    schwachstelle_link = schema.URI(title=u"Optional: Link auf eine Quelle in der die Schwachstelle (Vulnerability) beschrieben bzw. dokumentiert wird",
                               description=u"Beispiel: Link auf Datenbank von Heise Online", required=False)

    directives.widget("grad_wahrscheinlichkeit", RadioFieldWidget)
    grad_wahrscheinlichkeit = schema.Choice(title=u"Grad der Eintrittswahrscheinlichkeit", vocabulary=grad, required=True)

    wahrscheinlichkeit = schema.Text(title=u"Erläuterung zur Eintrittswahrscheinlichkeit", required=False)

    directives.widget("grad_schwere", RadioFieldWidget)
    grad_schwere = schema.Choice(title=u"Grad der Schwere des Schadens", vocabulary=grad, required=True)

    schwere = schema.Text(title=u"Erläuterung zur Schwere des Schaden", required=False)

    massnahmen = RelationList(title=u"Maßnahmen zur Minimierung oder Vermeidung des Risikos",
                              value_type=RelationChoice(vocabulary='plone.app.vocabularies.Catalog'),
                              required=False)

    erlaeuterung = schema.Text(title=u"Erläuterungen zu den Maßnahmen", required=False)

    bewertung = schema.Choice(title=u"Risikobewertung nach Umsetzung der aufgeführten Maßnahmen", vocabulary=ampel, default='light')

    directives.widget(
        "massnahmen",
        RelatedItemsFieldWidget,
        pattern_options={
            "selectableTypes": ["Massnahme"],
            "basePath": make_relation_root_path,
        },
    )


@implementer(IRisiko)
class Risiko(Item):
    """
    """
