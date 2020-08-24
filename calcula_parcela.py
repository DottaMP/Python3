from datetime import datetime, timedelta
import calendar
valor_divida = float(input("Qual o valor da sua divida? "))
valor_mensal = float(input("Quanto você pode pagar por mes? "))
dia_vencimento = int(input("Qual o melhor dia para o vencimento? "))

par = round(valor_divida / valor_mensal)

aplicado = 0.0
parcelas = []

for i in range(1, par + 1):
    valor = round(valor_divida / par, 2)
    aplicado += valor
    parcelas.append(valor)

diff = round(valor_divida - aplicado, 2)

if abs(diff) > 0.0:
    parcelas[-1] = round(parcelas[-1] + diff, 2)

def add_month(date):
    return date + timedelta(days=calendar.monthrange(date.year, date.month)[1])

now = datetime.now()
data_ref = datetime(now.year, now.month, 1) + timedelta(days=dia_vencimento-1)

for i, x in enumerate(parcelas, 1):
    data_ref = add_month(data_ref)
    print(f"Parcela {i}: {x}, Vencimento: {data_ref.isoformat()}")
