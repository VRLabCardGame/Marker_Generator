# **Bedienungsanleitung AR-Marker pattern-creator**
In diesem Repository befinden sich Skripte zur Erstellung von AR-Markern
sowie weitere Skripte zur Erstellung von Assets für das Kartenspiel des VRLabs 
der Hochschule Reutlingen.\

## Anforderungen:
- python 3.7.9
- Pillow 9.2.0 (über pip install)

## Aufbau des Repositories:
- **"examples"-Ordner:** Beispielhafte Skripte zur Erstellung von Markern aus dem Kartenspiel.
_**Wichtig:**_ Die referenzierten Bilder sind in diesem Repository nicht integriert.
Es werden eigene Bilder benötigt, oder man entfernt den Parameter image_path, 
wodurch die Marker mit einem Platzhalter erstellt werden.


- **create_pattern.py:** Das Skript zum Erstellen der AR-Marker. 
Die Methode create_pattern() kann in anderen Skripten genutzt werden, um eigene Marker zu erstellen.
Zu den zahlreichen Parametern der Methode gibt es eine Dokumentation bei der Definition der Methode selbst.


- **create_Spielfeld_layout.py:** Dieses Skript erstellt ein Bild des Spielfelds des Kartenspiels.
In der Mitte des Spielfelds befindet sich der Marker aus Spielfeld_config.py. 
Dieses Skript ist nicht entworfen worden, um modular einsetzbar zu sein, wie beispielsweise create_pattern.py.


- **icon_creator.py:** Skript zur Erstellung von Bildern in verschiedenen Auflösungen, die als Icons in ein
Unity-Projekt eingefügt werden können. Die Anleitung, wo die Bilder einzufügen sind, befindet sich in der allgemeinen
Dokumentation zum Kartenspiel-Projekt.


- **marker_print_conversion.py:** In diesem Skript werden die Bilder, die in den Skripten Zauberkarten_config.py, 
Player_config.py und Monsterkarten_config.py aus dem "examples"-Ordner in einem .pdf zusammengefasst, 
wobei sich immer vier Marker auf einer Seite befinden. Auch bei den print_conversion Skripten wurde keine
Priorität auf Wiederverwendbarkeit gelegt, weshalb diese ebenfalls nur als Beispiel dienen und für neue Projekte
individuell erstellt werden können/müssen.


- **marker_print_conversion_playground:** Dieses Skript erstellt ein .pdf aus dem Bild der Spielfeld_config.py.
Da das Spielfeld das Format A1 besitzt, jedoch davon ausgegangen wird, dass die meisten Privatpersonen nur über einen
Drucker für das Format A4 verfügen, ist die .pdf so aufgebaut, dass der Marker auf 8 Seiten verteilt ist und 
nach dem Druck zusammengesetzt werden kann.
