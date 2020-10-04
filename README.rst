.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

===============
edi.datenschutz
===============

Mit diesem Add-On soll das Datenschutz-Management unterstützt werden. Das Add-On erhält alle erforderlichen Dokumentarten und Container
zur Beschreibung und Dokumentation. Über Views werden die gespeicherten Daten für verschiedene Arten von Auskunftsersuchen zusammengefasst 
und verdichtet. Ein PDF-Export der Datenschutz-Dokumentation soll ermöglicht werden.

Struktur der Inhaltstypen
-------------------------

- Verarbeitungstätigkeit (Container)
    |
    |- Datenschutzfolgenabschätzung (Item)
    |- Risikomanagement (Item)
    |- Zielerfüllungsmanagement (Item)
    |- Maßnahmenkatalog (Container)
        |
        |- Maßnahme
            |
            |- Kontrolle oder Überprüfung

- Maßnahme
    |
    |- Kontrolle oder Überprüfung


Ansichten
---------

Hier werden künftig die möglichen Ansichten für die diversen Auskunfsersuchen dokumentiert.


ToDo:
-----

- Tests
- Einzelansichten fuer alle Inhaltstypeen
- PDF-Export


Beispiel
--------

doc.uv-kooperation.de

Installation
------------

Das Add-On edi.datenschutz muss der Buildout-Konfiguration hinzugefügt werden::

    [buildout]

    ...

    eggs =
        edi.datenschutz


danach kann ``bin/buildout`` ausgeführt werden.


Quellen
-------

Dokument „Das Standard-Datenschutzmodell“ 
Quelle: https://www.bfdi.bund.de/DE/Datenschutz/Themen/Technische_Anwendungen/TechnischeAnwendungenArtikel/Standard-Datenschutzmodell.html

Dokument „Referenz-Maßnahmenkatalog“
Quelle: https://www.datenschutz-mv.de/datenschutz/datenschutzmodell/

Außerdem:
Dokumente und Formulare auf der Seite des Bayerischen Landesdatenschutzbeauftragten
Quelle: https://www.datenschutz-bayern.de/dsfa/

Modul 1: Beschreibung einer Verarbeitungstätigkeit
Modul 2: DSFA-Bericht in Formularform für eine Verarbeitungstätigkeit
Modul 3: Tabellen für das Risikomanagement zu einer Verarbeitungstätigkeit
Modul 4: Tabellen für das Zielerfüllungsmanagement zu einer Verarbeitungstätigkeit

Unterstützung
-------------

- lars.walther@educorvi.de
- seppo.walther@educorvi.de

Lizenz
------

Das Projekt ist unter GPLv2 lizensiert.
