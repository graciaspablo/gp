import re
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2oKqn",
  database="gp"
)


def read_txt():
    f = open("chats/chat.txt", "r", encoding='utf-8')

    #Arreglar nombres
    data = f.read()
    data = data.replace('- antoni:', '- Anton:')
    data = data.replace('- Antoni:', '- Anton:')
    data = data.replace('- Sergowo Asterisco:', '- Sergio:')
    data = data.replace('- Sergio Acróbata:', '- Sergio:')
    data = data.replace('- Miden:', '- Miranda:')
    data = data.replace('- Netherlands:', '- Miranda:')
    data = data.replace('- Diego Smash:', '- Diego:')
    data = data.replace('- Paula Arcas:', '- Paula:')
    data = data.replace('- Laura Toro Diosdado:', '- Laura:')
    data = data.replace('- Jaoquien:', '- Joaquín:')
    data = data.replace('- Joaquin:', '- Joaquín:')
    data = data.replace('- aitor:', '- Aitor:')

    messages = re.findall('(\d+/\d+/\d+, \d+:\d+\d+) - (.*?): (gp$|Gp$|GP$)', data, re.MULTILINE)

    return messages



messages = read_txt()

for i in range(30):
    for message in messages:
        datetime = message[0]
        jugador = message[1]
        mensaje = message[2]

        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO `gp`.`gps` (`datetime`, `jugador`, `mensaje`) VALUES " + str(message))



mycursor.execute("SELECT * FROM student")

myresult = mycursor.fetchall()

mydb.commit()