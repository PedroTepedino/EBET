import bd
import mysql.connector


def create_better(mysql):
    #mysql = bd.SQL("ebet", "ebet", "ebetdb")

    comando = "DROP TABLE IF EXISTS apostador;"

    if mysql.executar(comando, ()):
       print ("Tabela APOSTADOR excluida com sucesso!")

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



def main():
    mysql_connection = bd.SQL("ebet", "ebet", "ebetdb")
    create_better(mysql_connection)

if __name__ == "__main__":
    main()
