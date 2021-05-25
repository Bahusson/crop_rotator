ABSTRAKT

Projekt "Crop Rotator" (to by było po polsku "Płodozmieniacz") to efekt mojego podejścia do pracy dyplomowej na Studiach podyplomowych z Rolnictwa dla absolwentów nierolniczych studiów wyższych Szkoły Głównej Gospodarstwa Wiejskiego w Warszawie.

Celem programu jest ułatwienie osobom posiadającym już kwalifikacje rolnicze, szybkie układanie złożonych planów zmianowania. Program adresowany jest w szczególności do osób zainteresowanych rolnictwem ekologicznym, gdyż przyjęto w nim założenie, że użytkownik chce zapewnić roślinom jak najlepsze warunki przy stosowaniu minimalnej ilości chemicznych środków ochrony roślin i nawozów sztucznych.

Promotorem tej pracy jest dr hab. Dariusz Gozdowski.

#############

ABSTRACT

Project "Crop Rotator" is an effect of my attempt at my thesis on post-graduate studies for graduates of non-agriculture students of Agriculture on Warsaw University of Life Sciences.

The purpose of this site is to help people that already have agricultural qualifications to quickly set up complex rotation plans. It is meant to be especially useful for those interested in ecological agriculture due to its programmed presumptions that user wants to supply their plants with best possible conditions, using lowest possible amounts of chemical means of plant protection and artificial fertilizers.

The promoter of this thesis is dr hab. Dariusz Gozdowski

##############

WSTĘP

Zmiany klimatu dotykają nas coraz dotkliwiej.
Pogłębia się susza i inne ekstremalne zjawiska pogodowe.
W takich warunkach kluczową jest umiejętność szybkiego
dostosowania się do dynamicznie zmieniająchych się warunków.
Stawką jest stabilne plonowanie, a co za tym idzie dobrostan społeczeństw.

Z drugiej strony pojawia się konieczność natychmiastowej rezygnacji
z paliw kopalnych (a wręc częściowe zastąpienie ich produktami rolnictwa,
tam gdzie nie byłoby to ze szkodą dla ludzi) a zatem ze zmniejszenia
ogólnych nakładów energetycnych i dramatycznej poprawy wydajności w ogóle.

Z powodu ryzyka uodpornienia patogenów i agrofagów na chemiczne środki ochrony,
oraz ich potencjalną niepożądaną, długoterminową szkodliwość dla reszty biosfery
(tzw. "forever chemicals") i wysokie nakłady energetyczne przy ich produkcji,
również i te metody należy ograniczyć w ramach tzw. integrowanej ochrony roślin.

Kluczowe staje się więc zarządzanie wiedzą i automatyzacja tego procesu
na szeroką skalę. W wielu krajach centralnie zarządzane systemy ostrzegania
przed agrofagami i patogenami z dużą dokładnością przewidują powstanie
zagrożenia i w porę informują rolników o konieczności przeprowadzenia
minimalnych koniecznych zabiegów, co wpływa korzystnie zarówno na plon,
jak i minimalizuje wpływ na środowisko.

Dalsze integrowanie systemów teleinformatycznych celem uzyskania
jeszcze większej ilości informacji i jeszcze większej synergii,
jest tylko kewstią czasu.

W związku z powyższymi czynnikami, tj. koniecznością redukcji energii z paliw
kopalnych, ograniczeniem środków ochrony roślin, potrzebą szybkiego dostosowania
się do warunków, a także szybkiej centralnie zarządzanej dystrybucji wiedzy
i doradztwa, rośnie zapotrzebowanie na system teleinformatyczny, który wspomoże
podejmowanie decyzji w zakresie odpowiedniego, złożonego zmianowania roślin.

Program, który napisałem w ramach swojej pracy dylomowej, a który będę poniżej przedstawiał, ma za zadanie po części zaadresować tę potrzebę i być może
w przyszłości stać się zaczątkiem bardziej zintegrowanego systemu.

###############

1. PODSTAWOWE ZADANIA STAWIANE PRZED PROGRAMEM

Celem programu jest umożliwienie użytkownikowi, który posiada już kwalifikacje,
rolnicze szybkie i intuicyjne układanie złożonych planów zmianowania,
aby następnie zostały one sprawdzone pod kątem błędów i kolizji.
W programie założono, że użytkownik chce zapewnić roślinom jak najlepsze warunki
rozwoju, zatem domyślne parametry wymagań dla gatunków są w górnej granicy.
Program nie zakłada użycia nawozów sztucznych, ale pozwala na użycie obornika
i/lub zniszczenie roślin na nawóz zielony, gdyż wynikają z tego pewne interakcje.

2. PODSTAWOWE FUNKCJE PROGRAMU - UŻYTKOWNIK

Program został pomyślany jako platforma internetowa dostosowana zarówno
do obsługo urządzeń stacjonarnych i mobilnych.

(...)

3. ZAAWANSOWANE FUNKCJE PROGRAMU - UŻYTKOWNIK

(...)

4. PODSTAWOWE FUNKCJE PROGRAMU - ADMINISTRATOR

(...)

5. ZAAWANSOWANE FUNKCJE PROGRAMU - ADMINISTRATOR

(...)

6. PODSUMOWANIE

(...)

################

X. DYSKUSJA

Program w obecnej formie, choć sprawny, jest zaledwie namiastką tego czym mógłby
być, gdyby poświęcić mu więcej czasu, oraz zintegrować z innymi systemami.
W tej sekcji poruszam możliwości potencjalnego rozwoju aplikacji w przyszłości,
gdyby ktoś chciał się tego podjąć.

W tej chwili program jest dostępny wyłącznie jako aplikacja online dostępna na
serwerze w Niemczech. Powoduje to niepotrzebne koszty energetyczne i opóźnienie
na łączu dochodzące nawet do 1s. Ten problem można rozwiązać instalując program
na szybkim serwerze w Polsce - np. w Warszawie, oraz oferując chętnym możliwość
ściągnięcia wersji desktop działającej offilne (do wykonnaia za pomocą np.
django2exe, pyinstaller). Można również stworzyć aplikację na smartfony, która
dane będzie pobierać ze strony za pomocą Django REST.

Prędkość liczenia można zwiększyć jeszcze bardziej (4.2x) przechodząc
z domyślnego kompilatora CPython na PyPy, który dobrze współgra
z frameworkiem Django.
