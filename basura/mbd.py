# Buscar mensajes de buenos días

import re
import pandas as pd
from datetime import date

import basura.config as config

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

    message_string = '|'.join(config.MENSAJES)
    messages = re.findall('(\d+/\d+/\d+, \d+:\d+\d+) - (Pablo): (' + message_string + ')', data)

    return messages

def make_dataframe():
    df = pd.DataFrame(read_txt(),columns=['Time', 'Name', 'Message'])

    df['Time'] = pd.to_datetime(df.Time, format='%d/%m/%y, %H:%M')

    #df.drop('Message', axis=1)

    #Dividir datetime a fecha y hora
    df['new_date'] = [d.date() for d in df['Time']]
    df['new_time'] = [d.time() for d in df['Time']]

    df = df.drop('Time', axis=1).drop('Name', axis=1)

    #Reordenar columnas
    cols = df.columns.tolist()

    cols = cols[-1:] + cols[:-1]
    cols = cols[-1:] + cols[:-1]

    df = df[cols] 

    df.columns = ['new_date', 'HORA_MBD', 'MBD_TIPO']

    df['new_date'] = pd.to_datetime(df.new_date, format='%Y/%m/%d')

    df = df.set_index('new_date').asfreq('D')

    return df

df_mbd = make_dataframe()

if __name__ == '__main__':
    print(df_mbd)