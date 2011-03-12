import unittest
from Socio3 import Socio3
from Filme3 import Filme3
from Copia3 import Copia3

class TestSocio(unittest.TestCase):
    
    def setUp(self):
        self.socio = Socio3()
        
    def testSocioExiste(self):
        assert self.socio != None, "Socio nao existe"
        
    def testNumInscricao(self):
        assert self.socio.numIns != None,"Numero de inscricao nao existe"
        
    def testNome(self):
        assert self.socio.nome != None,"Nome nao existe"
        
    def testEndereco(self):
        assert self.socio.end != None,"Endereco nao existe"
    
    def testTelefone(self):
        assert self.socio.tel != None,"Telefone nao existe"


class TestFilme(unittest.TestCase): 
    
    def setUp(self):
        self.filme = Filme3()
        
    def testFilmeExiste(self):
        assert self.filme != None, "Filme nao existe"

    def testCodigo(self):
        assert self.filme.cod != None,"Codigo nao existe"
        
    def testTitulo(self):
        assert self.filme.titulo != None,"Titulo nao existe"
        
    def testDuracao(self):
        assert self.filme.duracao != None,"Duracao nao existe"
    
    def testAno(self):
        assert self.filme.ano != None,"Ano nao existe"
    
    def testGenero(self):
        assert self.filme.genero != None,"Genero nao existe"
        
    def testDiretor(self):
        assert self.filme.diretor != None,"Diretor nao existe"
        
    def testArtista1(self):
        assert self.filme.artista1 != None,"Artista1 nao existe"
    
    def testArtista2(self):
        assert self.filme.artista2 != None,"Artista2 nao existe"
    

class TestCopia(unittest.TestCase):  
    
    def setUp(self):
        self.copia = Copia3()
              
    def testCopiaExiste(self):
        assert self.copia != None, "Copia nao existe"
            
    def testCodigo(self):
        assert self.copia.cod != None,"Codigo nao existe"
    
    def testDataAquisicao(self):
        assert self.copia.dataAq != None,"Data de Aquisicao nao existe"
    
    def testEstado(self):
        assert self.copia.estado != None,"Estado nao existe"
    
    def testListaEmprestimos(self):
        assert self.copia.listaE != None,"Lista de Emprestimos nao existe"
        

        
if  __name__=="__main__":
    unittest.main() 