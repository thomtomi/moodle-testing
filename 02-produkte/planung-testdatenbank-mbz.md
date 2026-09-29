---
title: "Planung – Moodle-Testdatenbank als MBZ"
author: lamt
date: 2026-09-29
status: Planung; Grundumfang und Ablageort bestätigt
---

# Planung der Moodle-Testdatenbank als MBZ

Ziel ist eine funktionierende Testdatenbank für Moodle 5.2, ausgeliefert als wiederherstellbare Aktivitätssicherung mit der Endung `.mbz`. Dieses Dokument hält den bestätigten Umfang, den empfohlenen Aufbau und die nötigen Funktionsprüfungen fest. Eine MBZ-Datei wurde in dieser Planungsphase noch nicht erstellt.

**Bestätigte Angaben vom 29.09.2026**

| Punkt | Vorgabe |
| --- | --- |
| Produkt | Moodle SaaS: 3000 |
| Speicherplatz | 800 GB |
| Moodle-Version für das Vorhaben | 5.2 |
| Ort der Testdurchführung | `https://moodlestaging.strickhof.ch` |
| Ort der Datenbank mit Testprotokollen | `https://moodle.strickhof.ch` |
| Lieferumfang | Anleitung, Felder, Ansichten und vorbereitete Testfälle in einer `.mbz` |
| Testteam | Drei Lehrpersonen mit Manager-Rechten; Thomas koordiniert |
| Ausgeschlossene Plugins | `mod_chat` und `mod_survey`; keine Auswahlwerte oder Testfälle in der geplanten Datenbank |
| Aktivitätsanleitung | [Anleitung mit Umgebungsangaben und Dokumentationslinks](anleitung-testdatenbank.md) |

Die Bezeichnung «Moodle SaaS: 3000» wird unverändert übernommen. Aus der Zahl wird keine eigenständige Aussage über gleichzeitige Nutzung, Testlast oder sonstige Kapazitäten abgeleitet.

Die beiden Liip-Dokumente sind in der Anleitung verlinkt. Ihre Inhalte konnten mit den verfügbaren Werkzeugen nicht abgerufen werden und sind noch nicht in konkrete Testfälle eingeflossen. Zugängliche Auszüge können später zur Ergänzung des Testkatalogs verwendet werden.

**Empfohlener Aufbau**

Grundlage bleibt der [Feld- und Prozessentwurf](vorschlag-moodle-testdatenbank.md). Die Umsetzung verwendet die Moodle-Standardaktivität Datenbank (`mod_data`) und deren Standardfelder. Die zu testenden Plugins werden als Auswahlwerte und Testfallinhalte geführt; die Dokumentationsaktivität soll keine zusätzlichen Datenbank-Feldplugins benötigen.

| Teil | Geplanter Inhalt |
| --- | --- |
| Aktivitätsbeschreibung | Zweck, Testsystem, Protokollablage, Umgebungsangaben, Liip-Links und kurze Arbeitsanleitung |
| Eingabeformular | Gruppierte Felder für Testplanung, Durchführung, Problemdetails und Koordination |
| Listenansicht | Kompakte Übersicht mit Testfall, Person, Browser, Teststand, Ergebnis und Bearbeitungsstatus |
| Einzelansicht | Vollständiger Testfall mit Schritten, Soll-/Ist-Ergebnis, Belegen und Verlauf |
| Erweiterte Suche | Testfall-ID, Bereich/Plugin, Person, Browser, Teststand, Ergebnis und Bearbeitungsstatus |
| Vorbereitete Einträge | Konkrete Prüfvorgänge mit stabilen Testfall-IDs, Schritten und erwartetem Ergebnis; Startstatus «Noch offen» |
| Lieferung | Wiederherstellbare `.mbz`, bearbeitbare Quelldateien und ein dokumentiertes Prüfprotokoll |

Ein Eintrag entspricht einem Testfall pro Person, Browser-/Gerätekombination und Durchlauf. Nachtests erhalten einen eigenen Eintrag und einen Verweis auf den ursprünglichen Test. Person und Browser werden vor dem Start zugeteilt; solange Namen und Verteilung fehlen, werden neutrale Platzhalter im Entwurf verwendet.

Die Such- und Listenansichten beruhen auf Moodle-Funktionen. Farben unterstützen Statuswörter. Notwendige Eingabe- und Suchfunktionen sollen ohne eigenes JavaScript funktionieren. Automatische Gesamtfreigaben und feldweise Rollenrechte werden nicht als Teil der Standarddatenbank vorausgesetzt.

**Vorbereitete Testfälle**

Die [Plugin-Einordnung](plugin-testbarkeit.md) liefert nach dem bestätigten Ausschluss von `mod_chat` und `mod_survey` die Ausgangsliste: 30 direkt bedienbare Hauptplugins, 6 mit besonderen Voraussetzungen, 30 Unterbausteine und 5 technische Integrationen. Diese Kategorien beschreiben die Testbarkeit. Sie bestätigen weder die Installation noch die Kompatibilität einer konkreten Plugin-Version mit Moodle 5.2.

- Grundfunktionen aus dem bestehenden Testprozess werden als konkrete Vorgänge vorbereitet.
- Für die im Betrieb vorgesehenen direkt bedienbaren Plugins werden Testfälle mit klaren Erfolgskriterien angelegt.
- Besondere Voraussetzungen, beispielsweise eine fertige HotPot-Datei oder ein eingerichteter Bewertungsdienst, stehen im jeweiligen Testfall.
- Unterbausteine von Custom certificate und HotPot werden dem Hauptplugin zugeordnet und gezielt in dessen Prüfschritte aufgenommen.
- Technische Integrationen erhalten nur abgestimmte Testaufträge mit passender Zuständigkeit.
- Zur Migration gehören auch vorhandene Kursinhalte, Darstellung und Konsistenz; die Liip-Checkliste wird nach inhaltlichem Zugriff abgeglichen.

Vor der endgültigen Befüllung wird die Plugin-Liste für Moodle 5.2 auf den tatsächlich vorgesehenen Umfang geprüft. Beispielsweise werden Atto-Plugins nur für Funktionstests eingeplant, wenn Atto auf dem Zielsystem angeboten wird; vorhandene damit erstellte Inhalte bleiben Teil der Inhaltsprüfung.

**Erstellung der MBZ und Übernahme der Testeinträge**

Eine einzelne Aktivität kann in Moodle als `.mbz` gesichert und in einem anderen Kurs wiederhergestellt werden. Das ist der geplante Lieferweg. Quelle: [Moodle 5.2: Aktivität sichern](https://docs.moodle.org/502/en/Activity_backup), [Aktivität wiederherstellen](https://docs.moodle.org/502/en/Activity_restore).

Eine Datenbank-Vorlagendatei enthält Felder und Ansichten, aber keine Einträge. Für die Übernahme vorbereiteter Datenbankeinträge durch eine Aktivitätssicherung sind Nutzerdaten und die Zuordnung der Einträge zu einem Autor zu berücksichtigen. Quellen: [Moodle: Datenbankvorlagen](https://docs.moodle.org/502/en/Building_Database), [Moodle: Datenbank-FAQ zur Sicherung von Einträgen](https://docs.moodle.org/500/en/Database_FAQ).

Deshalb wird früh eine kleine Sicherung mit wenigen vorbereiteten Testeinträgen wiederhergestellt. Dabei werden Einträge, Autorenzuordnung und Bearbeitbarkeit geprüft, bevor der vollständige Testkatalog eingebaut wird. Vorlageninhalte werden gezielt zusammengestellt; reale Testergebnisse und Kurskonten gehören nicht zum vorbereiteten Testkatalog.

Eine kleine Referenzsicherung einer Datenbankaktivität aus Moodle 5.2 ist für die Erstellung hilfreich. Sie soll Standardfelder und nach Möglichkeit einen neutralen Beispieleintrag enthalten. Falls keine Referenzdatei verfügbar ist, kann die Struktur anhand der Moodle-Sicherungsspezifikation vorbereitet werden; der praktische Wiederherstellungstest bleibt erforderlich.

Im lokalen Arbeitsbereich sind keine Moodle-Laufzeit, PHP oder Containerwerkzeuge vorhanden. Die Prüfung in Moodle muss daher auf einer verfügbaren Moodle-5.2-Instanz oder einer später eingerichteten Prüfumgebung erfolgen. Für das vorhandene Staging-System ist zunächst eine Wiederherstellung in einem eigenen Testkurs vorgesehen.

**Abnahmekriterien**

| Prüfung | Erwartetes Ergebnis |
| --- | --- |
| Wiederherstellung | Die `.mbz` lässt sich in Moodle 5.2 in einem eigenen Kurs wiederherstellen. |
| Anleitung | SaaS-Angaben, Domains und beide Liip-Links werden vollständig und korrekt angezeigt. |
| Testfallbestand | Alle vorgesehenen Testfälle sind nach Wiederherstellung vorhanden und stehen auf «Noch offen». |
| Ausschlüsse | `mod_chat` und `mod_survey` sind weder als Plugin-Auswahlwerte noch als vorbereitete Testfälle enthalten. |
| Autorenzuordnung | Vorbereitete Einträge sind korrekt zugeordnet; die tatsächlich testende Person bleibt ein eigenes Feld. |
| Bearbeitungsrechte | Eine Lehrperson mit der vorgesehenen Manager-Rolle kann zugeteilte Einträge bearbeiten und zusätzliche anlegen. |
| Pflichtfelder | Vorbereitete offene Tests sind speicherbar; ein klar unvollständiger Pflichtfeld-Eintrag wird abgewiesen. |
| Erfolgreicher Test | Ergebnis, Datum, Person, Umgebung und Teststand lassen sich erfassen und wieder öffnen. |
| Fehlermeldung | Soll-/Ist-Ergebnis, Schweregrad, Screenshot und Ticketverweis bleiben nach Speichern erhalten. |
| Nachtest | Ein neuer Durchlauf kann auf den Ursprung verweisen, ohne das ursprüngliche Ergebnis zu überschreiben. |
| Suche und Übersicht | Gezielte Suche nach offenen Tests, Bereich, Person, Browser und Fehlerstatus liefert die erwarteten Einträge. |
| Darstellung | Formular, Liste und Einzelansicht sind auf den vorgesehenen Geräten lesbar und bedienbar. |
| Export und erneute Sicherung | Ergebnisse lassen sich exportieren; Belege bleiben in einer erneuten Sicherung und Wiederherstellung zugeordnet. |

Die endgültige Datei gilt erst nach dokumentierter Wiederherstellung und den wesentlichen Funktionstests als geprüft. Bis dahin ist ihr Status «unvalidierter Entwurf».

**Noch zu ergänzen**

- Namen der drei Lehrpersonen sowie Browser-/Geräteverteilung; bis dahin neutrale Platzhalter.
- Testbeginn und Rückmeldefrist; bis dahin keine erfundenen Termine.
- Konkreter Kurs für die Protokolle und Bestätigung, dass dort zum Einspielen die vorgesehene Moodle-Version verfügbar ist.
- Möglichkeit, die Wiederherstellung auf Moodle 5.2 zu erproben; hilfreich ist eine kleine Referenz-`.mbz`.
- Tatsächlicher Plugin-Stand für Moodle 5.2 und gegebenenfalls zugängliche Inhalte der Liip-Dokumentation.
