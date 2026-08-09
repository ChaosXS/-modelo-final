import asyncio
from django.http import HttpResponse, JsonResponse
from asgiref.sync import sync_to_async


# 1. View do Exercício Anterior (Síncrona)
def post_view(request):
    return HttpResponse("Hello World")


# 2. Função auxiliar assíncrona (Suporte do Python Assíncrono)
async def calcular_potencia_assincrona(numero):
    await asyncio.sleep(0.2)  # Simula um cálculo ou processo assíncrono
    return {
        'numero': numero,
        'quadrado': numero**2,
        'cubo': numero**3,
    }


# 3. View do Novo Exercício (Assíncrona)
async def async_calc_view(request):
    numeros = [2, 5, 10, 15, 20]

    # Python Assíncrono: executa os cálculos em paralelo
    tarefas = [calcular_potencia_assincrona(n) for n in numeros]
    resultados_calculos = await asyncio.gather(*tarefas)

    soma_quadrados = sum(item['quadrado'] for item in resultados_calculos)

    # Django Assíncrono: usando suporte do sync_to_async do Django
    @sync_to_async
    def operacao_django_lenta():
        return f"Processado com sucesso {len(numeros)} itens"

    mensagem_django = await operacao_django_lenta()

    # Retorno da resposta em JSON
    return JsonResponse({
        'status': 'Sucesso',
        'mensagem_django': mensagem_django,
        'soma_dos_quadrados': soma_quadrados,
        'detalhes_calculo': resultados_calculos,
    })
    