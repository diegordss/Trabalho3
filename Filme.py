class Filme:
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
        self.diretor=diretor
        
    def getDiretor(self):
        return self.diretor
    
    def setArtista1(self,artista1):
        self.artista1=artista1
        
    def getArtista1(self):
        return self.artista1
    
    def setArtista2(self,artista2):
        self.artista2=artista2
        
    def getArtista2(self):
        return self.artista2
    
    def relatorioFilmeGenero(self,titulo,genero):
        list=[self.titulo,self.genero]
        return list
    
    def relatorioFilmeDiretor(self,titulo,diretor):
        list=[self.titulo,self.diretor]
        return list
    
    def relatorioFilmeArtista(self,titulo,artista1):
        list=[self.titulo,self.artista1]
        return list






