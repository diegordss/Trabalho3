import unittest
from Socio import Socio
from Filme import Filme
from Copia import Copia

class TestSocio(unittest.TestCase):
    def testSocioExiste(self):
        socio = Socio()
        assert socio != None, "Socio nao existe"
        
    def testNumInscricao(self):
        socio = Socio()
        assert socio.numIns != None,"Numero de inscricao nao existe"
        
    def testNome(self):
        socio = Socio()
        assert socio.nome != None,"Nome nao existe"
        
    def testEndereco(self):
        socio = Socio()
        assert socio.end != None,"Endereco nao existe"
    
    def testTelefone(self):
        socio = Socio()
        assert socio.tel != None,"Telefone nao existe"


class TestFilme(unittest.TestCase): 
    def testFilmeExiste(self):
        filme = Filme()
        assert filme != None, "Filme nao existe"

    def testCodigo(self):
        filme = Filme()
        assert filme.cod != None,"Codigo nao existe"
        
    def testTitulo(self):
        filme = Filme()
        assert filme.titulo != None,"Titulo nao existe"
        
    def testDuracao(self):
        filme = Filme()
        assert filme.duracao != None,"Duracao nao existe"
    
    def testAno(self):
        filme = Filme()
        assert filme.ano != None,"Ano nao existe"
    
    def testGenero(self):
        filme = Filme()
        assert filme.genero != None,"Genero nao existe"
        
    def testDiretor(self):
        filme = Filme()
        assert filme.diretor != None,"Diretor nao existe"
        
    def testArtista1(self):
        filme = Filme()
        assert filme.artista1 != None,"Artista1 nao existe"
    
    def testArtista2(self):
        filme = Filme()
        assert filme.artista2 != None,"Artista2 nao existe"
    

class TestCopia(unittest.TestCase):        
    def testCopiaExiste(self):
        copia = Copia()
        assert copia != None, "Copia nao existe"
            
    def testCodigo(self):
        copia = Copia()
        assert copia.cod != None,"Codigo nao existe"
    
    def testDataAquisicao(self):
        copia = Copia()
        assert copia.dataAq != None,"Data de Aquisicao nao existe"
    
    def testEstado(self):
        copia = Copia()
        assert copia.estado != None,"Estado nao existe"
    
    def testListaEmprestimos(self):
        copia = Copia()
        assert copia.listaE != None,"Lista de Emprestimos nao existe"
        

        
if  __name__=="__main__":
    unittest.main() 