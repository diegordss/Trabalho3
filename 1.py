import unittest
from Socio import Socio
from Filme import Filme
from Copia import Copia

class TestSocio(unittest.TestCase):
    def testSocioExiste(self):
        socio = Socio()
        assert socio != None, "Socio nao existe"

class TestFilme(unittest.TestCase): 
    def testFilmeExiste(self):
        filme = Filme()
        assert filme != None, "Filme nao existe"

class TestCopia(unittest.TestCase):
    def testCopiaExiste(self):
        copia = Copia()
        assert copia != None, "Copia nao existe"
        
if  __name__=="__main__":
    unittest.main() 