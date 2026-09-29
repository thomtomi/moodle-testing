---
title: "Plugin-Auswahl für Tests durch Lehrpersonen mit Manager-Rechten"
author: lamt
date: 2026-09-29
status: Recherche und Vorschlag
---

# Plugin-Auswahl für Tests durch Lehrpersonen mit Manager-Rechten

Die ursprüngliche Liste umfasst 73 Komponenten. Nach dem Ausschluss von `mod_chat` und `mod_survey` verbleiben 71 Komponenten. Davon empfehle ich 30 für die reguläre Testliste. Weitere 6 benötigen besondere Vorbereitung oder eine eingegrenzte Prüfung; 30 werden als Unterbausteine ihrer Hauptaktivität getestet. Bei 5 steht die Prüfung durch die Informatik im Vordergrund.

**Entscheidung vom 29.09.2026:** `mod_chat` und `mod_survey` werden künftig ausgeschlossen. Sie sind aus der CSV-Arbeitsliste entfernt und werden weder als auswählbare Plugins noch als vorbereitete Testfälle in die geplante Datenbank aufgenommen.

Die Einstufung ist eine Empfehlung auf Basis der verlinkten Herstellerbeschreibungen, MoodleDocs und Quellcode-Repositories, abgerufen am 29.09.2026. Auf der konkreten Moodle-Instanz wurden keine Tests ausgeführt. Die installierten Versionen, Freischaltungen und angepassten Rollen sind nicht bekannt. Versionskompatibilität muss vor dem Teststart mit dem Dienstleister abgeglichen werden.

Vorausgesetzt werden ein eigener Testkurs, installierte und freigegebene Plugins sowie ausreichende Rechte im betroffenen Kurs bzw. Kursbereich. Die Manager-Rolle kann angepasst sein und ersetzt keinen uneingeschränkten Administrationszugang. Quelle: [MoodleDocs zur Manager-Rolle](https://docs.moodle.org/403/en/Manager).

Für Teilnahme, Buchungen, Bewertungen, Abschlüsse und Sichtbarkeit sind eingeschriebene Lernenden-Testkonten vorzusehen. Eine reine Manager-Ansicht oder ein Rollenwechsel liefert dafür keine vollständige Prüfung. Einfache Testmaterialien wie PDF, DOCX, Bilder, Gruppen und Quizfragen können die Lehrpersonen selbst vorbereiten. Das zählt hier zur normalen Einrichtung eines Testfalls.

| Kategorie | Bedeutung | Anzahl |
| --- | --- | ---: |
| A | Reguläre Testliste: direkt über die Moodle-Oberfläche prüfbar | 30 |
| B | Mit besonderer Vorbereitung oder eingegrenztem Prüfumfang | 6 |
| C | Als Unterbaustein der Hauptaktivität testen | 30 |
| D | Technische Integration: Informatik koordiniert die Prüfung | 5 |

Die [CSV-Arbeitsliste](plugin-testbarkeit.csv) enthält die 71 verbleibenden Komponenten mit Kategorie, Testvorschlag, Voraussetzung, Hauptplugin und Quelle.

**A: Direkt testbare Aktivitäten**

| Plugin | Funktion | Konkreter Testvorschlag | Voraussetzung |
| --- | --- | --- | --- |
| [mod_attendance](https://moodle.org/plugins/view.php?moodle_version=39&plugin=mod_attendance) | Anwesenheit | Termin anlegen, Anwesenheit eines Testkontos erfassen, Bericht kontrollieren. | Eingeschriebenes Testkonto. |
| [mod_board](https://moodle.org/plugins/mod_board?comment_area=plugin_general&comment_component=local_plugins&comment_context=50&comment_itemid=2752&nonjscomment=1) | Board / Pinnwand | Spalten und Beiträge anlegen, Beiträge bearbeiten und Sichtbarkeit mit zweitem Konto prüfen. | Zweites Testkonto. |
| [mod_checklist](https://moodle.org/plugins/mod_checklist?comment_area=plugin_general&comment_component=local_plugins&comment_context=50&comment_itemid=158&comment_page=5&nonjscomment=1) | Checkliste | Punkte anlegen, als Lernende abhaken und Fortschritt als Lehrperson kontrollieren. | Eingeschriebenes Lernenden-Testkonto. |
| [mod_choicegroup](https://docs.moodle.org/502/en/Group_choice_quick_guide) | Gruppenwahl | Zwei Gruppen mit begrenzten Plätzen anbieten, Gruppe wählen und Mitgliedschaft prüfen. | Zwei im Kurs angelegte Gruppen und Lernenden-Testkonto. |
| [mod_customcert](https://moodle.org/plugins/mod_customcert?lang=eo) | Individuelles Zertifikat | Zertifikat mit Text, Namen und Bild gestalten, ausstellen und PDF prüfen. | Testkonto und kleine Bilddatei; Spezialelemente gesondert prüfen. |
| [mod_flashcard](https://docs.moodle.org/405/en/Flashcard_module) | Lernkarten | Wenige Frage-Antwort-Paare anlegen und den Kartensatz durcharbeiten. | Einfache selbst erstellte Textpaare. |
| [mod_journal](https://docs.moodle.org/502/en/Journals) | Journal | Schreibauftrag anlegen, Eintrag als Lernende erfassen und Feedback geben. | Lernenden-Testkonto. |
| [mod_kanban](https://marketplace.moodle.com/plugins/mod_kanban) | Kanban-Board | Spalten und Karten anlegen, Karte bearbeiten und in eine andere Spalte verschieben. | Testkurs. |
| [mod_pdfannotator](https://marketplace.moodle.com/plugins/mod_pdfannotator) | PDF-Annotation | PDF bereitstellen, Passage kommentieren und mit zweitem Konto antworten. | Kleine PDF-Datei und zweites Konto. |
| [mod_publication](https://moodle.org/plugins/mod_publication?lang=bs) | Studierendenordner | Datei als Lernende hochladen, Freigabe erteilen und Sichtbarkeit kontrollieren. | Kleine Testdatei und Lernenden-Testkonto. |
| [mod_scheduler](https://moodle.org/plugins/mod_scheduler?lang=mi_wwow) | Terminplaner | Zeitfenster anbieten, Termin als Lernende buchen und Buchung kontrollieren. | Lernenden-Testkonto; automatische Erinnerungen separat prüfen. |
| [mod_studentquiz](https://moodle.org/plugins/mod_studentquiz?comment_area=plugin_general&comment_component=local_plugins&comment_context=50&comment_itemid=1736&comment_page=5&nonjscomment=1) | StudentQuiz | Frage als Lernende erstellen, beantworten, kommentieren und bewerten. | Lernenden-Testkonten. |

Beim Zertifikat gehören die benötigten Elemente in den Prüfumfang; beim Terminplaner sind automatische Erinnerungen ein zusätzlicher Test mit zeitlichen und technischen Voraussetzungen.

**A: Direkt testbare Erweiterungen anderer Moodle-Bereiche**

| Plugin | Funktion | Konkreter Testvorschlag | Voraussetzung |
| --- | --- | --- | --- |
| [booktool_wordimport](https://moodle.org/plugins/booktool_wordimport?lang=ti) | Word-Import in ein Buch | DOCX mit Überschriften und Bild importieren; Kapitelaufteilung und Bild prüfen. | Ein Buch und eine kleine DOCX-Datei mit Überschriftformaten. |
| [quiz_archive](https://marketplace.moodle.com/plugins/quiz_archive) | Archivbericht für Tests | Abgeschlossenen Testversuch im Archivbericht öffnen und Druckansicht bzw. PDF-Druck kontrollieren. | Test mit abgeschlossenem Lernendenversuch. |
| [block_completion_progress](https://marketplace.moodle.com/plugins/block_completion_progress) | Abschlussfortschritt | Block hinzufügen, Aktivität abschliessen und Fortschrittsanzeige kontrollieren. | Aktivitätsabschluss aktiviert und für Testaktivitäten eingerichtet; Lernenden-Testkonto. |
| [block_people](https://marketplace.moodle.com/plugins/block_people) | Personen / Kurskontakte | Block hinzufügen und angezeigte Lehrpersonen sowie Profil-, Nachrichten- und Teilnehmendenlinks prüfen. | Dem Kurs zugeordnete Lehrperson. |
| [qtype_drawing](https://moodle.org/plugins/qtype_drawing?lang=en_us) | Freihandzeichnung | Frage erstellen, Zeichnung abgeben, manuell bewerten und kommentieren. | Testaktivität und Lernenden-Testkonto. |
| [qtype_gapfill](https://marketplace.moodle.com/plugins/qtype_gapfill) | Lückentext | Frage erstellen, richtige und falsche Antworten abgeben und Bewertung prüfen. | Testaktivität oder Fragenvorschau. |
| [qtype_kprime](https://marketplace.moodle.com/plugins/qtype_kprime) | Kprime | Frage mit vier Aussagen erstellen und Bewertung verschiedener Antwortkombinationen prüfen. | Testaktivität oder Fragenvorschau; erwartete Punkte vorher festlegen. |
| [qtype_mtf](https://marketplace.moodle.com/plugins/qtype_mtf) | Mehrfach Wahr/Falsch | Frage mit mehreren Aussagen erstellen, beantworten und Bewertung kontrollieren. | Testaktivität oder Fragenvorschau. |
| [qtype_wordselect](https://marketplace.moodle.com/plugins/qtype_wordselect) | Wörter auswählen | Text mit Zielwörtern erstellen, Wörter auswählen und Bewertung prüfen. | Testaktivität oder Fragenvorschau. |
| [filter_fontawesome](https://github.com/ffhs/moodle-filter_fontawesome) | FontAwesome-Symbole | Dokumentiertes Symbolkürzel in eine Textseite einsetzen und Darstellung nach Speichern prüfen. | Filter aktiviert und passende FontAwesome-Version durch Moodle/Theme bereitgestellt. |
| [atto_c4l](https://marketplace.moodle.com/plugins/atto_c4l) | C4L für Atto | Lernbaustein einfügen, speichern und erneut bearbeiten. | Atto muss als Editor verfügbar und die Schaltfläche freigegeben sein. |
| [atto_morebackcolors](https://marketplace.moodle.com/plugins/atto_morebackcolors) | Hintergrundfarben für Atto | Text hinterlegen, speichern und erneut bearbeiten. | Atto muss verfügbar und die Farbpalette eingerichtet sein. |
| [atto_morefontcolors](https://marketplace.moodle.com/plugins/atto_morefontcolors) | Schriftfarben für Atto | Text einfärben, speichern und erneut bearbeiten. | Atto muss verfügbar und die Farbpalette eingerichtet sein. |
| [tiny_c4l](https://marketplace.moodle.com/plugins/tiny_c4l) | C4L für TinyMCE | Lernbaustein einfügen, speichern und erneut bearbeiten. | TinyMCE und Plugin-Schaltfläche müssen verfügbar sein. |
| [tiny_fontcolor](https://marketplace.moodle.com/plugins/tiny_fontcolor) | Farben für TinyMCE | Schrift- und Hintergrundfarbe ändern, speichern und erneut bearbeiten. | TinyMCE und konfigurierte Farbauswahl müssen verfügbar sein. |
| [format_flexsections](https://docs.moodle.org/402/en/Flexible_sections_course_format) | Flexible Abschnitte | Format auswählen, Unterabschnitte anlegen und Sichtbarkeit aus Lernendensicht prüfen. | Eigener Testkurs; Format auswählbar. |
| [format_tiles](https://marketplace.moodle.com/plugins/format_tiles) | Kachelformat | Format auswählen, Kacheln gestalten und Aktivitäten darüber öffnen. | Eigener Testkurs; Format auswählbar. |
| [format_topcoll](https://github.com/gjbarnard/moodle-format_topcoll) | Collapsed Topics | Format auswählen, Abschnitte ein- und ausklappen und Aktivitäten bearbeiten. | Eigener Testkurs; Format auswählbar. |

Editor-Erweiterungen werden jeweils in ihrem eigenen Editor geprüft. Sind Atto und TinyMCE beide verfügbar, braucht es getrennte Testfälle. Falls Atto im vorgesehenen Betrieb nicht mehr angeboten wird, die Atto-Funktionstests begründet als «Entfällt» erfassen und vorhandene damit erstellte Inhalte auf korrekte Darstellung und Bearbeitbarkeit prüfen.

Für Fragetypen empfiehlt sich zusätzlich zur Vorschau mindestens ein echter Lernendenversuch mit anschliessender Kontrolle der gespeicherten Antwort und Bewertung. Bei `qtype_drawing` gehört die manuelle Bewertung dazu.

Für Kursformate nach Möglichkeit getrennte Testkurse verwenden. Neben der Neuanlage auch einen bestehenden Kurs nach dem Upgrade auf Inhalte, Navigation und Lernendensicht prüfen.

**B: Besondere Vorbereitung oder eingegrenzter Prüfumfang**

| Plugin | Funktion | Konkreter Testvorschlag | Voraussetzung |
| --- | --- | --- | --- |
| [mod_hotpot](https://marketplace.moodle.com/plugins/mod_hotpot) | HotPot | Vorhandene Übung hochladen, durchspielen und Antwort-/Ergebnisberichte prüfen. | Passende vorbereitete HotPot-Datei; benötigte Formate festlegen. |
| [mod_subcourse](https://moodle.org/plugins/view.php?moodle_version=15&plugin=mod_subcourse) | Unterkurs | Unterkurs verknüpfen, definierte Bewertung abrufen und Übernahme kontrollieren. | Zwei Testkurse, gemeinsames Lernendenkonto und bewerteter Versuch; automatischen Abruf zusätzlich mit Informatik prüfen. |
| [qtype_molsimilarity](https://moodle.org/plugins/qtype_molsimilarity?comment_area=plugin_general&comment_component=local_plugins&comment_itemid=2904&commentcontext=50&nonjscomment=1) | Molekülähnlichkeit | Referenzmolekül und definierte richtige/abweichende Antwort zeichnen; Bewertung prüfen. | Funktionsfähiger REST-Bewertungsdienst und fachlich vorbereitete Chemie-Beispielfrage. |
| [filter_amanote](https://guide.amanote.com/en/getting-started/start-note-taking/open-a-course-material-from-my-institution-s-platform) | Amanote | Kursmaterial in Amanote öffnen, annotieren, speichern und erneut öffnen. | Eingerichtete Amanote-Anbindung und nutzbarer Dienst; erforderliche Freigaben durch Administration. |
| [format_collapsibletopics](https://marketplace.moodle.com/plugins/format_collapsibletopics) | Collapsible Topics | Nach technischer Klärung bestehenden Testkurs öffnen und Abschnittsverhalten prüfen. | Hersteller pflegt das Plugin für Moodle 4.x nicht weiter; installierte Version und Zielversion vor Aufnahme klären. |
| [theme_boost_union](https://marketplace.moodle.com/plugins/2556) | Boost Union | Navigation, Kursbearbeitung, Dialoge und Darstellung bei verschiedenen Fenstergrössen prüfen. | Sichtprüfung direkt möglich, wenn das Theme aktiv ist; gezielte Prüfung globaler Optionen mit Administration vorbereiten. |

`mod_subcourse` ist trotz seiner Funktion zur Übernahme von Bewertungen auch über die Oberfläche testbar. Ein manueller Abruf prüft die Datenübernahme, bestätigt aber noch nicht den automatischen Abruf durch Hintergrundaufgaben. Die [Plugin-Beschreibung](https://moodle.org/plugins/view.php?moodle_version=15&plugin=mod_subcourse) nennt beide Wege.

`qtype_molsimilarity` benötigt laut [Herstellerbeschreibung](https://moodle.org/plugins/qtype_molsimilarity?comment_area=plugin_general&comment_component=local_plugins&comment_itemid=2904&commentcontext=50&nonjscomment=1) einen REST-Dienst zur Bewertung der Molekülähnlichkeit. Mit eingerichtetem Dienst und vorbereiteter Fachfrage können Lehrpersonen den Ablauf selbst testen.

Bei `filter_amanote` kann die Lehrperson den sichtbaren Ablauf prüfen, sobald die Anbindung bereitsteht. Die [Amanote-Anleitung](https://guide.amanote.com/en/getting-started/start-note-taking/open-a-course-material-from-my-institution-s-platform) beschreibt das Öffnen von Kursmaterial aus dem LMS. Je nach installierter Version gehören zusätzliche Webservice-Freigaben zur Einrichtung; diese setzt die Administration.

Bei `format_collapsibletopics` ist die Herstellerangabe zur eingestellten Pflege für Moodle 4.x ein konkreter Klärungspunkt. Ob lokal eine angepasste Fassung installiert ist, lässt sich aus dem Komponentennamen nicht erkennen. Das Plugin darf nicht mit `format_topcoll` verwechselt werden. Quelle: [Herstellerangabe zu Collapsible Topics](https://marketplace.moodle.com/plugins/format_collapsibletopics).

**C: Unterbausteine gemeinsam mit der Hauptaktivität prüfen**

Die Unterbausteine bleiben in der technischen Inventarliste enthalten. In der Arbeitsverteilung werden sie dem Hauptplugin zugeordnet und als konkrete Testschritte geführt. Ein erfolgreicher Basistest der Hauptaktivität bestätigt nicht automatisch jeden Unterbaustein.

| Hauptplugin | Zugehörige Komponenten aus der Liste | Testzuordnung |
| --- | --- | --- |
| `mod_hotpot` | `hotpotattempt_hp`, `hotpotattempt_html`, `hotpotattempt_qedoc` | Ausgabeformate anhand passender Übungen ausführen. |
| `mod_hotpot` | `hotpotsource_hp`, `hotpotsource_html`, `hotpotsource_qedoc` | Tatsächlich genutzte Quellformate mit je einer geeigneten Beispieldatei laden. |
| `mod_hotpot` | `hotpotreport_analysis`, `hotpotreport_clicktrail`, `hotpotreport_overview`, `hotpotreport_responses`, `hotpotreport_scores` | Nach Testversuchen jeden benötigten Bericht öffnen und mit den bekannten Antworten vergleichen. |
| `mod_customcert` | `customcertelement_bgimage`, `customcertelement_border`, `customcertelement_image`, `customcertelement_text` | Gestaltung und Positionierung im ausgegebenen PDF prüfen. |
| `mod_customcert` | `customcertelement_categoryname`, `customcertelement_coursefield`, `customcertelement_coursename` | Kursdaten mit bekannten Sollwerten vergleichen. |
| `mod_customcert` | `customcertelement_studentname`, `customcertelement_teachername`, `customcertelement_userfield`, `customcertelement_userpicture` | Personenbezogene Felder mit vorbereiteten Testkonten prüfen. |
| `mod_customcert` | `customcertelement_date`, `customcertelement_daterange`, `customcertelement_expiry` | Bezugsdaten festlegen und ausgegebene Datumswerte kontrollieren. Zeitabhängiges Verhalten gesondert planen. |
| `mod_customcert` | `customcertelement_grade`, `customcertelement_gradeitemname` | Vorbereitete Bewertung und Bezeichnung des Bewertungselements vergleichen. |
| `mod_customcert` | `customcertelement_code`, `customcertelement_qrcode` | Ausgestelltes Zertifikat prüfen; Code und gescannten QR-Code auf korrektes Ziel bzw. Verifikation prüfen. |
| `mod_customcert` | `customcertelement_digitalsignature` | Eigenen Test nach Bereitstellung geeigneter Signaturdatei und Rechte durchführen; PDF-Signatur kontrollieren. |

Die HotPot-Struktur mit Quellen, Ausgabeformaten und Berichten ist im [Repository des Herstellers](https://github.com/gbateson/moodle-mod_hotpot) dokumentiert. Die Zertifikatsbausteine finden sich im [Elementverzeichnis von Custom certificate](https://github.com/mdjnelson/moodle-mod_customcert/tree/main/element); die Einbindung von `daterange` ist versionsabhängig und im [Änderungsprotokoll](https://github.com/mdjnelson/moodle-mod_customcert/blob/main/CHANGES.md) beschrieben.

Die digitale Signatur benötigt eine geeignete Signaturdatei und gegebenenfalls ein Passwort. Dieser Baustein bekommt einen vorbereiteten Spezialtest; das Einfügen eines sichtbaren Unterschriftsbildes prüft die digitale PDF-Signatur nicht. Die technische Verwendung der Signaturdatei beschreibt der [Hersteller-Issue zur Signaturimplementierung](https://github.com/mdjnelson/moodle-mod_customcert/issues/879).

**D: Prüfung durch die Informatik koordinieren**

| Plugin | Funktion | Konkreter Testvorschlag | Voraussetzung |
| --- | --- | --- | --- |
| [auth_oidc](https://docs.moodle.org/500/en/Office365) | OpenID Connect | Mit freigegebenem Testkonto anmelden; Administration prüft Anbieteranbindung und Fehlerfälle. | Externer Identitätsanbieter und konfigurierte Anmeldung. |
| [auth_outage](https://github.com/catalyst/moodle-auth_outage) | Wartungs- und Ausfallsteuerung | In abgestimmtem Wartungsszenario Hinweise und Zugang für Testrollen prüfen. | Administration richtet das Wartungsszenario ein. |
| [message_msgraph](https://marketplace.moodle.com/plugins/message_msgraph) | Nachrichtenversand über Microsoft Graph | Definierte Moodle-Benachrichtigung auslösen und externen Empfang prüfen; Versandweg und Logs durch Informatik bestätigen. | Konfigurierte Microsoft-Graph-Anbindung und Testpostfach. |
| [local_ldap](https://marketplace.moodle.com/plugins/local_ldap) | LDAP-Kohortenabgleich | Definierte LDAP-Gruppenänderung durchführen lassen und resultierende Kohortenmitgliedschaft prüfen. | LDAP-Zugriff, definierte Testdaten und Ausführung der Synchronisation durch Informatik. |
| [local_o365](https://github.com/microsoft/moodle-local_o365) | Microsoft-365-Integration | Vereinbarte tatsächlich genutzte Synchronisation mit bekannten Testdaten prüfen. | Microsoft-365-Testkonfiguration und Abstimmung mit Administration. |

Die Lehrpersonen können bei diesen Integrationen sichtbare Ergebnisse prüfen, beispielsweise erfolgreiche Anmeldung, empfangene Benachrichtigung oder korrekte Kohortenmitgliedschaft. Für belastbare Aussagen müssen Testauslöser, Synchronisationslauf und gegebenenfalls Protokolle durch die Informatik zugeordnet werden. Eine erfolgreich empfangene Nachricht bestätigt beispielsweise nur dann `message_msgraph`, wenn sie tatsächlich über diesen Versandweg gesendet wurde.

**Verwendung in der Testdatenbank**

Die 30 Komponenten aus A bilden die vorgeschlagene Ausgangsliste für die regulären Tests. Aus B werden die tatsächlich genutzten Funktionen nach Vorbereitung ergänzt. Die Komponenten aus C werden ihren Hauptaktivitäten zugeordnet; D erhält separate technische Prüfpunkte mit zuständiger Person aus der Informatik.

Für jeden ausgewählten Vorgang wird ein Eintrag gemäss dem [Datenbankentwurf](vorschlag-moodle-testdatenbank.md) vorbereitet. Die Kategorie zur Testbarkeit beschreibt die Arbeitsverteilung und bleibt vom Testergebnis getrennt. Eine Kategorie A bedeutet, dass der Test einfach durchführbar ist; ob das Plugin funktioniert, wird erst im Test festgestellt.
