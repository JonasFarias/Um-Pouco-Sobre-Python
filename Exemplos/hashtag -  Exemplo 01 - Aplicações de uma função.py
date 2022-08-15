
#Criamos uma função que verifica se a bebida é alcoolica
#como funciona

def bebidaalcolica(bebida):
    # a variavel bebida tem todo seu texto transformado em maiusculo primeiro
    bebida = bebida.upper()
    #depois verificamos se o texto 'BEB' esta na variavel se estiver ela é alcoolica
    if 'BEB' in bebida:
        return True
    else:
        return False



produtos = ['beb46275','TFA23962','TFA64715','TFA69555',
            'TFA56743','BSA45510','TFA44968','CAR75448',
            'CAR23596','CAR13490','BEB21365','BEB31623',
            'BSA62419','BEB73344','TFA20079','BEB80694',
            'BSA11769','BEB19495','TFA14792','TFA78043',
            'BSA33484','BEB97471','BEB62362','TFA27311',
            'TFA17715','BEB85146','BEB48898','BEB79496',
            'CAR38417','TFA19947','TFA58799','CAR94811',
            'BSA59251','BEB15385','BEB24213','BEB56262',
            'BSA96915','CAR53454','BEB75073']

for produto in produtos:
    if bebidaalcolica(produto):
        print(f'Enviar {produto}, para setor de bebida alcoolica')
