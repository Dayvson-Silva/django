

from django.shortcuts import render

def home(request):
    # para vc usar interpolação no html usar context
    context = {
        'name': 'Dayvson'
    }
    # add context 
    return render(request, 'index.html',context)

def product(request):
    context = {
        'product':{
            'name': 'Inglês em Foco',
            'description':'Muito Bom',
            'price': 50,
            'stock': 4
        }
     }
    return render(request, 'product.html',context)

# usando condição if 
def autenticar(request):
    context = {
        'autenticar':{
            'name': 'Dayvson',
            'idade': 30
        }
    }
    return render(request, 'authenticated.html',context)

def pessoas(request):
    context = {
        'loja': [

            {
            'name': 'camisa do biu',
            'description':'Muito Bom',
            'price': 50.00,
            'stock': 4
            },
            {
            'name': 'jaqueta do biu',
            'description':'algodão puro',
            'price': 266.00,
            'stock': 25
            },
            {
            'name': 'kit sobrevivência do biu',
            'description':'salvar sua vida ',
            'price': 710.00,
            'stock': 0
            }
            
        ]
    }
    return render(request, 'for.html',context)