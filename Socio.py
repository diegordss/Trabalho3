class Socio:
    numIns=None
    nome=None
    end=None
    tel=None
    
    def cadastrarSocio(self):
        while 1:
            cont=0
            numIns = raw_input("Digite o numero de inscricao do socio:")
            self.setNumIns(numIns)
            
            nome = raw_input("Digite o nome do socio:")
            self.setNome(nome)
            
            end = raw_input("Digite o endereco do socio:")
            self.setEnd(end)
            
            tel = raw_input("Digite o telefone do socio:")
            self.setTel(tel)
            
            listaCadastro=[numIns,nome,end,tel]
            print listaCadastro
            ++cont
            opcaoContinuar = raw_input("Voce deseja continuar a cadastrar?(sim/nao)")
            if opcaoContinuar=='nao':break
        return listaCadastro

    
    def setNumIns(self,numIns):
        self.numIns=numIns
    
    def getNumIns(self):
        return self.numIns
    
    def setNome(self,nome):
        self.nome=nome
        
    def getNome(self):
        return self.nome
    
    def setEnd(self,end):
        self.end=end
        
    def getEnd(self):
        return self.end
    
    def setTel(self,tel):
        self.tel=tel
        
    def getTel(self):
        return self.tel
