class Fusee():
    """La classe fusee prend en attribut, la taille, le poids, le nombre de modules"""
    def __init__(self, taille, poids):
        self.taille = taille
        self.poids = poids
        self.nombre_modules = len(taille)

    def _get_taille(self):
        print("On accede a l'attribut taille")
        return self._taille
    def _set_taille(self, nouvelle_taille):
        print("On modifie l'attribut taille")
        self._taille = nouvelle_taille
    taille = property(_get_taille, _set_taille)

    def _get_poids(self):
        print("On accede a l'attribut poids")
        return self._poids
    def _set_poids(self, nouveau_poids):
        print("On modifie l'attribut poids")
        self._poids = nouveau_poids
    poids = property(_get_poids,_set_poids)

    def _get_nombre_modules(self):
        print("On accede a l'attribut nombre de module")
        return self._nombre_modules
    def _set_nombre_modules(self, nouveau_nombre_modules):
        print ("On modifie l'attribut nombre_modules")
        self._nombre_modules = nouveau_nombre_modules
    nombre_modules = property(_get_nombre_modules, _set_nombre_modules)





