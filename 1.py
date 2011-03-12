import unittest
from Socio import Socio
from Filme import Filme
from Copia import Copia

class TestSocio(unittest.TestCase):
    
    def setUp(self):
        self.socio = Socio()
        
    def testSocioExiste(self):
        assert self.socio != None, "Socio nao existe"
        
    def testInsereNumInscricao(self):
        self.socio.setNumIns(1234)
        assert self.socio.numIns != None,"Numero de inscricao esta vazio"
        
    def testInsereNome(self):
        self.socio.setNome("Luiz Inacio Lula") 
        assert self.socio.nome != None,"Nome esta vazio"
        
    def testInsereEndereco(self):
        self.socio.setEnd("Brasilia")        
        assert self.socio.end != None,"Endereco esta vazio"
    
    def testInsereTelefone(self):
        self.socio.setTel(27238644)        
        assert self.socio.tel != None,"Telefone esta vazio"
        
        
        
    def testImprimeNumInscricao(self):
        self.socio.setNumIns(1234)
        numInsc= self.socio.getNumIns()
        assert numInsc != None,"Numero de inscricao esta vazio"
        
    def testImprimeNome(self):
        self.socio.setNome("Luiz Inacio Lula")
        nome= self.socio.getNome() 
        assert nome != None,"Nome esta vazio"
        
    def testImprimeEndereco(self):
        self.socio.setEnd("Brasilia")
        end= self.socio.getEnd()  
        assert end != None,"Endereco esta vazio"
    
    def testImprimeTelefone(self):
        self.socio.setTel(27238644)
        tel= self.socio.getTel()       
        assert tel != None,"Telefone esta vazio"


class TestFilme(unittest.TestCase): 
    
    def setUp(self):
        self.filme = Filme()
        
    def testFilmeExiste(self):
        assert self.filme != None, "Filme nao existe"

    def testInsereCodigo(self):
        self.filme.setCod(001)             
        assert self.filme.cod != None,"Codigo nao existe"
        
    def testInsereTitulo(self):
        self.filme.setTitulo("Avatar")
        assert self.filme.titulo != None,"Titulo nao existe"
        
    def testInsereDuracao(self):
        self.filme.setDuracao("02:00")
        assert self.filme.duracao != None,"Duracao nao existe"
    
    def testInsereAno(self):
        self.filme.setAno(2010)
        assert self.filme.ano != None,"Ano nao existe"
    
    def testInsereGenero(self):
        self.filme.setGenero("Ficcao Cientifica")
        assert self.filme.genero != None,"Genero nao existe"
        
    def testInsereDiretor(self):
        self.filme.setDiretor("James Cameron")
        assert self.filme.diretor != None,"Diretor nao existe"
        
    def testInsereArtista1(self):
        self.filme.setArtista1("A1")
        assert self.filme.artista1 != None,"Artista1 nao existe"
    
    def testInsereArtista2(self):
        self.filme.setArtista2("A2")
        assert self.filme.artista2 != None,"Artista2 nao existe"




    def testImprimeCodigo(self):
        self.filme.setCod(001)
        cod=self.filme.getCod()              
        assert cod != None,"Codigo nao existe"
        
    def testImprimeTitulo(self):
        self.filme.setTitulo("Avatar")
        titulo=self.filme.getTitulo()
        assert titulo != None,"Titulo nao existe"
        
    def testImprimeDuracao(self):
        self.filme.setDuracao("02:00")
        duracao=self.filme.getDuracao()
        assert duracao != None,"Duracao nao existe"
    
    def testImprimeAno(self):
        self.filme.setAno(2010)
        ano=self.filme.getAno()
        assert ano != None,"Ano nao existe"
    
    def testImprimeGenero(self):
        self.filme.setGenero("Ficcao Cientifica")
        genero=self.filme.getGenero()
        assert genero != None,"Genero nao existe"
        
    def testImprimeDiretor(self):
        self.filme.setDiretor("James Cameron")
        diretor=self.filme.getDiretor()
        assert diretor != None,"Diretor nao existe"
        
    def testImprimeArtista1(self):
        self.filme.setArtista1("A1")
        artista1=self.filme.getArtista1()
        assert artista1 != None,"Artista1 nao existe"
    
    def testImprimeArtista2(self):
        self.filme.setArtista2("A2")
        artista2=self.filme.getArtista2()
        assert artista2 != None,"Artista2 nao existe"
        
        
    def testRelatorioFilmeGenero(self):
        tit=self.filme.getTitulo()
        gen=self.filme.getGenero()
        self.filme.relatorioFilmeGenero(tit, gen)
        
        
    def testRelatorioFilmeDiretor(self):
        tit=self.filme.getTitulo()
        dir=self.filme.getDiretor()
        self.filme.relatorioFilmeDiretor(tit, dir)
        
    def testRelatorioFilmeArtista(self):
        tit=self.filme.getTitulo()
        art1=self.filme.getArtista1()
        self.filme.relatorioFilmeArtista(tit, art1)


class TestCopia(unittest.TestCase):  
    
    def setUp(self):
        self.copia = Copia()
              
    def testCopiaExiste(self):
        assert self.copia != None, "Copia esta vazio"
            
    def testInsereCodigo(self):
        self.copia.setCod(001)
        assert self.copia.cod != None,"Codigo esta vazio"
    
    def testInsereDataAquisicao(self):
        self.copia.setDataAq(2010)
        assert self.copia.dataAq != None,"Data de Aquisicao esta vazio"
    
    def testInsereEstado(self):
        self.copia.setEstado("bom")
        assert self.copia.estado != None,"Estado esta vazio"
    
    def testInsereListaEmprestimos(self):
        self.copia.setListaE(['numIns','dataE','dataD','valorP'])
        assert self.copia.listaE != None,"Lista de Emprestimos esta vazio"
     
     
        
    def testImprimeCodigo(self):  
        self.copia.setCod(001)
        cod=self.copia.getCod()
        assert cod != None,"Codigo esta vazio"
    
    def testImprimeDataAquisicao(self):
        self.copia.setDataAq(2010)
        dataAq=self.copia.getDataAq()
        assert dataAq != None,"Data de Aquisicao esta vazio"
    
    def testImprimeEstado(self):
        self.copia.setEstado("bom")
        estado=self.copia.getEstado()
        assert estado != None,"Estado esta vazio"
    
    def testImprimeListaEmprestimos(self):
        self.copia.setListaE(['numIns','dataE','dataD','valorP'])
        listaE=self.copia.getListaE()
        assert listaE != None,"Lista de Emprestimos esta vazio"
        
    def testRelatorioFilmeQuant(self):
        tit=self.filme.getTitulo()
        cod=self.copia.getCod()
        self.copia.relatorioFilmeQuant(tit, cod)
    

        
if  __name__=="__main__":
    unittest.main() 