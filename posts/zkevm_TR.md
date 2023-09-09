[category]: <> (Türkçe)
[date]: <> (2022/08/04)
[title]: <> (Farklı ZK-EVM Türleri)
[pandoc]: <> ()

_PSE, Polygon Hermez, Zksync, Scroll, Matter Labs ve Starkware ekiplerine münazara ve inceleme, çeviri için [eren](https://twitter.com/notereneth)'e özel teşekkürler._

Son zamanlarda birçok "ZK-EVM" projesinin çarpıcı duyurular yaptığı görüldü. [Polygon](https://polygon.technology/blog/the-future-is-now-for-ethereum-scaling-introducing-polygon-zkevm) ZK-EVM projesini açık kaynaklı hale getirdi, [ZKSync](https://blog.matter-labs.io/100-days-to-mainnet-6f230893bd73?gi=e44b181330f2), ZKSync 2.0 için planlarını yayınladı ve görece yeni bir oyuncu olan [Scroll](https://mirror.xyz/scroll.eth/XQyXDgyxoefag6hcBgGJFz8qrb10rmSU-zUBvY3Q9_A), ZK-EVM'lerini duyurdu. Ayrıca [Privacy and Scaling Explorations](https://github.com/privacy-scaling-explorations/zkevm-circuits) ekibinin, [Nicolas Liochon ve arkadaşlarının](https://ethresear.ch/t/a-zk-evm-specification/11549) ekibinin, EVM'den Starkware'ın ZK-dostu dili [Cairo](https://starkware.co/cairo/)'ya yönelik bir [alfa derleyici](https://medium.com/starkware/starknet-alpha-2-4aa116f0ecfc) ve kaçırdığım en az birkaç kişinin daha kesinlikle devam eden çabaları da var.

Tüm bu projelerin temel hedefi aynı: [ZK-SNARK](https://vitalik.ca/general/2021/01/26/snarks.html) teknolojisini kullanarak Ethereum-benzeri işlemlerin kriptografik yürütülme kanıtlarını oluşturmak, bu kanıtları Ethereum zincirini doğrulamayı çok daha kolay hale getirmek veya Ethereum'un sunduğuna (neredeyse) eşdeğer ancak çok daha ölçeklenebilir olan [ZK-rollup'lar](https://vitalik.ca/general/2021/01/05/rollup.html) inşa etmek için kullanmaktır. Ancak bu projeler arasında ince farklılıklar bulunmakta ve bunlar pratiklik ile hız arasındaki değiş tokuşları nasıl yaptıklarını belirlemektedir. Bu yazı, EVM denkliğinin farklı "tiplerinin" bir taksonomisini ve her bir tipe ulaşmaya çalışmanın fayda ve maliyetlerinin neler olduğunu açıklamaya çalışacaktır.

## Genel Bakış (grafik biçiminde)

![](../../../../images/zkevm/chart_tr.png)

## Tip 1 (tamamen Ethereum-dengi)

Tip 1 ZK-EVM'ler, tamamen ve ödün vermeden Ethereum-dengi olmaya çalışırlar. Kanıtları oluşturmayı kolaylaştırmak için Ethereum sisteminin herhangi bir parçasını değiştirmezler. Ne kadar çevresel olursa olsun hash'leri, state tree'leri, transaction tree'leri, ön-derlemeleri veya başka herhangi bir konsensüse dahil mantığı değiştirmezler.

#### <span style="color:#008800">Avantaj: mükemmel uyumluluk</span>

Hedef, Ethereum bloklarını bugünkü haliyle doğrulayabilmektir - veya en azından [yürütme-katmanı tarafını](https://hackmd.io/@n0ble/the-merge-terminology) doğrulayabilmektir (bu nedenle, beacon zinciri konsensüs mantığı dahil değil, ancak tüm işlem yürütme ve akıllı kontrat ve hesap mantığı dahil).

Tip 1 ZK-EVM'ler, Ethereum katman 1'inin daha ölçeklenebilir hale gelmesini sağlamak için sonunda ihtiyacımız olan şeydir. Uzun vadede, Tip 2 veya Tip 3 ZK-EVM'lerde test edilmiş Ethereum'a yapılan modifikasyonlar, Ethereum'a uygun bir şekilde tanıtılabilir, ancak böyle bir yeniden tasarlama kendi komplekslikleri ile gelir.

Tip 1 ZK-EVM'ler aynı zamanda rollup'lar için idealdir, çünkü rollup'ların birçok altyapıyı tekrar kullanmalarına izin verirler. Örneğin, Ethereum execution istemcileri, rollup blokları oluşturmak ve işlemek için olduğu gibi kullanılabilir (veya en azından [para çekme işlemleri implement edildiğinde](https://github.com/ethereum/consensus-specs/blob/dev/specs/capella/beacon-chain.md) ve bu işlevsellik, rollup'a ETH yatırılmasını desteklemek için tekrar kullanılabilir), bu nedenle blok gezginleri, blok üretimi vb. gibi araçlar çok kolay bir şekilde tekrar kullanılabilir.

#### <span style="color:#cc0000">Dezavantaj: kanıtlayıcı zamanı</span>

Ethereum, başlangıçta ZK-dostu olacak şekilde tasarlanmamıştı, bu nedenle Ethereum protokolünün, ZK-kanıtlama için büyük miktarda hesaplama gerektiren _birçok_ parçası var. Tip 1, Ethereum'u tam olarak kopyalamayı amaçlıyor, o yüzden bu verimsizlikleri hafifletebilecek bir yola sahip değil. Şu anda, Ethereum bloklarının kanıtlarının üretilmesi saatler sürüyor. Bu durum, kanıtlayıcıyı büyük ölçüde paralelleştirmeye yönelik zekice mühendislikle veya uzun vadede ZK-SNARK ASIC'ler ile hafifletilebilir.

#### <span style="color:#880088">Bunu kim inşa ediyor?</span>

[ZK-EVM Topluluk Sürümü](https://github.com/privacy-scaling-explorations/zkevm-specs) ([Privacy and Scaling Explorations](https://github.com/privacy-scaling-explorations/), [Scroll ekibi](https://scroll.io/), [Taiko](https://taiko.xyz/) ve diğerlerinin topluluk katkılarıyla başlatılan) Tier 1 bir ZK-EVM'dir.

## Tip 2 (tamamen EVM-dengi)

Tip 2 ZK-EVM'ler tam anlamıyla EVM-dengi olmaya çalışır, ancak tam olarak Ethereum-dengi değildirler. Yani, "içeriden" bakıldığında tam olarak Ethereum gibi görünürler, ancak dışarıda bazı farklılıklar, özellikle blok yapısı ve [state tree](https://medium.com/@eiki1212/ethereum-state-trie-architecture-explained-a30237009d4e) gibi veri yapılarında bulunur.

Hedef, mevcut uygulamalarla tamamen uyumlu olmak, ancak geliştirmeyi kolaylaştırmak ve kanıt oluşturmayı daha hızlı hale getirmek için Ethereum'da bazı küçük değişiklikler yapmaktır.

#### <span style="color:#008800">Avantaj: VM seviyesinde mükemmel denklik</span>

Tip 2 ZK-EVM'ler, Ethereum durumu gibi verileri tutan veri yapılarına değişiklikler yaparlar. Neyse ki, bunlar EVM'in doğrudan erişemeyeceği yapılar olduğundan, Ethereum üzerinde çalışan uygulamalar neredeyse her zaman Tip 2 ZK-EVM rollup'larında da çalışmaya devam eder. Ethereum execution istemcilerini olduğu gibi kullanamazsınız, ancak bazı değişikliklerle kullanabilirsiniz ve hala EVM hata ayıklama araçlarını ve çoğu diğer geliştirici altyapısını kullanabilirsiniz.

Az sayıda istisna vardır. Örneğin geçmiş işlemler, makbuzlar veya durum hakkındaki iddiaları doğrulamak için [geçmiş Ethereum bloklarının](https://github.com/aragon/evm-storage-proofs) Merkle kanıtlarını doğrulayan uygulamalarda bir uyumsuzluk ortaya çıkar (örn. köprüler bazen bunu yapar). Keccak'ı farklı bir hash fonksiyonuyla değiştiren bir ZK-EVM, bu kanıtları bozabilir. Bununla birlikte, zaten genellikle uygulamaların bu şekilde inşa edilmesini önermem, çünkü gelecek Ethereum değişiklikleri (örn. [Verkle ağaçları](https://notes.ethereum.org/@vbuterin/verkle_tree_eip)) bu tür uygulamaları Ethereum'un kendisinin üzerinde bile bozacaktır. Daha iyi bir alternatif, Ethereum'un [geleceğe-hazır geçmiş erişim ön-derlemelerini](https://ethresear.ch/t/future-proof-shard-and-history-access-precompiles/9781) eklemesidir. 

#### <span style="color:#cc0000">Dezavantaj: Gelişmiş ancak hala yavaş kanıtlayıcı süresi</span>

Tip 2 ZK-EVM'ler, Ethereum yığınının gereksiz derecede karmaşık ve ZK dostu olmayan kriptografiye dayanan kısımlarını kaldırarak Tip 1'den daha hızlı kanıtlayıcı süreleri sağlar. Özellikle Ethereum'un Keccak'ını ve RLP tabanlı Merkle Patricia ağacını ve belki de blok ve makbuz yapılarını değiştirebilirler. Tip 2 ZK-EVM'ler, farklı bir hash fonksiyonu kullanabilirler, örneğin [Poseidon](https://www.poseidon-hash.info/). Başka bir doğal değişiklik, state tree'yi kod hash'ini ve keccak'ı depolayacak şekilde değiştirerek `EXTCODEHASH` ve `EXTCODECOPY` opcode'larını işlemek için hash doğrulama ihtiyacını ortadan kaldırmaktır.

Bu değişiklikler kanıtlayıcı sürelerini önemli ölçüde iyileştirir ancak her sorunu çözmez. EVM'i olduğu gibi kanıtlama zorunluluğundan kaynaklanan yavaşlık, EVM'in doğasında bulunan tüm verimsizlikler ve ZK dostu olmama durumuyla birlikte hala devam ediyor. Bunun basit bir örneği bellektir: Bir `MLOAD`, "hizalanmamış" parçalar (başlangıç ve bitişin 32'nin katı olmadığı) dahil olmak üzere herhangi bir 32 byte'ı okuyabildiğinden, bir MLOAD basitçe bir parçayı okuyormuş gibi yorumlanamaz; bunun yerine, sonucu birleştirmek için iki ardışık parçanın okunmasını ve bit işlemleri gerçekleştirilmesini gerektirebilir.

#### <span style="color:#880088">Bunu kim inşa ediyor?</span>

[Scroll'un ZK-EVM](https://mirror.xyz/scroll.eth/XQyXDgyxoefag6hcBgGJFz8qrb10rmSU-zUBvY3Q9_A) projesi, [Polygon Hermez](https://blog.polygon.technology/the-future-is-now-for-ethereum-scaling-introducing-polygon-zkevm) gibi Tip 2 ZK-EVM'e doğru ilerliyor. Bununla birlikte, her iki proje de henüz tam olarak oraya ulaşmadı; özellikle daha karmaşık ön-derlemelerin çoğu henüz implement edilmedi. Dolayısıyla şu anda her iki projenin de [Tip 3](https://vitalik.ca/general/2022/08/04/zkevm.html#type-3-almost-evm-equivalent). olarak değerlendirilmesi daha iyi.

## Tip 2.5 (EVM-dengi, gaz ücretleri hariç)

<span style="color:#008800">En kötü durumda kanıt sürelerini önemli ölçüde iyileştirmenin</span> bir yolu, EVM'deki ZK-kanıtlaması çok zor olan belirli işlemlerin gaz ücretlerini büyük ölçüde artırmaktır. Bu, ön-derlemeleri, KECCAK opcode'unu ve muhtemelen belirli kontrat çağırma kalıplarını veya belleğe/depolamaya erişmeyi veya geri döndürmeyi (revert) içerebilir.

Gaz ücretlerini değiştirmek, <span style="color:#cc0000">geliştirici araçlarının uyumluluğunu azaltabilir ve birkaç uygulamayı bozabilir</span>, ancak genellikle "derin" EVM değişikliklerinden daha az riskli olarak kabul edilir. Geliştiriciler, bir işlemde bir bloğa sığmayacak kadar fazla gaz gerektirmemeye ve hard-coded gaz miktarlarıyla çağrılar yapmamaya dikkat etmelidir (bu zaten geliştiriciler için uzun süredir standart bir öneridir).

Kaynak sınırlamalarını yönetmenin alternatif bir yolu, her operasyonun kaç kez çağrılabileceği konusunda katı sınırlar belirlemektir. Bunun devrelerde uygulanması daha kolaydır, ancak EVM güvenlik varsayımlarıyla daha az uyumludur. Ben buna Tip 2.5 yerine Tip 3 yaklaşımı derim.

## Tip 3 (neredeyse EVM-dengi)

Tip 3 ZK-EVM'ler _neredeyse_ EVM-dengidir, ancak kanıt sürelerini daha da iyileştirmek ve EVM'i geliştirmeyi kolaylaştırmak için tam denklikten ödün verirler.

#### <span style="color:#008800">Avantaj: Daha kolay inşa edilir ve daha hızlı kanıtlayıcı süreleri sunar.</span>

Tip 3 ZK-EVM'ler, ZK-EVM implementasyonunda uygulanması son derece zor olan birkaç özelliği kaldırabilir. Genellikle [ön-derlemeler](https://docs.moonbeam.network/builders/build/canonical-contracts/precompiles/eth-mainnet/) bu listede en üsttedir. Ek olarak, Tip 3 ZK-EVM'lerin bazen kontrat kodunu, belleği veya yığını nasıl ele aldıkları konusunda da küçük farklılıkları vardır.

#### <span style="color:#cc0000">Dezavantaj: Daha fazla uyumsuzluk.</span>

Tip 3 ZK-EVM'in hedefi, çoğu uygulama ile uyumlu olup geri kalanları için sadece minimal yeniden yazım gerektirmektir. Bununla beraber, Tip 3 ZK-EVM'in kaldırdığı ön-derlemeleri kullanan veya VM'lerin farklı işlediği ince ayrıntılardaki bağımlılıklardan dolayı yeniden yazılması gereken bazı uygulamalar olacaktır.

#### <span style="color:#880088">Bunu kim inşa ediyor?</span>

Scroll ve Polygon'un her ikisi de mevcut formlarıyla Tip 3'tür, ancak zamanla uyumluluğu artırmaları bekleniyor. Polygon, [zkASM](https://github.com/0xPolygonHermez/zkevm-doc/blob/main/mkdocs/docs/zkEVM/zkASM/Introduction.md) denen kendi dahili dilini ZK-doğruladıkları ve zkASM implementasyonunu kullanarak ZK-EVM kodunu yorumladıkları benzersiz bir tasarıma sahiptir. Bu implementasyon detayına rağmen yine de buna hakiki Tip 3 ZK-EVM diyeceğim; çünkü hala EVM kodunu doğrulayabiliyor, sadece bunu yapmak için yalnızca farklı bir dahili mantık kullanır.

Bugün, hiçbir ZK-EVM ekibi Tip 3 olmak _istemez_; Tip 3, ön-derlemelerin eklenmesi gibi karmaşık işler bitene ve proje Tip 2.5'a geçinceye kadar sadece bir geçiş aşamasıdır. Ancak gelecekte Tip 1 veya Tip 2 ZK-EVM'ler, düşük kanıtlayıcı süreleri ve gaz ücretleri ile geliştiriciler için işlevsellik sağlayan _yeni_ ZK-SNARK dostu ön-derlemeler ekleyerek gönüllü olarak Tip 3 ZK-EVM'lere dönüşebilirler.

## Tip 4 (yüksek-seviye-dil denkliği)

Bir Tip 4 sistemi, yüksek seviyeli bir dilde (örn. [Solidity](https://docs.soliditylang.org/en/v0.8.15/), [Vyper](https://vyper.readthedocs.io/en/stable/) veya her ikisinin de derlediği bir ara dilde) yazılmış akıllı kontrat kaynak kodunu alarak ve bunu açıkça ZK-SNARK dostu olacak şekilde tasarlanmış bir dilde derleyerek çalışır.

#### <span style="color:#008800">Avantaj: Çok hızlı kanıtlayıcı süreleri</span>

Her EVM yürütülme işleminin tüm farklı bölümlerini ZK-kanıtlamayarak ve doğrudan yüksek seviye koddan başlayarak önlenebilecek _çok sayıda_ ek yük vardır.

Bu avantajı bu yazımda sadece bir cümleyle açıklıyorum (aşağıdaki, uyumlulukla ilgili dezavantajlar için olan büyük listeyle karşılaştırıldığında), ancak bu bir değer yargısı olarak yorumlanmamalıdır! Yüksek seviyeli dillerden doğrudan derlemek gerçekten maliyetleri büyük ölçüde azaltabilir ve bir kanıtlayıcı olmayı daha kolay hale getirerek merkeziyetsizleşmeye yardımcı olabilir.

#### <span style="color:#cc0000">Dezavantaj: Daha fazla uyumsuzluk</span>

Vyper veya Solidity ile yazılmış "normal" bir uygulama derlenebilir ve "sadece çalışır", ancak pek çok uygulamanın "normal" olmadığı bazı önemli yollar vardır:

 * **Kontratlar Tip 4 bir sistemde EVM'de olduğu gibi aynı adreslere sahip olmayabilir**, çünkü CREATE2 kontrat adresleri tamı tamına bytecode'a bağlıdır. Bu, henüz deploy edilmemiş "Karşıolgusal kontratlara", ERC-4337 cüzdanlara, [EIP-2470 tekillerine](https://eips.ethereum.org/EIPS/eip-2470) ve birçok diğer uygulamaya dayanan uygulamaları bozar.
 * **Elle yazılmış EVM bytecode** kullanmak daha zordur. Birçok uygulama, verimlilik için bazı bölümlerinde elle yazılmış EVM bytecode kullanır. Tip 4 sistemleri bunu desteklemeyebilir, ancak bu kullanım durumlarını karşılamak için tam anlamıyla bir Tip 3 ZK-EVM olmanın çabasına girmeden sınırlı EVM bytecode desteği uygulamanın yolları vardır.
 * **Birçok hata ayıklama altyapısı taşınamaz**, çünkü bu tür altyapılar EVM bytecode'u üzerinden çalışır.  Bununla birlikte, bu dezavantaj "geleneksel" yüksek seviyeli veya ara diller (örn. LLVM) tarafından sunulan hata ayıklama altyapısına _daha fazla_ erişim ile hafifletilir.

Geliştiriciler bu konuları akıllarında bulundurmalıdır.

#### <span style="color:#880088">Bunu kim inşa ediyor?</span>

[ZKSync](https://matterlabs.medium.com/100-days-to-mainnet-6f230893bd73) bir Tip 4 sistemidir ancak zamanla EVM bytecode'u için uyumluluk ekleyebilir. Nethermind'ın [Warp](https://github.com/NethermindEth/warp) projesi, Solidity'den Starkware'in Cairo'suna derleyici inşa ediyor ve bu, StarkNet'i fiili bir Tip 4 sistemine dönüştürecektir.

## The future of ZK-EVM types

Tipler diğer tiplerden açıkça "daha iyi" veya "daha kötü" değildir. Aksine, bunlar takas alanındaki farklı noktalardır: daha düşük-numaralı tipler mevcut altyapı ile daha uyumludur, ancak daha yavaştır ve daha yüksek-numaralı tipler mevcut altyapı ile daha az uyumludur, ancak daha hızlıdır. Genel olarak bu tiplerin tamamının keşfedilmesi alan açısından sağlıklıdır.

Ek olarak, ZK-EVM projeleri kolaylıkla yüksek-numaralı tiplerden başlayabilir ve zamanla daha düşük-numaralı tiplere atlayabilir (veya tam tersi). Örneğin:

* Bir ZK-EVM, özellikle ZK-kanıtlanması zor olan bazı özellikleri dahil etmemeye karar vererek Tip 3 olarak başlayabilir. Daha sonra zamanla bu özellikleri ekleyip Tip 2'ye geçebilirler.
* Bir ZK-EVM, Tip 2 olarak başlayabilir ve daha sonra, tamamen Ethereum'a uyumluluk modu ile veya daha hızlı kanıtlanabilen değiştirilmiş bir state tree ile çalışma olanağı sunarak hibrit bir Tip 2 / Tip 1 ZK-EVM haline gelebilir. Scroll bu yönde ilerlemeyi düşünüyor.
* Tip 4 olarak başlayan sistem, daha sonra EVM kodunu işleme yeteneğinin eklenmesiyle zamanla Tip 3 haline gelebilir (yine de geliştiriciler ücretleri ve kanıt sürelerini azaltmak için yüksek seviyeli dillerle doğrudan derlemeye yönelecektir).
* Tip 2 veya Tip 3 ZK-EVM, Ethereum'un daha ZK dostu olma çabasıyla modifikasyonlarını benimsemesi durumunda Tip 1 ZK-EVM haline gelebilir.
* Bir Tip 1 veya Tip 2 ZK-EVM, oldukça ZK-SNARK dostu bir dilde kodu doğrulamak için bir ön-derleme ekleyerek Tip 3 ZK-EVM haline gelebilir. Bu, geliştiricilere Ethereum uyumluluğu ve hız arasında bir seçenek sunar. Bu Tip 3 olacaktır çünkü mükemmel EVM-denkliğini bozar, ancak pratik amaçlar ve niyetler için Tip 1 ve 2'nin birçok avantajına sahip olur. Ana dezavantaj, bazı geliştirici araçlarının ZK-EVM'in özel ön-derlemelerini anlamayabileceğidir, ancak bu sorun düzeltilebilir: geliştirici araçları, ön-derlemenin EVM kodu dengi bir implementasyonunu içeren bir yapılandırma formatını destekleyerek evrensel ön-derleme desteği ekleyebilir.

Şahsen, benim umudum ZK-EVM'lerdeki iyileştirmeler ve Ethereum'un kendisini daha ZK-SNARK dostu hale getirecek iyileştirmelerin bir araya gelmesiyle her şeyin zamanla Tip 1 haline gelmesidir. Böyle bir gelecekte, hem ZK rollup'ları hem de Ethereum zincirinin kendisini doğrulamak için kullanılabilecek birden fazla ZK-EVM implementasyonuna sahip olurduk. Teorik olarak Ethereum'un L1 kullanımı için tek bir ZK-EVM implementasyonu üzerinde standartlaşmasına gerek yoktur; farklı istemciler farklı kanıtlar kullanabilir, bu nedenle kod fazlalığından yararlanmaya devam edelim.

Ancak böyle bir geleceğe ulaşmamız oldukça zaman alacak. Bu esnada, Ethereum ve Ethereum tabanlı ZK-rollup'larını ölçeklendirmenin farklı yollarında birçok inovasyon göreceğiz.
