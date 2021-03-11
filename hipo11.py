#hipo11
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
numero_cuota = 1
pago_mensual2 = 3684.11
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    if pago_extra_mes_comienzo <= numero_cuota <= pago_extra_mes_fin:  
        saldo = saldo * (1+tasa/12) - (pago_mensual+pago_extra);
        total_pagado = total_pagado + (pago_mensual+pago_extra);
        numero_cuota+=1;
        print(numero_cuota, round(total_pagado, 2), round(saldo, 2));
    elif saldo < pago_mensual:
        pago_ultimo = saldo * (1+tasa/12);
        saldo = saldo * (1+tasa/12) - pago_ultimo;
        total_pagado = total_pagado + pago_ultimo;
        numero_cuota+=1
        print(numero_cuota, round(total_pagado, 2), round(saldo, 2));
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual;
        total_pagado = total_pagado + pago_mensual;
        numero_cuota+=1;
        print(numero_cuota, round(total_pagado, 2), round(saldo, 2));
print('Total pagado', round(total_pagado, 2),round(numero_cuota,2))




