[category]: <> (Español)
[date]: <> (2021/01/05)
[title]: <> (La Guía Incompleta de los Rollups)
[pandoc]: <> ()

_Gracias a [j4c0b0bl4nd0n](https://github.com/j4c0b0bl4nd0n) por la traducción_

Los Rollups están de moda en la comunidad de Ethereum y están [destinados a ser la solución de escalabilidad clave](https://ethereum-magicians.org/t/a-rollup-centric-ethereum-roadmap/4698)  para Ethereum en el futuro previsible. Pero, ¿qué es exactamente esta tecnología, qué podemos esperar de ella y cómo podremos usarla? Este post intentará responder algunas de esas preguntas clave.

## Antecedentes: ¿Qué es el escalado de capa-1 y capa-2?

**Hay dos formas de escalar un ecosistema blockchain. Primero, puede hacer que la propia cadena de bloques tenga una mayor capacidad de transacción**. El principal desafío con esta técnica es que las cadenas de bloques con "bloques más grandes" son inherentemente más difíciles de verificar y es probable que se vuelvan más centralizadas. Para evitar tales riesgos, los desarrolladores pueden aumentar la eficiencia del software del cliente o, de manera más sostenible, utilizar técnicas [como la fragmentación](https://eth.wiki/sharding/Sharding-FAQs)  para permitir que el trabajo de construcción y verificación de la cadena se divida en muchos nodos; el [esfuerzo conocido como "eth2"](https://ethereum.org/en/eth2) actualmente está construyendo esta actualización en Ethereum.

**En segundo lugar, puede cambiar la forma en que usa la cadena de bloques**. En lugar de poner toda la actividad en la cadena de bloques directamente, los usuarios realizan la mayor parte de su actividad fuera de la cadena en un protocolo de "capa-2". Hay un contrato inteligente en la cadena, que solo tiene dos tareas: procesar depósitos y retiros, y verificar las pruebas de que todo lo que sucede fuera de la cadena sigue las reglas. Hay varias formas de hacer estas pruebas, pero todas comparten la propiedad que verificar las pruebas en la cadena es mucho más económico que hacer el cálculo original fuera de la cadena.

## State channels vs plasma vs rollups

Los tres tipos principales de escalado de capa-2 son [state channels](https://statechannels.org/), [Plasma](http://plasma.io/) y Rollups. Estos son tres paradigmas diferentes, con diferentes fortalezas y debilidades, y en este punto estamos bastante seguros de que toda la escala de capa-2 cae aproximadamente en estas tres categorías (aunque existen controversias de nombres en los bordes, por ejemplo, ver ["validium"](https://medium.com/starkware/volition-and-the-emerging-data-availability-spectrum-87e8bfa09bb)).

### Cómo funcionan State channels?

_Ver también: [https://www.jeffcoleman.ca/state-channels](https://www.jeffcoleman.ca/state-channels) y [statechannels.org](https://statechannels.org/)_

Imaginemos que Alice le ofrece una conexión a Internet a Bob, a cambio de que Bob le pague $0,001 por megabyte. En lugar de realizar una transacción para cada pago, Alice y Bob utilizan el siguiente esquema de capa-2.

Primero, Bob pone $ 1 (o algún ETH o equivalente de moneda estable) en un contrato inteligente. Para realizar su primer pago a Alice, Bob firma un "boleto" (un mensaje fuera de la cadena), que simplemente dice "$0.001", y se lo envía a Alice. Para hacer su segundo pago, Bob firmaría otro boleto que dice "$0.002" y se lo enviaría a Alice. Y así sucesivamente para tantos pagos como sea necesario. Cuando Alice y Bob terminen de realizar transacciones, Alice puede publicar el boleto de mayor valor para encadenarlo, envuelto en otra firma suya. El contrato inteligente verifica las firmas de Alice y Bob, le paga a Alice el monto del boleto de Bob y le devuelve el resto a Bob. Si Alice no está dispuesta a cerrar el canal (debido a malicia o falla técnica), Bob puede iniciar un período de retiro (por ejemplo, 7 días); si Alice no proporciona un boleto dentro de ese tiempo, entonces Bob recupera todo su dinero.

Esta técnica es poderosa: se puede ajustar para manejar pagos bidireccionales, relaciones de contratos inteligentes (por ejemplo, Alice y Bob hacen un contrato financiero dentro del canal) y composición (si Alice y Bob tienen un canal abierto y también Bob y Charlie, Alice puede interactuar sin confianza con Charlie). Pero hay límites a lo que pueden hacer los canales. Los canales no se pueden usar para enviar fondos fuera de la cadena a personas que aún no son participantes. Los canales no se pueden utilizar para representar objetos que no tengan un propietario lógico claro (p. ej., Uniswap). Y los canales, especialmente si se utilizan para hacer cosas más complejas que simples pagos recurrentes, requieren una gran cantidad de capital para bloquearse.

### Cómo funciona Plasma?

_Ver también: el paper original de [Plasma](http://plasma.io/plasma-deprecated.pdf), y [Plasma Cash](https://ethresear.ch/t/plasma-cash-plasma-with-much-less-per-user-data-checking/1298)._

Para depositar un activo, un usuario lo envía al contrato inteligente que administra la cadena Plasma. La cadena Plasma asigna a ese activo una nueva identificación única (por ejemplo, 537). Cada cadena de Plasma tiene un _operador_ (podría ser un actor centralizado, multisig o algo más complejo como PoS o DPoS). Cada intervalo (esto podría ser de 15 segundos, una hora o cualquier intervalo), el operador genera un "batch" que consta de todas las transacciones de Plasma que han recibido fuera de la cadena. Generan un árbol de Merkle, en el que en cada índice "X" del árbol hay una transacción que transfiere el ID de activo "X" si existe tal transacción y, de lo contrario, esa hoja es cero. Publican el Merkle root de este árbol a la cadena. También envían la rama Merkle de cada índice `X` al propietario actual de ese activo. Para retirar un activo, un usuario publica la sucursal de Merkle de la transacción más reciente que le envía el activo. El contrato inicia un período de impugnación, durante el cual cualquiera puede intentar usar otras sucursales de Merkle para invalidar la salida al demostrar que (I) el remitente no era propietario del activo en el momento en que lo envió, o (II) envió el activo a otra persona en algún momento posterior. Si nadie prueba que la salida es fraudulenta durante (por ejemplo) 7 días, el usuario puede retirar el activo.

Plasma proporciona propiedades más sólidas que los State channels: puede enviar activos a participantes que nunca formaron parte del sistema y los requisitos de capital son mucho más bajos. Pero tiene un costo: los canales no requieren datos en absoluto para conectarse en cadena durante el "funcionamiento normal", pero Plasma requiere que cada cadena publique un hash a intervalos regulares. Además, las transferencias de Plasma no son instantáneas: hay que esperar a que finalice el intervalo y se publique el bloque.

Además, Plasma y State channels comparten una debilidad clave en común: la teoría del juego detrás de por qué son seguros se basa en la idea de que cada objeto controlado por ambos sistemas tiene algún "propietario" lógico. Si a ese propietario no le importa su activo, puede resultar en un resultado "no válido" que involucre a ese activo. Esto está bien para muchas aplicaciones, pero es un factor decisivo para muchas otras (por ejemplo: Uniswap). Incluso los sistemas en los que se puede cambiar el estado de un objeto sin el consentimiento del propietario (por ejemplo: los sistemas basados en cuentas, en los que puede _aumentar_ el saldo de alguien sin su consentimiento) no funcionan bien con Plasma. Todo esto significa que se requiere una gran cantidad de "razonamiento específico de la aplicación" en cualquier despliegue realista de Plasma o State channels, y no es posible hacer un sistema Plasma o State channels que solo simule el entorno completo de ethereum (o "el EVM") . Para solucionar este problema, llegamos a... Rollups.

### Rollups

_Ver También: [EthHub en optimistic rollups](https://docs.ethhub.io/ethereum-roadmap/layer-2-scaling/optimistic_rollups/) y [ZK rollups](https://docs.ethhub.io/ethereum-roadmap/layer-2-scaling/zk-rollups/)._

Plasma y State channels son esquemas de capa-2 "completos", en el sentido de que intentan mover tanto los datos como la computación fuera de la cadena. Sin embargo, [los problemas fundamentales de la teoría de juegos en torno a la disponibilidad de datos](https://www.youtube.com/watch?v=OJT_fR7wexw) significan que es imposible hacer esto de manera segura para todas las aplicaciones. Plasma y State channels evitan esto al basarse en una noción explícita de propietarios, pero esto les impide ser completamente generales. Los Rollups, por otro lado, son un esquema de capa-2 "híbrido". **Los Rollups mueven el cómputo (y el almacenamiento de estado) fuera de la cadena, pero mantienen algunos datos por transacción adentro de la cadena**. Para mejorar la eficiencia, utilizan una gran cantidad de trucos de compresión sofisticados para _reemplazar los datos con computación_ siempre que sea posible. El resultado es un sistema en el que la escalabilidad sigue estando limitada por el ancho de banda de datos de la cadena de bloques subyacente, pero en una proporción muy favorable: mientras que una transferencia de token ERC20 de capa base de Ethereum cuesta ~45000 gas, una transferencia de token ERC20 en un Rollup ocupa 16 bytes de espacio en cadena y costos por debajo de 300 de gas.

El hecho de que los datos estén en la cadena es clave (nota: poner los datos "en IPFS" _no funciona_, porque IPFS no brinda _consenso_ sobre si un dato determinado está disponible o no; los datos _deben_ ir en una cadena de bloques). Poner datos en la cadena y tener consenso sobre ese hecho permite que cualquier persona procese localmente todas las operaciones en el Rollup si así lo desea, lo que les permite detectar fraudes, iniciar retiros o comenzar personalmente a producir batch de transacciones. La falta de problemas de disponibilidad de datos significa que un operador malintencionado o fuera de línea puede causar incluso menos daño (por ejemplo: no puede causar un retraso de 1 semana), lo que abre un espacio de diseño mucho más grande para quién tiene derecho a publicar batch y hace que los Rollups sean mucho más sencillos. Y lo que es más importante, la falta de problemas de disponibilidad de datos significa que ya no es necesario asignar activos a los propietarios, lo que lleva a la razón clave por la cual la comunidad de Ethereum está mucho más entusiasmada con los Rollups que con las formas anteriores de escalado de capa-2: **Los Rollups son totalmente de multi-propósito, e incluso se puede ejecutar un EVM dentro de un Rollup, lo que permite que las aplicaciones Ethereum existentes migren a Rollups casi sin necesidad de escribir ningún código nuevo**.

## OK, entonces, ¿cómo funciona exactamente un Rollup?

Hay un contrato inteligente dentro de la cadena que mantiene una **estado root**: el Merkle root del estado del Rollup (es decir, los saldos de cuenta, el código del contrato, etc., lo que está "dentro" del Rollup).

<br>
<center>
<img src="https://vitalik.ca/images/rollup-files/diag1.png" />
</center><br>

Cualquiera puede publicar un **batch**, una colección de transacciones en un formato altamente comprimido junto con el root del estado anterior y el root del nuevo estado (el Merkle root _después_ de procesar las transacciones). El contrato verifica que el root de estado anterior en el batch coincida con su root de estado actual; si lo hace, cambia el root del estado a el nuevo root del estado.

<br>
<center>
<img src="https://vitalik.ca/images/rollup-files/diag2.png" />
</center><br>

Para admitir depósitos y retiros, agregamos la capacidad de tener transacciones cuya entrada o salida está "fuera" del estado del Rollup. Si un batch tiene entradas desde el exterior, la transacción que envía el batch también debe transferir estos activos al contrato de Rollup. Si un batch tiene salidas al exterior, luego de procesar el batch, el contrato inteligente inicia esos retiros.

¡Y eso es! Excepto por un detalle importante: **¿cómo saber si los roots posteriores al estado en el batch son correctas?** Si alguien puede enviar un batch con cualquier root posterior al estado sin consecuencias, podría simplemente transferir todas las monedas que contiene el Rollup a sí mismos. Esta pregunta es clave porque hay dos familias de soluciones muy diferentes para el problema, y estas dos familias de soluciones conducen a los dos tipos de Rollups.

### Optimistic Rollups vs ZK Rollups

Los dos tipos de Rollups son:

1. **Optimistic Rollups**, que utilizan **pruebas de fraude**: el contrato del Rollup realiza un seguimiento de todo su historial de state roots y el hash de cada batch. Si alguien descubre que un batch tenía un root posterior al estado incorrecta, puede publicar una prueba en cadena, demostrando que el batch se calculó incorrectamente. El contrato verifica la prueba y revierte ese batch y todos los batches posteriores.
2. **ZK Rollups**, que usan **pruebas de validez**: cada batch incluye una prueba criptográfica llamada ZK-SNARK (por ejemplo: usando el protocolo [PLONK](https://vitalik.ca/general/2019/09/22/plonk.html)), lo que demuestra que el root posterior al estado es el resultado correcto para ejecutar el batch. No importa cuán grande sea el cálculo, la prueba se puede verificar muy rápidamente en la cadena.

Hay compensaciones complejas entre los dos tipos de Rollups:

| Propiedad | Optimistic Rollups | ZK Rollups |
| - | - | - |
| Costo fijo de gas por batch | **~40,000** (una transacción liviana que principalmente solo cambia el valor del root del estado) | ~500,000 (la verificación de un ZK-SNARK es bastante intensiva computacionalmente) |
| Tiempo de retiro | ~1 semana (los retiros deben retrasarse para dar tiempo a que alguien publique una prueba de fraude y cancele el retiro si es fraudulento) | **Muy rápida** (solo espera el siguiente batch) |
| Complejidad de la tecnología | **Baja** | Alta (ZK-SNARK es una tecnología muy nueva y matemáticamente compleja) |
| Generalizabilidad |**Más fácil** (Los Rollups de EVM de propósito general ya están cerca de la red principal) | Más difícil (para ZK-SNARK probar la ejecución de EVM de propósito general es mucho más difícil que probar cálculos simples, aunque hay esfuerzos (por ejemplo: [Cairo](https://medium.com/starkware/hello-cairo-3cb43b13b209)) trabajando para mejorar esto) |
| Costos de gas en cadena por transacción | Altos | **Bajos** (si los datos en una transacción solo se usan para verificar, y no para causar cambios de estado, entonces estos datos pueden omitirse, mientras que en un Optimist Rollup tendrían que publicarse en caso de que deban verificarse en una prueba de fraude)|
| Costos de computación fuera de la cadena | **Bajos** (aunque hay más necesidad de muchos nodos completos para rehacer el cálculo) | Altos (La prueba de ZK-SNARK, especialmente para el cómputo de propósito general, puede ser costosa, potencialmente miles de veces más costosa que ejecutar el cómputo directamente.) |

En general, mi opinión es que, a corto plazo, es probable que los Optimist Rollups ganen para el cómputo de EVM de propósito general y que los ZK Rollups probablemente ganen para pagos simples, intercambios y otros casos de uso específicos de la aplicación, pero en Los Rollups de ZK a mediano y largo plazo ganarán en todos los casos de uso a medida que mejore la tecnología ZK-SNARK.

### Anatomía de prueba de fraude

La seguridad de un Rollup de Optimistic depende de la idea de que si alguien publica un batch inválido en el Rollup, _cualquier otra persona_ que se mantuvo al día con la cadena y detectó el fraude puede publicar una prueba de fraude, demostrando al contrato que ese batch no es válido y debe revertirse.

<br>
<center>
<img src="https://vitalik.ca/images/rollup-files/tree.png" />
</center><br>

Una prueba de fraude que afirme que un batch no es válido contendría los datos en verde: el batch en sí (que podría verificarse con un hash almacenado en cadena) y las partes del árbol Merkle necesarias para probar solo las cuentas específicas que se leyeron y/o modificado por el batch. Los nodos del árbol en amarillo se pueden reconstruir a partir de los nodos en verde, por lo que no es necesario proporcionarlos. Estos datos son suficientes para ejecutar el batch y calcular el root posterior al estado (tenga en cuenta que esto es exactamente igual a cómo los [clientes sin estado](https://ethresear.ch/t/the-stateless-client-concept/172) verifican bloques individuales). Si el root posterior al estado calculado y el root posterior al estado proporcionado en el batch no son iguales, entonces el batch es fraudulento.

Se garantiza que si un batch se construyó incorrectamente, _y todos los batches anteriores se construyeron correctamente_, entonces es posible crear una prueba de fraude que muestre que el batch se construyó incorrectamente. Tenga en cuenta la afirmación sobre los batches anteriores: si hubo más de un batch no válido publicado en el Rollup, entonces es mejor intentar probar que el primero no es válido. Por supuesto, también se garantiza que si un batch se construyó correctamente, nunca será posible crear una prueba de fraude que demuestre que el batch no es válido.

### ¿Cómo funciona la compresión?

Una transacción simple de Ethereum (para enviar ETH) requiere ~110 bytes. Sin embargo, una transferencia ETH en un Rollup solo requiere ~12 bytes:

| Parametro | Ethereum | Rollup |
| - | - | - |
| Nonce | ~3 | 0 |
| Gasprice | ~8 | 0-0.5 |
| Gas | 3 | 0-0.5 |
| To | 21 | 4 |
| Value | ~9 | ~3 |
| Signature | ~68 (2 + 33 + 33) | ~0.5 |
| From | 0 (recovered from sig) | 4 |
| Total | ~112 | ~12 |

Parte de esto es simplemente una codificación superior: el RLP de Ethereum desperdicia 1 byte por valor en la longitud de cada valor. Pero también hay algunos trucos de compresión muy inteligentes que están sucediendo:

* **Nonce**: el propósito de este parámetro es evitar repeticiones. Si el nonce actual de una cuenta es 5, la próxima transacción de esa cuenta debe tener un nonce 5, pero una vez que se procese la transacción, el nonce en la cuenta se incrementará a 6 para que la transacción no se pueda procesar nuevamente. En el Rollup, podemos omitir el nonce por completo, porque solo recuperamos el nonce del estado anterior; si alguien intenta reproducir una transacción con un nonce anterior, la firma no se verificará, ya que la firma se verificará con los datos que contienen el nuevo nonce superior.
*  **Gasprice**: podemos permitir que los usuarios paguen con un rango fijo de precios de gas, por ejemplo: una elección de 16 potencias consecutivas de dos. Alternativamente, podríamos simplemente tener un nivel de tarifa fijo en cada batch, o incluso mover el pago de gas fuera del protocolo de acumulación por completo y hacer que los transactores paguen a los creadores de batch para su inclusión a través de un canal.
*  **Gas**: de manera similar, podríamos restringir el gas total a una elección de potencias consecutivas de dos. Alternativamente, podríamos tener un límite de gas solo a nivel de batch.
*  **To**: podemos reemplazar la dirección de 20 bytes con un _index_ (por ejemplo, si una dirección es la dirección 4527 agregada al árbol, solo usamos el index 4527 para referirnos a ella. Agregaríamos un subárbol al estado para almacenar el mapeo de índices a direcciones).
*  **Value**: podemos almacenar valor en notación científica. En la mayoría de los casos, las transferencias solo necesitan de 1 a 3 dígitos significativos.
*  **Signature**: podemos usar [BLS firmas agregadas](https://ethresear.ch/t/pragmatic-signature-aggregation-with-bls/2105), que nos permite agregar muchas firmas en una sola firma de ~32-96 bytes (según el protocolo). Luego, esta firma se puede verificar con el conjunto completo de mensajes y remitentes en un batch, todo a la vez. El ~0.5 en la tabla representa el hecho de que existe un límite en la cantidad de firmas que se pueden combinar en un agregado que se puede verificar en un solo bloque, por lo que los batches grandes necesitarían una firma por cada ~100 transacciones.

Un truco de compresión importante que es específico de los Rollups de ZK es que si una parte de una transacción solo se usa para la verificación y no es relevante para calcular la actualización del estado, entonces esa parte se puede dejar fuera de la cadena. Esto no se puede hacer en un Rollup de Optimistic porque esos datos aún deberían incluirse en la cadena en caso de que deban verificarse más tarde en una prueba de fraude, mientras que en un Rollup de ZK, el SNARK que prueba la corrección del batch ya prueba que cualquier dato necesario para la verificación. Un ejemplo importante de esto son los Rollup que preservan la privacidad: en un Rollup de Optimistic, el ZK-SNARK de ~500 bytes utilizado para la privacidad en cada transacción debe ir en cadena, mientras que en un Rollup de ZK, el ZK-SNARK que cubre todo el batch ya no deja duda que los ZK-SNARK "internos" sean válidos.

Estos trucos de compresión son clave para la escalabilidad de los Rollups; sin ellos, los Rollups serían quizás solo una mejora de ~10x en la escalabilidad de la cadena base (aunque hay algunas aplicaciones específicas de computación pesada donde incluso los resúmenes simples son poderosos), mientras que con los trucos de compresión, el factor de escala puede superar 100x por casi todas las aplicaciones.

### ¿Quién puede enviar un batch?

Hay varias escuelas de pensamiento sobre quién puede enviar un batch en un Rollup Optimistic o ZK. En general, todos están de acuerdo en que para poder enviar un batch, un usuario debe hacer un depósito grande; si ese usuario alguna vez envía un batch fraudulento (por ejemplo, con un root de estado no válido), ese depósito se quemará en parte y se entregará en parte como recompensa al probador de fraude. Pero más allá de eso, hay muchas posibilidades:

* **Anarquía total**: cualquiera puede enviar un batch en cualquier momento. Este es el enfoque más simple, pero tiene algunos inconvenientes importantes. En particular, existe el riesgo de que varios participantes generen e intenten enviar batches en paralelo, y solo uno de esos batches se puede incluir con éxito. Esto conduce a una gran cantidad de esfuerzo desperdiciado en la generación de pruebas y/o gas desperdiciado en la publicación de batch en cadena.
* **Secuenciador centralizado**: hay un solo actor, el **secuenciador**, que puede enviar batches (con la excepción de los retiros: la técnica habitual es que un usuario primero puede enviar una solicitud de retiro y luego, si el secuenciador no procesa ese retiro en el siguiente batch, entonces el usuario puede enviar un batch de una sola operación por sí mismo). Este es el más "eficiente", pero depende de un actor central para la vitalidad.
* **Subasta de secuenciador**: se lleva a cabo una subasta (por ejemplo: todos los días) para determinar quién tiene derecho a ser el secuenciador para el día siguiente. Esta técnica tiene la ventaja de que recauda fondos que podrían ser distribuidos por ejemplo: un DAO controlado por el Rollup (ver: [Subastas MEV](https://ethresear.ch/t/mev-auction-auctioning-transaction-ordering-rights-as-a-solution-to-miner-extractable-value/6788))
* **Selección aleatoria desde el conjunto PoS**: cualquiera puede depositar ETH (o quizás el token de protocolo propio del Rollup) en el contrato del Rollup, y el secuenciador de cada batch se selecciona aleatoriamente de uno de los depositantes, con la probabilidad de ser seleccionado proporcional a la cantidad depositada. El principal inconveniente de esta técnica es que conduce al bloqueo de grandes cantidades de capital innecesarias.
* **Votación DPoS**: solo hay un secuenciador seleccionado con una subasta, pero si su rendimiento es bajo, los poseedores de tokens pueden votar para expulsarlos y realizar una nueva subasta para reemplazarlos.

#### Procesamiento por batches dividido y aprovisionamiento de state root

Algunos de los Rollups que se están desarrollando actualmente usan un paradigma de "batch dividido", donde la acción de enviar un batch de transacciones de capa-2 y la acción de enviar una state root se realizan por separado. Esto tiene algunas ventajas clave:

1. Puede permitir que muchos secuenciadores publiquen batches en paralelo para mejorar la resistencia a la censura, sin preocuparse de que algunos batches no sean válidos porque se incluyó otro primero.
2. Si un state root es fraudulento, no necesita revertir todo el batch; puede revertir solo el root del estado y esperar a que alguien proporcione un nuevo root del estado para el mismo batch. Esto brinda a los remitentes de transacciones una mejor garantía de que sus transacciones no se revertirán.

Entonces, en general, hay un zoológico bastante complejo de técnicas que intentan equilibrar complicadas compensaciones que involucran eficiencia, simplicidad, resistencia a la censura y otros objetivos. Todavía es demasiado pronto para decir qué combinación de estas ideas funciona mejor; el tiempo dirá.

## ¿Cuánta escalabilidad te dan los Rollups?

En la cadena Ethereum existente, el límite de gas es de 12,5 millones, y cada byte de datos en una transacción cuesta 16 de gas. Esto significa que si un bloque no contiene nada más que un solo batch (diremos que se usa un Rollup de ZK, gastando 500k de gas en la verificación de prueba), ese batch puede tener (12 millones/16) = 750,000 bytes de datos. Como se muestra arriba, un Rollup para transferencias ETH requiere solo 12 bytes por operación de usuario, lo que significa que el batch puede contener hasta 62 500 transacciones. Con un tiempo de bloque promedio de 13 segundos, esto se traduce en ~4807 TPS (en comparación con 12,5 millones/21000/13 ~= 45 TPS para transferencias ETH directamente en Ethereum).

Aquí hay una tabla para algunos otros casos de uso de ejemplo:
| Applicación | Bytes en Rollup | costo Gas en capa-1 | Max aumento escalabilidad |
| - | - | - | - |
| ETH transferencia | **12** | 21,000 | 105x |
| ERC20 transferencia | **16** (4 bytes más para especificar qué token) | ~50,000 | 187x |
| Uniswap trade | **~14** (remitente de 4 bytes + Destinatario de 4 bytes + valor de 3 bytes + Precio máximo de 1 byte + Miscelánea de 1 byte) | ~100,000 | 428x |
| Retiro preservando la privacidad (Rollup de Optimistic) | **296** (4 bytes index root + 32 bytes anulador + 4 bytes destinatario + 256 bytes prueba ZK-SNARK | [~380,000](https://etherscan.io/tx/0x6e311f84655af72614966705584569b52d6e314f2d61b965db91db41fd01b1e1) | 77x 

<small><i>La ganancia máxima de escalabilidad se calcula como (L1 costo gas) / (bytes enRrollup * 16) * 12 million / 12.5 millones.</i></small>

Ahora, vale la pena tener en cuenta que estas cifras son demasiado optimistas por varias razones. Lo que es más importante, un bloque casi nunca contendría solo un batch, al menos porque hay y habrá múltiples Rollups. Segundo, los depósitos y retiros seguirán existiendo. En tercer lugar, _en el corto plazo_ el uso será bajo, por lo que dominarán los costos fijos. Pero incluso teniendo en cuenta estos factores, se espera que las ganancias de escalabilidad de más de 100x sean la norma.

Ahora, ¿qué sucede si queremos superar ~1000-4000 TPS (según el caso de uso específico)? Aquí es donde entra en juego la [fragmentación de datos eth2](https://hackmd.io/@HWeNw8hNRimMm2m2GH56Cw/sharding_proposal). La propuesta de fragmentación abre un espacio de 16 MB cada 12 segundos que se puede llenar con cualquier dato, y el sistema garantiza el consenso sobre la disponibilidad de esos datos. Este espacio de datos puede ser utilizado por los Rollups. Estos ~1398k bytes por segundo son una mejora de 23 veces sobre los ~60 kB/seg de la cadena Ethereum existente y, a largo plazo, se espera que la capacidad de datos crezca aún más. Por lo tanto, los Rollups que utilizan datos fragmentados de eth2 pueden procesar colectivamente hasta ~100 000 TPS, e incluso más en el futuro.

## ¿Cuáles son algunos de los desafíos que aún no se han resuelto por completo en los Rollups?

Si bien el concepto básico de un Rollup ahora se comprende bien, estamos bastante seguros de que son fundamentalmente factibles y seguros, y ya se han implementado varios Rollups en la red principal, todavía hay muchas áreas del diseño del Rollup que no se han explorado bien, y bastantes desafíos para llevar por completo grandes partes del ecosistema Ethereum a Rollups para aprovechar su escalabilidad. Algunos desafíos clave incluyen:

* **Incorporación de usuarios y ecosistemas** - no muchas aplicaciones usan Rollups, los Rollups no son familiares para los usuarios y pocas billeteras han comenzado a integrar Rollups. Los comerciantes y las organizaciones benéficas aún no los aceptan para pagos.
* **Transacciones cruzadas** - mover activos y datos de manera eficiente (por ejemplo: salidas de oracúlo) de un Rollup a otro sin incurrir en el gasto de pasar por la capa base.
* **Incentivos de auditoría** - ¿Cómo maximizar la posibilidad de que al menos un nodo honesto realmente verifique completamente un Rollup de Optimistic para que puedan publicar una prueba de fraude si algo sale mal? Para Rollups a pequeña escala (hasta unos pocos cientos de TPS), este no es un problema importante y uno simplemente puede confiar en el altruismo, pero para Rollups a mayor escala se necesita un razonamiento más explícito sobre esto.
* **Explorando el espacio de diseño entre Plasma y Rollups** - ¿Existen técnicas que pongan _algunos_ datos relevantes para la actualización del estado en la cadena, pero no _todos_, y hay algo útil que pueda resultar de eso?
* **Maximizar la seguridad de las confirmaciones previas** - muchos Rollups brindan una noción de "confirmación previa" para una UX más rápida, donde el secuenciador promete de inmediato que una transacción se incluirá en el siguiente Batch, y el depósito del secuenciador se destruye si no cumplen su palabra. Pero la seguridad económica de este esquema es limitada, debido a la posibilidad de hacer muchas promesas a muchos actores al mismo tiempo. ¿Se puede mejorar este mecanismo?
* **Mejora de la velocidad de respuesta a los secuenciadores ausentes** - Si el secuenciador de un Rollup se desconecta repentinamente, sería valioso recuperarse de esa situación de la manera más rápida y económica, ya sea saliendo en masa de manera rápida y económica a un Rollup diferente o reemplazando el secuenciador.
* **Eficiente ZK-VM** - generando una prueba ZK-SNARK de que el código EVM de propósito general (o alguna VM diferente en la que se puedan compilar los contratos inteligentes existentes) se ha ejecutado correctamente y tiene un resultado determinado.

## Conclusiones

Los rollups son un nuevo y poderoso paradigma de escalamiento de capa-2, y se espera que sean la piedra angular del escalamiento de Ethereum en el futuro a corto y mediano plazo (y posiblemente también a largo plazo). Han visto una gran cantidad de entusiasmo por parte de la comunidad Ethereum porque, a diferencia de los intentos anteriores de escalado de capa-2, pueden admitir código EVM de uso general, lo que permite que las aplicaciones existentes se migren fácilmente. Lo hacen al hacer un compromiso clave: no intentar salir completamente de la cadena, sino dejar una pequeña cantidad de datos por transacción en la cadena.

Hay muchos tipos de resúmenes y muchas opciones en el espacio de diseño: uno puede tener un Rollup de Optimistic usando pruebas de fraude o un Rollup de ZK usando pruebas de validez (también conocido como ZK-SNARK). El secuenciador (el usuario que puede publicar batch de transacciones para encadenar) puede ser un actor centralizado, un free-for-all o muchas otras opciones intermedias. Los Rollups aún son una tecnología en etapa inicial y el desarrollo continúa rápidamente, pero funcionan y algunos (en particular, [Loopring](https://loopring.io/), [ZKSync](https://wallet.zksync.io/) y [DeversiFi](https://www.deversifi.com/)) ya se han estado ejecutando durante meses. Esperamos un trabajo mucho más emocionante que surja del espacio acumulativo en los años venideros.
