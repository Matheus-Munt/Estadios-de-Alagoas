import requests
import sqlite3 as lt
import folium

con = lt.connect('Estadio.db')
c = con.cursor()

con1 = lt.connect('Propriedade.db')
c1 = con1.cursor()

df = requests.get('http://dados.al.gov.br/dataset/1870ba20-2c86-4c97-ab39-cf1bc0aebc61/resource/833b1ef4-894a-4d39-b1c2-ecf5d951b44f/download/estadios.geojson.geojson')
n = df.json()
    
def Create_Table():
    c.execute("CREATE TABLE IF NOT EXISTS Propriedade(Estadio TEXT, Propriedade TEXT)")
    c1.execute("CREATE TABLE IF NOT EXISTS Municipio(Estadio TEXT, Municipio TEXT)")
        
def Entrada(Estadio,Propriedade,Municipio):
    
    c.execute("INSERT INTO Propriedade (Estadio, Propriedade) VALUES (?,?)",(Estadio,Propriedade))
    c1.execute("INSERT INTO Municipio (Estadio, Municipio) VALUES (?,?)",(Estadio,Municipio))
    con.commit
    con1.commit

Create_Table()

for i in range(len(n['Feature'])):   
    Estadio = n['Feature'][i]['properties']['Nome']
    Propriedade = n['Feature'][i]['properties']['Propriedade']   
    Municipio = n['Feature'][i]['properties']['Município']

Entrada(Estadio,Propriedade,Municipio)

c.close
con.close

c1.close
con1.close

c.execute("SELECT * FROM (Propriedade)")
c1.execute("SELECT * FROM (Municipio)")

rows = c.fetchall()
rows1= c1.fetchall()
