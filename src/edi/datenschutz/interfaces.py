# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.interface import Interface
from zope import schema
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

class IEdiDatenschutzLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

class IAnlagenVerweise(Interface):

    nr = schema.Int(title=u"Nr.")
    bezeichnung = schema.TextLine(title=u"Bezeichnung der Anlage bzw. des Verweises")
    anmerkung = schema.TextLine(title=u"Anmerkung")

class IAenderungen(Interface):

    wann = schema.Date(title=u"Wann?")
    wer = schema.TextLine(title=u"Wer?")
    was = schema.TextLine(title=u"Was?")

class IKategorienDaten(Interface):

    nr = schema.Int(title=u"Nr.")
    bezeichnung = schema.TextLine(title=u"Bezeichnung der Daten")

class IKategorienDatenProzesse(Interface):

    nr = schema.Int(title=u"Nr.")
    bezeichnung = schema.TextLine(title=u"Bezeichnung der Datenkategorie")
    anmerkung = schema.TextLine(title=u"Anmerkung")

class IKategorienPersonen(Interface):

    nr = schema.Int(title=u"Nr.")
    bezeichnung = schema.TextLine(title=u"Betroffene Personen")

class IKategorienPersonenDSFA(Interface):

    nr = schema.Int(title=u"Nr.")
    bezeichnung = schema.TextLine(title=u"Bezeichnung der Kategorien betroffener Personen")
    anmerkung = schema.TextLine(title=u"Anmerkung")

class IKategorienEmpfaenger(Interface):

    nr = schema.Int(title=u"Nr.")
    bezeichnung = schema.TextLine(title=u"Empfaenger")
    anmerkung = schema.TextLine(title=u"Anlass der Offenlegung")

class IInternationaleOrganisationen(Interface):

    nr = schema.Int(title=u"Nr.")     
    bezeichnung = schema.TextLine(title=u"Drittland oder internationale Organisation")
    anmerkung = schema.TextLine(title=u"Geeignete Garantien im Falle einer Übermittlung (Art.49 Abs.1 Unterabsatz 2 DSGVO)")

class IFristenLoeschung(Interface):

    nr = schema.Int(title=u"Nr.")
    bezeichnung = schema.TextLine(title=u"Löschungsfrist")

class IOffenlegungen(Interface):

    nr = schema.Int(title=u"Nr.")
    empfaenger = schema.TextLine(title=u"Empfänger")
    anlass = schema.TextLine(title=u"Anlass der Offenlegung")
    anmerkung = schema.TextLine(title=u"Anmerkung")

grad = SimpleVocabulary((
    SimpleTerm(value=1, token="1", title="1"),
    SimpleTerm(value=2, token="2", title="2"),
    SimpleTerm(value=3, token="3", title="3"),
    SimpleTerm(value=4, token="4", title="4"),
    ))

ampel = SimpleVocabulary((
    SimpleTerm(value="gr", token="gr", title=u"grün"),
    SimpleTerm(value="ge", token="ge", title=u"gelb"),
    SimpleTerm(value="ro", token="ro", title=u"rot"),
    ))

class IRisikomanagement(Interface):

    id = schema.TextLine(title=u"ID")
    schwachstelle = schema.Text(title=u"Schwachstelle")
    quelle = schema.TextLine(title=u"Risikoquelle")
    szenario = schema.Text(title=u"Risko-Szenario")
    schwere = schema.Choice(title=u"Schaden/Schwere", vocabulary=grad)
    wahrscheinlichkeit = schema.Choice(title=u"Wahrscheinlichkeit", vocabulary=grad)

class IZielmanagement(Interface):

    id = schema.TextLine(title=u"ID")
    schwachstelle = schema.Text(title=u"Schwachstelle")
    quelle = schema.TextLine(title=u"Risikoquelle")
    szenario = schema.Text(title=u"Risko-Szenario")
    bewertung = schema.Choice(title=u"Wahrscheinlichkeit", vocabulary=ampel)
