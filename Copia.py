class Copia():
    cod=None
    dataAq=None
    estado=None
    listaE=None
    quant=None
    
    def __init__(self):
        pass
   
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
    
    def setListaE(self,listaE):
        self.listaE=listaE
        
    def getListaE(self):
        return self.listaE
    
    def setQuant(self,quant):
        self.quant=quant
        
    def getQuant(self):
        return self.quant
    
    def relatorioFilmeQuant(self,cod,quant):
        list=[self.cod,self.quant]
        return list
    
    
    
    

