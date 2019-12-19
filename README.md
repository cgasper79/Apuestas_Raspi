# Generador de Apuestas Euromillones Y Primitiva en Python

Visitad el Canal de Telegram dónde se publican las combinaciones para ambos sorteos:
- Euromillones: Se generan 5 combinaciones de números los lunes y jueves para el sorteo del martes y viernes.
- Primitiva: Se generan 5 combinaciones de números los miércoles y viernes par ael sorteo del jueves y sábado.

Estos dos programas en Python generan apuestas para la Euromillones y la Primitiva en base a los números (no combinaciones) que más se repiten a lo largo de los sorteos.

Los históricos los podéis encontrar en:

https://www.lotoideas.com/euromillones-resultados-historicos-de-todos-los-sorteos/ https://www.lotoideas.com/primitiva-resultados-historicos-de-todos-los-sorteos/

La probabilidad de cada número se calcula en los archivos excel Historico_Euro_Prob.xlsx y Historico_Primi_Prob.xlsx, con esta probabilidad conseguimos que se almacenan repetidos los numeros en cada matriz. De este modo, por ejemplo, el 1 estará 50 veces en la lista y el 8, 40 veces repetido.

Para escoger los números de la matriz utilizamos la función "random.choice" tantas veces como números queremos según el tipo de sorteo. Se utiliza una nueva matriz para almacenar solo los números que no se repitan, de ese modo evitamos repetidos.

Las combinaciones generadas quedan ordenadas y se envia un POST a WebHook para publicarlas en IFTTT y de allí conseguir que se envíen a Telegram, notificación Push, correo, etc...

Ambos códigos en Python vienen preparados para funcionar, tan solo hay que poner los datos de vuestro Webhook (evento y KEY), el resultado se mostrará siempre por pantalla y se publicará en Webhook.

Tienes más información de IFTTT y Webhooks en: https://ifttt.com/maker_webhooks
