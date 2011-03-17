import unittest
from Artista import Artista
from Diretor import Diretor
from Socio import Socio
from Filme import Filme
from Copia import Copia
from Emprestimo import Emprestimo

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
        cod=self.filme.getCod()
        tit=self.filme.getTitulo()
        gen=self.filme.getGenero()
        relFilmeGenero=self.filme.relatorioFilmeGenero(cod,tit,gen)
        assert relFilmeGenero != None,"Relatorio nao existe"
        
    def testRelatorioFilmeDiretor(self):
        cod=self.filme.getCod()
        tit=self.filme.getTitulo()
        dir=self.filme.getDiretor()
        relFilmeDiretor=self.filme.relatorioFilmeDiretor(cod,tit,dir)
        assert relFilmeDiretor != None,"Relatorio nao existe"
        
    def testRelatorioFilmeArtista(self):
        cod=self.filme.getCod()
        tit=self.filme.getTitulo()
        art1=self.filme.getArtista1()
        relFilmeArtista=self.filme.relatorioFilmeArtista(cod,tit,art1)
        assert relFilmeArtista != None,"Relatorio nao existe"
        
class TestCopia(unittest.TestCase):  
    
    def setUp(self):
        self.copia = Copia()
              
    def testCopiaExiste(self):
        assert self.copia != None, "Copia nao existe"
            
    def testInsereCodigo(self):
        self.copia.setCod(001)
        assert self.copia.cod != None,"Codigo esta vazio"
    
    def testInsereDataAquisicao(self):
        self.copia.setDataAq(2010)
        assert self.copia.dataAq != None,"Data de Aquisicao esta vazio"
    
    def testInsereEstado(self):
        self.copia.setEstado("bom")
        assert self.copia.estado != None,"Estado esta vazio"
    
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
            
    def testRelatorioFilmeQuant(self): 
        self.copia.setCod(203)
        self.copia.setQuant(7)
        cod=self.copia.getCod()
        quant=self.copia.getQuant()
        relFQ=self.copia.relatorioFilmeQuant(cod,quant)
        assert relFQ != [None,None], "Relatorio esta vazio"
        
   

class TestDiretor(unittest.TestCase):  
    
    def setUp(self):
        self.diretor = Diretor()
              
    def testCopiaExiste(self):
        assert self.diretor != None, "Diretor nao existe"
            
    def testInsereCodigo(self):
        self.diretor.setCodD(001)
        assert self.diretor.codD != None,"Codigo esta vazio"
    
    def testInsereNomeDiretor(self):
        self.diretor.setnomeD("Pedro Luiz")
        assert self.diretor.nomeD != None,"Nome do Diretor esta vazio"
    
    def testInserePaisOrigem(self):
        self.diretor.setpaisOrigem("Estados Unidos")
        assert self.diretor.paisOrigem != None,"Pais de Origem esta vazio"
    
    def testInsereDataNascimento(self):
        self.diretor.setdataNascimento("26/05/1984")
        assert self.diretor.dataNascimento != None,"Data de Nascimento esta vazio"
    
     
    
    def testImprimeCodigo(self):
        self.diretor.setCodD(001)
        cod=self.diretor.getCodD()
        assert cod != None,"Codigo esta vazio"
    
    def testImprimeNomeDiretor(self):
        self.diretor.setnomeD("Pedro Luiz")
        nomeD=self.diretor.getnomeD()
        assert nomeD != None,"Nome do Diretor esta vazio"
    
    def testImprimePaisOrigem(self):
        self.diretor.setpaisOrigem("Estados Unidos")
        paisOrigem=self.diretor.getpaisOrigem()
        assert paisOrigem != None,"Pais de Origem esta vazio"
    
    def testImprimeDataNascimento(self):
        self.diretor.setdataNascimento("26/05/1984")
        dataNascimento=self.diretor.getdataNascimento()
        assert dataNascimento != None,"Data de Nascimento esta vazio"

class TestArtista(unittest.TestCase):  
    
    def setUp(self):
        self.artista = Artista()
              
    def testCopiaExiste(self):
        assert self.artista != None, "Artista nao existe"
            
    def testInsereCodigo(self):
        self.artista.setCodA(001)
        assert self.artista.codA != None,"Codigo esta vazio"
    
    def testInsereNomeArtista(self):
        self.artista.setnomeA("Pedro Luiz")
        assert self.artista.nomeA != None,"Nome do Artista esta vazio"
    
    def testInserePaisOrigem(self):
        self.artista.setpaisOrigem("Estados Unidos")
        assert self.artista.paisOrigem != None,"Pais de Origem esta vazio"
    
    def testInsereDataNascimento(self):
        self.artista.setdataNascimento("26/05/1984")
        assert self.artista.dataNascimento != None,"Data de Nascimento esta vazio"
    
     
    
    def testImprimeCodigo(self):
        self.artista.setCodA(001)
        cod=self.artista.getCodA()
        assert cod != None,"Codigo esta vazio"
    
    def testImprimeNomeDiretor(self):
        self.artista.setnomeA("Pedro Luiz")
        nomeA=self.artista.getnomeA()
        assert nomeA != None,"Nome do Artista esta vazio"
    
    def testImprimePaisOrigem(self):
        self.artista.setpaisOrigem("Estados Unidos")
        paisOrigem=self.artista.getpaisOrigem()
        assert paisOrigem != None,"Pais de Origem esta vazio"
    
    def testImprimeDataNascimento(self):
        self.artista.setdataNascimento("26/05/1984")
        dataNascimento=self.artista.getdataNascimento()
        assert dataNascimento != None,"Data de Nascimento esta vazio"

class TestEmprestimo(unittest.TestCase):  
        
    def setUp(self):
        self.emprestimo = Emprestimo()
              
    def testEmprestimoExiste(self):
        assert self.emprestimo != None, "Emprestimo nao existe"
            
    def testInsereCodigo(self):
        self.emprestimo.setCodE(001)
        assert self.emprestimo.codE != None,"Codigo esta vazio"
    
    def testInsereDataEmprestimo(self):
        self.emprestimo.setdataE("23/02/2011")
        assert self.emprestimo.dataE != None,"Data de Emprestimo esta vazio"
    
    def testInsereDataDevolucao(self):
        self.emprestimo.setdataD("26/02/2011")
        assert self.emprestimo.dataD != None,"Data de Devolucao esta vazio"
   
    def testImprimeCodigo(self):
        self.emprestimo.setCodE(001)
        cod=self.emprestimo.getCodE()
        assert cod != None,"Codigo esta vazio"
    
    def testImprimeDataEmprestimo(self):
        self.emprestimo.setdataE("23/02/2011")
        dataE=self.emprestimo.getdataE()
        assert dataE != None,"Data de Emprestimo esta vazio"
    
    def testImprimeDataDevolucao(self):
        self.emprestimo.setdataD("26/02/2011")
        dataD=self.emprestimo.getdataD()
        assert dataD != None,"Data de Devolucao esta vazio"  
        
    def testDevolucao(self):
        lFinal=self.emprestimo.devolver()        
        pFinal=lFinal[0]  
        pFinal=int(pFinal)
        self.assertEqual(pFinal,self.emprestimo.preco,msg="Erro: Preco Final com Valores Diferentes") 
        
    def testCopiaRuim(self):
        lFinal=self.emprestimo.devolver()
        print "teste lista"
        print lFinal
        listaEstadoR=lFinal[2]
        if listaEstadoR=="ruim":
            self.assertNotEqual(self.emprestimo.listaEstadoR,None,msg="Erro: Socio Inadimplente")
       
    def testSocioInadimplente(self):
        pagar=self.emprestimo.socioStatus(001)
        if pagar=="nao":
            self.assertNotEqual(self.emprestimo.ListSocioI,None,msg="Erro: Socio Inadimplente")
            
        
    
            
 
if  __name__=="__main__":
    unittest.main() 