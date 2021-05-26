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

Program został pomyślany jako platforma internetowa dostosowana zarówno
do obsługi urządzeń stacjonarnych i mobilnych. Dzięki temu zawsze jest aktualny
i nie wymaga pobrania w całości, a jednocześnie zawsze pasuje do urządzenia i
systemu operacyjnego użytkownika - tj. jest "responsywny".

2. FUNKCJE PROGRAMU - UŻYTKOWNIK NIEZALOGOWANY

Obecnie program korzysta z pakietu tłumaczeniowego "django-modeltranslation", który pozwala w łatwy sposób tłumaczyć treści na stronie. W tej chwili zainstalowany jest język polski i angielski, ale w dowolnym momencie można dostosować ilość języków wedle uznania. W tej chwili program wykrywa język użytkownika na podstawie ustawień przeglądarki, a jeśli nie posiada takowego wybiera Polski. Użytkownik może zmieniać język w prawym górnym rogu na pasku nawigacji.

[Fig. 0 - Ikona zmiany języka na pasku nawigacji]

Niezalogowany użytkownik ma możliwość przeglądania gotowych planów zmianowania opublikowanych wcześniej przez innych użytkowników. Ogólne pojęcie o zawartości
planu daje zestawienie statystyk na temat wyróżnionych kategorii.

[Fig. 1 - podsumowanie zawartości planu]

Bez logowania użytkownikowi przysługuje również możliwość przeglądania biblioteki
wyszystkich roślin sortowanych alfabetycznie, według rodzin i kategorii.
Po wejściu w odpowiednią opcję może on obejrzeć interakcje związane z danym
elementem, jak również dowiedzieć się z opisu z czego one wynikają,
oraz z jakich źródeł wynika taka a nie inna interakcja.

[Fig. 2 i 3 - przełącznik strony "według rodzin/tagów/alfabetycznie",
 oraz "przykładowy Crop"]

Można w ten sposób także przejrzeć aktualne statystyki projektu, na stronie
"o projekcie" gdzie mieści się uproszczona nawigacja. Można tam także obejrzeć
zestawienie wszystkich używanych dotychczas przez interakcje źródeł.

[Fig. 4 i 5 - statystyki i źródła]

Poza tym można się jeszcze zalogować lub zarejestrować. W tym momencie program
generuje prosty login mnemotechniczny i nie jest zaopatrzony w narzędzie do
odzyskiwania hasła (nie wysyła maili), ponieważ jest to tylko wersja demonstracyjna
i nie było moim celem gromadzenie ani przetwarzanie niczyich danych osobowych.

[Fig. 6 - rejestracja]

3. FUNKCJE PROGRAMU - UŻYTKOWNIK ZALOGOWANY

Po rejestracji użytkownik uzyskuje dostęp do panelu "Moje Plany", w którym ma
możliwość przeglądania, dodawania / usuwania i edycji swoich własnych planów zmianowania. [Fig. 7]

[Fig. 7 - Lokalizacja "Moich Planów"]

Edycja planu polega na dodawaniu, kolejnych kroków, które reprezentują kolejne
lata w planie zmianowania. Kroki można dla wygody zamieniać miejscami, a ostatni
z nich można usuwać. [Fig. 8]

[Fig. 8 - Zakreślone lokalizacje przycisków "dodaj/usuń/edytuj krok" oraz "zamień miejscami"]

Przed usunięciem każdego kroku, a także samego planu, program upewni się,
czy napewno chcemy to zrobić, ograniczając straty czasu w razie pomyłki. [Fig. 9]

[Fig. 9 - Pokazane jak działa "safety valve"]

W tym momencie zarówno przycisk "dodaj nowy krok", jak i "edytuj" (patrz: Fig.8) przenoszą do strony edycji kroku. Mamy tam możliwość dla edytowania tytułu i opisu kroku. Te dane mają dla nas wartość jedynie informacyjną. Użytkownicy dodają je wyłącznie w swoich językach, jednak administratorzy mają możliwość dodać je we wszystkich językach wgranych do programu, co może być przydatne przy emisji oficjalnych / sugerowanych planów zmianowania.

[Fig 10. edycja tytułu i opisu kroku.]

Poniżej znajduje się możliwość zakomunikowania programowi o trzech potencjalnych
"użyciach" pola w danym roku:
- Na wiosnę, które program odbiera jako "Jare", lub plon wczesny,
  znajduje się pod przyciskiem "Dodaj wczesny plon".
- W lecie, które program odbiera jako wysadzenie średnio-późne
  i zostało stworzone z myślą głównie o krótkich śródplonach
  i płodozmianie warzywnym, a która to opcja jest pod przyciskiem "dodaj śródplon".
- Na jesieni, które program odbiera jako "Ozime", lub plon późny, znajduje się
  pod przyciskiem "dodaj późny plon"

[Fig. 11 - przyciski wczesny/średni/późny plon]

Zasada działania jest taka, że wybranie kolejnego "plonu" oznacza zebranie kolejnego.
W przeciwnym wypadku program zakłada, że pozwala się mu rosnąć dalej, w myśl reguły,
że na polu zawsze coś musi rosnąć, żeby przeciwdziałać erozji gleby i utraty składników
odżywczych. Z resztą takie jest teraz prawo. Pozwala to sadzić różne kombinacje i
zbierać je nawet po bardzo krótkim czasie. Program po prostu uzna, że jest to międzyplon,
choć w takim wypadku daje nam jeszcze możliwość użycia opcji "zniszcz ma zielony nawóz".
Efektem użycia tego przycisku będzie specjalne powiadomienie na ekranie głównym planu,
że ten krok został zniszczony na nawóz zielony.

[Fig. 12 i 13 - Przycisk "zniszcz na zielony nawóz" i jak wygląda efekt jego użycia na głównej stronie planu]

Żeby lepiej zobrazować działanie wymienionej wcześniej mechaniki na przykładzie:
Załóżmy, że wysiewamy jęczmień na wiosnę (program automatycznie zakłada,
że jest to jęczmień jary), czyli dodajemy go do zakładki "wczesny plon". Ponieważ
będzie on rósł do lipca-sierpnia, to zakładkę "śródplon" możemy zostawić w spokoju.
Natomiast najpóźniej na jesieni, w zakładce "późny plon" należałoby wstawić coś nowego.
W przeciwnym wypadku program założy, że pozwoliliśmy ziarnu osypać się na ziemię
a pole zaczynają porastać chwasty.

[Fig. 14 - Wizualizacja przykładu powyżej. Wysiew koniczyny po zbiorze jęczmienia]

Dodawanie roślin do sub-kroku (np. do "wczesnego plonu") odbywa się poprzez wybranie odpowiadającej nam pozycji z rozwijanego menu i wciśnięcie przycisku "dodaj pozycję". Wybrane pozycje pojawiają się powyżej rozwijanego menu i przy każdej z nich znajduje się przycisk "usuń pozycję" umożliwiający ich pojedyncze usunięcie.
Do każdego takiego sub-kroku można dodać obornik za pomocą przycisku "dodaj obornik", którego efekt na planie głównym jest analogiczny do wymienionego wcześniej przycisku "nawozu zielonego".

[Fig. 15 - Dodawanie i usuwanie poszczególnych elementów]

Do planu automatycznie dodawane/usuwane z niego są też zdefiniowane wcześniej przez administratora, niewidoczne dla użytkownika mieszanki, które posiadają swoje własne interakcje.
W prezentowanym przykładzie po dodaniu do sub-kroku dowolnego elementu z kategorii "trawa" i drugiego z kategorii "koniczyna", do planu zostaje dodany ukryty element o nazwie "mieszanka trawy i koniczyny", która posiada pozytywne interakcje następcze ze wszystkimi elementami należącymi do rodziny Kapustnych. W związku z tym na planie głównym ta interakcja ujawni się po wciśnięciu przycisku "ewaluacji".

[Fig. 16 - Ukryte interakcje mieszanek]

Po wybraniu wszystkich elementów planu użytkownik ma możliwość jego ewaluacji za pomocą wspomnianego wyżej przycisku "ewaluacja". (Fig. 17)
Proces odbywa się dwuetapowo, tj. dla zaoszczędzenia zasobów program najpierw sprawdza,
czy dla wszystkich wymienionych w planie roślin ilość kroków (lat) jest wystarczająca.
Jeśli jest zbyt mała, nie liczy dalej, tylko podaje nazwy roślin dla których trzeba zwiększyć ilość kroków w planie, lub je usunąć.

[Fig. 17 - Przycisk ewaluacja i błąd długości płodozmianu]

Jeżeli długość płodozmianu jest właściwa, to w kolejnym etapie program sprawdza, czy  wszystkie rośliny z tych samych rodzin zostały posadzone w odpowiednim odstępie czasowym od siebie. Jeżeli nie, to zwraca ten błąd jako "kolizję" wytłuszczoną czcionką. (fig. 18)
Następnie wyciąga za pomocą permutacji wszystkie możliwe interakcje na planie i porównuje je z bazą danych interakcji jakie posiada. W razie trafienia zwraca je obok rośliny zwykłą czcionką.

[Fig. 18 - Błąd kolizji w rodzinie i przykładowa interakcja na planie]

Jeżeli użytkownik jest zadowolony ze swojego planu i chce się nim podzielić, może go teraz opublikować za pomocą przycisku "opublikuj", aby reszta użytkowników miała do niego dostęp. Opublikowane plany są dostępne w omówionej wcześniej bibliotece planów, oraz mogą zostać wylosowane na stronie głównej i zaproponowane zwiedzającym.
W dowolnym momencie użytkownik może wycofać swój plan z publikacji wciskając przycisk "wycofaj z publikacji", który zastępuje ten pierwszy.

[Fig. 19 - Miejsce gdzie znajduje się przycisk "opublikuj"/"wycofaj"]

4. FUNKCJE PROGRAMU - ADMINISTRATOR

Na skutek pojawienia się trzech kategorii danych podlegających interakcjom program ma w sumie do policzenia aż 9 różnych kombinacji (fig. 20). Gdybyśmy chcieli je liczyć za każdym razem, gdy wciskamy przycisk "ewaluacja", to mogłoby to zająć nawet minutę, czyli znacznie więcej niż przeciętny użytkownik internetu jest gotów czekać na wynik. Jest to też oczywiście dużym marnotrawstwem zasobów i szybko doprowadziłoby do zawieszenia serwera. Zwłaszcza, że tak naprawdę w ostatecznym rozrachunku to co program musi zrobić to sprowadzić je do najprostszego wspólnego mianownika, czyli do relacji roślina-roślina.

[Tabela 1 - Kombinacje do policzenia i ta, której tak naprawde potrzebuje program]

W związku z powyższym w panelu administratora "CR" został wbudowany mechanizm, który pozwala na szybkie (właśnie około 1 minuty) policzenie wszystkich tych interakcji wynikających z pozostałych ośmiu interakcji i przekonwertowanie ich na interakcje typu roślina-roślina. Efektem tego działania jest ponad ośmiokrotne zwiększenie się liczby interakcji w bazie danych i bardzo duże (<1s na serwerze lokalnym) przyśpieszenie ewaluacji planów.

Dodatkowym plusem tego rozwiązania jest możliwość dodawania wyjątków od reguł. Np. nie każdy członek kategorii "zboża" musi mieć pozytywną relację z "bobowatymi", jeśli go z niej wykluczymy. Wynika to z hierarchii jaką program stosuje przy tworzeniu relacji i reguły, że nie mogą być sprzeczne (tak naprawdę po prostu nie widzi znaku interakcji, a nie wolno mu powtórzyć już istniejącej interakcji).

W praktyce oznacza to, że pierwszeństwo mają interakcje manualnie zdefiniowane przez użytkownika na poziomie roślina-roślina, potem wszystkie interakcje na poziomie rodzin, a dopiero potem kategorii.

Minusem tego rozwiązania jest konieczność powtarzania zabiegu przeliczania bazy danych za każdym razem, gdy zostaną zmienione, lub dodane do niej nowe interakcje, zmienione zostaną kategorie, lub rodziny.

Jest co prawda eksperymentalna funkcja dodawania i usuwania tagów, która powinna działać w ten sposób, że dodanie/usunięcie taga nie wymaga odświeżenia całej bazy tagów generowanych maszynowo, jednak nie było dość czasów na testy i nie polegałbym na niej za bardzo.

Panel CR pozwala ustalić zmienne istotne dla funkcjonowania programu. Zmienne są w miarę jasno opisane, ale pozwolę je sobie tutaj opisać dla porządku:

- Maksymalna ilość kroków w planie, to ilość kroków, którą użytkownik może maksymalnie dodać do swojego planu nim na widoku planu zniknie opcja "dodaj nowy krok". W istocie jest to maksymalna liczba lat na jaką pozwalamu użytkownikowi planować swój płodozmian.

- Maksymalna ilość planów zmianowania na użytkownika, to maksymalna ilość planów jaką może dodać jeden użytkownik programu zanim otrzyma powiadomienie, że osiągnął swój limit, a opcja "dodaj now plan" zniknie.

- Czas cachowania w minutach planów widzianych z zewnątrz, pozwala na zaoszczędzenie zasobów serwera na użytkowników, którzy dużo klikają w kółko w jeden plan, oraz tzw. "web-crawlery". Serwer przez ten czas od wygenerowania strony, wyrażony w minutach, będzie serwował stronę z cache bazodanowego oszczędzając tym samym procesor.

- Czas cachowania w sekundach planu po ewaluacji, pozwala na zaoszczędzenie zasobów serwera na użytkowników, którzy doświadczyli problemów na łączach, lub są zwyczajnie niecierpliwi i wciąż odświeżają stronę jeśli nie pojawi się ona w czasie krótszym niż przez nich oczekiwany. Serwer, jak powyżej nie reaguje wtedy na kolejne zapytania, tylko serwuje, w czasie wyrażonym w sekundach, stronę z cache bazodanowego.


- Opisz pokrótce panel CR, tj. cachowanie i co ma na celu,
  oraz ograniczanie ilości planów usera i co ma na celu.

- Opisz jak działa uźródłowianie obrazków i ogólnie wszystkiego. Szeregowanie
  źródeł i czemu to ma służyć.


(...)

6. PODSUMOWANIE (?)

(...)

################

DYSKUSJA

Program w obecnej formie, choć sprawny, jest zaledwie namiastką tego czym mógłby
być, gdyby poświęcić mu więcej czasu, oraz zintegrować z innymi systemami.
W tej sekcji poruszam możliwości potencjalnego rozwoju aplikacji w przyszłości,
gdyby ktoś chciał się tego podjąć.

W tej chwili program jest dostępny wyłącznie jako aplikacja online dostępna z
serwera w Niemczech. Powoduje to niepotrzebne koszty energetyczne i opóźnienie
na łączu dochodzące nawet do 1s. Ten problem można rozwiązać instalując program
na szybkim serwerze w Polsce - np. w Warszawie, oraz oferując chętnym możliwość
ściągnięcia wersji desktop działającej offline (do wykonnaia za pomocą np.
django2exe, pyinstaller). Można również stworzyć aplikację na smartfony, która
dane będzie pobierać ze strony za pomocą Django REST.

Prędkość liczenia można zwiększyć jeszcze bardziej (4.2x) przechodząc
z domyślnego kompilatora CPython na PyPy, który dobrze współgra
z frameworkiem Django.

-Można zrobić tak, żeby user widział, czy plan jest opublikowany.

-Można pozwolić userowy wybrać jak bardzo sztywno reguł ma się trzymać program
 obliczając wymagania dla danej rodziny/rośliny i pozwolić mu np. zaznaczyć to
 w opcjach zaawansowanych dla danego planu. Można zrobić opcje globalne, które
 będą dla danego usera domyślne w ustawieniach. (W tej chwili jest na sztywno,
 a są wprowadzone widełki przy rodzinach, a nawet przy konkretnych roślinach)

-Należy skompresować zdjęcia roślin, aby były mniejsze i/lub wykonać własne.

-Należy dodać tag i ikonkę informującą o typie i wielkości systemu korzeniowego
 i na tej podstawie stworzyć interakcje.

-Należy dodać tag i ikonkę informujące o poziomie wymagań pokarmowych danej
 rośliny i stworzyć na tej podstawie interakcje.

-Można zrobić globalne cachowanie strony usera po ostatniej ewaluacji,
 aby użytkownik podglądający cudzy plan widział w nieskończoność ten plan
 (wbrew pozorom oszczędza to energię przy spiderach).

-Rejonizacja za pomocą wbudowanego w Django3 geo-taga + mapy powiatów x odmiany
 roślin x klasa ziemi i automatyczne filtrowanie sugerowanie roślin/mieszanek
 zależnie od regionu.

-Komunikaty/sugestie upraw/ gotowe plany zmianowania zaciągane automatycznie
 z COBORU dla danego regionu.

-Komunikaty/sugestie zaciągane automatycznie z centrum monitorowania agrofagów.

-Inne ważne, rejonizowane komunikaty i sugestie od pozostałych agencji.

-Sklep wysyłkowy z nasionami/sadzonkami kwalifikowanymi. Na podstawie lokalizacji
 program sugeruje odmiany o konkretnych parametrach (odporność na suszę,
 wymarzanie, konkretne patogeny, zamienniki lepiej dopasowane do lokalizacji itp.)
 i automatycznie komponuje koszyk od najbliższych dostawców, żeby zaoszczędzić na
 kosztach dostaw, a docelowo np. można mieć jakieś punkty przeładunkowe jak Amazon.

-Narzędzie do raportowania zwrotnego (zbierania danych masowych) jak dane
 zestawienie sprawdziło się na konkretnym terenie. Rolnik pobiera wtedy unikalny
 token identyfikujący i bierze udział w badaniu np. w zamian za rabat na
 nawozy/nasiona zamówione przez portal, albo darmową wysyłkę.

-Wyszukiwarka planów według zadanego kryterium (po tagu, po roślinie)

-Wyszukiwarka roślin w kategorii "alfabetycznie".

-Dodanie kosmetycznej klasy wsiewek dla lepszego uporządkowania pracy.

-Wprowadzenie orientacyjnych maksymalnych czasów plonowania i w związku z tym
 ostrzeżeń, jeśli w płodozmianie są dziury.

-Dodanie opcji "autosugestie" dla takich dziur w planie.

-Porządny panel administracyjny.
