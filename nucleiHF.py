# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

print('*'*10,' HEADER ','*'*10)
print('RUN read-dict.py (with python3)')
print('*'*30)

# ---------------------------------------------------------
# INPUTS
# ---------------------------------------------------------

# Files to read
dict_par='data/dict-par.txt'
dict_res='data/dict-res.txt'
dict_data='data/dict-data.txt'

models = [ 'SKY', 'RNL', 'RDD' ]

nuclei = [ '16O', '34Si', '40Ca', '48Ca', '52Ca', '54Ca', '48Ni', '56Ni', '78Ni', '90Zr', '100Sn', '132Sn', '208Pb' ]

print('-'*10)
print('This code reads the dictionaries:')
print('Data   :',dict_data)
print('Param  :',dict_par)
print('Results:',dict_res)
print('the models are',models)
print('the nuclei are',nuclei)
print('and interact with user to show results.')

# ---------------------------------------------------------
# READ INPUT DICTIONARY FILES
# ---------------------------------------------------------

print('-'*10)
print('READ DICTs FROM FILEs:')

with open(dict_par, 'r') as f:
    magic = eval(f.read())

with open(dict_res, 'r') as f:
    res = eval(f.read())

with open(dict_data, 'r') as f:
    data = eval(f.read())

nbOfNuclei = len(nuclei)
nbOfNuclei2 = len(res['SKY']['content'].keys())
nbOfData = len(res['SKY']['content']['16O'])

print('Number of nuclei     :',nbOfNuclei,nbOfNuclei2)
print('Number of data/nuclei:',nbOfData)


# ---------------------------------------------------------
# ENTER THE INTERACTIVE USER MODE
# ---------------------------------------------------------


print('-'*10)
print('INTERACTIVE USER MODE')
print('.'*5)
while True:
    print('Possible models:',models)
    print('in files:',magic.keys())
    model = input('select your model (case sensitive):')
    if (model in models):
        break
print('.'*5)
while True:
    print('Possible parameter set:',res[model].keys())
    param = input('Select your parameter set (case sensitive):')
    if (param in res[model].keys()):
        break

print('.'*5)
print('parameters for the model',model)
for i in range(0,len(magic[model]['content'])):
    print(magic[model]['content'][i],'=>',magic[model][param][i])

print('.'*5)
while True:
    print('Possible nuclei:',nuclei)
    print('in files:',data.keys())
    nucleus = input('Select your nucleus (case sensitive):')
    if (nucleus in nuclei):
        break
print('.'*5)
print('For nucleus:',nucleus,nbOfData)
print('Exp:',data[nucleus])
for i in range(0,nbOfData):
    if ( i == 3 ):
        print(i,' ',res[model]['content'][nucleus][i],'=>',res[model][param][nucleus][i],'<=',data[nucleus][0],'+-',data[nucleus][1],'DIF:',(float(data[nucleus][0])-float(res[model][param][nucleus][i])))
    if ( i == 4 & len(data[nucleus])>2 ):
        print(i,' ',res[model]['content'][nucleus][i],'=>',res[model][param][nucleus][i],'<=',data[nucleus][2],'+-',data[nucleus][3],'DIF:',(float(data[nucleus][2])-float(res[model][param][nucleus][i])))
    else:
        print(i,' ',res[model]['content'][nucleus][i],'=>',res[model][param][nucleus][i])
        
exit()
