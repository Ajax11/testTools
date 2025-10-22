import pandas as pd

# Cargar el CSV
# Asegúrate de cambiar 'formulario.csv' por el nombre real de tu archivo
#df = pd.read_csv("testMartes.csv", sep=';')
df = pd.read_csv("NotasWorkshopLicense.csv", sep=';')

#headers_list_direct = list(df)
headers_list = list(df)
#headers_list = df.columns.tolist()
print((headers_list))
#print((headers_list[1:]))

# Crear un DF con las answer
answer = ["Weak copyleft license","Weak copyleft license","Copyleft license","Copyleft license","Weak copyleft license","Permissive software license","Permissive software license","Permissive software license","Attribution","Non-Commercial"]
headers_list_sub_set = headers_list[1:]
dfAnswer = pd.DataFrame([answer], columns=headers_list_sub_set)

list = []
for index, row in df.iterrows():
    rowElement =[]
    i = -1
    for header in headers_list:
        if header == 'Nombre':
            rowElement.append(row[header])
        else:
            #value = row[header] == answer[i]
            #value = row[header] == dfAnswer[header]
            value = 0
            if row[header] == dfAnswer.loc[0,header]:
                value = 1
            rowElement.append(value)
        i += 1
    #print(rowElement)
    list.append(rowElement)
#lambda x: 1 if str(x).strip().lower() == respuestas_correctas["Respuesta1"].lower() else 0

dfFinal=pd.DataFrame(list, columns=headers_list)
print(dfFinal)
dfFinal.to_csv("gradesTestLicensing.csv", index=False)


# Guardar en un nuevo CSV con las notas
#df.to_csv("formulario_notas.csv", index=False)


# Crear un DF con las respuestas
#respuestas = ["Weak copyleft license","Weak copyleft license","Copyleft license","Copyleft license","Weak copyleft license","Permissive software license","Permissive software license","Permissive software license","Attribution","Non-Commercial"]
#dRespuestas = {"respuesta": ["Weak copyleft license","Weak copyleft license","Copyleft license","Copyleft license","Weak copyleft license","Permissive software license","Permissive software license","Permissive software license","Attribution","Non-Commercial"]}


#dLabels = {}

#listaValores = [0]*11
#"Nombre","EPL","MPL","GPL","AGPL","LGPL","BSD_2-Clause","MIT","Apache","CC_A","CC_B"


