from django.shortcuts import render

# def home(request):
#     return render(request, 'home.html')
    
# def produtos(request):
#     return render(request,'produtos.html'),

def produtos(request):
    context = {
        'produtos': [

            {
            'name': 'camisa do biu',
            'description':'Muito Bom',
            'price': 50.00,
            'category': 'acessorios'
            },
            {
            'name': 'bone do biu',
            'description':'Muito Bom',
            'price': 20.00,
            'category': 'acessorios'
            }
            
         
            
        ]
    }
    return render(request, 'produtos.html',context)

def categorias(request):
    context= {
        'categorias': [

            'eletronicos',
            'acessorios'

        ]
    }

    return render(request, 'categorias.html', context)