from Socio import Socio
from Copia import Copia

class Emprestimo():
    codE=None
    dataE=None
    dataD=None
    valorPago=None
    limiteT=None
    preco=None
    tipo=None
    listaEstadoR=[]
    ListSocioI=[]
    ListEmprestimo=[]
    
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
    
    def addMulta(self,preco):
        self.preco=preco 
        return self.preco
    
    def getpreco(self):
        return self.preco
     
    def pagamento(self,valorPagar):
         #Pagamento de Emprestimo
         self.preco=0
         self.valorPago=1
         return self.valorPago 
         
    
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
        copia=Copia()
        cod = raw_input("Digite o codigo da copia:")

        estado = raw_input("Informe qual e o estado da copia(bom/ruim)")
        if estado=="ruim":
            self.listaEstadoR=self.listaEstadoR+[cod]
            print "Lista Atualizada"
            print self.listaEstadoR
            copia.setEstado("ruim")
    
        dataDev = raw_input("Digite a data da devolucao:")
        self.setdataD(dataDev)
        dataEmprestimo=self.getdataD();
        print dataEmprestimo
        
        #Informar quantidade de horas do aluguel
        
        limiteT = raw_input("Digite a quantidade de horas que o socio ficou com o filme")
        limiteT=int(limiteT)
        self.setlimiteT(limiteT)
        
        multa=5
        tipo = raw_input("Digite o tipo do filme(Lancamento/Comum)")
        self.setpreco(tipo)
        preco=self.getpreco()       
        if limiteT>=72: 
            print "Multa sera acrescentada"
            precoFinal=self.addMulta(preco+multa) 
            list=[precoFinal,dataEmprestimo,estado]
            print list
            return list
        else:
            print "Multa nao sera acrescentada" 
            list=[preco,dataEmprestimo,estado]
            print list  
            return list
    
    
    def socioStatus(self,numS):
        ListSocioI=0
        socio = Socio()
        socio.setNumIns(numS)
        numIns=socio.getNumIns()
        
        valor=self.devolver()
        
        pagar = raw_input("Deseja pagar o emprestimo(sim/nao)")
        if pagar=="sim":
            pago=self.pagamento(valor)
            print "Socio efetuou o pagamento com sucesso"
            return pagar
        else:
            print "Socio Inadimplente"
            self.ListSocioI=self.ListSocioI+[numIns]
            return pagar
            
            
    def listaEmprestimo(self):
        listA=self.alugar()
        listD=self.devolver()
        listD.pop(2)
        print listD
        listE=listA+listD
        print listE
        return listE
        
         
  
    
