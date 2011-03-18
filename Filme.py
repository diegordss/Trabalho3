from Diretor import Diretor
from Artista import Artista

class Filme(Diretor,Artista):
    cod=None
    titulo=None
    duracao=None
    ano=None
    genero=None
    diretor=None
    artista1=None
    artista2=None
  
    
    def setCod(self,cod):
        self.cod=cod
    
    def getCod(self):
        return self.cod
    
    def setTitulo(self,titulo):
        self.titulo=titulo
        
    def getTitulo(self):
        return self.titulo
    
    def setDuracao(self,duracao):
        self.duracao=duracao
        
    def getDuracao(self):
        return self.duracao
    
    def setAno(self,ano):
        self.ano=ano
        
    def getAno(self):
        return self.ano
    
    def setGenero(self,genero):
        self.genero=genero
        
    def getGenero(self):
        return self.genero
    
    def setDiretor(self,diretor):
        dir=Diretor()
        dir.setnomeD(diretor)
        nome=dir.getnomeD()
        self.diretor=nome
        
    def getDiretor(self):
        return self.diretor
    
    def setArtista1(self,artista1):
        art1=Artista()
        art1.setnomeA(artista1)
        nome=art1.getnomeA()
        self.artista1=nome
        
    def getArtista1(self):
        return self.artista1
    
    def setArtista2(self,artista2):
        art2=Artista()
        art2.setnomeA(artista2)
        nome=art2.getnomeA()
        self.artista2=nome
        
    def getArtista2(self):
        return self.artista2
    
   
    def relatorioFilmeGenero(self,cod,titulo,genero):
        list=[self.cod,self.titulo,self.genero]
        print list
        return list
    
    def relatorioFilmeDiretor(self,cod,titulo,diretor):
        list=[self.cod,self.titulo,self.diretor]
        print list
        return list
    
    def relatorioFilmeArtista(self,cod,titulo,artista1):
        list=[self.cod,self.titulo,self.artista1]
        print list
        return list
    
   
   






