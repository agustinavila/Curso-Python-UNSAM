saldo = 500000.0
tasa = 0.05
total_pagado = 0.0
pago_mensual = 2684.11
cant_meses = 0
mes_inicio = 12 * 5
mes_final = mes_inicio + ( 12 * 4 )

while saldo > 0:
    if saldo <= pago_mensual:
        pago_mensual = saldo
        saldo = saldo - pago_mensual
        total_pagado = total_pagado + pago_mensual
        # break
    else:    
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
        if cant_meses < mes_final and cant_meses >= mes_inicio:
            saldo -= 1000
            total_pagado = total_pagado + 1000
    cant_meses += 1
    print(cant_meses,round(total_pagado,2),round(saldo,2))

print('Total pagado', round(total_pagado, 2))
print('Cantidad de meses: ', cant_meses)