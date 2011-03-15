from Socio import Socio

class Emprestimo(Socio):
    codE=None
    dataE=None
    dataD=None
    pago=None
    limiteT=None
    preco=None
    tipo=None
    
    def __init__(self):
        pass
        
    def setCodE(self,codE):
        self.codE=codE
            
    def getCodE(self):
        return self.codE
    
    def setdataE(self,dataE):
        self.dataE=dataE
    
    def getdataE(self):
        return self.dataE

    def setdataD(self,dataD):
        self.dataD=dataD
    
    def getdataD(self):
        return self.dataD
    
      
    
    def setpago(self,pago):
        self.pago=pago
    
    def getpago(self):
        return self.pago
    
    
    def setlimiteT(self,limiteT):
        self.limiteT=limiteT
    
    def getlimiteT(self):
        return self.limiteT
    
    def setpreco(self,tipo):
        if tipo=="Lancamento":
            preco=4
        else:
            preco=2      
        self.preco=preco
        p=self.preco
        return p
    
    def getpreco(self):
        return self.preco

     
     
    
    def alugar(self):
        #Informar numero de inscricao de socio
        
        socio = Socio()
        numS = raw_input("Digite o numero do socio:")
        socio.setNumIns(numS)
        numIns=socio.getNumIns()
        
        #Cadastrar data de emprestimo
             
        dataEmp = raw_input("Digite a data do aluguel:")
        self.setdataE(dataEmp)
        dataEmprestimo=self.getdataE();
       
        
        list=[numIns,dataEmprestimo]
        print list
        return list
        
        
     
     
    def devolver(self):
        multa=5
        self.setpreco("Lancamento")
        preco=self.getpreco()
        
        dataDev = raw_input("Digite a data da devolucao:")
        self.setdataD(dataDev)
        dataEmprestimo=self.getdataE();
        
        #Informar quantidade de horas do aluguel
        
        limiteT = raw_input("Digite a quantidade de horas que o socio ficou com o filme")
        limiteT=int(limiteT)
        self.setlimiteT(limiteT)
                      
        if limiteT>=72:
            self.getpreco()
            print "Multa sera acrescentada" 
            precoFinal=self.preco=self.preco+multa
            list=[precoFinal,dataEmprestimo]
            return list
        else:
            print "Multa nao sera acrescentada" 
            list=[preco,dataEmprestimo]  
            return list
    
         
  
    
