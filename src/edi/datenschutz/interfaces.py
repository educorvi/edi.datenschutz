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

    nr = schema.TextLine(title=u"Nr.")
    bezeichnung = schema.TextLine(title=u"Bezeichnung der Anlage bzw. des Verweises", required=False)
    anmerkung = schema.TextLine(title=u"Anmerkung", required=False)

class IAenderungen(Interface):

    wann = schema.Date(title=u"Wann?")
    wer = schema.TextLine(title=u"Wer?")
    was = schema.TextLine(title=u"Was?")

class IKategorienDaten(Interface):

    nr = schema.TextLine(title=u"Nr.")
    bezeichnung = schema.TextLine(title=u"Bezeichnung der Daten", required=False)

class IKategorienDatenProzesse(Interface):

    nr = schema.TextLine(title=u"Nr.")
    bezeichnung = schema.TextLine(title=u"Bezeichnung der Datenkategorie", required=False)
    anmerkung = schema.TextLine(title=u"Anmerkung", required=False)

class IKategorienPersonen(Interface):

    nr = schema.TextLine(title=u"Nr.")
    bezeichnung = schema.TextLine(title=u"Betroffene Personen", required=False)

class IKategorienPersonenDSFA(Interface):

    nr = schema.TextLine(title=u"Nr.")
    bezeichnung = schema.TextLine(title=u"Bezeichnung der Kategorien betroffener Personen", required=False)
    anmerkung = schema.TextLine(title=u"Anmerkung", required=False)

class IKategorienEmpfaenger(Interface):

    nr = schema.TextLine(title=u"Nr.")
    bezeichnung = schema.TextLine(title=u"Empfaenger", required=False)
    anmerkung = schema.TextLine(title=u"Anlass der Offenlegung", required=False)

class IInternationaleOrganisationen(Interface):

    nr = schema.TextLine(title=u"Nr.")
    bezeichnung = schema.TextLine(title=u"Drittland oder internationale Organisation", required=False)
    anmerkung = schema.TextLine(title=u"Geeignete Garantien im Falle einer Übermittlung (Art.49 Abs.1 Unterabsatz 2 DSGVO)", required=False)

class IFristenLoeschung(Interface):

    nr = schema.TextLine(title=u"Nr.")
    bezeichnung = schema.TextLine(title=u"Löschungsfrist", required=False)

class IOffenlegungen(Interface):

    nr = schema.TextLine(title=u"Nr.")
    empfaenger = schema.TextLine(title=u"Empfänger", required=False)
    anlass = schema.TextLine(title=u"Anlass der Offenlegung", required=False)
    anmerkung = schema.TextLine(title=u"Anmerkung", required=False)

grad = SimpleVocabulary((
    SimpleTerm(value=1, token="1", title="1"),
    SimpleTerm(value=2, token="2", title="2"),
    SimpleTerm(value=3, token="3", title="3"),
    SimpleTerm(value=4, token="4", title="4"),
    ))

ampel = SimpleVocabulary((
    SimpleTerm(value="success", token="gr", title=u"grün"),
    SimpleTerm(value="warning", token="ge", title=u"gelb"),
    SimpleTerm(value="danger", token="ro", title=u"rot"),
    ))

def get_ampel(context):
    return ampel

ziele = SimpleVocabulary((
    SimpleTerm(value="verfuegbarkeit", token="verfuegbarkeit", title=u"Verfügbarkeit"),
    SimpleTerm(value="vertraulichkeit", token="vertraulichkeit", title=u"Vertraulichkeit"),
    SimpleTerm(value="datenintegritaet", token="datenintegritaet", title=u"Datenintegrität"),
    SimpleTerm(value="datenminimierung", token="datenminimierung", title=u"Datenminimierung"),
    SimpleTerm(value="intervenierbarkeit", token="intervenierbarkeit", title=u"Intervenierbarkeit"),
    SimpleTerm(value="transparenz", token="tranparenz", title="Transparenz"),
    SimpleTerm(value="nichtverkettung", token="nichtverkettung", title=u"Nichtverkettung"),
    SimpleTerm(value="konzeptionseinhaltung", token="konzeptionseinhaltung", title=u"Konzeptionseinhaltung"),
    SimpleTerm(value="richtigkeit", token="richtigkeit", title=u"Richtigkeit")
    ))

risikomanagement = SimpleVocabulary((
    SimpleTerm(value="verfuegbarkeit", token="verfuegbarkeit", title=u"Verfügbarkeit"),
    SimpleTerm(value="vertraulichkeit", token="vertraulichkeit", title=u"Vertraulichkeit"),
    SimpleTerm(value="datenintegritaet", token="datenintegritaet", title=u"Datenintegrität"),
    ))

zielmanagement = SimpleVocabulary((
    SimpleTerm(value="datenminimierung", token="datenminimierung", title=u"Datenminimierung"),
    SimpleTerm(value="intervenierbarkeit", token="intervenierbarkeit", title=u"Intervenierbarkeit"),
    SimpleTerm(value="transparenz", token="tranparenz", title="Transparenz"),
    SimpleTerm(value="nichtverkettung", token="nichtverkettung", title=u"Nichtverkettung"),
    SimpleTerm(value="konzeptionseinhaltung", token="konzeptionseinhaltung", title=u"Konzeptionseinhaltung"),
    SimpleTerm(value="richtigkeit", token="richtigkeit", title=u"Richtigkeit")
    ))

class IRisikomanagement(Interface):

    id = schema.TextLine(title=u"ID")
    schwachstelle = schema.Text(title=u"Schwachstelle", required=False)
    quelle = schema.TextLine(title=u"Risikoquelle", required=False)
    szenario = schema.Text(title=u"Risko-Szenario", required=False)
    schwere = schema.Choice(title=u"Schaden/Schwere", vocabulary=grad, required=False)
    wahrscheinlichkeit = schema.Choice(title=u"Wahrscheinlichkeit", vocabulary=grad, required=False)

class IZielmanagement(Interface):

    id = schema.TextLine(title=u"ID")
    schwachstelle = schema.Text(title=u"Schwachstelle", required=False)
    quelle = schema.TextLine(title=u"Risikoquelle", required=False)
    szenario = schema.Text(title=u"Risko-Szenario", required=False)
    bewertung = schema.Choice(title=u"Wahrscheinlichkeit", vocabulary=ampel, required=False)
