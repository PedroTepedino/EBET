import bd
import mysql.connector

mysql = bd.SQL("root", "hiragi7", "ebet")

comando = "DROP TABLE IF EXISTS apostador;"

if mysql.executar(comando, ()):
   print ("Tabela APOSTADOR excluída com sucesso!")


comando = """
          CREATE TABLE apostador (idt_ap INT AUTO_INCREMENT PRIMARY KEY,
          nmecomp_ap VARCHAR(256) NOT NULL, 
          datanasc_ap DATE NOT NULL, 
          cpf_ap VARCHAR(14) NOT NULL,
          email_ap VARCHAR(256) NOT NULL,
          username_ap VARCHAR(256) NOT NULL,
          senha_ap VARCHAR(256) NOT NULL,
          confsenha_ap VARCHAR(256) NOT NULL);
         """

if mysql.executar(comando, ()):
   print ("Tabela APOSTADOR criada com sucesso!")
