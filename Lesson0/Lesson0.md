# Lesson 0

1. Begrüßung
Ich möchte euch, nach und nach, das Thema Künstliche Intelligenz zeigen.

Künstliche Intelligenz klingt kompliziert, gerade weil auch das Wort "Intelligenz" vorkommt.
Aber wie bei fast allen Themen, wenn man sie weit genug auseinandernimmt, wird auch KI enorm einfach, wenn man sie in passende Häppchen zerlegt.

Und genau das möchte ich mit euch machen!
Oh, noch eines: Ich werde euch so oft wie möglich die Chance geben Dinge selbst auszuprobieren - hier oder später zuhause.
Dafür verteile ich nachher ein Kärtchen mit einem QR-Code, der euch zu einem Ort bringt wo ihr alles was wir hier besprechen nachlesen und auf eurem PC zuhause ausprobieren könnt.

1. Einstieg
Wir starten mit einer Frage: Wer von euch kennt ChatGPT? => Bitte melden!
Ok, von denen, die sich grad melden: Wer hat es schonmal ausprobiert (alle anderen bitte die Hand runter)? => Bitte weiter melden!
Von denen, die sich grad melden: Was macht ChatGPT? => Einfach reinrufen! Bspw.: "Es beantwortet Fragen!"
Und jetzt wird's schwierig: Hat jemand eine Idee WIE es tut was es tut?

2. Wie speichert ChatGPT sein Wissen?
Lasst uns einen Blick in den Kopf von ChatGPT werfen:
Stellt euch vor, ihr seht ein riesiges Bücherregal mit Millionen von Büchern. 
Aber statt die Bücher Seite für Seite durchzulesen, speichert ChatGPT die Bücher in sowas wie einzelnen Wörtern. 

Und die Wörter schreibt ChatGPT in seinem Kopf nicht einfach hintereinander, sondern speichert sie an bestimmmten Positionen.
So, als würdet ihr das Kochbuch in die Küche legen und das Vokabelbuch auf euren Schreibtisch.

In ChatGPTs Kopf sieht das dann so aus:

3.Koordinaten und Vektoren
Bild: Ein Koordinatensystem mit X- und Y-Achse, jeweils 0 bis 4 an den Achsen.
Darin ein Punkt bei (2,3).

Jetzt könnt ihr euch der Einfachheit halber vorstellen, dass ChatGPT das Wort Katze bei (2,3) speichert.

4. Nah und fern
Ein Wort wie "Hund" wäre bei ChatGPT nah an Katze, weil beide Worte ähnlich sind:
- Beide sind Tiere, 
- sogar beliebte Haustiere.

Wegen dieser Ähnlichkeit wäre "Hund" dann bspw. bei (2,2).

Dagegen "Auto", weil deutlich anders als Hund und Katze, könnte weit weg, bspw. bei (4,4) sein.

5. Wie versteht ChatGPT meine Frage?
Wenn du eine Frage stellst, zerlegt ChatGPT sie in diese einzelnen Wörter und wandelt die Wörter in solche Zahlen-Vektoren um.

Zum Beispiel:
Deine Frage: "Was ist ChatGPT?" wandelt ChatGPT jedes Wort in Zahlen um, sodass die ganze Frage so aussieht:
[[0.5, -0.9], [0.7, 2.0], [0.3, 1.0]]

Dann sucht ChatGPT nach ähnlichen Vektoren in ihrem "Wissens-Bücherregal", um herauszufinden, welche Antworten zu den Frage-Vektoren passen.

6. Wie wählt die KI eine Antwort?
Die KI hat Millionen von Beispielen gesehen und gelernt, welche Worte oft zusammen benutzt werden.

Sie prüft, welche Wörter und Sätze in der Vergangenheit auf ähnliche Fragen geantwortet haben.
Sie berechnet, welche Wörter am wahrscheinlichsten als nächstes kommen.
Zum Beispiel:

Die KI weiß, dass auf „Was ist eine KI?“ oft „Eine KI ist ein Programm, das …“ folgt.
Also wählt sie die nächstwahrscheinlichsten Wörter aus und baut damit eine Antwort.
Stell es dir vor wie ein Spiel, bei dem du den Satz vervollständigst:
"Wenn es regnet, dann wird die Straße …"
(Wahrscheinlich sagst du „nass“.)
Die KI macht genau das – nur mit mehr Wörtern auf einmal.

7. Realität: Vektor-Dimensionen:
Unser Diagramm hat nur 2 Achsen, also 2 Dimensionen.

Moderne Sprachmodelle, wie ChatGPT, bilden ihren Vektorraum aber bspw. mit 4096 Dimensionen.

Beispiel:
Ich habe einmal statt Katze das englische "Cat" genommen:
Mit Ausführen von getVector.py erhaltet ihr die 4096 Vektor-Koordinaten des Wortes "Cat" im Sprachmodell LLaMA3.1

Um zu sehen, dass Cat viel näher an Dog ist als Cat an Car könnt ihr getSimilarities.py ausführen.

Und um herauszufinden, welches Wort bzw. "Token" am weitesten von Cat entfernt ist, könnt ihr getFarAway.py ausführen.
