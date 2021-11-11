import random

class GeraDados:

   def numeroInt(self, inicio, fim):
       zeroUm = random.random()
       return int(zeroUm *(fim-inicio) + inicio)

   def numeroFloat(self, inicio, fim):
       zeroUm = random.random()
       return zeroUm * (fim - inicio) + inicio

   def caractere(self):
       asc=self.numeroInt(32, 127)
       return chr(asc)

   def letra(self):
       sorteio = self.numeroInt(0,53)
       if sorteio < 27:
           return chr(65 + sorteio)
       else:
           return chr(97 + (sorteio-26))
       return chr(sorteio)


   def letras(self, qtd):
       sorteio = self.numeroInt(65,123)
       while sorteio > 90 and sorteio < 97:
           sorteio = self.numeroInt(65,123)
       return chr(sorteio)

   def caracteres(self, qtd):
       ret=""
       for i in range(qtd):
           ret += self.caractere()
       return ret

   def data(self):
       ret=""
       ano = self.numeroInt(1900, 2030)
       mes = self.numeroInt(1, 12)
       dia = self.numeroInt(1, 28)
       ret = str(ano) + "-" + str(mes) + "-" + str(dia)
       return ret

   def hora(self):
       hr = self.numeroInt(0, 23)
       mn = self.numeroInt(0, 59)
       sg = self.numeroInt(0, 59)
       ret = str(hr) + ":" + str(mn) + ":" + str(sg)
       return ret

   def nome(self):
       nomes = ["Laura", "Beatriz", "Guilherme", "Maria", "Júlia", "Ana", "Alice", "Maria Eduarda", "Marcus", "Larissa", "Sofia", "Mariana", "Isabela", "Renato", "Camila", "Valentina", "Helena", "Lara", "Letícia", "Amanda", "Rogério", "Luana", "Yasmin", "Sophia", "Rebeca", "Juliana", "Roberto"]
       sorteio = self.numeroInt(0,len(nomes))
       return nomes[sorteio]

