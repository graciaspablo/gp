# Contar cantidad de mensajes diarios al grupo

import re
import pandas as pd
from datetime import date

def read_txt():
    f = open("chats/chat.txt", "r", encoding='utf-8')

    #Arreglar nombres
    data = f.read()
    data = data.replace('- antoni:', '- Anton:')
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

    messages = re.findall('(\d+/\d+/\d+, \d+:\d+\d+) - (.*?): (.*)', data, re.MULTILINE)

    return messages

def make_dataframe():
    df = pd.DataFrame(read_txt(),columns=['Time', 'Name', 'Message'])

    df['Time'] = pd.to_datetime(df.Time, format='%d/%m/%y, %H:%M')

    #Dividir datetime a fecha y hora
    df['new_date'] = [d.date() for d in df['Time']]
    df['new_time'] = [d.time() for d in df['Time']]

    df = df.drop('Time', axis=1).drop('Name', axis=1).drop('new_time', axis=1)


    df = df['new_date'].value_counts()

    df = df.reset_index()

    df = df.set_index('index').asfreq('D')

    df['Mensajes'] = df['new_date']
    df = df.drop('new_date', axis=1)
    df = df.fillna(0)
    df = df.astype(int)

    #pd.set_option('precision', 0)




    return df

df_dm = make_dataframe()

if __name__ == '__main__':
    print(df_dm)
    df_dm.to_csv('dm.csv', encoding='utf-8')
