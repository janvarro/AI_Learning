Architekturális nézőpontból:

## LLM

Az **LLM** egy nyelvi modell, vagyis egy komponens, amely bemeneti szövegből kimeneti szöveget generál.

Példák:

- GPT
- Claude
- Llama
- Gemini

Egy LLM önmagában:

- nem rendelkezik tartós memóriával, hacsak nem építenek köré;
- nem hajt végre valódi műveleteket külső rendszerekben;
- nem „tervez” hosszabb folyamatokat megbízhatóan önállóan;
- alapvetően prediktív szöveggenerátor;
- a megadott kontextus alapján válaszol.

Architekturálisan az LLM egy **intelligens feldolgozó motor**.

---

## AI agent

Az **AI agent** egy rendszerarchitektúra, amely általában használ egy vagy több LLM-et, de kiegészíti őket további komponensekkel.

Egy agent tipikusan tartalmaz:

- **LLM-et** a gondolkodáshoz/nyelvi feldolgozáshoz;
- **eszközhasználatot**, például API-hívásokat, adatbázis-lekérdezést, böngészést, fájlkezelést;
- **memóriát**, például korábbi interakciók, felhasználói preferenciák, üzleti állapot tárolását;
- **tervező/logikai réteget**, amely részfeladatokra bontja a célt;
- **végrehajtási ciklust**, amely lépésenként halad, ellenőrzi az eredményt, majd dönt a következő lépésről;
- **policy és guardrail réteget**, amely szabályozza, mit tehet és mit nem.

Architekturálisan az AI agent egy **LLM-alapú döntéshozó és végrehajtó rendszer**.

---

## Egyszerű különbség

| Szempont | LLM | AI agent |
|---|---|---|
| Mi ez? | Modell | Rendszer |
| Fő funkció | Szöveg generálása | Cél elérése lépésekben |
| Használ eszközöket? | Nem önmagában | Igen, jellemzően |
| Van memóriája? | Csak a kontextusablakban | Lehet tartós memóriája |
| Képes cselekedni? | Nem közvetlenül | Igen, külső rendszereken keresztül |
| Példa | „Írj egy emailt” | „Foglalj időpontot, küldj emailt, frissítsd a CRM-et” |

---

## Példa

Egy LLM-nek ezt mondod:

> „Írj egy válasz emailt az ügyfélnek.”

Az LLM megírja a szöveget.

Egy AI agentnek ezt mondod:

> „Kezeld ezt az ügyfélpanaszt.”

Az agent:

1. elolvassa az ügyfél üzenetét;
2. lekérdezi a rendelést az adatbázisból;
3. ellenőrzi a szabályzatot;
4. javasol kompenzációt;
5. megírja az emailt;
6. jóváhagyást kér vagy elküldi;
7. naplózza az eseményt a CRM-ben.

---

## Röviden

Az **LLM az agy egyik komponense**, míg az **AI agent egy teljes működési rendszer**, amely az LLM-et használja gondolkodásra, de eszközökkel, memóriával, szabályokkal és végrehajtási logikával képes célorientált feladatokat elvégezni.
