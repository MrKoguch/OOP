class Molecule:
    def __init__(self):
        self._atoms = {}
        self._bonds = {}

    def add_atom(self, atom: str, *, map_: int = None):
        if map_ is None:
            map_ = max(self._atoms, default=0) + 1
        elif not isinstance(map_, int):
            raise TypeError
        elif map_ < 1:
            raise ValueError
        elif map_ in self._atoms:
            raise KeyError

        if not isinstance(atom, str):
            raise TypeError
        elif atom.upper() not in ("C", "N", "CL", "F", "BR", "S", "O", "I"):
            raise ValueError
        self._atoms[map_] = atom.upper()
        self._bonds[map_] = {}
        return map_  # чтобы значть что это был за атом, чтобы понять, какой это был атом, т.к. мы могли и не знать мап
        # данного атома

    def add_bond(self, map1, map2, bond):
        if not isinstance(bond, int):
            raise TypeError
        if bond not in (1, 2, 3):
            raise ValueError

        # есть ли в селф.атом , что мап1 не равно map2, что уже есть связь м\у этими атомами, что одноатомн мол-ла
        neigh1 = self._bonds[map1]
        neigh2 = self._bonds[map2]

        if neigh1 is neigh2:  # что map1 не равно map2
            raise KeyError
        elif map1 in neigh2:  # что уже есть связь м\у этими атомами
            raise KeyError

        neigh1[map2] = bond
        neigh2[map1] = bond

    def show_bonds(self):
        return self._bonds

    def show_atoms(self):
        return self._atoms

    # def _check_list(self, start):  # Проверка графа на связность.
    #     ...

    def del_bond(self, map1, map2):
        if map2 not in self._bonds[map1]:
            raise KeyError
        self._bonds[map1].pop(map2)
        self._bonds[map2].pop(map1)
        if not self._bonds[map1]:  # удаляет атом если у него больше нет пар
            self._bonds.pop(map1)
            self._atoms.pop(map1, None)
        if not self._bonds[map2]:
            self._bonds.pop(map2)
            self._atoms.pop(map2, None)

    def del_atom(self, map_):
        self._atoms.pop(map_)
        n = self._bonds.pop(map_)
        for i in n.keys():
            self._bonds[i].pop(map_)
            if not self._bonds[i]:  # удаляет атом если у него больше нет пар
                self._bonds.pop(i)
                self._atoms.pop(i)
        if not self._bonds:
            raise RuntimeError


# дописать проверки для atom - 15 строка
# добавить метод : del_atom(map_), del_bond(map1, map2)


ol = Molecule()
ol.add_atom("C")
ol.add_atom("c")
ol.add_atom("N")
ol.add_atom("n")
ol.add_atom("O")
ol.add_atom("o")
print(ol.show_atoms())
ol.add_bond(1, 2, 1)
ol.add_bond(2, 3, 1)
ol.add_bond(3, 4, 1)
ol.add_bond(3, 5, 2)
ol.add_bond(6, 4, 1)
ol.add_bond(6, 5, 2)
print(ol.show_bonds())
ol.del_bond(1, 2)
print(ol.show_bonds())
print(ol.show_atoms())
ol.del_atom(2)
print(ol.show_bonds())
print(ol.show_atoms())
