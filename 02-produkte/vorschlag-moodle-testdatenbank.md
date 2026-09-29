---
title: "Vorschlag für eine Moodle-Datenbank zur Testdokumentation"
author: lamt
date: 2026-09-29
status: Entwurf
---

# Vorschlag für eine Moodle-Datenbank zur Testdokumentation

Dieser Entwurf beschreibt eine gemeinsame Testdatenbank für Thomas und die drei testenden Lehrpersonen. Er baut auf dem [bisherigen Testablauf](../01-kontextwissen/bisheriger-testablauf.md) und dem [Vergleich der Moodle-Aktivitäten](../01-kontextwissen/moodle-aktivitaetstypen.md) auf. Die Feldstruktur ist ein Vorschlag; in Moodle wurde noch nichts eingerichtet.

**Ergänzung vom 29.09.2026:** Für das Vorhaben ist Moodle 5.2 angegeben (Moodle SaaS: 3000; Speicherplatz: 800 GB). Die Tests finden auf `https://moodlestaging.strickhof.ch` statt; die Testdatenbank liegt gemäss bestätigter Entscheidung auf `https://moodle.strickhof.ch`. Ziel ist eine `.mbz` mit Anleitung, Feldern, Ansichten und vorbereiteten Testfällen. Die [Aktivitätsanleitung](anleitung-testdatenbank.md) enthält die Umgebungsangaben und Dokumentationslinks; die [MBZ-Planung](planung-testdatenbank-mbz.md) hält Umsetzung und Abnahme fest.

Empfehlung: Pro Upgrade eine Datenbank mit dem Namen «Moodle-Testing – [Upgrade / Zeitraum]». Sie enthält geplante Tests, erfolgreiche Durchführungen, Fehler und Nachtests. Damit ist auch sichtbar, was noch ungeprüft ist.

Ein Eintrag steht für **einen konkreten Testfall, eine testende Person, eine Browser-/Gerätekombination und einen Durchlauf**. Beispielsweise: «Eine Datei als Lernende abgeben» statt pauschal «Aufgabe funktioniert». Eine zweite Person oder ein anderer Browser erhält einen eigenen Eintrag. Ein Nachtest wird ebenfalls separat erfasst und mit dem ursprünglichen Eintrag verknüpft.

Die Datenbank-Aktivität unterstützt passende Feldtypen, Pflichtfelder sowie anpassbare Eingabe-, Listen- und Einzelansichten. Die Gestaltung unten ist ein darauf aufbauender Prozessvorschlag. Quellen: [MoodleDocs: Felder](https://docs.moodle.org/501/en/Building_Database), [MoodleDocs: Vorlagen](https://docs.moodle.org/502/en/Database_templates).

**Vorbereitung durch Thomas**

Vor dem Start werden die vereinbarten Testfälle mit Testfall-ID, Schritten und erwartetem Ergebnis vorbereitet und den Lehrpersonen sowie Browsern zugeordnet. Auch eine noch nicht getestete Kombination erhält einen Eintrag mit «Noch offen». Zusätzliche Beobachtungen können die Lehrpersonen selbst als neue Testfälle anlegen.

In der Beschreibung der Datenbank stehen einmalig Testzeitraum, Frist für Rückmeldungen, Testsystem, Zuständigkeiten und die Regel für das Go/No-Go. Eine kleine Tabelle erklärt die auswählbaren Teststände: eindeutige Kennung, Datum der Bereitstellung, genaue Moodle-Version und Verweis auf den Plugin-Stand. Nach einer Korrektur erhält das System eine neue Teststand-Kennung. Bereits verwendete Kennungen werden nicht umgedeutet.

**Felder für Planung und Testergebnis**

«Bei Durchführung» bezeichnet eine fachliche Anforderung. Damit vorbereitete Einträge gespeichert werden können, bleiben solche Felder technisch optional, sofern keine zusätzliche Validierung eingerichtet wird. Die Vollständigkeit wird vor Abschluss kontrolliert.

| Feld | Moodle-Feldtyp | Inhalt und Verwendung |
| --- | --- | --- |
| Testfall-ID | Text | Pflicht ab Planung. Stabile Kennung, z. B. `AUF-01`; bei anderen Browsern und Nachtests dieselbe Kennung. Vergabe koordiniert Thomas. |
| Kurztitel | Text | Pflicht ab Planung. Konkreter Vorgang, z. B. «Datei als Lernende abgeben». |
| Bereich / Aktivität / Plugin | Auswahlmenü | Pflicht ab Planung. Einheitliche Liste der Grundfunktionen, Aktivitäten und tatsächlich installierten Plugins. |
| Testende Person | Auswahlmenü | Pflicht ab Planung. Namen der drei Lehrpersonen und bei Bedarf Thomas; bei Durchführung muss die tatsächlich testende Person eingetragen sein. |
| Getestete Rolle | Auswahlmenü | Pflicht ab Planung. Lernende, Lehrperson, Manager/in, Administrator/in; je Eintrag die relevante Rolle. |
| Browser | Auswahlmenü | Pflicht ab Planung. Die für den Test vereinbarten Browser. Bei Durchführung den tatsächlich verwendeten Browser eintragen. |
| Browser-Version, Betriebssystem und Gerät | Text | Bei Durchführung. Beispiel für das Format: «Firefox [Version], Windows [Version], Laptop». Bei mobilen Tests das Gerät genauer benennen. |
| Teststand | Auswahlmenü | Bei Durchführung. Eindeutige Kennung aus der zentralen Übersicht, z. B. «Stand A» oder «Stand B nach Korrektur». |
| Testdatum | Datum | Bei Durchführung. Tatsächliches Datum des Tests. |
| Kurs / Aktivität | URL | Bei Durchführung, soweit anwendbar. Direkter Link zur untersuchten Stelle im Testsystem. |
| Voraussetzungen und Testschritte | Textbereich | Pflicht ab Planung. Benötigte Einstellungen, Testdaten und nummerierte Schritte; bei Durchführung Abweichungen ergänzen. |
| Erwartetes Ergebnis | Textbereich | Pflicht ab Planung. Beobachtbares Erfolgskriterium, z. B. «Datei ist abgegeben und für die Lehrperson sichtbar». |
| Tatsächliches Ergebnis | Textbereich | Bei Durchführung. Bei Erfolg reicht eine knappe Bestätigung des beobachteten Resultats; bei Problemen genaue Beobachtung und Wortlaut einer Fehlermeldung. |
| Testergebnis | Auswahlmenü | Pflicht ab Planung. «Noch offen», «Bestanden», «Fehler», «Blockiert», «Entfällt». Startwert ist «Noch offen». |
| Bezug zum früheren Eintrag | URL | Bei Nachtests oder bereits bekanntem Problem. Direkter Link zum ursprünglichen Testeintrag. |

Die getestete Rolle ist von der Person zu unterscheiden: Eine Lehrperson kann einen Test mit einem Lernenden-Testkonto durchführen. Bei Prüfungen von Berechtigungen und Sichtbarkeit ist ein passendes Testkonto vorzusehen.

Der automatisch angezeigte Autor ist die Person, die den Eintrag angelegt hat. Bei vorbereiteten Einträgen ist das häufig Thomas. Deshalb braucht es zusätzlich das Feld «Testende Person». Erstellungs- und Änderungszeit können über die Vorlage angezeigt werden; das Testdatum bleibt ein eigener Wert. Quelle: [MoodleDocs: Vorlagen-Tags](https://docs.moodle.org/502/en/Database_templates).

**Zusatzfelder bei Fehlern oder blockierten Tests**

Diese Felder stehen in einem eigenen Formularabschnitt. Bei erfolgreichen Tests dürfen sie leer bleiben. «Nur bei Problemen ausfüllen» ist zunächst eine Arbeitsanweisung; eine automatische bedingte Pflichtprüfung ist nicht Bestandteil dieses Entwurfs.

| Feld | Moodle-Feldtyp | Inhalt und Verwendung |
| --- | --- | --- |
| Auswirkung / Schweregrad | Auswahlmenü | Kritisch, erheblich, gering; Definitionen unten. Bei Fehlern erforderlich. |
| Wiederholbarkeit | Auswahlmenü | Jedes Mal, gelegentlich, einmal beobachtet, noch nicht erneut geprüft. Bei Bedarf Häufigkeit im tatsächlichen Ergebnis ergänzen. |
| Screenshot | Bild | Wenn er das Problem verständlicher macht. |
| Ergänzende Datei | Datei | Bei Bedarf etwa eine verwendete Testdatei oder zusätzliche Dokumentation. |
| Hindernis / Übergangslösung | Textbereich | Bei blockierten Tests: Warum ist der Test nicht möglich? Bei Fehlern: Gibt es eine brauchbare Übergangslösung und welche Nachteile hat sie? |

Ein vollständiger Fehlerbericht enthält den betroffenen Bereich, Umgebung und Teststand, Voraussetzungen, Schritte, Soll- und Ist-Ergebnis sowie die Auswirkung. Ein Screenshot ergänzt die Beschreibung.

**Felder für Koordination und Nachverfolgung**

| Feld | Moodle-Feldtyp | Inhalt und Verwendung |
| --- | --- | --- |
| Bearbeitungsstatus | Auswahlmenü | «Nicht nötig», «Neu», «In Klärung», «Beim Dienstleister», «Bereit zum Nachtest», «Abgeschlossen», «Akzeptiertes Restrisiko». |
| Zuständig für nächsten Schritt | Text | Konkrete Person; z. B. Thomas für die Ticketaufnahme oder eine Lehrperson für den Nachtest. |
| Termin für nächsten Schritt | Datum | Sobald eine weitere Bearbeitung nötig ist. |
| Ticketnummer | Text | Nach Eröffnung beim Dienstleister; auch bei weiteren Einträgen zum gleichen Fehler dieselbe Nummer verwenden. |
| Ticketlink | URL | Direkter Verweis auf das Ticket, sofern verfügbar. |
| Bearbeitungsverlauf / Entscheid | Textbereich | Datierte kurze Ergänzungen: Klärung, Rückmeldung des Dienstleisters, Verweis auf den Nachtest und Abschlussgrund. Bei akzeptiertem Restrisiko auch Begründung und entscheidende Person. |

Thomas pflegt die Koordinationsfelder. Das ist zunächst eine organisatorische Zuständigkeit. Die tatsächlichen Bearbeitungsrechte der Kursrollen müssen bei der Einrichtung geprüft werden; ein entsprechend beschrifteter Formularabschnitt begrenzt noch keine Rechte.

Kommentare können für Rückfragen genutzt werden. Entscheidungen, Ticketnummer und Nachtest-Verweis werden zusätzlich in den dafür vorgesehenen Feldern dokumentiert, damit sie in der Auswertung erhalten bleiben.

**Bedeutung der Ergebnisse und Schweregrade**

| Testergebnis | Bedeutung |
| --- | --- |
| Noch offen | Geplant, aber noch nicht durchgeführt. |
| Bestanden | Die vorgesehenen Schritte wurden ausgeführt und das erwartete Ergebnis wurde beobachtet. |
| Fehler | Das tatsächliche Ergebnis weicht vom erwarteten Ergebnis ab. |
| Blockiert | Die Prüfung ist wegen einer fehlenden Voraussetzung nicht möglich, z. B. fehlendem Testkonto. Das ist kein erfolgreicher Test. |
| Entfällt | Bewusst aus dem Umfang genommen; Thomas bestätigt die Begründung im Bearbeitungsverlauf. |

| Schweregrad | Orientierung für die Einordnung |
| --- | --- |
| Kritisch | Zentrale Nutzung unmöglich, unzulässiger Zugriff oder Verlust wesentlicher Daten bzw. Ergebnisse; keine brauchbare Übergangslösung. Sofort an Thomas melden. |
| Erheblich | Eine wichtige Funktion ist beeinträchtigt; eine Übergangslösung ist möglich oder nur ein Teil der Nutzung betroffen. |
| Gering | Begrenztes Darstellungs- oder Komfortproblem; der Vorgang bleibt korrekt ausführbar. |

Testergebnis und Bearbeitungsstatus beantworten unterschiedliche Fragen. Ein ursprünglicher Test kann dauerhaft «Fehler» zeigen und nach erfolgreichem Nachtest den Bearbeitungsstatus «Abgeschlossen» erhalten. Das belegte frühere Fehlverhalten bleibt dadurch sichtbar.

**Darstellung und Suche**

Für die Listenansicht genügen diese Spalten: Testfall-ID mit Kurztitel, Bereich, Person, Browser, Teststand, Testergebnis, Schweregrad und Bearbeitungsstatus. Längere Texte und Bilder erscheinen in der Einzelansicht. Farben dürfen das Ergebnis ergänzen; die Statuswörter bleiben sichtbar.

Die erweiterte Suche erhält insbesondere Felder für Testfall-ID, Bereich, Person, Browser, Teststand, Testergebnis, Schweregrad und Bearbeitungsstatus. So lassen sich offene Tests, Fehler und anstehende Nachtests gezielt suchen. Listen-, Einzel-, Eingabe- und Suchvorlage sind Teil der Moodle-Datenbank. Quelle: [MoodleDocs: Datenbankvorlagen](https://docs.moodle.org/502/en/Database_templates).

Eine automatische Gesamtampel oder Berechnung der Testabdeckung ist nicht Bestandteil der ersten Umsetzung. Thomas gleicht die Ergebnisse mit den geplanten Testkombinationen ab. Zusätzliche Fehlerberichte und Nachtests dürfen dabei nicht als zusätzliche erledigte Pflichtfälle gezählt werden.

**Testumfang aus der bisherigen Checkliste**

**Entscheidung vom 29.09.2026:** `mod_chat` und `mod_survey` sind vom künftigen Testumfang ausgeschlossen und werden weder als Plugin-Auswahlwerte noch als vorbereitete Testfälle aufgenommen.

Die bestehende Checkliste wird in konkrete Vorgänge zerlegt. Ausgangspunkte sind:

- Benutzerprofil prüfen; Anmeldung und Zugriff ergänzend als grundlegende Vorgänge aufnehmen.
- Kurs erstellen und bestehenden Kurs bearbeiten; vorhandene Inhalte nach dem Upgrade prüfen.
- Teilnehmende einschreiben und entfernen; relevante Einschreibemethoden testen.
- Rollen und Sichtbarkeit prüfen; berechtigten sowie unberechtigten Zugriff berücksichtigen.
- Block hinzufügen und konfigurieren.
- Berichte öffnen und Logs filtern.
- Badge anlegen und an Kriterien binden.
- Fragesammlung bearbeiten.
- Dokumente, Bilder und Videos hochladen und aus Lernendensicht öffnen.
- Messaging nutzen und Forumseintrag erstellen.
- Vereinbarte Plugins in einem typischen Unterrichtsablauf prüfen.

Bei Aktivitäten werden die benötigten Vorgänge getrennt betrachtet: anlegen, konfigurieren, als Lernende nutzen und gegebenenfalls Ergebnisse oder Bewertungen prüfen. Bestehende Inhalte und neu erstellte Inhalte erhalten bei Bedarf eigene Testfälle.

Die bisherige Vorgabe «mindestens fünf Plugins pro Person» kann zur Arbeitsverteilung dienen. Für die Abdeckung braucht es zusätzlich eine vollständige Liste der tatsächlich zu prüfenden Plugins und Abläufe. Thomas verteilt diese auf die drei Lehrpersonen. Zentrale Vorgänge werden gezielt auf den vereinbarten Browsern und mindestens durch eine zweite Person geprüft. Nicht jeder kleine Vorgang muss von allen dreimal getestet werden.

Browser und Geräte werden vor Beginn bewusst verteilt. Das bestehende Ziel, unterschiedliche Browser-Engines abzudecken, bleibt bestehen. Welche Kombinationen tatsächlich verfügbar und erforderlich sind, wird vor dem Befüllen des Testplans festgelegt.

**Bearbeitung und Abschluss**

1. Thomas bereitet Testumfang, Teststände, Zuständigkeiten und offene Einträge vor. Die Lehrpersonen prüfen ihre Zuteilung.
2. Die Lehrpersonen testen und dokumentieren auch erfolgreiche Ergebnisse. Weitere Testfälle können sie selbst ergänzen.
3. Bei Fehlern ergänzt die testende Person die Problemdetails und setzt den Bearbeitungsstatus auf «Neu». Bei einem blockierten Test werden Hindernis und nächster Schritt geklärt.
4. Thomas prüft die Meldung, bündelt Einträge zum gleichen Fehler und eröffnet bei Bedarf ein Ticket. Die zugehörigen Einträge erhalten dieselbe Ticketnummer.
5. Nach Bereitstellung einer Korrektur wird der neue Teststand dokumentiert. Der ursprüngliche Eintrag erhält «Bereit zum Nachtest» und eine zuständige Person.
6. Die zuständige Lehrperson erstellt einen neuen Durchlauf mit derselben Testfall-ID, dem neuen Teststand und einem Link zum ursprünglichen Eintrag. Sie führt den Test erneut aus.
7. Thomas schliesst die Bearbeitung erst mit einem dokumentierten erfolgreichen Nachtest ab oder hält ausdrücklich ein akzeptiertes Restrisiko fest. Scheitert der Nachtest, bleibt das Problem in Bearbeitung.
8. Vor dem Go/No-Go prüft Thomas die vollständige geplante Abdeckung, verbleibende Fehler und blockierte Tests. Die einzelnen Rückmeldungen der drei Lehrpersonen sowie der abschliessende Entscheid mit Datum werden weiterhin ausdrücklich dokumentiert.

Empfohlene Freigabekriterien: Alle vereinbarten Pflichtfälle sind auf dem freizugebenden Stand bestanden oder eine frühere Prüfung wurde nach Bewertung der Änderungen ausdrücklich als weiterhin gültig bestätigt. Es gibt keine offenen kritischen Fehler und keine ungeklärten blockierten Pflichtfälle. Für verbleibende erhebliche oder geringe Fehler sind Auswirkung, Zuständigkeit und Akzeptanz dokumentiert. Die Freigabe wird nicht allein aus der Anzahl grüner Einträge abgeleitet.

**Empfohlene Moodle-Einstellungen und Einführung**

- Alle Testenden können von Anfang an die Einträge des ganzen Testteams sehen. Keine Einträge als Voraussetzung für das Lesen verlangen; keine Gruppentrennung vorsehen.
- Freigabe neuer Einträge deaktivieren, damit Rückmeldungen unmittelbar sichtbar sind. Kommentare aktivieren, Bewertungen deaktivieren und genügend Einträge pro Person zulassen. Diese Optionen sind in den [Moodle-Datenbankeinstellungen](https://docs.moodle.org/502/en/Database_activity_settings) beschrieben.
- Rollen so einrichten, dass die Lehrpersonen die vorgesehenen Einträge bearbeiten können und Thomas die Koordination übernehmen kann. Bei von Thomas vorbereiteten Einträgen muss die Bearbeitung durch die zugeteilte Lehrperson ausdrücklich geprüft werden.
- Eingabeformular in Planung/Test, Problemdetails und Koordination gliedern. Vorbereitete Felder reduzieren den Aufwand bei erfolgreichen Tests.
- Testprotokoll an einem Ort führen, an dem es beim Erneuern der Testinstanz erhalten bleibt. Vor einer Erneuerung die Einträge samt Belegen sichern.
- Nach Abschluss Einträge exportieren und Belege mitnehmen; CSV/ODS-Export und das Einbeziehen von Dateien sind dokumentiert. Einen Beispielexport auf Vollständigkeit prüfen, insbesondere Zuordnung und Lesbarkeit der Belege. Quelle: [MoodleDocs: Einträge exportieren](https://docs.moodle.org/501/en/Using_Database#Exporting_entries).
- Vor dem Einsatz drei Probeeinträge durchspielen: Erfolg, Fehler mit Ticket und erfolgreicher Nachtest. Dabei Sichtbarkeit, Bearbeitungsrechte, Suche und Export mit einer testenden Lehrperson prüfen.

Offen für die konkrete Einrichtung bleiben die Namen und konkreten Kursrechte der Testenden, Browser-/Geräteverteilung, Testfristen, der genaue Ablagekurs sowie die für Moodle 5.2 tatsächlich freigegebenen Plugin-Versionen. Die gelieferte Plugin-Liste ist in der [Plugin-Einordnung](plugin-testbarkeit.md) dokumentiert. Moodle-Version, Protokollinstanz und Lieferumfang wurden am 29.09.2026 wie oben festgehalten ergänzt.
