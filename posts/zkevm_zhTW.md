[category]: <> (中文)
[date]: <> (2022/08/29)
[title]: <> (不同類型的 ZK-EVM)
[pandoc]: <> ()

*特別感謝 PSE, Polygon Hermez, Zksync, Scroll, Matter Labs and Starkware 團隊參與討論和協助校稿*

近來各家 ZK-EVM 紛紛登場。[Polygon](https://blog.polygon.technology/the-future-is-now-for-ethereum-scaling-introducing-polygon-zkevm/) 的 ZK-EVM 以開源的方式釋出，[ZKSync](https://blog.matter-labs.io/100-days-to-mainnet-6f230893bd73?gi=1bc4e1596b2d) 公佈了 ZKSync 2.0 的規劃，相對晚進場的 [Scroll](https://scroll.mirror.xyz/XQyXDgyxoefag6hcBgGJFz8qrb10rmSU-zUBvY3Q9_A) 也推出了他們的 ZK-EVM。正在開發 ZK-EVM 的，還有 [PSE](https://github.com/privacy-scaling-explorations/zkevm-circuits), [Nicholas Liochon 等人](https://ethresear.ch/t/a-zk-evm-specification/11549)，以及 Starkware 正在開發的 [alpha compiler](https://medium.com/starkware/starknet-alpha-2-4aa116f0ecfc) (能把 EVM 編譯成 Starkware 所開發的 [Cairo](https://starkware.co/cairo/))，族繁不及備載。

上述專案有一個共同的目標：利用 [ZK-SNARK](https://vitalik.ca/general/2021/01/26/snarks.html) 進行密碼學證明，驗證以太坊生態（Ethereum-like）交易的執行。這樣更好驗證以太坊 L1 鏈上的交易與狀態，也建立（接近）與以太等價且擴展性更好的 [ZK-rollups](https://vitalik.ca/general/2021/01/05/rollup.html)。但這幾個專案之間的些微的差異，反映在實用性和速度之間的取捨。本文試著提出分類不同 EVM 的方法，並說明其中的利弊得失。

## 懶人包（以圖表呈現）
![zkevm](https://user-images.githubusercontent.com/85469891/186605516-b6e9a19a-895d-4e36-b7b9-729bb2b198d0.png)

## 第 1 類：等價以太坊（fully Ethereum-equivalent）的 ZK-EVM
第 1 類 ZK-EVM 志在完整、毫無妥協的達到以太坊等價。它沒有改動以太坊生態任何部份的設計以讓證明更簡單，也沒有換掉雜湊的運算（hashes）、狀態樹（state trees）、交易樹（transaction trees）、預編譯的合約（precompiles)，而且再怎麼邊陲的共識邏輯（in-consensus logic），都沒有換掉。

### 優點：完美的相容性
一切的用意在於用現況下的以太鏈—至少，要驗證[執行層](https://hackmd.io/@n0ble/the-merge-terminology)（也因此不包含信標鏈（Beacon Chain）的共識邏輯，但是所有交易執行和智能合約、帳戶的概念，都有涵蓋）。

第 1 類的 ZK-EVM 是以太坊 L1 更有擴展性的最終解。長遠來看，對以太坊的修正，可能會在第 2 類或第 3 類測試之後，引入到正規以太坊。然後，要作架構的重規劃，則會有其複雜之處。

第 1 類的 ZK-EVM 也對 rollups 很理想，因為 rollups 能夠重複利用許多的基礎設施。舉例來說，以太坊的執行端可以被用來生成和處理 rollup blocks（退一步來說，等到[解除質押存款生效後](https://github.com/ethereum/consensus-specs/blob/dev/specs/capella/beacon-chain.md)，這個功能可以被重新用在 rollup 的以太質押存款），所以比如區塊鏈瀏覽器、block production 等工具，都很容易重複利用。

### 缺點：證明者運算時間 （prover time)
以太坊原生不以零知識證明基礎建構，所以有*許多*以太坊固有元件，若要作零知識驗證，需要消耗龐大的運算時間。第 1 類 ZK-EVM 為求完全複製以太坊運作，因此沒有避開低效率的證明流程。就現階段來說，從以太坊既有區塊產生零知識證明，要花上好幾個小時。然而，這個障礙可以透過巧妙的工程設計，大幅提升驗證者平行化產出零知識證明的能力，或建構出 ZK-SNARK ASIC 等方式，緩解其缺點。

### 實例
[PSE](https://github.com/privacy-scaling-explorations/zkevm-circuits) 正在蓋的 ZK-EVM 屬於第 1 類。

## 第 2 類：等價以太坊虛擬機（fully EVM-equivalent）的 ZK-EVM
第 2 類 ZK-EVM 試作到跟 EVM 等價，但又不完全跟以太坊等價。也就是說，他們「內部」跟以太坊一樣，但是從外面看上去會有些差異，尤其是區塊結構（block structure）、[狀態樹（state tree）](https://medium.com/@eiki1212/ethereum-state-trie-architecture-explained-a30237009d4e)等資料結構。

一切的用意在於要跟既有的應用軟體完全相容，但是針對以太坊作一些微調，讓開發更容易、生成證明更快速。

### 優點：等價於虛擬機
第 2 類 ZK-EVM 改動了儲存諸如 Ethereum state 的資料結構。幸運的是，這是都是 EVM 本身無法直接存取的結構，所以在 Ethereum 之上執行的應用程式幾乎都可以在第 2 類 ZK-EVM rollup 上使用。你無法直接利用以太的執行端，但經過微調之後可以，EVM 的除錯工具，和多數的開發設施，也都能照常使用。

也有少數的例外的情況。對於使用[以太坊歷史區塊（historical Ethereum blocks）](https://github.com/aragon/evm-storage-proofs)的雜湊數驗證（Merkle proofs） 來驗證對歷史交易、交易明細、或狀態（claims about historical transactions, receipts, or state）（例如：跨鏈橋有時候會這麼作）就會有不相容的情況發生。如果有 ZK-EVM 用其他雜湊函數取代 Keccak，這些證明會失效。然而，我本來就不建議這樣設計應用程式，因為未來以太坊會引用的改變（例如 [Verkle trees](https://notes.ethereum.org/@vbuterin/verkle_tree_eip)）會讓這些應用程式連在以太坊上都不能使用。比較好的替代方案，是以太坊本身應該要新增[不容易被未來科技淘汰的歷史取用預編譯合約（future-proof history access precompiles）](https://ethresear.ch/t/future-proof-shard-and-history-access-precompiles/9781)。

### 缺點：證明者運算時間稍有改善到仍然很慢
第 2 類 ZK-EVM 的證明者運算速度，比第 1 類更快，主要的原因，是因為不再使用某些以太坊上，對零知識技術毫無意義地不友善的密碼學。尤其，他們可能會改變 Ethereum 的 Keccak 和基於 RLP 的 Merkle Patricia tree，還有或許區塊及交易明細的結構。第 2 類 ZK-EVM 可能會使用不同的雜湊函數，例如 [Poseidon](https://www.poseidon-hash.info/)。也很自然發生的改變是修正狀態樹，以儲存合約碼雜湊值（code hash）和 keccak，免除對於執行`EXTCODEHASH`和`EXTCODECOPY`所需要的雜湊驗證。

這些改動大幅的改善證明者運算時間，但不會完全解決所有問題。證明現況下的EVM的緩慢效率，以及源自於EVM的其他不效率、對zk的不友善，都還留著。舉一個簡單例子：記憶體。因為一個`MLOAD`只能一次讀 32 bytes，包含「沒有對齊的」字節（起始端和終端都不是32的倍數），一個 MLOAD 無法被直接讀取為一個 chunk，它可能需要讀超過兩個連續的 chuck，並作一些運算，合併結果。

### 實例
[Scroll 的 ZK-EVM](https://mirror.xyz/scroll.eth/XQyXDgyxoefag6hcBgGJFz8qrb10rmSU-zUBvY3Q9_A) 以及 [Polygon](https://blog.polygon.technology/the-future-is-now-for-ethereum-scaling-introducing-polygon-zkevm/) Hermez 都屬於第 2 類。然而，兩個專案距離到位都還早。尤其因為還沒加入比較複雜的預編譯，因此，以目前來說，兩個專案都更應該被分類在第 3 類。

## 第 2.5 類：跟以太坊虛擬機結構一樣，但是 gas 訂價例外
想要大幅減少最壞可能的證明者運算時間（worst-case prover times）的方法，就是針對 EVM 內很難的零知識證明運算，大幅提升所需的 gas 訂價。這會牽扯到預編譯、KECCAK 操作碼、以及或許呼叫合約的特殊模式（specific patterns of calling contracts）、存取記憶體（accessing memory）、 儲存空間（storage）或還原（reverting）。

改善 gas 訂價可能會降低開發者工具的相容性，並會讓一些應用程式不能用（break），但是它比起更「深層」的 EVM 改動風險較低。開發者應該要注意，不要在一筆交易中花費超過一個區塊能容納的 gas，也永遠不要把呼叫合約時所需要花用的 gas 寫死（這本來就是會給開發者的標準建議）。

另一個解決資源限制問題的替代方式，是直接對每一個運算可以被呼叫的次數設下硬性的限制。這在電路上更容易實作，但是對 EVM 的安全性假設就沒有那麼合適。這種作法我認為屬於第 3 類而非第 2.5 類。

## 第 3 類：接近以太坊虛擬機等效（almost EVM-equivalent）
第 3 類 ZK-EVM 是*接近* EVM 等效，只有作了退讓，以改善證明者運算時間，並讓開發更容易。

### 優點：更容易實作，證明者運算時間縮短
第 3 類 ZK-EVM 可能會拿掉一些特別難改成 ZK-EVM 的功能。最有可能被拿掉的，就是[預編譯](https://docs.moonbeam.network/builders/pallets-precompiles/precompiles/eth-mainnet/)。此外，各種第 3 類 ZK-EVM，在處理合約程式碼（contract code）、記憶體（memory）或堆疊（stack）上，也有些微差異。

### 缺點：不相容性
第 3 類 ZK-EVM 的目標是跟*多數*的應用程式相容，並且只需要重寫極少部分。即便如此，還是有一些需要重寫的應用程式，因為他們要麼使用了第 3 類 ZK-EVM 拿掉的預編譯功能，或是在特殊情況（edge cases）之下，某些之間虛擬機處理方法不同的相依性問題（dependencies）。

### 實例
Scroll 和 Polygon，雖然它們預期會在未來改善相容性，但目前都屬於第 3 類。Polygon 有一個特別設計，是要驗證自己的語言，zkASM，而他們編譯 ZK-EVM 程式用的是 zkASM。雖然如此，我還是認為這是第 3 類 ZK-EVM。它仍能驗證EVM程式碼，只是換了內部邏輯。

現況下，沒有哪個 ZK-EVM 團隊是*想要成為*第 3 類 ZK-EVM。第 3 類只是一個過渡期，正在等待預編譯功能完成，再換到第 2.5 類。但是在未來，第 1 或 2 類可能會加入 ZK-SNARK 友善的預編譯，自發的變成第 3 類，讓證明者運算時間和 gas 都降低。

## 第 4 類（等價高階語言（high-level-language equivalent））
第 4 類把（例如：[Solidity](https://docs.soliditylang.org/en/v0.8.15/)、[Vyper](https://vyper.readthedocs.io/en/stable/)，或其他這兩種語言都會編譯成為的中間語言）然後把*高階語言*編譯成其他有特別設計過、對 ZK-SNARK 友善的語言。

### 優點：證明者所需運算時間非常短
只要從高階語言就有利用零知識證明，而非等到執行階段的各個步驟，才開始用在 EVM 上，就可以省掉*很多*麻煩。

我雖然只用了一句話描述這個優點（但下面列出那麼多相容性的缺點），但我並不是要說第 4 類沒什麼優點。這是個非常大的優點！直接從高階語言編譯真的可以大幅降低成本，也因為參與證明的門檻變低，所以更去中心化。

### 缺點：相容性低
通常一個「一般」的，由 Vyper 或 Solidity 寫成的應用程式可以編譯然後就能用了，但是有很多應用程式沒辦法那麼「一般」，而且理由很重要：

- 因為在 CREATE2 合約地址要看 bytecode 決定，所以 **「第 4 類系統中的合約地址」與「EVM 的合約地址」不一定相同**。這會造成很多應用程式不能使用，例如倚賴尚未部署的「反事實合約（counterfactual contracts）」的系統、ERC-4337 錢包、[EIP-2470 singletons](https://eips.ethereum.org/EIPS/eip-2470)、等應用程式。 
- **手刻的 EVM bytecode 更難被利用**。許多程式某些部分會用手刻 EVM bytecode 來提高效率。第 4 類的系統就不支援。雖然有些方法可以實作有限的 EVM bytecode support 來滿足這些情況，不一定要直上第 3 類 ZK-EVM。
- **很多除錯的基礎設施無法被直接利用**，因為這些基礎設施只能跑在 EVM bytecode 上。話雖如此，有很多來自傳統高階或中階語言（例如 LLVM）的除錯工具可以用來緩解這個缺點。

以上都是工程師需要留意的問題。

### 實例
[ZKSync](https://blog.matter-labs.io/100-days-to-mainnet-6f230893bd73) 是第 4 類系統，雖然隨著時間他們可能會改善對 EVM bytecode 的相容性。Nethermind 的 [Warp](https://github.com/NethermindEth/warp) 專案正在蓋一個能把 Solidity 編譯成 Starkware 的 Cairo 語言的編譯器，這會因此把 StarkNet 在實然上變成第 4 類系統。

## ZK-EVM 類型的未來展望
以上不同類型之間沒有誰更「好」或更「壞」，而是取捨的不同：越靠近 第 1 類的類型跟既有的基礎設施相容性更高，但是更慢。越靠近第 4 類的類型相容性比較差，但是速度更快。通常來說，對整個生態比較好的作法，就是每種不同類型，都有人研究。

靠近第 4 類的 ZK-EVM 類型，也可以隨著時間，再慢慢改成靠近第 1 類的類型。反之亦然。舉例來說：
- ZK-EVM 可以先跳過很難用零知識證明的功能，當第 3 類就好。之後，再慢慢把功能加上去，逐漸轉成第 2 類。
- ZK-EVM 也可以先當第 2 類，然後之後提供在以太坊完全等效的環境中，或是證明速度更快、改動過的狀態樹，變成第 2 和第 1 類的綜合體。Scroll 正在考慮用這個策略發展。
- 原本是第 4 類的系統，也可以慢慢加上處理 EVM opcode 的能力（雖然開發者仍然被鼓勵直接從高階語言編譯，以節省手續費和改善證明者運算所需時間）。
- 假設以太坊本身變得更零知識友善，原本是第 2 類或第 3 類開始的ZK-EVM，就會變成第 1 類。
- 如果在第 1 類或第 2 類 ZK-EVM 預編譯元件（precompiles），這樣就能使其變成第 3 類 ZK-EVM。這些預編譯元件的驗證效率很高，是由一種 ZK-SNARK 友善的語言撰寫而成。這樣開發者就能在以太坊的相容性和速度之間能作選擇。這種 ZK-EVM 屬於第 3 類，因為它犧牲了完美以太坊等價性，但是從實用性的角度來看，它比起第 1 類或第 2 類有更多好處。主要的缺失在於某些開發者工具不支援 ZK-EVM 客製化的預編譯，然而，這可以被改善：透過開發者手動指定設定檔，開發者工具可以支援將預編譯元件轉換回同等功能的 EVM 程式碼，這樣就能適用於所有環境。

我個人的希望，是隨著時間，ZK-EVM 技術的進步，以及以太坊本身對 ZK-SNARK 的設計更友善之後，所有的ZK-EVM能漸漸發展為第 1 類。在這樣的未來，我們會有好幾個能夠同時作為 ZK-rollup 以及驗證以太鏈本身的 ZK-EVM。理論上，沒有必要將以太坊標準化為只能供一種 ZK-EVM 使用的 L1。要有不同的客戶端使用不同的證明方式，我們才能收穫冗餘實作（code redundancy）的好處。

然而，要花一些時間，才會抵達這樣的未來。在這條路上，將會看到很多擴展以太坊、以太坊 ZK-rollups 技術的日新月異。
