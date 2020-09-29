# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.interface import Interface
from zope import schema

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

class IKategorienPersonen(Interface):

    nr = schema.Int(title=u"Nr.")
    bezeichnung = schema.TextLine(title=u"Betroffene Personen")

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
