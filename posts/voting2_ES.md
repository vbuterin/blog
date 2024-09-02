[category]: <> (Translations)
[date]: <> (2021/05/25)
[title]: <> (La votación mediante blockchain está sobrevalorada entre personas desinformadas pero subestimada entre personas informadas)
[pandoc]: <> (--mathjax)

_Agradecimientos especiales a Karl Floersch, Albert Ni, Mr Silly y otros por sus comentarios y discusiones. Agradecimientos especiales a crisgarner por traducir._

La votación es un procedimiento que tiene una necesidad muy importante de integridad en el proceso. El resultado de la votación debe ser correcto y esto debe garantizarse mediante un proceso transparente para que todos puedan estar convencidos de que el resultado es correcto. No debería ser posible [interferir exitosamente con el intento de voto](https://en.wikipedia.org/wiki/Voter_suppression) de nadie o impedir que su voto sea contado.

Las blockchains son una tecnología que se trata de proporcionar garantías sobre la integridad del proceso. Si un proceso se ejecuta en una blockchain, se garantiza que el proceso se ejecutará de acuerdo con algún código preacordado y proporcionará la salida correcta. Nadie puede evitar la ejecución, nadie puede manipular la ejecución y nadie puede censurar ni bloquear el procesamiento de las entradas de los usuarios.

Entonces, a primera vista, parece que las blockchains proporcionan exactamente lo que necesita una votación. Y no soy el único que ha tenido ese pensamiento; [muchos](https://www.alaskapublic.org/2021/04/15/alaska-would-be-first-state-to-use-blockchain-based-voting-system-under-proposed-bill/) usuarios [potenciales](https://inc42.com/buzz/india-explores-blockchain-based-e-voting-by-2024-general-elections/) importantes [están interesados](https://fortune.com/2018/07/03/blockchain-voting-trial-zug/). Pero resulta que algunas personas tienen una opinión muy diferente....

<center><br>
<a href="https://www.computerworld.com/article/3430697/why-blockchain-could-be-a-threat-to-democracy.html"><img src="../../../../images/voting2-files/votingthreat.jpg" style="width:550px" /></a>
</center><br><br>

A pesar de la aparente combinación perfecta entre las necesidades de la votación y los beneficios tecnológicos que proporcionan las blockchains, regularmente vemos artículos aterradores [argumentando en contra de la combinación](https://www.computerworld.com/article/3430697/why-blockchain-could-be-a-threat-to-democracy) de ambas. Y no es solo un artículo: [aquí hay un artículo en contra de la votación mediante blockchain de Scientific American](https://www.scientificamerican.com/article/are-blockchains-the-answer-for-secure-elections-probably-not/), aquí hay [otro de CNet](https://www.cnet.com/news/blockchain-isnt-answer-to-voting-system-woes/), y aquí hay [otro de ArsTechnica](https://arstechnica.com/tech-policy/2018/11/blockchain-based-elections-would-be-a-disaster-for-democracy/). Y no son solo periodistas de tecnología al azar: [Bruce Schneier](https://www.schneier.com/blog/archives/2020/11/on-blockchain-voting.html) está en contra de la votación mediante blockchain, y los investigadores del MIT [escribieron un artículo completo](https://people.csail.mit.edu/rivest/pubs/PSNR20.pdf) argumentando que es una mala idea. ¿Entonces, qué está pasando?

## Esquema

Hay **dos líneas críticas clave** que son las más comúnmente expresadas por los críticos de los protocolos de votación mediante blockchain:

1. **Las blockchains son la herramienta de software incorrecta** para llevar a cabo una elección. Las propiedades de confianza que proporcionan no se ajustan bien a las propiedades que necesita una votación, y otros tipos de herramientas de software con flujos de información y propiedades de confianza diferentes funcionarían mejor.
2. **El software en general no puede confiarse** para llevar a cabo elecciones, sin importar qué software sea. El riesgo de errores de software y hardware indetectables es demasiado alto, sin importar cómo esté organizada la plataforma.

**Este artículo discutirá ambas afirmaciones ("refutar" es una palabra demasiado fuerte, pero definitivamente estoy en desacuerdo más de lo que estoy de acuerdo con ambas afirmaciones)**. Primero, discutiré los problemas de seguridad con los intentos existentes de usar blockchains para votar y cómo **la solución correcta no es abandonar las blockchains, sino combinarlas con otras tecnologías criptográficas**. En segundo lugar, abordaré la preocupación sobre si el software (y hardware) puede confiarse o no. La respuesta: **la seguridad informática está mejorando bastante**, y podemos trabajar arduamente para continuar esa tendencia.

A largo plazo, **insistir permanentemente en el papel sería una _enorme_ desventaja para nuestra capacidad de mejorar la votación**. Un voto por N años es una forma de democracia de 250 años de antigüedad, y podríamos tener una democracia mucho mejor si la votación fuera mucho más conveniente y sencilla, para que pudiéramos hacerlo con mucha más frecuencia.

**Cabe decir que toda esta publicación se basa en que exista una buena tecnología de escalado de blockchain (por ejemplo, [sharding](../../../2021/04/07/sharding.html)).** Por supuesto, si las blockchains no pueden escalar, nada de esto puede suceder. Pero hasta ahora, el desarrollo de esta tecnología está avanzando rápidamente y no hay razón para creer que no pueda suceder.

## Malos protocolos de votación mediante blockchain

Los protocolos de votación mediante blockchain son hackeados todo el tiempo. Hace dos años, una empresa tecnológica de votación mediante blockchain llamada Voatz estaba en boca de todos, y mucha gente estaba muy emocionada al respecto. Pero el año pasado, algunos investigadores del MIT descubrieron una [cadena de vulnerabilidades críticas de seguridad](https://internetpolicy.mit.edu/wp-content/uploads/2020/02/SecurityAnalysisOfVoatz_Public.pdf) en su plataforma. Mientras tanto, en Moscú, un sistema de votación mediante blockchain que iba a ser utilizado en una próxima elección [fue hackeado](https://medium.com/swlh/why-was-moscows-blockchain-voting-system-cracked-a-month-before-an-election-6da5e6d9abbb), afortunadamente un mes antes de que tuviera lugar la elección.

Los hackeos fueron bastante serios. Aquí hay una tabla de las capacidades de ataque que [los investigadores que analizaron Voatz](https://internetpolicy.mit.edu/wp-content/uploads/2020/02/SecurityAnalysisOfVoatz_Public.pdf) lograron descubrir:

<center><br>
<img src="../../../../images/voting2-files/voatzpaper.png" style="width:650px" class="padded" />
</center><br><br>

Esto por sí mismo no es un argumento en contra de _nunca_ usar la votación mediante blockchain. Pero sí es un argumento de que el software de votación mediante blockchain debería diseñarse con más cuidado y escalarse de manera lenta e incremental con el tiempo.

## Privacidad y resistencia a la coerción

Pero incluso los protocolos de votación mediante blockchain que no están técnicamente rotos a menudo son deficientes. Para entender por qué, necesitamos profundizar más en _qué propiedades de seguridad específicas_ proporcionan las blockchains y qué propiedades de seguridad específicas necesita la votación; cuando lo hagamos, veremos que hay una discrepancia.

Las blockchains proporcionan dos propiedades clave: **ejecución correcta** y **resistencia a la censura**. La ejecución correcta simplemente significa que la blockchain acepta entradas ("transacciones") de usuarios, las procesa correctamente según algunas reglas predefinidas y devuelve la salida correcta (o ajusta el "estado" de la blockchain de la manera correcta). La resistencia a la censura también es fácil de entender: cualquier usuario que _quiera_ enviar una transacción y esté dispuesto a pagar una tarifa lo suficientemente alta, _puede_ enviar la transacción y esperar verla incluida rápidamente en la cadena.

Ambas propiedades son muy importantes para la votación: deseas que la salida de la votación sea realmente el resultado de contar el número de votos para cada candidato y seleccionar al candidato con la mayoría de los votos, y definitivamente deseas que cualquier persona elegible para votar pueda hacerlo, incluso si algún actor poderoso intenta bloquearlos. **Pero la votación también requiere algunas propiedades cruciales que las blockchains _no_ proporcionan**:

* **Privacidad**: no debería ser posible decir por quién votó alguien en específico, o incluso si votó en absoluto.
* **Resistencia a la coerción**: no debería ser posible _demostrar_ a otra persona cómo votaste, _incluso si quieres_

La necesidad del primer requisito es obvia: deseas que las personas voten basándose en sus sentimientos personales y no en cómo se sentirán las personas a su alrededor, su empleador, la policía o matones aleatorios en la calle acerca de su elección. El segundo requisito es necesario para evitar la venta de votos: si puedes demostrar cómo votaste, vender tu voto se vuelve muy fácil. La demostración de votos también habilitaría formas de coerción donde el que ejerce coerción exige ver algún tipo de prueba de voto por su candidato preferido. La mayoría de las personas, incluso aquellas conscientes del primer requisito, no piensan en el segundo requisito. Pero el segundo requisito también es necesario y es técnicamente no trivial proporcionarlo. **Cabe decir que el promedio del "sistema de votación mediante blockchain" que ves en la práctica ni siquiera intenta proporcionar la segunda propiedad y suele fallar en proporcionar la primera**.

## Votación electrónica segura sin blockchains

El concepto de ejecución criptográficamente asegurada de mecanismos sociales no fue inventado por los entusiastas de blockchain y, de hecho, existió mucho antes que nosotros. Fuera del espacio de blockchain, existe una tradición de 20 años de criptógrafos trabajando en el problema de la votación electrónica segura, y la buena noticia es que _ha habido_ soluciones. Un documento importante que es citado por gran parte de la literatura de las últimas dos décadas es el artículo de Juels, Catalano y Jakobsson de 2002 titulado "[Coercion-Resistant Electronic Elections](https://eprint.iacr.org/2002/165.pdf)":

<center><br>
<img src="../../../../images/voting2-files/elections.png" style="width:650px" class="padded" />
<br><br><br>
</center>

Desde entonces, ha habido muchas iteraciones sobre el concepto; [Civitas](https://orbilu.uni.lu/bitstream/10993/29212/1/Civitas-VFinal.pdf) es un ejemplo destacado, aunque también hay [otros](https://www.usenix.org/system/files/conference/jets15/jets_0302-achenbach.pdf) [muchos](https://www.researchgate.net/publication/221947496_Coercion-Resistant_Cryptographic_Voting_Implementing_Free_and_Secret_Electronic_Elections) [otros](https://link.springer.com/chapter/10.1007/978-3-642-32747-6_5). Estos protocolos utilizan un conjunto similar de técnicas básicas. Hay un conjunto acordado de "talliers" y hay una suposición de confianza de que la mayoría de los talliers son honestos. Los talliers tienen "particiones" de una clave privada compartida entre ellos, y la clave pública correspondiente se publica. Los votantes publican votos encriptados a la clave pública de los talliers, y los talliers utilizan un [protocolo de computación segura entre partes (MPC)](https://www.cs.virginia.edu/~evans/pragmaticmpc/pragmaticmpc.pdf) para descifrar y verificar los votos y calcular el recuento. La computación del recuento se realiza "dentro del MPC": los talliers nunca aprenden su clave privada, y calculan el resultado final sin aprender nada sobre ningún voto individual más allá de lo que se puede aprender al mirar el resultado final mismo.

El cifrado de votos proporciona privacidad, y se agrega alguna infraestructura adicional como [mix-nets](https://en.wikipedia.org/wiki/Mix_network) para hacer la privacidad más fuerte. Para proporcionar resistencia a la coerción, se utiliza una de dos técnicas. Una opción es que durante la fase de registro (la fase en la que los talliers aprenden la clave pública de cada votante registrado), el votante genera o recibe una clave secreta. La clave pública correspondiente se comparte en secreto entre los talliers, y el MPC de los talliers solo cuenta un voto si está firmado con la clave secreta. Un votante no tiene forma de demostrar a un tercero cuál es su clave secreta, por lo que si son sobornados o coercidos, simplemente pueden mostrar y emitir un voto firmado con la clave secreta incorrecta. Alternativamente, un votante podría tener la capacidad de enviar un mensaje para _cambiar_ su clave secreta. Un votante no tiene forma de demostrar a un tercero que _no_ enviaron tal mensaje, lo que lleva al mismo resultado.

La segunda opción es una técnica en la que los votantes pueden realizar múltiples votos donde el segundo anula al primero. Si un votante es sobornado o coercido, puede emitir un voto por el candidato preferido del sobornador/coercer, pero luego enviar otro voto para anular el primero.

<center><br>
<img src="../../../../images/voting2-files/tallyingscheme.png" style="width:650px" class="padded" />
<br><br>
<small><i>Conceder a los votantes la capacidad de emitir un voto posterior que puede anular un voto anterior es el mecanismo clave de resistencia a la coerción de <a href="https://www.usenix.org/system/files/conference/jets15/jets_0302-achenbach.pdf">este protocolo de 2015.</a></i></small><br><br>
</center>

Ahora, llegamos a un matiz clave e importante en todos estos protocolos. Todos ellos dependen de un primitivo externo para completar sus garantías de seguridad: el **tablero de anuncios** (esto es el "BB" en la figura de arriba). El tablero de anuncios es un lugar donde cualquier votante puede enviar un mensaje, con la garantía de que (i) cualquiera puede leer el tablero de anuncios y (ii) cualquiera puede enviar un mensaje al tablero de anuncios que es aceptado. La mayoría de los documentos de votación resistente a la coerción que puedes encontrar harán referencia casual a la existencia de un tablero de anuncios ([por ejemplo](https://www.usenix.org/system/files/conference/jets15/jets_0302-achenbach.pdf) "como es común en los esquemas de votación electrónica, asumimos un tablero de anuncios accesible públicamente y de solo agregar"), pero muchos menos documentos hablan sobre cómo este tablero de anuncios puede ser _implementado_ en realidad. Y aquí es donde, con suerte, ves a dónde voy con esto: **la forma más segura de implementar un tablero de anuncios _es_ simplemente usar una blockchain existente.**

## Votación electrónica segura con blockchains

Por supuesto, ha habido muchos intentos previos a blockchain de hacer un tablero de anuncios. [Este documento de 2008](https://epubs.surrey.ac.uk/107392/5/append-only.pdf) es un intento de este tipo; su modelo de confianza es un requisito estándar de que "`k` de `n` servidores deben ser honestos" (`k = n/2` es común). [Esta revisión de literatura de 2021](https://eprint.iacr.org/2021/047.pdf) cubre algunos intentos previos a blockchain de tableros de anuncios, así como explora el uso de blockchains para el trabajo; las soluciones previas a blockchain revisadas también confían en un modelo de confianza k-de-n.

Una blockchain también es un modelo de confianza k-de-n; requiere que al menos la mitad de los mineros o validadores de prueba de participación sigan el protocolo, y si esa suposición falla, eso suele resultar en un "ataque del 51%". Entonces, ¿por qué una blockchain es mejor que un tablero de anuncios especializado? La respuesta es: configurar un sistema k-de-n que realmente sea de confianza es difícil, y las blockchains son el único sistema que ya lo ha resuelto, y a gran escala. Supongamos que algún gobierno anunciara que estaba haciendo un sistema de votación y proporcionara una lista de 15 organizaciones locales y universidades que administrarían un tablero de anuncios especializado. ¿Cómo sabrías, como observador externo, que el gobierno no eligió esas 15 organizaciones de una lista de 1000 según su disposición a colaborar secretamente con una agencia de inteligencia?

**Las blockchains públicas, por otro lado, tienen mecanismos de consenso económico sin permisos (prueba de trabajo o prueba de participación) en los que cualquiera puede participar, y tienen una infraestructura diversa y altamente incentivada de exploradores de bloques, intercambios y otros nodos de observación para verificar constantemente en tiempo real que no está sucediendo nada malo.**

Estos sistemas de votación más sofisticados no _solo_ utilizan blockchains; confían en la criptografía, como [pruebas de conocimiento cero](../../../2021/01/26/snarks.html) para garantizar la corrección, y en la computación multipartita para garantizar la resistencia a la coerción. Por lo tanto, evitan las debilidades de sistemas más ingenuos que simplemente "ponen votos directamente en la blockchain" e ignoran los problemas resultantes de privacidad y resistencia a la coerción. Sin embargo, el tablero de anuncios de la blockchain sigue siendo una parte clave del modelo de seguridad de todo el diseño: si el comité está roto pero la blockchain no lo está, se pierde la resistencia a la coerción, pero todas las demás garantías en torno al proceso de votación siguen vigentes.

### MACI: votación en blockchain resistente a la coerción en Ethereum

El ecosistema de Ethereum está experimentando actualmente con un [sistema llamado MACI](https://github.com/appliedZKP/maci) que combina una blockchain, ZK-SNARKs y un único actor central que garantiza la resistencia a la coerción (pero no tiene el poder de comprometer ninguna propiedad que no sea la resistencia a la coerción). MACI no es muy técnicamente complicado. Los usuarios participan firmando un mensaje con su clave privada, cifrando el mensaje firmado con una clave pública publicada por un servidor central y publicando el mensaje firmado cifrado en la blockchain. El servidor descarga los mensajes de la blockchain, los descifra, los procesa y produce el resultado junto con un ZK-SNARK para asegurar que hizo el cálculo correctamente.

<br><center><img src="../../../../images/round9/maci2.png" style="width:500px" class="padded" /></center><br><br>

Los usuarios no pueden demostrar cómo participaron, porque tienen la capacidad de enviar un mensaje de "cambio de clave" para engañar a cualquiera que intente auditarlos: primero pueden enviar un mensaje de cambio de clave para cambiar su clave de A a B y luego enviar un "mensaje falso" firmado con A. El servidor rechazaría el mensaje, pero nadie más tendría forma de saber que se había enviado el mensaje de cambio de clave. Hay un requisito de confianza en el servidor, aunque solo para la privacidad y la resistencia a la coerción; el servidor no puede publicar un resultado incorrecto ya sea calculando incorrectamente o censurando mensajes. A largo plazo, se puede utilizar la computación multipartita para descentralizar el servidor en cierta medida, fortaleciendo las garantías de privacidad y resistencia a la coerción.

Hay una demostración funcional de este esquema en [clr.fund](https://clr.fund/) que se utiliza para la financiación cuadrática. El uso de la blockchain de Ethereum para garantizar la resistencia a la censura de los votos asegura un grado mucho mayor de resistencia a la censura de lo que sería posible si en su lugar se confiara en un comité para esto.

### Resumen

* El proceso de votación tiene cuatro requisitos de seguridad importantes que deben cumplirse para que una votación sea segura: **corrección**, **resistencia a la censura**, **privacidad** y **resistencia a la coerción**.
* Las blockchains son buenas en los dos primeros. Son malas en los dos últimos.
* La **encriptación** de votos en una blockchain puede agregar privacidad. Las **pruebas de conocimiento cero** pueden devolver la corrección a pesar de que los observadores no pueden sumar votos directamente porque están encriptados.
* La **computación multipartita** que desencripta y verifica votos puede proporcionar resistencia a la coerción, si se combina con un mecanismo donde los usuarios pueden interactuar con el sistema varias veces; la primera interacción invalida la segunda, o viceversa.
* El uso de una blockchain garantiza que tiene una resistencia a la censura de alta seguridad y mantiene esta resistencia a la censura _incluso si_ el comité colude y rompe la resistencia a la coerción. **Introducir una blockchain puede aumentar significativamente el nivel de seguridad del sistema.**

## Pero, ¿se puede confiar en la tecnología?

Pero ahora volvemos a la segunda crítica, más profunda, a cualquier tipo de votación electrónica, blockchain o no: que la tecnología en sí misma es demasiado insegura para confiar en ella.

El [reciente artículo del MIT](https://people.csail.mit.edu/rivest/pubs/PSNR20.pdf) que critica la votación en blockchain incluye esta útil tabla, que representa _cualquier_ forma de votación sin papel como fundamentalmente demasiado difícil de asegurar:

<br><center><img src="../../../../images/voting2-files/fourcategories.png" style="width:650px" class="padded" /></center><br><br>

La propiedad clave en la que se centran los autores es la **independencia del software**, que definen como "la propiedad de que un cambio o error no detectado en el software de un sistema no puede causar un cambio no detectado en el resultado de la elección". Básicamente, un error en el código no debería poder hacer accidentalmente que Prezzy McPresidentface sea el nuevo presidente del país (o, más realista, un error insertado deliberadamente no debería poder aumentar la participación de algún candidato del 42% al 52%).

Pero hay otras formas de lidiar con los errores. Por ejemplo, cualquier sistema de votación basado en blockchain que utilice pruebas de conocimiento cero públicamente verificables puede ser verificado de forma independiente. Alguien puede escribir su propia implementación del verificador de pruebas y verificar el Zk-SNARK por sí mismo. Incluso podrían escribir su propio software para votar. Claro, la complejidad técnica de hacer esto está más allá del 99.99% de cualquier base de votantes realista, pero si miles de expertos independientes tienen la capacidad de hacer esto y verificar que funcione, eso es más que suficiente en la práctica.

Sin embargo, para los autores del MIT, eso no es suficiente:

<br>
<blockquote style="margin-left: 35px; margin-right: 35px">
Así, cualquier sistema que sea exclusivamente electrónico, incluso si es verificable de extremo a extremo, parece inadecuado para elecciones políticas en el futuro previsible. La Fundación U.S. Vote ha señalado la promesa de los métodos E2E-V para mejorar la seguridad de la votación en línea, pero ha emitido un informe detallado recomendando evitar su uso para la votación en línea a menos que y hasta que la tecnología esté mucho más madura y completamente probada en la votación en lugares físicos [38].

Otros han propuesto extensiones de estas ideas. Por ejemplo, la propuesta de Juels et al. [55] enfatiza el uso de la criptografía para proporcionar diversas formas de "resistencia a la coerción". La propuesta Civitas de Clarkson et al. [24] implementa mecanismos adicionales para la resistencia a la coerción, que Iovino et al. [53] incorporan y desarrollan aún más en su sistema Selene. Desde nuestra perspectiva, estas propuestas son innovadoras pero poco realistas: son bastante complejas y, lo que es más importante, su seguridad depende de que los dispositivos de los votantes no estén comprometidos y funcionen según lo previsto, una suposición poco realista.

</blockquote>
<br>

El problema en el que se centran los autores no es la seguridad del _hardware del sistema de votación_; los riesgos en ese lado pueden mitigarse con pruebas de conocimiento cero. Más bien, los autores se centran en un problema de seguridad diferente: ¿se pueden hacer seguros los _dispositivos de los usuarios_ incluso en principio?

Dada la larga historia de todo tipo de exploits y ataques a dispositivos de consumo, uno estaría muy justificado en pensar que la respuesta es "no". Citando mi propio [artículo sobre seguridad de billeteras Bitcoin de 2013](https://bitcoinmagazine.com/culture/bitcoin-self-defense-part-i-wallet-protection-1368758841):

> Anoche, alrededor de las 9 p. m. PDT, hice clic en un enlace para ir a CoinChat[.]freetzi[.]com, y se me pidió que ejecutara Java. Lo hice (pensando que era una sala de chat legítima), y no pasó nada. Cerré la ventana y no pensé más en ello. Abrí mi billetera bitcoin-qt aproximadamente 14 minutos después y vi una transacción que NO aprobé que se dirigía a la billetera 1Es3QVvKN1qA2p6me7jLCVMZpQXVXWPNTC por casi toda mi billetera...

Y:

> En junio de 2011, el miembro de Bitcointalk "allinvain" perdió 25,000 BTC (valorados en $500,000 en ese momento) después de que un intruso desconocido de alguna manera obtuvo acceso directo a su computadora. El atacante pudo acceder al archivo wallet.dat de allinvain y vaciar rápidamente la billetera, ya sea enviando una transacción desde la computadora de allinvain o simplemente subiendo el archivo wallet.dat y vaciándolo en su propia máquina.

Pero estos desastres oscurecen una verdad mayor: **_en los últimos veinte años, la seguridad informática ha mejorado [lenta y constantemente](https://www.infosecurity-magazine.com/opinions/cybersecurity-getting-better-worse/)_**. Los ataques son mucho más difíciles de encontrar, a menudo requiriendo que el atacante encuentre errores en múltiples subsistemas en lugar de encontrar un solo agujero en un código grande y complejo. Los incidentes de alto perfil son más grandes que nunca, pero esto no es una señal de que algo esté menos seguro; más bien, es simplemente una señal de que estamos volviéndonos mucho más dependientes de Internet.

**[El hardware de confianza](https://link.springer.com/referenceworkentry/10.1007%2F978-0-387-39940-9_1491)** es una fuente muy importante de mejoras recientes. Algunos de los nuevos "teléfonos blockchain" (por ejemplo, [este de HTC](https://www.htcexodus.com/mea-en/cryptophone/exodus1s/)) llegan bastante lejos con esta tecnología y colocan un sistema operativo minimalista centrado en la seguridad en el chip de hardware de confianza, permitiendo que aplicaciones que requieren alta seguridad (por ejemplo, billeteras de criptomonedas) se mantengan separadas de otras aplicaciones. Samsung ha comenzado a fabricar teléfonos utilizando [tecnología](https://pixelplex.io/blog/what-is-samsung-blockchain-keystore/) [similar](https://www.samsung.com/us/business/solutions/samsung-knox/). E incluso dispositivos que nunca se anuncian como "dispositivos blockchain" (por ejemplo, iPhones) a menudo tienen algún tipo de hardware de confianza. Las billeteras de hardware de criptomonedas son efectivamente lo mismo, excepto que el módulo de hardware de confianza está físicamente ubicado fuera de la computadora en lugar de dentro. El hardware de confianza (¡merecidamente!) a menudo tiene mala reputación en círculos de seguridad y especialmente en la comunidad blockchain, porque simplemente [sigue](https://arstechnica.com/information-technology/2020/03/hackers-can-steal-secret-data-stored-in-intels-sgx-secure-enclave/) [siendo](https://techmonitor.ai/techonology/cybersecurity/intel-sgx-plundervolt-attack) [vulnerado](https://www.theregister.com/2020/11/14/intel_sgx_physical_security/) una y otra [vez](https://www.theregister.com/2020/11/14/intel_sgx_physical_security/). Y de hecho, definitivamente no querrías usarlo para _reemplazar_ tu protección de seguridad. Pero como _complemento_, es una gran mejora.

Finalmente, aplicaciones individuales, como billeteras de criptomonedas y sistemas de votación, son mucho más simples y tienen menos margen de error que un sistema operativo de consumo completo, incluso si tienes que incorporar soporte para [votación cuadrática](../../../2019/12/07/quadratic.html), [sorteo](https://en.wikipedia.org/wiki/Sortition), [sorteo cuadrático](https://ethresear.ch/t/quadratic-voting-with-sortition/6065) y cualesquiera horrores que invente la generación futura de Glen Weyl en 2040. La ventaja de herramientas como el hardware de confianza es su capacidad para _aislar_ lo simple de lo complejo y posiblemente defectuoso, y estas herramientas están teniendo cierto éxito.

## Entonces, los riesgos podrían disminuir con el tiempo. Pero, ¿cuáles son los beneficios?

Estas mejoras en la tecnología de seguridad apuntan a un futuro donde el hardware de consumo podría ser más confiable en el futuro de lo que es hoy. Las inversiones realizadas en esta área en los últimos años probablemente sigan dando frutos en la próxima década, y podríamos esperar mejoras significativas adicionales. Pero, ¿cuáles son los beneficios de hacer que la votación sea electrónica (basada en blockchain o de otra manera) que justifican explorar todo este espacio?

**Mi respuesta es simple: la votación se volvería mucho más eficiente, permitiéndonos hacerlo con mucha más frecuencia**. Actualmente, la participación democrática formal en organizaciones (gubernamentales o corporativas) tiende a limitarse a un solo voto cada 1-6 años. Esto significa efectivamente que cada votante solo aporta menos de un bit de información al sistema cada año. Quizás en gran parte como resultado de esto, la toma de decisiones descentralizada en nuestra sociedad está fuertemente bifurcada en dos extremos: democracia pura y mercados puros. La democracia es o muy ineficiente (votos corporativos y gubernamentales) o muy insegura (me gusta y retuitea en las redes sociales). Los mercados son mucho más eficientes tecnológicamente y son mucho más seguros que las redes sociales, pero su lógica económica fundamental los convierte en una mala opción para muchos tipos de problemas de decisión, especialmente aquellos relacionados con bienes públicos.

<center><br>
<img src="../../../../images/voting2-files/triangle.png" class="padded" /><br><br>
<i><small>Sí, sé que es otro triángulo y realmente me disculpo por tener que usarlo. Pero por favor, aguanta solo esta vez... (bueno, está bien, estoy seguro de que haré aún más triángulos en el futuro; simplemente acéptalo y supéralo)</small></i>
</center><br><br>

Hay mucho que podríamos hacer si pudiéramos construir más sistemas que estén en algún punto intermedio entre la democracia y los mercados, aprovechando el igualitarismo de lo primero, la eficiencia técnica de lo segundo y las propiedades económicas en todo el espectro entre los dos extremos. [La financiación cuadrática](../../../2019/12/07/quadratic.html) es un excelente ejemplo de esto. La democracia líquida es otro excelente ejemplo. Incluso si no introducimos mecanismos de delegación o matemáticas cuadráticas sofisticadas, hay mucho que podríamos hacer al votar _mucho más_ y a escalas más pequeñas, adaptándonos mejor a la información disponible para cada votante. Pero el desafío con todas estas ideas es que, para tener un esquema que mantenga duraderamente _cualquier_ nivel de democraticidad, necesitas alguna forma de resistencia al ataque Sybil y mitigación de la compra de votos: exactamente los problemas que estos sofisticados esquemas de votación con ZK-SNARK + MPC + blockchain están tratando de resolver.

## El espacio cripto puede ayudar

Uno de los beneficios subestimados del espacio cripto es que es una excelente "zona económica especial virtual" para probar ideas económicas y criptográficas en un entorno altamente adversarial. Cualquier cosa que construyas y lances, una vez que el poder económico que controla alcanza cierto tamaño, una gran cantidad de actores diversos, a veces altruistas, a veces motivados por el beneficio y a veces maliciosos, muchos de los cuales son completamente anónimos, se abalanzarán sobre el sistema e intentarán dirigir ese poder económico hacia sus propios objetivos.

Los incentivos para los atacantes son altos: si un atacante roba $100 de tu dispositivo criptoeconómico, a menudo pueden obtener la recompensa completa de $100, y a menudo pueden salir impunes. Pero los incentivos para los defensores también son altos: si desarrollas una herramienta que ayuda a los usuarios a _no_ perder sus fondos, podrías (al menos en ocasiones) convertir eso en una herramienta y ganar millones. Cripto es la zona de entrenamiento definitiva: si puedes construir algo que pueda sobrevivir en este entorno a gran escala, probablemente también pueda sobrevivir en el mundo real.

Esto se aplica a [la financiación cuadrática](../../../2021/04/02/round9.html), se aplica a [multifirmas](https://gnosis-safe.io/) y [carteras de recuperación social](../../../2021/01/11/recovery.html), y también puede aplicarse a los sistemas de votación. El espacio blockchain ya ha contribuido a motivar el surgimiento de tecnologías de seguridad importantes:

* Carteras de hardware
* Pruebas de conocimiento cero eficientes de propósito general
* Herramientas de verificación formal
* "Teléfonos blockchain" con chips de hardware confiable
* Esquemas anti-Sybil como [Prueba de Humanidad](https://www.proofofhumanity.id/)

En todos estos casos, alguna versión de la tecnología existía antes de que los blockchains llegaran a la escena. Pero es difícil negar que los blockchains han tenido un impacto significativo en impulsar estos esfuerzos hacia adelante, y el importante papel de los incentivos inherentes al espacio juega un papel clave en elevar las apuestas lo suficiente como para que realmente ocurra el desarrollo tecnológico.

### Conclusión

**En el corto plazo, cualquier forma de votación en blockchain debería permanecer confinada a pequeños experimentos**, ya sea en pequeñas pruebas para aplicaciones más convencionales o para el propio espacio blockchain. La seguridad en la actualidad definitivamente no es lo suficientemente buena como para confiar en las computadoras para todo. Pero está mejorando, y si estoy equivocado y la seguridad _no mejora_, no solo la votación en blockchain, sino también las criptomonedas en su conjunto, tendrán dificultades para tener éxito. Por lo tanto, hay un gran incentivo para que la tecnología continúe mejorando.

Todos deberíamos seguir observando la tecnología y los esfuerzos que se realizan en todas partes para tratar de aumentar la seguridad, y gradualmente sentirnos más cómodos utilizando la tecnología en procesos sociales muy importantes. La tecnología ya es clave en nuestros mercados financieros, y una cripto-ización de una gran parte de la economía (o incluso solo reemplazando el oro) pondrá una parte aún mayor de la economía en manos de nuestros algoritmos criptográficos y el hardware que los ejecuta. Deberíamos observar y apoyar este proceso cuidadosamente y, con el tiempo, aprovechar sus beneficios para llevar nuestras tecnologías de gobernanza al siglo XXI.
