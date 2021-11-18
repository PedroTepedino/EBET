import bd

def create_better(mysql):

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
            senha_ap VARCHAR(256) NOT NULL);
            """

    if mysql.executar(comando, ()):
        print ("Tabela APOSTADOR criada com sucesso!")

def create_jogo(mysql):

    comando = "DROP TABLE IF EXISTS jogo;"

    if mysql.executar(comando, ()):
        print ("Tabela JOGO excluída com sucesso!")

    comando = """
            CREATE TABLE jogo (idt_pt INT AUTO_INCREMENT PRIMARY KEY,
            nme_jg VARCHAR(256) NOT NULL,
            desc_jg VARCHAR(256) NOT NULL);
            """
    if mysql.executar(comando, ()):
        print ("Tabela JOGO criada com sucesso!")
            

def main():
    mysql_connection = bd.SQL("ENhmDU84Vz", "kdEBNUvuo4", "ENhmDU84Vz", "remotemysql.com", "3306")
    create_better(mysql_connection)
    create_jogo(mysql_connection)

if __name__ == "__main__":
    main()
