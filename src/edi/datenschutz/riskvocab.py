from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

asset = SimpleVocabulary((
    SimpleTerm(value=u"server_machines", token=u"server_machines", title=u"Server"),
    SimpleTerm(value=u"pc", token=u"pc", title=u"PC & Laptops"),
    SimpleTerm(value=u"mobile_devices", token=u"mobile_devices", title=u"mobile Geräte"),
    SimpleTerm(value=u"it_networks", token=u"it_networks", title=u"IT-Netzwerke"),
    SimpleTerm(value=u"software_and_apps", token=u"software_and_apps", title=u"Software und Apps"),
    SimpleTerm(value=u"data_&_information", token=u"data_&_information", title=u"Daten & Informationen"),
    SimpleTerm(value=u"connected_devices", token=u"connected_devices", title=u"verbundene Geräte"),
    SimpleTerm(value=u"wearable_devices", token=u"wearable_devices", title=u"tragbare Geräte"),
    SimpleTerm(value=u"physical_infrastructures", token=u"physical_infrastructures", title=u"Physische Infrastrukturen"),
    SimpleTerm(value=u"others", token=u"others", title=u"sonstige Vermögensgegenstände")
))

threat = SimpleVocabulary((
    SimpleTerm(value=u"intern_employee", token=u"intern_employee", title=u"interne Mitarbeiter"),
    SimpleTerm(value=u"extern_employee", token=u"extern_employee", title=u"externe Mitarbeiter"),
    SimpleTerm(value=u"partner", token=u"partner", title=u"Kooperationspartner"),
    SimpleTerm(value=u"service", token=u"service", title=u"externe Dienstleister"),
    SimpleTerm(value=u"hacker", token=u"hacker", title=u"Hacker/Scriptkiddies"),
    SimpleTerm(value=u"criminals", token=u"criminals", title=u"(Cyber-)Kriminelle"),
    SimpleTerm(value=u"terrorists", token=u"terrorists", title=u"Terroristen"),
    SimpleTerm(value=u"press", token=u"press", title=u"Presse, Öffentlichkeit"),
    SimpleTerm(value=u"competitors", token=u"competitors", title=u"Mitbewerber/Konkurrenten"),
    SimpleTerm(value=u"nature", token=u"nature", title=u"höhere Gewalt"),
    SimpleTerm(value=u"others", token=u"others", title=u"sonstige Bedrohungen")
))

vulnerability = SimpleVocabulary((
    SimpleTerm(value=u"bugs", token=u"bugs", title=u"Software-/Hardware-Fehler"),
    SimpleTerm(value=u"broken_processes", token=u"broken_processes", title=u"dysfunktionale Programmabläufe oder Schnittstellen"),
    SimpleTerm(value=u"ineffektive_controls", token=u"ineffektive_controls", title=u"ineffektive Kontrollen oder Maßnahmen"),
    SimpleTerm(value=u"business_change", token=u"business_change", title=u"Änderung der Geschäftprozesse"),
    SimpleTerm(value=u"legacy_systems", token=u"legacy_systems", title=u"Altsysteme (z.B. ohne Wartung)"),
    SimpleTerm(value=u"human_errors", token=u"human_errors", title=u"menschliche Fehler"),
    SimpleTerm(value=u"others", token=u"others", title=u"sonstige Schwachstellen")
))
