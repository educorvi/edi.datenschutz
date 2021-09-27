# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer
from zope.schema.interfaces import IContextAwareDefaultFactory
from zope.interface import provider

from edi.datenschutz import _


@provider(IContextAwareDefaultFactory)
def get_title(context):
    title = u'Datenschutzfolgenabschätzung: %s' % context.title
    return title

@provider(IContextAwareDefaultFactory)
def get_datenschutzbeauftragter(context):
    return context.datenschutzbeauftragter

@provider(IContextAwareDefaultFactory)
def get_dsfa_beteiligte_person(context):
    return context.beteiligte_personen_und_ihre_rollen

@provider(IContextAwareDefaultFactory)
def get_anmerkung_zum_status(context):
    return context.anmerkung_zum_status

@provider(IContextAwareDefaultFactory)
def get_anlagen_beschreibung(context):
    return context.anlagen_beschreibung
    
@provider(IContextAwareDefaultFactory)
def get_datum(context):
    return context.datumsangabe
    
@provider(IContextAwareDefaultFactory)
def get_dsfa_geplante_verarbeitung(context):
    return context.title

@provider(IContextAwareDefaultFactory)
def get_dsfa_zwecke_der_verarbeitung(context):
    return context.zwecke

@provider(IContextAwareDefaultFactory)
def get_dsfa_rechtsgrundlagen_der_verarbeitung(context):
    return context.rechtsgrundlagen_befugnis

@provider(IContextAwareDefaultFactory)
def get_kategorien_personenbezogener_daten(context):
    vorlage = context.kategorien_daten
    default = []
    for i in vorlage:
        i['anmerkung'] = u""
        default.append(i)
    return default

@provider(IContextAwareDefaultFactory)
def get_kategorien_betroffener_personen(context):
    vorlage = context.kategorien_personen
    default = []
    for i in vorlage:
        i['anmerkung'] = u""
        default.append(i)
    return default
    
@provider(IContextAwareDefaultFactory)
def get_empfaenger_fuer_offenlegung(context):
    vorlage = context.kategorien_empfaenger
    default = []
    for i in vorlage:
        newdict = {}
        newdict['nr'] = i['nr']
        newdict['empfaenger'] = i['bezeichnung']
        newdict['anlass'] = i['anmerkung']
        newdict['anmerkung'] = u""
        default.append(newdict)
    return default

class IDatenschutzfolgenabschaetzung(model.Schema):
    """ Marker interface and Dexterity Python Schema for Datenschutzfolgenabschaetzung
    """
    model.load('datenschutzfolgenabschaetzung.xml')

@implementer(IDatenschutzfolgenabschaetzung)
class Datenschutzfolgenabschaetzung(Container):
    """
    """
