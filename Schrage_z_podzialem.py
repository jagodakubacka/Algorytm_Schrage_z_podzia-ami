s = []  # Moment rozpoczęcia
c = []  # Moment zakończeni
r = []  # Termin dostępności
p = []  # Czas wykonania
q = []  # Czas dostarczenia

A = []  # Tablica poomocnicza do odczytu danych
n = 0

N_0 = []
N = []  # Tablica zadń oraz r
P = []  # Tablica zadń oraz p
G_0 = []  # Tablica zadń oraz q
G = []  # Tablica gotowych zadań


C = []  # Tablica momentów wykonań
D = []  # Tablica momentów dostarczeń


def wczytaj(plik):
    f = open(plik, "r")
    global n
    for i in f:
        A.append(i)  # Przypisanie danych z pliku
    n = int(A[0])
    for x in range(len(A)):
        if x > 0:
            B = A[x].split()
            r.append(int(B[0]))  # Termin dostępności
            p.append(int(B[1]))  # Czas wykonania
            q.append(int(B[2]))  # Czas dostarczenia

    for x in range(n):
        a = (r[x], x)
        N.append(a)

    for x in range(n):
        a = (r[x], x)
        N_0.append(a)

    for x in range(n):
        a = (q[x], x)
        G_0.append(a)

    for x in range(n):
        a = (p[x], x)
        P.append(a)

# Stworzenie zbioru N -> rosnące r
def Sort_N():
    N.sort()

# Stworzenie zbioru N -> malejące q
def Sort_G():
    G.sort(reverse=True)


def Schrage():
    Sort_N()

    C_max = 0  # Maksymalny z terminów dostarczenia zadń
    t = 0
    count = 0

    while len(G) != 0 or len(N) != 0:
        while len(N) != 0 and N[0][0] <= t:  # N[0][0] to r pierwszego elementu (o ineksie 0)
            e = N[0][1]  # index zadania o najmniejszym r
            x = (G_0[e][0], e)  # x -> ineks zadanie o najmniejszym r; G_0[x][0] -> q tego zadania
            G.append(x)  # Dodanie powyższego elementu do zbioru zadan gotowych
            N.pop(0)  # Usunięcie elementu ze zbioru zadań niegotowych

            if count != 0:
                if G_0[e][0] > G_0[l][0]: czy ma większe od l (czas dostarczenia)
                    P[l] = (t - N_0[e][0], P[l][1]) przerywane
                    t = N_0[e][0]
                    if P[l][0] > 0:
                        G.append((G_0[l][0], l))

        if len(G) == 0:
            t = N[0][0]
        else:
            Sort_G()  # Sortowanie G -> Malejące q
            print(G)
            e = G[0][1]  # index zadania o największym q (jest to element o indeksie 0)
            G.pop(0)  # Usuwanie 1 elementu

            l = e
            count += 1
            t = t + P[e][0]  # Akualizacja czasu
            C_max = max(C_max, t + G_0[e][0])  # Wyznaczenie maksymalnego terminu dostarczenia
    return C_max


def main():
    wczytaj("SCHRAGE5.DAT")
    print(Schrage())


main()
