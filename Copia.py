from Filme import Filme
class Copia(Filme):
    cod=None
    dataAq=None
    estado=None
    quant=None
    
    def __init__(self):
        pass
   
    def cadastrarFilme(self):
        filme= Filme()
        while 1:
            cont=0
            codEscolhido = raw_input("Digite o codigo do filme que voce quer cadastrar:")
            filme.setCod(codEscolhido)
            
            codCopEscolhido = raw_input("Digite o codigo da copia que voce quer cadastrar:")
            self.setCod(codCopEscolhido)
            
            dataAqEscolhido = raw_input("Digite a data da aquisicao referente ao filme que voce quer cadastrar:")
            self.setDataAq(dataAqEscolhido)
            
            codCopia = raw_input("Digite o codigo da copia que voce quer cadastrar:")
            self.setCod(codCopia)

            tituloEscolhido = raw_input("Digite o titulo do filme que voce quer cadastrar:")
            filme.setTitulo(tituloEscolhido)
            
            duracaoEscolhida = raw_input("Digite a duracao do filme que voce quer cadastrar:")
            filme.setDuracao(duracaoEscolhida)

            anoEscolhido = raw_input("Digite o ano do filme que voce quer cadastrar:")
            filme.setAno(anoEscolhido)
            
            generoEscolhido = raw_input("Digite o genero do filme que voce quer cadastrar:")
            filme.setGenero(generoEscolhido)

            diretorEscolhido = raw_input("Digite o diretor do filme que voce quer cadastrar:")
            filme.setDiretor(diretorEscolhido)
                       
            artista1Escolhido = raw_input("Digite o nome de um ator do filme que voce quer cadastrar:")
            filme.setArtista1(artista1Escolhido)
            
            artista2Escolhido = raw_input("Digite o nome de um ator do filme que voce quer cadastrar:")
            filme.setArtista2(artista2Escolhido)
            
            listaCadastro=[codEscolhido,codCopEscolhido,dataAqEscolhido,codCopia,tituloEscolhido,duracaoEscolhida,anoEscolhido,generoEscolhido,diretorEscolhido,artista1Escolhido,artista2Escolhido]
            print listaCadastro
            ++cont
            opcaoContinuar = raw_input("Voce deseja continuar a cadastrar?(sim/nao)")
            if opcaoContinuar=='nao':break  
        return listaCadastro

   
    def setCod(self,cod):
        self.cod=cod
    
    def getCod(self):
        return self.cod
    
    def setDataAq(self,dataAq):
        self.dataAq=dataAq
        
    def getDataAq(self):
        return self.dataAq
    
    def setEstado(self,estado):
        self.estado=estado
        
    def getEstado(self):
        return self.estado
    
    def setQuant(self,quant):
        self.quant=quant
        
    def getQuant(self):
        return self.quant
    
    def relatorioFilmeQuant(self,cod,quant):
        list=[self.cod,self.quant]
        print list
        return list
        
    

