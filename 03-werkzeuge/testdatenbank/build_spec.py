#!/usr/bin/env python3
"""Erzeugt Inhalt und Standardfeld-Konfiguration der Strickhof-Testdatenbank."""
import csv
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / '02-produkte/testdatenbank-5.2'
SRC = Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)
with (ROOT / '02-produkte/plugin-testbarkeit.csv').open() as handle:
    plugins = list(csv.DictReader(handle, delimiter=';'))
assert len(plugins) == 71
assert not {'mod_chat', 'mod_survey'} & {p['plugin'] for p in plugins}
lookup = {p['plugin']: p for p in plugins}
mainplugins = [p for p in plugins if p['kategorie'] != 'C']
pluginlabel = {p['plugin']: f"{p['bezeichnung']} · {p['plugin']}" for p in mainplugins}

fields = []
def field(name, label, kind='text', required=False, options=None, helptext=''):
    values = {f'param{i}': '' for i in range(1, 11)}
    if options:
        values['param1'] = '\n'.join(options)
    if kind == 'textarea':
        values.update(param2='60', param3='5')
    if kind == 'picture':
        values.update(param1='1000', param2='750', param3='120', param4='90')
    if kind == 'url':
        values.update(param1='1', param2='')
    fields.append(dict(name=name, label=label, type=kind, required=int(required),
                       description=helptext or label, **values))

field('testfall_id', 'Testfall-ID', required=True, helptext='Stabile Kennung, zum Beispiel BAS-01. Bei einem Nachtest dieselbe Kennung verwenden.')
field('titel', 'Kurztitel', required=True)
field('bereich', 'Bereich / Plugin', 'menu', True,
      ['Grundfunktionen', 'Migration und Darstellung'] + sorted(pluginlabel.values()))
field('pruefumfang', 'Prüfumfang', 'menu', True,
      ['Regulärer Test', 'Nach Vorbereitung', 'Technische Integration'])
field('person', 'Testende Person', required=True,
      helptext='Bei vorbereiteten Einträgen: Noch nicht zugeteilt. Vor dem Test den eigenen Namen eintragen.')
field('rolle', 'Getestete Rolle', 'menu', True,
      ['Lehrperson', 'Lernende', 'Lehrperson und Lernende', 'Manager/in', 'Administration'])
field('browser', 'Browser', 'menu', True,
      ['Noch nicht zugeteilt', 'Firefox', 'Chrome', 'Edge', 'Safari', 'Anderer Browser'])
field('umgebung', 'Browser-Version, Betriebssystem und Gerät', helptext='Zum Beispiel: Firefox [Version], Windows [Version], Laptop.')
field('teststand', 'Teststand', helptext='Vor dem Test eindeutige Kennung des bereitgestellten Stands eintragen. Moodle 5.2 allein reicht nach Korrekturen nicht.')
field('testdatum', 'Testdatum', helptext='JJJJ-MM-TT. Bis zur Durchführung leer lassen.')
field('kurslink', 'Link zur getesteten Stelle', 'url', helptext='Direkter Link zur Aktivität auf moodlestaging.strickhof.ch.')
field('schritte', 'Voraussetzungen und Testschritte', 'textarea', True)
field('soll', 'Erwartetes Ergebnis', 'textarea', True)
field('ist', 'Tatsächliches Ergebnis', 'textarea', helptext='Bei Erfolg eine konkrete Beobachtung; bei Fehlern genaue Abweichung und Wortlaut der Fehlermeldung.')
field('ergebnis', 'Testergebnis', 'menu', True,
      ['Noch offen', 'Bestanden', 'Fehler', 'Blockiert', 'Entfällt'])
field('bezug', 'Früherer Test / bekanntes Problem', 'url')
field('schweregrad', 'Schweregrad', 'menu', options=['Nicht eingestuft', 'Kritisch', 'Erheblich', 'Gering'])
field('wiederholbarkeit', 'Wiederholbarkeit', 'menu', options=['Noch nicht erneut geprüft', 'Jedes Mal', 'Gelegentlich', 'Einmal beobachtet'])
field('screenshot', 'Screenshot', 'picture')
field('anhang', 'Ergänzende Datei', 'file')
field('hindernis', 'Hindernis / Übergangslösung', 'textarea')
field('bearbeitung', 'Bearbeitungsstatus', 'menu', True,
      ['Nicht nötig', 'Neu', 'In Klärung', 'Beim Dienstleister', 'Bereit zum Nachtest', 'Abgeschlossen', 'Akzeptiertes Restrisiko'])
field('zustaendig', 'Zuständig für den nächsten Schritt')
field('termin', 'Termin für den nächsten Schritt', helptext='JJJJ-MM-TT. Leer lassen, wenn kein Termin vereinbart ist.')
field('ticket', 'Ticketnummer')
field('ticketlink', 'Ticketlink', 'url')
field('verlauf', 'Bearbeitungsverlauf / Entscheid', 'textarea')

cases = []
def case(code, plugin, title, steps, expected, role='Lehrperson und Lernende', prep='', scope='Regulärer Test'):
    if plugin in lookup:
        prep = prep or lookup[plugin]['voraussetzung']
        area = pluginlabel[plugin]
    else:
        area = plugin
    stepshtml = '<p><strong>Voraussetzungen:</strong> ' + html.escape(prep or 'Eigener Testkurs und eingeschriebene Testkonten auf der Staging-Instanz.') + '</p>'
    stepshtml += '<ol>' + ''.join('<li>' + html.escape(s) + '</li>' for s in steps) + '</ol>'
    values = {f['name']: '' for f in fields}
    values.update(testfall_id=code, titel=title, bereich=area, pruefumfang=scope,
                  person='Noch nicht zugeteilt', rolle=role, browser='Noch nicht zugeteilt',
                  schritte=stepshtml, soll='<p>' + html.escape(expected) + '</p>',
                  ergebnis='Noch offen', schweregrad='Nicht eingestuft',
                  wiederholbarkeit='Noch nicht erneut geprüft', bearbeitung='Nicht nötig')
    cases.append(values)

basecases = [
('BAS-01', 'Profil und persönliche Einstellungen', ['Eigenes Profil und hinterlegte Angaben öffnen.', 'Eine für das Testkonto freigegebene Einstellung ändern, speichern und erneut öffnen.', 'Den vorherigen Wert wiederherstellen.'], 'Profildaten werden korrekt angezeigt; erlaubte Änderungen bleiben nach erneutem Öffnen erhalten.', 'Lehrperson'),
('BAS-02', 'Kurs erstellen und bearbeiten', ['Im Testbereich einen Kurs erstellen.', 'Titel, Beschreibung und Abschnitt ändern; eine Textseite hinzufügen.', 'Kurs erneut öffnen und Änderungen kontrollieren.'], 'Der Kurs lässt sich erstellen und bearbeiten; Inhalte und Einstellungen bleiben gespeichert.', 'Manager/in'),
('BAS-03', 'Teilnehmende einschreiben und entfernen', ['Ein vorgesehenes Testkonto mit der Rolle Lernende einschreiben.', 'Mit diesem Konto Kurszugriff prüfen.', 'Einschreibung entfernen und den Zugriff erneut prüfen; weitere tatsächlich verwendete Einschreibemethoden gesondert dokumentieren.'], 'Der Zugriff entspricht der Einschreibung; entfernte Konten erhalten keinen Zugang über diese Einschreibemethode.', 'Manager/in'),
('BAS-04', 'Rollen und verborgene Inhalte', ['Im Testkurs eine sichtbare und eine verborgene Aktivität anlegen.', 'Mit einem Lernenden-Testkonto die Kursseite und den direkten Link zur verborgenen Aktivität prüfen.', 'Mit der Lehrperson die Bearbeitung und Sichtbarkeit kontrollieren.'], 'Lernende sehen nur freigegebene Inhalte; Lehrpersonen können die vorbereiteten Aktivitäten bearbeiten.', 'Lehrperson und Lernende'),
('BAS-05', 'Dateien hochladen und öffnen', ['Ein Dokument, ein Bild und ein kurzes Video bereitstellen.', 'Alle Materialien mit dem Lernenden-Testkonto öffnen.', 'Eine Datei ersetzen und die aktualisierte Fassung erneut prüfen.'], 'Dateien sind vollständig zugänglich; Bild und Video funktionieren im vorgesehenen Anzeigeweg; die neue Dateiversion ist erreichbar.', 'Lehrperson und Lernende'),
('BAS-06', 'Fragesammlung bearbeiten und wiederverwenden', ['Eine Frage in der Fragesammlung erstellen.', 'Text und richtige Antwort ändern und die Vorschau prüfen.', 'Die Frage in einen Test aufnehmen.'], 'Die gespeicherte Frage lässt sich bearbeiten, in der Vorschau beantworten und im Test verwenden.', 'Lehrperson'),
('BAS-07', 'Testversuch und Bewertung speichern', ['Einen kurzen Test mit eindeutig bewertbaren Fragen bereitstellen.', 'Mit dem Lernenden-Testkonto einen Versuch starten, beantworten und abschliessen.', 'Antworten und Bewertung als Lehrperson und Lernende erneut öffnen.'], 'Abgeschlossener Versuch, Antworten, Punkte und freigegebenes Feedback stimmen mit den definierten Sollwerten überein.', 'Lehrperson und Lernende'),
('BAS-08', 'Aufgabe abgeben und rückmelden', ['Eine Aufgabe mit Dateiabgabe anlegen.', 'Als Lernende eine Datei abgeben.', 'Als Lehrperson Datei öffnen, bewerten und Feedback erfassen; als Lernende das freigegebene Ergebnis öffnen.'], 'Die richtige Datei ist verfügbar; Bewertung und Feedback werden gespeichert und entsprechend der Freigabe angezeigt.', 'Lehrperson und Lernende'),
('BAS-09', 'Abschluss und Zugangsvoraussetzung', ['Für eine Aktivität eine eindeutige Abschlussbedingung festlegen.', 'Eine Folgeaktivität an diesen Abschluss binden.', 'Mit einem Lernenden-Testkonto den Zustand vor und nach Erfüllung der Bedingung prüfen.'], 'Abschlussstatus und Zugang zur Folgeaktivität ändern sich entsprechend der festgelegten Bedingung.', 'Lehrperson und Lernende'),
('BAS-10', 'Forum und persönliche Nachrichten', ['In einem Testforum einen Beitrag erstellen und mit einem zweiten Konto antworten.', 'Eine persönliche Nachricht zwischen zwei vorgesehenen Testkonten senden.', 'Beitrag, Antwort und Nachrichtenverlauf erneut öffnen.'], 'Beiträge und Antworten bleiben gespeichert; die Nachricht ist beim richtigen Testkonto sichtbar. Externer E-Mail-Versand wird gesondert geprüft.', 'Lehrperson und Lernende'),
('BAS-11', 'Kurslogs anzeigen und filtern', ['Mit einem Testkonto eine bekannte Aktivität öffnen.', 'Als Manager/in den Kursbericht mit Logs öffnen.', 'Nach Testkonto und Aktivität filtern und den soeben ausgeführten Vorgang suchen.'], 'Die bekannten Ereignisse sind vorhanden und die Filter grenzen den Bericht korrekt ein.', 'Manager/in'),
('BAS-12', 'Badge und Kriterien konfigurieren', ['Im Testkurs einen Badge mit Testbild erstellen.', 'Ein geeignetes Kriterium festlegen und die Konfiguration speichern.', 'Die Kriterien erneut öffnen; bei aktivierter Vergabe mit einem Testkonto das Kriterium erfüllen und die Vergabe prüfen.'], 'Badge und Kriterien bleiben gespeichert. Eine geprüfte Vergabe entspricht den erfüllten Kriterien; nötige Hintergrundverarbeitung wird im Ergebnis vermerkt.', 'Lehrperson und Lernende'),
('MIG-01', 'Bestehenden Kurs nach der Migration vergleichen', ['Einen repräsentativen bestehenden Kurs in Produktion als Referenz ansehen.', 'Den entsprechenden Kurs auf Staging öffnen.', 'Abschnitte, Texte, Links, Dateien und zentrale Aktivitäten vergleichen; Unterschiede einzeln dokumentieren.'], 'Die vereinbarten Kursinhalte und Beziehungen sind auf Staging vollständig und nutzbar. Die Produktionsreferenz wird für diesen Vergleich nur gelesen.', 'Lehrperson und Lernende'),
('MIG-02', 'Darstellung und Bedienbarkeit prüfen', ['Kursnavigation, ein Formular und eine zentrale Aktivität auf Staging öffnen.', 'Darstellung in normaler und schmaler Fensterbreite prüfen.', 'Wichtige Links, Schaltflächen und Formularfelder auch mit der Tastatur bedienen.'], 'Inhalte bleiben lesbar, Bedienelemente erreichbar und Fehlermeldungen verständlich; es werden keine wesentlichen Inhalte abgeschnitten.', 'Lehrperson und Lernende'),
]
for code, title, steps, expected, role in basecases:
    case(code, 'Migration und Darstellung' if code.startswith('MIG') else 'Grundfunktionen', title, steps, expected, role)

activitycases = [
('ATT-01', 'mod_attendance', 'Anwesenheit erfassen und Bericht prüfen', ['Eine Sitzung anlegen.', 'Für Testkonten unterschiedliche Anwesenheitswerte erfassen und speichern.', 'Die Sitzung und den Bericht erneut öffnen und mit den Eingaben vergleichen.'], 'Anwesenheitswerte und Kommentare sind den richtigen Konten und der richtigen Sitzung zugeordnet.'),
('BOA-01', 'mod_board', 'Pinnwand gemeinsam bearbeiten', ['Board mit zwei Spalten anlegen.', 'Mit zwei Konten Beiträge hinzufügen und einen eigenen Beitrag ändern.', 'Ansicht aktualisieren und Inhalt sowie erlaubte Bearbeitungen prüfen.'], 'Beiträge und Änderungen erscheinen in den vorgesehenen Spalten; die Rechte entsprechen der Konfiguration.'),
('CHK-01', 'mod_checklist', 'Checkliste und Fortschritt', ['Drei Punkte anlegen und die gewünschte Abhakberechtigung einstellen.', 'Mit einem Lernenden-Testkonto zwei Punkte abhaken.', 'Als Lehrperson den Fortschritt und die einzelnen Markierungen kontrollieren.'], 'Nur die abgehakten Punkte sind erledigt; die Fortschrittsanzeige entspricht der Liste.'),
('GRP-01', 'mod_choicegroup', 'Gruppe wählen und Platzgrenze prüfen', ['Zwei Gruppen bereitstellen; für eine Gruppe einen Platz erlauben.', 'Diese Gruppe mit dem ersten Lernenden-Testkonto wählen.', 'Mit dem zweiten Testkonto dieselbe Gruppe versuchen und die tatsächlichen Gruppenmitgliedschaften prüfen.'], 'Die gewählte Mitgliedschaft wird gespeichert; die festgelegte Platzgrenze wird eingehalten.'),
('CER-01', 'mod_customcert', 'Zertifikat gestalten und PDF ausstellen', ['Eine Zertifikatvorlage mit Text, Rahmen, Bild oder Hintergrundbild anlegen.', 'Namen der Lernenden, Kursname und Datum hinzufügen.', 'Mit einem Lernenden-Testkonto ein Zertifikat ausstellen und das PDF öffnen.'], 'Das ausgegebene PDF zeigt die vorgesehenen Elemente, korrekte Werte und eine lesbare Anordnung.'),
('FLA-01', 'mod_flashcard', 'Lernkarten erstellen und durcharbeiten', ['Drei Frage-Antwort-Paare erfassen.', 'Kartensatz öffnen und beide Seiten jeder Karte prüfen.', 'Lerndurchlauf ausführen und den Satz erneut öffnen.'], 'Alle Paare sind korrekt gespeichert und nutzbar; der vorgesehene Lerndurchlauf funktioniert.'),
('JOU-01', 'mod_journal', 'Journaleintrag und Feedback', ['Schreibauftrag anlegen.', 'Als Lernende einen Eintrag verfassen und danach überarbeiten.', 'Als Lehrperson Feedback erfassen; mit dem Lernendenkonto erneut öffnen.'], 'Die überarbeitete Fassung und das Feedback bleiben erhalten; andere Lernende können den privaten Eintrag nicht einsehen.'),
('KAN-01', 'mod_kanban', 'Karten zwischen Spalten verschieben', ['Board mit Spalten Offen, In Arbeit und Erledigt anlegen.', 'Zwei Karten erstellen und eine Karte bearbeiten.', 'Eine Karte verschieben, Seite neu laden und Board mit zweitem Konto prüfen.'], 'Inhalt und Position der Karten bleiben erhalten; Sichtbarkeit entspricht dem gewählten Board-Typ.'),
('PDF-01', 'mod_pdfannotator', 'PDF kommentieren und beantworten', ['Eine kleine mehrseitige PDF-Datei bereitstellen.', 'Eine Passage kommentieren.', 'Mit einem zweiten Konto auf den Kommentar antworten und das Dokument erneut öffnen.'], 'Kommentar und Antwort bleiben der richtigen Passage zugeordnet und sind für berechtigte Konten sichtbar.'),
('PUB-01', 'mod_publication', 'Datei mit Freigabe veröffentlichen', ['Studierendenordner mit einem Freigabeverfahren konfigurieren.', 'Als Lernende eine Testdatei hochladen.', 'Sichtbarkeit vor und nach der vorgesehenen Freigabe mit einem zweiten Lernendenkonto prüfen.'], 'Die richtige Datei wird erst entsprechend dem eingestellten Freigabeverfahren für andere sichtbar.'),
('SCH-01', 'mod_scheduler', 'Termin buchen und freigeben', ['Zwei Zeitfenster mit definierter Platzanzahl anlegen.', 'Als Lernende ein Zeitfenster buchen und als Lehrperson kontrollieren.', 'Buchung soweit erlaubt zurücknehmen oder als Lehrperson entfernen und verfügbare Plätze kontrollieren.'], 'Termin, Person und Platzanzahl sind korrekt; die Aufhebung gibt den Platz wieder frei.'),
('STQ-01', 'mod_studentquiz', 'Frage beitragen und gemeinsam üben', ['StudentQuiz anlegen und Beitrags-/Freigabeeinstellungen prüfen.', 'Als Lernende eine einfache Frage erstellen und gegebenenfalls freigeben lassen.', 'Mit einem zweiten Lernendenkonto beantworten, kommentieren und bewerten.'], 'Frage, Antwortauswertung, Kommentar und Bewertung bleiben gespeichert und folgen den gewählten Freigaberegeln.'),
]
for args in activitycases:
    case(*args)

case('BUC-01', 'booktool_wordimport', 'Word-Datei als Buchkapitel importieren', ['DOCX mit Überschrift 1, Überschrift 2, Text und Bild vorbereiten.', 'Datei über die Importfunktion eines Buchs importieren.', 'Kapitelstruktur, Text und Bild als Lehrperson und Lernende öffnen.'], 'Die Überschriften erzeugen die erwarteten Kapitel; Text und Bild sind vollständig und lesbar.')
case('ARC-01', 'quiz_archive', 'Testversuche als Archivbericht ausgeben', ['Einen kurzen Test mit zwei Lernenden-Testversuchen abschliessen.', 'Im Test den Archivbericht öffnen.', 'Druckansicht beziehungsweise PDF über den Browser erzeugen und beide Versuche vergleichen.'], 'Beide vorgesehenen Versuche enthalten die richtigen Fragen, Antworten und Bewertungen; die Ausgabe ist lesbar.', role='Lehrperson')
case('PRO-01', 'block_completion_progress', 'Abschlussfortschritt im Block', ['Zwei Aktivitäten mit manueller oder eindeutig auslösbarer Abschlussbedingung einrichten.', 'Fortschrittsblock hinzufügen; als Lernende eine Aktivität abschliessen.', 'Block und Übersicht der Lehrperson mit den tatsächlichen Abschlüssen vergleichen.'], 'Erledigte und offene Aktivitäten werden korrekt unterschieden und dem richtigen Konto zugeordnet.')
case('PEO-01', 'block_people', 'Kurskontakte und Links', ['Eine Lehrperson dem Kurs zuordnen und Personenblock hinzufügen.', 'Angezeigte Lehrpersonen und Rollen kontrollieren.', 'Profil-, Nachrichten- und Teilnehmendenlink mit einem Lernenden-Testkonto öffnen.'], 'Die vorgesehenen Kontakte erscheinen; die Links führen zum richtigen Ziel und respektieren die Kursrechte.')
questioncases = [
('ZEI-01','qtype_drawing','Zeichnung abgeben und manuell bewerten',['Eine Zeichnungsfrage erstellen und in einen Test aufnehmen.', 'Als Lernende eine klar erkennbare Zeichnung abgeben.', 'Als Lehrperson die gespeicherte Zeichnung öffnen, kommentieren und bewerten.'],'Zeichnung, Kommentar und manuelle Bewertung werden korrekt gespeichert und angezeigt.'),
('LUE-01','qtype_gapfill','Lücken beantworten und auswerten',['Lückentext mit zwei eindeutigen Lösungen erstellen.', 'In Vorschau oder Test eine richtige und eine falsche Antwort eingeben.', 'Bewertung prüfen; anschliessend beide Lösungen richtig eingeben.'],'Die richtigen und falschen Antworten sowie die erreichten Punkte entsprechen den definierten Lösungen.'),
('KPR-01','qtype_kprime','Vier Aussagen und Teilbewertung',['Vier Aussagen mit bekannten Wahr/Falsch-Lösungen anlegen und Bewertungsmodus festlegen.', 'Eine vollständig richtige und eine teilweise falsche Kombination beantworten.', 'Die erzielten Punkte mit den Regeln des gewählten Modus vergleichen.'],'Die vier Aussagen sind korrekt dargestellt; die Punkte entsprechen dem ausgewählten Bewertungsmodus.'),
('MTF-01','qtype_mtf','Mehrere Wahr/Falsch-Aussagen',['Frage mit mehreren Aussagen und festgelegter Bewertung erstellen.', 'Richtige und falsche Entscheidungen abgeben.', 'Gespeicherte Antworten, Feedback und Punkte prüfen.'],'Antworten und Bewertung stimmen mit den eingestellten Regeln überein.'),
('WOR-01','qtype_wordselect','Zielwörter auswählen',['Einen kurzen Text mit eindeutig markierten Zielwörtern als Frage erstellen.', 'Zielwörter und anschliessend auch ein falsches Wort auswählen.', 'Auswertung und gespeicherte Auswahl kontrollieren.'],'Wörter sind auswählbar; richtige und falsche Auswahl wird gemäss Konfiguration bewertet.'),
]
for args in questioncases:
    case(*args)
case('ICO-01','filter_fontawesome','Symbole in einem Text anzeigen',['In einer Textseite ein zur vorhandenen FontAwesome-Version passendes dokumentiertes Symbolkürzel einfügen.', 'Speichern und die Seite als Lernende öffnen.', 'Text erneut bearbeiten und speichern.'],'Das erwartete Symbol wird im gefilterten Inhalt angezeigt und bleibt nach Bearbeitung erhalten.',role='Lehrperson')
for code, plugin, title, action in [
('ATO-01','atto_c4l','C4L-Baustein in Atto','Einen C4L-Lernbaustein einfügen und mit einem kurzen Text füllen.'),
('ATO-02','atto_morebackcolors','Texthintergrund in Atto','Einen Textabschnitt markieren und eine verfügbare Hintergrundfarbe wählen.'),
('ATO-03','atto_morefontcolors','Schriftfarbe in Atto','Einen Textabschnitt markieren und eine verfügbare Schriftfarbe wählen.'),
('TIN-01','tiny_c4l','C4L-Baustein in TinyMCE','Einen C4L-Lernbaustein einfügen und mit einem kurzen Text füllen.'),
('TIN-02','tiny_fontcolor','Schrift- und Hintergrundfarbe in TinyMCE','Zwei Textabschnitte jeweils mit Schrift- und Hintergrundfarbe formatieren.'),
]:
    editor='Atto' if plugin.startswith('atto_') else 'TinyMCE'
    case(code,plugin,title,[f'{editor} als verfügbaren Editor verwenden und eine Textseite bearbeiten.',action,'Speichern, als Lernende ansehen und danach nochmals bearbeiten.'],'Die gewählte Gestaltung bleibt erhalten; der Inhalt ist lesbar und weiter bearbeitbar.',prep=lookup[plugin]['voraussetzung']+' Falls der Editor im Zielbetrieb entfällt: mit Thomas klären und begründet als Entfällt dokumentieren; vorhandene Inhalte weiterhin prüfen.')
for code, plugin, title, action in [
('FOR-01','format_flexsections','Verschachtelte Kursabschnitte','Einen Abschnitt mit Unterabschnitt anlegen und eine Aktivität einfügen.'),
('FOR-02','format_tiles','Kacheln und Aktivitätszugriff','Zwei Kacheln gestalten und jeweils eine Aktivität zuordnen.'),
('FOR-03','format_topcoll','Aufklappbare Kursabschnitte','Mehrere Abschnitte anlegen und einzeln auf- und zuklappen.'),
]:
    case(code,plugin,title,['Im eigenen Testkurs das vorgesehene Format auswählen.',action,'Eine Aktivität bearbeiten und danach als Lernende über die Kursnavigation öffnen; auch schmale Fensterbreite prüfen.'],'Abschnitte und Aktivitäten bleiben korrekt erreichbar; Darstellung und Bearbeitung funktionieren in beiden Rollen.')

# Unterbausteine werden innerhalb von Custom certificate als konkrete zusätzliche Vorgänge geprüft.
case('CER-02','mod_customcert','Kurs-, Personen- und Bewertungsfelder im Zertifikat',['Ein Testkonto mit Profilbild, bekannten Profilwerten und einer bekannten Bewertung vorbereiten.', 'Kategoriename, Kursname, Kursfeld, Lernendenname, Lehrpersonenname, Nutzerfeld, Profilbild, Bewertung und Name des Bewertungselements in die Vorlage aufnehmen.', 'Zertifikat tatsächlich ausstellen und alle Werte mit den vorbereiteten Sollwerten vergleichen.'],'Jedes ausgewählte Element zeigt den richtigen Wert für das ausstellende Kurs-/Nutzerkontext; keine Platzhalter oder fremden Bewertungen.',prep='Vorbereitete Testdaten und im Zielbetrieb verwendete Zertifikatsfelder; fehlende Voraussetzungen zuerst klären.',scope='Nach Vorbereitung')
case('CER-03','mod_customcert','Zertifikatscode und QR-Code prüfen',['Code und QR-Code in ein Testzertifikat aufnehmen.', 'Zertifikat für ein Lernenden-Testkonto ausstellen.', 'QR-Code scannen und die vorgesehene Verifikationsfunktion mit dem ausgegebenen Code prüfen.'],'QR-Code und Code beziehen sich auf das richtige ausgestellte Zertifikat; die konfigurierte Verifikation liefert das erwartete Ergebnis.',prep='Zertifikatvorlage mit eingerichteter Verifikation, sofern im Betrieb verwendet.',scope='Nach Vorbereitung')
case('CER-04','mod_customcert','Datum, Zeitraum und Ablaufdatum',['Die verwendeten Datumsquellen und erwarteten Werte festlegen.', 'Datum, Datumsbereich und Ablaufdatum soweit installiert und vorgesehen einfügen.', 'Ein tatsächlich ausgestelltes PDF kontrollieren. Zeitabhängiges Verhalten mit einem eigenen Termin planen.'],'Die ausgegebenen Datumswerte entsprechen den festgelegten Quellen und Regeln.',prep='Installierte Datumselemente, bekannte Bezugsdaten und definierte Ablaufeinstellung.',scope='Nach Vorbereitung')
case('CER-05','mod_customcert','Digitale PDF-Signatur prüfen',['Mit der Informatik eine geeignete Test-Signaturdatei und Konfiguration bereitstellen.', 'Das Element für die digitale Signatur konfigurieren und ein Zertifikat ausstellen.', 'Die Signaturinformationen im PDF-Programm prüfen und mit den vorgegebenen Test-Sollwerten vergleichen.'],'Das PDF enthält die erwartete digitale Signatur. Ein sichtbares Unterschriftsbild allein gilt nicht als Nachweis.',prep='Signaturdatei, erforderliche Berechtigungen und festgelegte Prüfkriterien der Informatik.',scope='Nach Vorbereitung')

assert len(cases) == 48, len(cases)
assert len({c['testfall_id'] for c in cases}) == len(cases)
assert {p['plugin'] for p in plugins if p['kategorie']=='A'} == {
    p for p,label in pluginlabel.items() if any(c['bereich']==label for c in cases)
}
spec = dict(name='Moodle-Testing 5.2 · Strickhof', fields=fields, records=cases,
            testsite='https://moodlestaging.strickhof.ch',
            protocolsite='https://moodle.strickhof.ch')
(OUT/'datenbank.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n')
with (OUT/'testfaelle.csv').open('w',newline='') as handle:
    writer=csv.DictWriter(handle,fieldnames=[f['label'] for f in fields])
    writer.writeheader()
    writer.writerows({f['label']:c[f['name']] for f in fields} for c in cases)
print(f'{len(fields)} Felder, {len(cases)} vorbereitete Testfälle, alle 30 ausgewählten Hauptplugins enthalten.')
