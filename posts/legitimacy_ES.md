[category]: <> (Español)
[date]: <> (2021/03/23)
[title]: <> (El recurso escaso más importante es la legitimidad)
[pandoc]: <> (--mathjax)

_Un agradecimiento especial a Karl Floersch, Aya Miyaguchi, Mr Silly por sus ideas, comentarios y reseñas y Jacobo Blandón por traducción._

Los ecosistemas de cadenas de bloques Bitcoin y Ethereum gastan más en seguridad de la red - objetivo de la minería por prueba de trabajo (POW) - que en todo lo demás combinado. La cadena de bloques Bitcoin ha pagado un promedio de alrededor _de $38 millones al día_ en recompensas a los mineros desde el comienzo del año, más [alrededor de $5 millones en tarifas de transacción diario](https://ycharts.com/indicators/bitcoin_total_transaction_fees_per_day). La cadena de bloques Ethereum ocupa el segundo lugar, con $19.5 millones al día en recompensas en bloque más [$18 millones en tarifas de transacción diario](https://etherscan.io/chart/transactionfee). Mientras tanto, el presupuesto anual de la Fundación Ethereum, que paga la investigación, el desarrollo de protocolos, las subvenciones y todo tipo de otros gastos, es de apenas 30 millones de dólares _al año_. También existen fondos que no provienen de la Fundación Ethereum, pero a lo sumo son un poco más grandes. Es probable que los gastos del ecosistema de Bitcoin en I+D sean incluso menores. La I+D del ecosistema Bitcoin está financiada en gran parte por empresas (con un total de 250 millones de dólares recaudados hasta ahora [según esta página](https://www.crunchbase.com/hub/bitcoin-companies-seed-funding)), y [este informe](https://blog.bitmex.com/who-funds-bitcoin-development/) sugiere unos 57 empleados; asumiendo salarios bastante altos y muchos desarrolladores pagados que no se cuentan, eso equivale a unos 20 millones de dólares al año.

<center>
<img src="https://vitalik.ca/images/legitimacy-files/chart.png" /><br><br>
</center>

Claramente, este patrón de gastos _es una mala asignación masiva de recursos_. El último 20% de la potencia de hash de la red proporciona mucho menos valor al ecosistema que lo que tendrían esos mismos recursos si se hubieran dedicado a la investigación y al desarrollo del protocolo central. Entonces, ¿por qué no ... recortar el presupuesto de PoW en un 20% y redirigir los fondos a esas otras cosas en su lugar?

La respuesta estándar a este acertijo tiene que ver con conceptos como "[teoría de la elección pública](http://www.daviddfriedman.com/Academic/Price_Theory/PThy_Chapter_19/PThy_Chap_19.html)" y "[vallas de Schelling](https://www.lesswrong.com/posts/Kbm6QnJv9dgWsPHQP/schelling-fences-on-slippery-slopes)": aunque podríamos identificar fácilmente algunos bienes públicos valiosos a los que redirigir algunos fondos como únicos, haciendo un _patrón institucionalizado regular_ de tales decisiones conllevan riesgos de caos político y captura que a la larga no valen la pena. Pero independientemente de las razones por las cuales, nos enfrentamos al hecho interesante que **los ecosistemas de Bitcoin y Ethereum son capaces de convocar miles de millones de dólares de capital, pero tienen restricciones extrañas y difíciles de entender sobre dónde puede ir ese capital**.

Vale la pena comprender la poderosa fuerza social que está creando este efecto. Como veremos, también es la misma fuerza social detrás de por qué el ecosistema Ethereum es capaz de convocar estos recursos en primer lugar (y que el ecosistema Ethereum Classic que es casi idéntico tecnológicamente no es capaz). También es una fuerza social que es clave para ayudar a la cadena a recuperarse de un ataque del 51%. Y es una fuerza social que subyace a todo tipo de mecanismos extremadamente poderosos mucho más allá del espacio blockchain. Por razones que quedarán claras en las próximas secciones, le daré un nombre a esta poderosa fuerza social: **legitimidad**.


### Las monedas pueden ser propiedad de contratos sociales

Para comprender mejor la fuerza a la que nos dirigimos, otro ejemplo importante es la saga épica de Steem y [Hive](https://hive.io/). A principios de 2020, [Justin Sun](https://www.theverge.com/21459906/bittorrent-tron-acquisition-justin-sun-us-china) compró [Steem-the-company](https://www.coindesk.com/justin-sun-bought-steemit-steem-moved-to-limit-his-power), que no es lo mismo que Steem-the-blockchain, pero poseía aproximadamente el 20% del suministro de tokens STEEM. La comunidad, naturalmente, no confió en Justin Sun. Así que hicieron una votación en cadena para formalizar lo que consideraban un "acuerdo de caballeros", acordando que las monedas de Steem-the-company se mantenían en fideicomiso por el bien común de Steem-the-blockchain y no deberían usarse para votar. Con la ayuda de las monedas en poder de los intercambios, Justin Sun hizo un contraataque y ganó el control de suficientes delegados para controlar unilateralmente la cadena. La comunidad no vio más opciones dentro del protocolo. Entonces, en su lugar, hicieron una bifurcación de Steem-the-blockchain, llamada Hive, y copiaron todos los saldos de tokens de STEEM, excepto aquellos, incluido el de Justin Sun, que participaron en el ataque.

<center>
<br><img src="https://vitalik.ca/images/legitimacy-files/hive.png" style="width:500px" />
<br><br>
<i><small>Y consiguieron muchas aplicaciones a bordo. Si no hubieran logrado esto, muchos más usuarios se habrían quedado en Steem o se habrían mudado a un proyecto diferente por completo.</small></i>
<br><br><br>
</center>

La lección que podemos aprender de esta situación es la siguiente: _Steem-the-company nunca "poseyó" las monedas_. Si lo hubieran hecho, habrían tenido la capacidad práctica de [usar, disfrutar y abusar](https://cours-de-droit.net/usus-fructus-abusus-les-elements-constitutifs-de-la-propriete-a130283250/) de las monedas de la forma que quisieran. Pero en realidad, cuando la empresa trató de disfrutar y abusar de las monedas de una manera que a la comunidad no le gustó, _fueron detenidas con éxito_. Lo que está sucediendo aquí es un patrón similar al que vimos con las recompensas de monedas Bitcoin y Ethereum aún no emitidas: las monedas finalmente no eran propiedad de una clave criptográfica, sino de algún tipo de contrato social.

Podemos aplicar el mismo razonamiento a muchas otras estructuras en el espacio blockchain. Considere, por ejemplo, la [ENS](https://ens.domains) root multisig. La [root multisig está controlada](https://consensys.net/diligence/audits/2019/03/ens-permanent-registrar/) por siete miembros prominentes de la comunidad de ENS y Ethereum. Pero, ¿qué pasaría si cuatro de ellos se unieran y "actualizaran" el registrador a uno que les transfiera los mejores dominios? Dentro del contexto de ENS, el-sistema-de-contrato-inteligente, tienen la capacidad completa e indiscutible para hacer esto. Pero si realmente intentaran abusar de su capacidad técnica de esta manera, lo que sucedería está claro para cualquiera: serían excluidos de la comunidad, los miembros restantes de la comunidad ENS harían un nuevo contrato ENS que restaura a los propietarios originales del dominio, y cada aplicación Ethereum que usa ENS volvería a reescribir su interfaz de usuario para ser usada de nuevo.

Esto va mucho más allá de las estructuras de contratos inteligentes. ¿Por qué Elon Musk puede vender un NFT del tweet de Elon Musk, pero a Jeff Bezos le costaría mucho más hacer lo mismo? Elon y Jeff tienen el mismo nivel de capacidad para capturar el tweet de Elon y pegarlo en un dapp NFT, entonces, ¿cuál es la diferencia? Para cualquiera que tenga una comprensión intuitiva básica de la psicología social humana (o la [escena del arte falso](https://www.austinartistsmarket.com/famous-fakes-art-history/)), la respuesta es obvia: Elon vendiendo el tweet de Elon es algo real, y Jeff haciendo lo mismo no lo es. Una vez más, millones de dólares de valor están siendo controlados y asignados, no por individuos o claves criptográficas, sino por concepciones sociales de legitimidad.

Y, yendo aún más lejos, la legitimidad gobierna todo tipo de juegos de estatus social, [discurso intelectual](https://samoburja.com/intellectual-legitimacy/), lenguaje, derechos de propiedad, sistemas políticos y fronteras nacionales. Incluso el consenso de blockchain funciona de la misma manera: la única diferencia entre una bifurcación blanda que es aceptada por la comunidad y un ataque de censura del 51% después del cual la comunidad coordina una [bifurcación de recuperación extra-protocolo](https://ethresear.ch/t/responding-to-51-attacks-in-casper-ffg/6363) para eliminar al atacante es la legitimidad.


## Entonces, ¿qué es la legitimidad?

_Ver también: mi anterior [publicación sobre la gobernanza de blockchain](https://vitalik.ca/general/2017/12/17/voting.html)._


Para comprender el funcionamiento de la legitimidad, necesitamos profundizar en alguna teoría de juegos.Hay muchas situaciones en la vida que exigen un **comportamiento coordinado**: si actúa de cierta manera solo, es probable que no llegue a ninguna parte (o algo peor), pero si todos actúan juntos, se puede lograr el resultado deseado.

<center><br>
<img src="https://vitalik.ca/images/voting-files/coordinationgame.png" />
<br><br>
<i><small> Un juego de coordinación abstracto. Usted se beneficia enormemente de hacer el mismo movimiento que todos los demás.</small></i><br><br>
</center>

Un ejemplo natural es conducir en el lado izquierdo o en el derecho de la carretera: realmente no importa en _qué_ lado de la carretera conduzcan las personas, siempre y cuando conduzcan por el mismo lado. Si cambia de bando al mismo tiempo que todos los demás, y la mayoría de la gente prefiere el nuevo arreglo, puede haber un beneficio neto. Pero si cambia de lado solo, no importa cuánto prefiera conducir por el otro lado, el resultado neto para usted será bastante negativo. 

Ahora, estamos listos para definir la legitimidad.

> <b style="color:black">La legitimidad es un patrón de aceptación de orden superior. Un resultado en algún contexto social es _legítimo_ si la gente en ese contexto social acepta ampliamente y juega su papel en la promulgación de ese resultado, y cada persona individual lo hace porque espera que todos los demás hagan lo mismo.</b>

La legitimidad es un fenómeno que surge de forma natural en los juegos de coordinación. Si usted no está en un juego de coordinación, no hay razón para actuar de acuerdo con sus expectativas de cómo actuarán otras personas, por lo que la legitimidad no es importante. Pero, como hemos visto, los juegos de coordinación están en todas partes en la sociedad, por lo que la legitimidad resulta ser bastante importante. En casi cualquier entorno con juegos de coordinación que exista durante bastante tiempo, inevitablemente surgen algunos mecanismos que pueden elegir qué decisión tomar. Estos mecanismos están impulsados por una cultura establecida de que todos prestan atención a estos mecanismos y (generalmente) hacen lo que dicen. Cada persona razona que debido a que _todos los demás_ siguen estos mecanismos, si hacen algo diferente, solo crearán conflicto y sufrirán, o al menos se quedarán solos en un ecosistema bifurcado y solitario. Si un mecanismo tiene la capacidad de tomar estas decisiones con éxito, entonces ese mecanismo tiene legitimidad.

<center><br>
<img src="https://vitalik.ca/images/voting-files/byzantinegeneral.jpg" style="width:500px" />
<br><br>
<i><small>Un general bizantino reuniendo a sus tropas hacia adelante. El propósito de esto no es solo hacer que los soldados se sientan valientes y emocionados, sino también asegurarles que todos los demás se sienten valientes y emocionados y también cargarán hacia adelante, por lo que un soldado individual no solo se está suicidando al cargar solo hacia adelante.</small></i><br><br>
</center>

En cualquier contexto en el que haya un juego de coordinación que haya existido durante bastante tiempo, es probable que exista una concepción de legitimidad. **Y las cadenas de bloques están llenas de juegos de coordinación**. ¿Qué software de cliente ejecuta? ¿Qué registro de nombre de dominio descentralizado solicita qué dirección corresponde a un nombre .eth? ¿Qué copia del contrato de Uniswap acepta como "el" intercambio de Uniswap? Incluso los NFT son un juego de coordinación. Las dos partes más importantes del valor de un NFT son (I) el orgullo de tener el NFT y la capacidad de mostrar su propiedad, y (II) la posibilidad de venderlo en el futuro. Para ambos componentes, es realmente importante que cualquier NFT que compre sea reconocido como legítimo por todos los demás. En todos estos casos, es muy beneficioso tener la misma respuesta que todos los demás, y el mecanismo que determina ese equilibrio tiene mucho poder.


### Teorías de la legitimidad

Hay muchas formas diferentes en las que puede surgir la legitimidad. En general, la legitimidad surge porque lo que gana legitimidad es psicológicamente atractivo para la mayoría de las personas. Pero, por supuesto, las intuiciones psicológicas de las personas pueden ser bastante complejas. Es imposible hacer una lista completa de las teorías de la legitimidad, pero podemos comenzar con algunas:

* **Legitimidad por fuerza bruta**: alguien convence a todos de que son lo suficientemente poderosos como para imponer su voluntad y resistirlos será muy difícil. Esto impulsa a la mayoría de las personas a someterse porque cada uno espera que _todos los demás_ también estén demasiado asustados para resistir.
* **Legitimidad por continuidad**: si algo era legítimo en el momento T, es legítimo por defecto en el momento T + 1.
* **Legitimidad por equidad**: algo puede volverse legítimo porque satisface una noción intuitiva de justicia. Ver también: [mi publicación sobre neutralidad creíble](https://nakamoto.com/credible-neutrality/), aunque tenga en cuenta que este no es el único tipo de equidad.
* **Legitimidad por proceso**: si un proceso es legítimo, los resultados de ese proceso ganan legitimidad (por ejemplo, las leyes aprobadas por las democracias a veces se describen de esta manera).
* **Legitimidad por desempeño**: si los productos de un proceso conducen a resultados que satisfacen a las personas, entonces ese proceso puede ganar legitimidad (por ejemplo, las dictaduras exitosas a veces se describen de esta manera).
* **Legitimidad por participación**: si las personas participan en la elección de un resultado, es más probable que lo consideren legítimo. Esto es similar a la equidad, pero no del todo: se basa en un deseo psicológico de ser coherente con sus acciones anteriores.

Tenga en cuenta que la legitimidad es un concepto descriptivo; algo puede ser legítimo incluso si usted personalmente piensa que es horrible. Dicho esto, si suficientes personas piensan que un resultado es horrible, existe una mayor probabilidad de que suceda algún evento en el futuro que haga que esa legitimidad desaparezca, a menudo al principio de forma gradual y luego repentinamente.


## La legitimidad es una poderosa tecnología social y deberíamos usarla

La situación de la financiación de bienes públicos en los ecosistemas de criptomonedas es bastante mala. Hay cientos de miles de millones de dólares de capital circulando, pero los bienes públicos que son clave para la supervivencia continua de ese capital están recibiendo solo decenas de millones de dólares por año de financiación.

Hay dos formas de responder a este hecho. La primera forma es enorgullecerse de estas limitaciones y de los valientes, aunque no particularmente efectivos, esfuerzos que su comunidad hace para solucionarlos.

<center>
<br>
<table><tr style="border:0px">
<td style="border:0px"><a href="https://twitter.com/francispouliot_/status/1366465485546655744"><img src="https://vitalik.ca/images/legitimacy-files/bitcoin1.png" /></a></td>
<td style="border:0px"><a href="https://blog.wasabiwallet.io/bitcoin-knots-donation/"><img src="https://vitalik.ca/images/legitimacy-files/bitcoin2.png" /></a></td>
</tr></table>
<br>
</center>

El autosacrificio personal de los equipos que financian el desarrollo central es, por supuesto, admirable, pero es admirable de la misma manera que [Eliud Kipchoge corriendo un maratón en menos de 2 horas](https://www.bbc.com/sport/athletics/50025543) es admirable: es una demostración impresionante de fortaleza humana, pero no es el futuro del transporte. (o, en este caso, financiación de bienes públicos). Al igual que tenemos tecnologías mucho mejores para permitir que las personas se muevan 42 km en menos de una hora sin una fortaleza excepcional y años de capacitación, **también deberíamos enfocarnos en construir mejores tecnologías sociales para financiar los bienes públicos a las escalas que necesitamos, y como una parte sistémica de nuestra ecología económica y no actos puntuales de iniciativa filantrópica**.

Ahora, volvamos a las criptomonedas. Un poder importante de la criptomoneda (y otros activos digitales como nombres de dominio, tierra virtual y NFT) está permitiendo a las comunidades reunir grandes cantidades de capital sin que ninguna persona individual tenga que donar personalmente ese capital. Sin embargo, este capital está limitado por _concepciones de legitimidad_: no se puede simplemente asignarlo a un equipo centralizado sin comprometer lo que lo hace valioso. Si bien Bitcoin y Ethereum ya se basan en concepciones de legitimidad para [responder a los ataques del 51%](https://ethresear.ch/t/responding-to-51-attacks-in-casper-ffg/6363), utilizar las concepciones de legitimidad para guiar la financiación de bienes públicos dentro del protocolo es mucho más difícil. Pero en la capa de aplicaciones [cada vez más rica](https://www.theverge.com/2021/3/11/22325054/beeple-christies-nft-sale-cost-everydays-69-million) en la que se crean constantemente nuevos protocolos, tenemos un poco más de flexibilidad en cuanto a dónde podría ir esa financiación.


### Legitimidad en Bitshares

Una de las ideas olvidadas hace mucho tiempo, pero en mi opinión muy innovadoras, del espacio temprano de las criptomonedas fue el modelo de [consenso social](http://web.archive.org/web/20140209035756/https://invictus-innovations.com/social-consensus/) [de Bitshares](https://bitsharestalk.org/index.php?PHPSESSID=h7u4curkvqm5dn9gs9q3end8j0&topic=5.0). Esencialmente, Bitshares se describió a sí misma como una comunidad de personas ([titulares de PTS y AGS](https://bitsharestalk.org/index.php?topic=1964.0)) que estaban dispuestas a ayudar a apoyar colectivamente un ecosistema de nuevos proyectos, pero para que un proyecto sea bienvenido en el ecosistema, tendría que asignar el 10% de su token. suministro a los titulares de PTS y AGS existentes.

Ahora, por supuesto, cualquiera puede hacer un proyecto que no asigne ninguna moneda a los titulares de PTS / AGS, o incluso bifurcar un proyecto que sí hizo una asignación y eliminar la asignación. Pero, como dice Dan Larimer:

>No se puede obligar a nadie a hacer nada, pero en este mercado todo es efecto de red. Si a alguien se le ocurre una implementación convincente, entonces puede adoptarla toda la comunidad de PTS por el costo de generar un nuevo bloque de génesis. El individuo que decidiera empezar de cero tendría que construir una comunidad completamente nueva alrededor de su sistema. Teniendo en cuenta el efecto de red, sospecho que la moneda que honra a ProtoShares ganará.

Esta es también una concepción de legitimidad: cualquier proyecto que haga la asignación a los titulares de PTS / AGS obtendrá la atención y el apoyo de la comunidad (y valdrá la pena que cada miembro de la comunidad individual se interese en el proyecto porque el resto de la comunidad también lo está haciendo), y cualquier proyecto que no haga la asignación no lo hará. **Ahora bien, esta no es ciertamente una concepción de legitimidad que queremos replicar literalmente (hay poco apetito en la comunidad de Ethereum por enriquecer a un pequeño grupo de primeros adoptantes), pero el concepto central se puede adaptar a algo mucho más socialmente valioso**.


### Extendiendo el modelo a Ethereum

Los ecosistemas blockchain, incluido Ethereum, valoran la libertad y la descentralización. Pero, lamentablemente, la ecología de bienes públicos de la mayoría de estas cadenas de bloques sigue estando bastante impulsada por la autoridad y centralización: ya sea Ethereum, Zcash o cualquier otra cadena de bloques importante, normalmente hay una (o como máximo 2-3) entidades que gastan mucho más que todos. de lo contrario, dar pocas opciones a los equipos independientes que quieran construir bienes públicos. A este modelo de financiación de bienes públicos lo llamo "Coordinadores centrales de capital para bienes públicos" (CCCP).

<br><center><img src="https://vitalik.ca/images/legitimacy-files/cccp.png" /></center><br><br>

**Este estado de cosas no es culpa de las propias organizaciones, que normalmente hacen todo lo posible con valentía para apoyar el ecosistema. Más bien, son las reglas del ecosistema las que están siendo _injustas con esa organización_, porque mantienen a la organización en un estándar injustamente alto**. Cualquier organización centralizada tendrá inevitablemente puntos ciegos y al menos algunas categorías y equipos cuyo valor no comprenderá; esto no se debe a que cualquiera de los involucrados esté haciendo algo malo, sino a que tal perfección está fuera del alcance de pequeños grupos de humanos. Así que hay un gran valor en la creación de un enfoque más diversificado y resistente a los bienes públicos que financian a tomar la presión de una sola organización.

Afortunadamente, ¡ya tenemos la semilla de esa alternativa! El ecosistema de aplicación de capa en Ethereum existe, se está volviendo cada vez más poderosa y ya está mostrando su espíritu público. Empresas como Gnosis han estado contribuyendo al desarrollo de clientes en Ethereum, y varios proyectos Ethereum DEFI han donado cientos de miles de dólares en subvenciones de Gitcoin Grants.

<center><br>
<img src="https://vitalik.ca/images/round_7_files/matching.jpg" />
<br>
</center><br><br>

Gitcoin Grants ya ha alcanzado un alto nivel de legitimidad: su mecanismo de financiación de bienes públicos, [la financiación cuadrática](https://vitalik.ca/general/2019/12/07/quadratic.html), ha demostrado ser [credibilidad neutral](https://nakamoto.com/credible-neutrality/) y eficaz para reflejar las prioridades y valores de la comunidad y tapar los huecos que dejan los mecanismos de financiación existentes. A veces, los principales beneficiarios de contrapartida de Gitcoin Grants incluso los utilizan como inspiración para las subvenciones por parte de otras entidades otorgantes de subvenciones más centralizadas. La propia Fundación Ethereum ha desempeñado un papel clave en el apoyo de esta experimentación y diversidad, incubando esfuerzos como Gitcoin Grants, junto con MolochDAO y otros, que luego obtienen un apoyo de la comunidad más amplia.

Podemos fortalecer aún más este incipiente ecosistema de financiamiento de bienes públicos tomando el modelo de Bitshares y haciendo una modificación: en lugar de brindar el apoyo comunitario más fuerte a los proyectos que asignaron tokens a una pequeña oligarquía que compró PTS o AGS en 2013, **apoyamos proyectos que aportan una pequeña parte de su tesoro a los bienes públicos que los hacen posibles y al ecosistema del que dependen**. Y, lo que es más importante, podemos negar estos beneficios a los proyectos que bifurcan un proyecto existente y no devuelven valor al ecosistema en general.

Hay muchas formas de respaldar los bienes públicos: hacer un compromiso a largo plazo para respaldar el grupo de contrapartida de Gitcoin Grants, respaldar el desarrollo de clientes en Ethereum (también una tarea razonablemente creíble-neutral, ya que existe una definición clara de lo que es un cliente de Ethereum), o incluso ejecutando su propio programa de subvenciones cuyo alcance va más allá de ese proyecto de capa de aplicación en particular. La forma más fácil de ponerse de acuerdo sobre lo que cuenta como apoyo suficiente es acordar cuánto, por ejemplo, el 5% del gasto de un proyecto se destinará a respaldar el ecosistema más amplio y otro 1% a bienes públicos que van más allá del espacio blockchain, y dependen de buena fe para elegir adónde irían esos fondos.


### ¿La comunidad realmente tiene tanta influencia?

Por supuesto, existen límites para el valor de este tipo de apoyo comunitario. Si un proyecto de la competencia (o incluso una bifurcación de un proyecto existente) ofrece a sus usuarios una oferta mucho mejor, entonces los usuarios acudirán en masa, independientemente de cuántas personas les griten que utilicen alguna alternativa que consideren más pro-social.

Pero estos límites son diferentes en diferentes contextos; a veces, la influencia de la comunidad es débil, pero en otras ocasiones es bastante fuerte. Un caso de estudio interesante en este sentido es el caso de [Tether](https://tether.to/) vs [DAI](https://makerdao.com/). Tether [tiene](https://ag.ny.gov/press-release/2021/attorney-general-james-ends-virtual-currency-trading-platform-bitfinexs-illegal) [muchos](https://www.forbes.com/sites/francescoppola/2019/03/14/tethers-u-s-dollar-peg-is-no-longer-credible/?sh=6beff930451b) [escándalos](https://seekingalpha.com/article/4403640-tethers-credibility-and-impact-on-bitcoin), pero a pesar de esto, los comerciantes usan Tether para mantener y mover dólares todo el tiempo. El [DAI](https://makerdao.com/) más descentralizado y transparente, a pesar de sus beneficios, no puede quitarle gran parte de la participación de mercado de Tether, al menos en lo que respecta a los traders. Pero donde DAI sobresale son las aplicaciones: [Augur](https://augur2.eth.link) usa DAI, [xDai](https://www.xdaichain.com/) usa DAI, [PoolTogether](https://app.pooltogether.com/) usa DAI, [zk.money](https://zk.money/asset/DAI) planea usar DAI, y [la lista continúa](https://github.com/makerdao/awesome-makerdao#dai-1). ¿Qué dapps usan USDT? Muchas menos.

Por lo tanto, aunque el poder de los efectos de legitimidad impulsados por la comunidad no es infinito, hay un margen considerable de influencia, suficiente para alentar a los proyectos a dirigir al menos un pequeño porcentaje de sus presupuestos al ecosistema más amplio. Incluso hay una razón egoísta para participar en este equilibrio: si fueras el desarrollador de una billetera Ethereum, o un autor de un podcast o un boletín informativo, y viste dos proyectos en competencia, uno de los cuales contribuye significativamente a los bienes públicos a nivel del ecosistema, incluyéndote a ti mismo. y uno que no lo hace, ¿por cuál haría todo lo posible para ayudarlos a obtener una mayor participación en el mercado?


### NFT: apoyo a los bienes públicos más allá de Ethereum

El concepto de apoyar los bienes públicos a través del valor generado "a partir del Ether" por concepciones de legitimidad respaldadas públicamente tiene un valor que va mucho más allá del ecosistema Ethereum. Un desafío y una oportunidad importantes e inmediatos son los NFT. Los NFT tienen una gran posibilidad de ayudar significativamente a muchos tipos de bienes públicos, especialmente de la variedad creativa, a resolver al menos [parcialmente sus deficiencias de financiamiento crónicos y sistémicos](https://en.wikipedia.org/wiki/Tragedy_of_the_commons).

<center><br>
<a href="https://www.theverge.com/2021/3/9/22321464/jack-dorsey-nft-tweet-auction-bitcoin-donate-charity"><img src="https://vitalik.ca/images/legitimacy-files/jack.jpg" style="width:450px" /></a>
<br><br>
<i><small>De hecho, un primer paso muy admirable.</small></i>
</center><br><br>

Pero también podrían ser una oportunidad perdida: hay poco valor social en ayudar a Elon Musk a ganar otro millón de dólares vendiendo su tweet cuando, por lo que sabemos, el dinero solo va para él (y, para su crédito, finalmente [decidió no vender](https://www.cnbc.com/2021/03/17/elon-musk-turns-down-1-million-offer-to-buy-his-tweet-as-an-nft.html)). Si los NFT simplemente se convierten en un casino que beneficia en gran medida a las celebridades ya ricas, ese sería un resultado mucho menos interesante.

**Afortunadamente, tenemos la capacidad de ayudar a moldear el resultado**. Qué NFT le resulta atractivo comprar a la gente y cuáles no, es una cuestión de legitimidad: si todos están de acuerdo en que un NFT es interesante y otro NFT es poco convincente, entonces la gente preferirá comprar el primero, porque tendría ambos más altos valor por los derechos de fanfarronear y el orgullo personal de poseerlo, y porque podría revenderse por más porque todos los demás piensan de la misma manera. Si la concepción de la legitimidad de las NFT se puede llevar en una buena dirección, existe la oportunidad de establecer un canal sólido de financiación para artistas, organizaciones benéficas y otros.

Aquí hay dos ideas potenciales:

1. Alguna institución (o incluso DAO) podría "bendecir" a los NFT a cambio de una garantía de que una parte de los ingresos se destina a una causa benéfica, asegurando que varios grupos se beneficien al mismo tiempo. Esta bendición podría incluso venir con una categorización oficial: ¿el NFT está dedicado al alivio de la pobreza global, la investigación científica, las artes creativas, el periodismo local, el desarrollo de software de código abierto, el empoderamiento de las comunidades marginadas o algo más?
2. Podemos trabajar con plataformas de redes sociales para hacer que las NFT sean más visibles en los perfiles de las personas, brindando a los compradores una forma de mostrar los valores con los que se comprometieron, no solo con sus palabras, sino con el dinero que tanto les costó ganar. Esto podría combinarse con (1) para impulsar a los usuarios hacia las NFT que contribuyen a causas sociales valiosas.

Definitivamente hay más ideas, pero esta es un área que ciertamente merece una coordinación y reflexión más activas.

## En resumen

* El concepto de **legitimidad (aceptación de orden superior) es muy poderoso**. La legitimidad aparece en cualquier contexto donde haya **[coordinación](https://vitalik.ca/general/2020/09/11/coordination.html)**, y especialmente en internet, la coordinación está en todas partes.
* Hay diferentes formas en las que la legitimidad llega a ser: **la fuerza bruta, la continuidad, la equidad, el proceso, el desempeño** y **la participación** están entre las más importantes.
*La criptomoneda es poderosa porque nos permite reunir grandes fondos de capital por voluntad económica colectiva, y estos fondos de capital, al principio, no están controlados por ninguna persona. Más bien, **estos fondos de capital están _controlados directamente por conceptos de legitimidad_**.
* Es demasiado arriesgado comenzar a financiar bienes públicos imprimiendo tokens en la capa base. Afortunadamente, sin embargo, Ethereum tiene un **ecosistema de capas de aplicaciones** muy rico, donde tenemos mucha más flexibilidad. Esto se debe en parte a que existe la oportunidad no solo de influir en los proyectos existentes, sino también de dar forma a otros nuevos que surgirán en el futuro.
* **Los proyectos de la capa de aplicación que apoyan los bienes públicos en la comunidad deben obtener el apoyo de la comunidad**, y esto es un gran problema. ¡El ejemplo de DAI muestra que este apoyo realmente importa!
* El ecosistema Ethereum se preocupa por el diseño de mecanismos y la innovación en la capa social. ¡Los **desafíos de financiamiento de bienes públicos del ecosistema Ethereum son un excelente lugar para comenzar**!
* Pero esto va mucho más allá del propio Ethereum. Los NFT son un ejemplo de una gran cantidad de capital que depende de conceptos de legitimidad. **La industria NFT podría ser de gran ayuda** para los artistas, organizaciones benéficas y otros proveedores de bienes públicos mucho más allá de nuestro propio rincón virtual del mundo, pero **este resultado no está predeterminado; depende de la coordinación y el apoyo activos**.
