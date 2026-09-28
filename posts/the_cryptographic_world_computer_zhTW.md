[category]: <> (Translations)
[date]: <> (2026/09/27)
[title]: <> (密碼學世界電腦)

我們把以太坊稱為「一條區塊鏈」，彷彿它本質上與中本聰在 2009 年創造的比特幣是同一種技術。在很多方面確實如此；在某些方面，就連按照 [Strawmap](https://strawmap.org/) 路線[正在打造](https://leanroadmap.org/)的未來「精簡以太坊」（lean Ethereum），也保留了區塊鏈的核心特徵。但與此同時，這項技術在過去十五年間已有長足的演進，而且在接下來的三年還將進一步演進——以至於我們可以合理地說，以太坊正在邁向的是一種性質上截然不同的系統。

今天的以太坊擁有通用計算、權益證明、使用零知識證明的鏈上應用，以及提供擴展與隱私的 L2。明天的以太坊則將擁有：可在極致規模與完全通用之間自由調節的計算、多種形式的多方區塊建構、經過高度最佳化的權益證明，以及內建於協議、在基礎層扮演關鍵角色的零知識證明。

本文將從技術的角度，以及從使用者可以期待獲得哪些特性的角度，逐一介紹 2010 年的區塊鏈與 2030 年的區塊鏈之間一些最重要的根本差異。

首先，讓我們逐節瀏覽原始的比特幣白皮書，看看它與以太坊相比如何——分別是 2015 年（<mark style="background-color: rgb(255, 255, 0)">黃色</mark>）、2025 年（<mark style="background-color: rgb(0, 255, 0)">綠色</mark>）和 2030 年（<mark style="background-color: rgb(159, 197, 232)">藍色</mark>）的以太坊。

<figure data-type="resizable-media" data-align="center">
<img src="../../../../images/the_cryptographic_world_computer/whitepaper_2_zhTW.png" width="1235" alt="比特幣白皮書第 2 節「交易」，附以太坊的對照註解" />
</figure>

<figure data-type="resizable-media" data-align="center">
<img src="../../../../images/the_cryptographic_world_computer/whitepaper_4_zhTW.png" width="1235" alt="比特幣白皮書第 4 節「工作量證明」，附以太坊的對照註解" />
</figure>

<figure data-type="resizable-media" data-align="center">
<img src="../../../../images/the_cryptographic_world_computer/whitepaper_5_zhTW.png" width="1326" alt="比特幣白皮書第 5 節「網路」，附以太坊的對照註解" />
</figure>

<figure data-type="resizable-media" data-align="center">
<img src="../../../../images/the_cryptographic_world_computer/whitepaper_7_zhTW.png" width="1238" alt="比特幣白皮書第 7 節「回收磁碟空間」，附以太坊的對照註解" />
</figure>

<figure data-type="resizable-media" data-align="center">
<img src="../../../../images/the_cryptographic_world_computer/whitepaper_10_zhTW.png" width="1344" alt="比特幣白皮書第 10 節「隱私」，附以太坊的對照註解" />
</figure>

基本上每一節都有重大變化。為了更精簡，我們把它整理成一張表：

<figure data-type="resizable-media" data-align="center">
<svg xmlns="http://www.w3.org/2000/svg" width="600" height="636" viewBox="0 0 600 636" font-family="Helvetica, Arial, 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif" lang="zh-Hant" class="svg-scope-1qzhbm">
<style>.svg-scope-1qzhbm text { font-size:10px; fill:#1a1a1a }
.svg-scope-1qzhbm .cat { font-weight:bold }
.svg-scope-1qzhbm .hdr { font-size:11px; font-weight:bold }
.svg-scope-1qzhbm .dim { fill:#444 }
.svg-scope-1qzhbm line { stroke:#999; stroke-width:1 }</style>
<rect width="600" height="636" fill="#fff"/>
<rect x="0" y="0" width="600" height="24" fill="#e8e8ee"/>
<text x="10" y="16" class="hdr" font-size="11" fill="#1a1a1a" font-weight="bold">主題</text>
<text x="100" y="16" class="hdr" font-size="11" fill="#1a1a1a" font-weight="bold">2010 年的策略</text>
<text x="354" y="16" class="hdr" font-size="11" fill="#1a1a1a" font-weight="bold">2030 年的策略</text>
<line x1="0" y1="0" x2="600" y2="0" stroke="#999" stroke-width="1"/>
<line x1="0" y1="24" x2="600" y2="24" stroke="#999" stroke-width="1"/>
<line x1="0" y1="72" x2="600" y2="72" stroke="#999" stroke-width="1"/>
<line x1="0" y1="120" x2="600" y2="120" stroke="#999" stroke-width="1"/>
<line x1="0" y1="168" x2="600" y2="168" stroke="#999" stroke-width="1"/>
<line x1="0" y1="258" x2="600" y2="258" stroke="#999" stroke-width="1"/>
<line x1="0" y1="319" x2="600" y2="319" stroke="#999" stroke-width="1"/>
<line x1="0" y1="393" x2="600" y2="393" stroke="#999" stroke-width="1"/>
<line x1="0" y1="441" x2="600" y2="441" stroke="#999" stroke-width="1"/>
<line x1="0" y1="476" x2="600" y2="476" stroke="#999" stroke-width="1"/>
<line x1="0" y1="511" x2="600" y2="511" stroke="#999" stroke-width="1"/>
<line x1="0" y1="588" x2="600" y2="588" stroke="#999" stroke-width="1"/>
<line x1="0" y1="636" x2="600" y2="636" stroke="#999" stroke-width="1"/>
<line x1="0" y1="0" x2="0" y2="636" stroke="#999" stroke-width="1"/>
<line x1="92" y1="0" x2="92" y2="636" stroke="#999" stroke-width="1"/>
<line x1="346" y1="0" x2="346" y2="636" stroke="#999" stroke-width="1"/>
<line x1="600" y1="0" x2="599" y2="636" stroke="#999" stroke-width="1"/>
<text x="10" y="39" class="cat" font-size="10" fill="#1a1a1a" font-weight="bold">如何確認交易</text>
<text x="10" y="52" class="cat" font-size="10" fill="#1a1a1a" font-weight="bold">已獲授權？</text>
<text x="100" y="39" font-size="10" fill="#1a1a1a">簽章</text>
<text x="354" y="39" font-size="10" fill="#1a1a1a">有時是抗量子簽章（或多個），</text>
<text x="354" y="52" font-size="10" fill="#1a1a1a">有時是零知識證明</text>
<text x="10" y="87" class="cat" font-size="10" fill="#1a1a1a" font-weight="bold">如何辨識</text>
<text x="10" y="100" class="cat" font-size="10" fill="#1a1a1a" font-weight="bold">正統鏈？</text>
<text x="100" y="87" font-size="10" fill="#1a1a1a">PoW</text>
<text x="354" y="87" font-size="10" fill="#1a1a1a">PoS，具備數個時隙內的最終確定性與可用鏈</text>
<text x="10" y="135" class="cat" font-size="10" fill="#1a1a1a" font-weight="bold">如何驗證</text>
<text x="10" y="148" class="cat" font-size="10" fill="#1a1a1a" font-weight="bold">區塊？</text>
<text x="100" y="135" font-size="10" fill="#1a1a1a">完整重新下載並重新計算</text>
<text x="354" y="135" font-size="10" fill="#1a1a1a">SNARK 驗證 + 以 PeerDAS 確保資料可用性</text>
<text x="10" y="183" class="cat" font-size="10" fill="#1a1a1a" font-weight="bold">交易被納入</text>
<text x="10" y="196" class="cat" font-size="10" fill="#1a1a1a" font-weight="bold">區塊的流程</text>
<text x="10" y="209" class="cat" font-size="10" fill="#1a1a1a" font-weight="bold">是怎樣的？</text>
<text x="100" y="183" font-size="10" fill="#1a1a1a">使用者 → 記憶池 → 礦工 → 區塊</text>
<text x="354" y="183" font-size="10" fill="#1a1a1a">使用者 → 具強隱私性的記憶池 →</text>
<text x="354" y="196" font-size="10" fill="#1a1a1a">FOCIL 參與者或建構者 → 區塊</text>
<text x="362" y="225" class="dim" font-size="10" fill="#444">簽章／證明會被提早剝離，</text>
<text x="362" y="238" class="dim" font-size="10" fill="#444">並先由記憶池節點、再由建構者進行聚合</text>
<text x="10" y="273" class="cat" font-size="10" fill="#1a1a1a" font-weight="bold">計算的結構</text>
<text x="10" y="286" class="cat" font-size="10" fill="#1a1a1a" font-weight="bold">是怎樣的？</text>
<text x="100" y="273" font-size="10" fill="#1a1a1a">線性／序列</text>
<text x="354" y="273" font-size="10" fill="#1a1a1a">平行：</text>
<text x="362" y="286" class="dim" font-size="10" fill="#444">簽章／證明在記憶池內平行處理</text>
<text x="362" y="299" class="dim" font-size="10" fill="#444">Gas 規則激勵適合平行化的工作流程</text>
<text x="10" y="334" class="cat" font-size="10" fill="#1a1a1a" font-weight="bold">客戶端節點</text>
<text x="10" y="347" class="cat" font-size="10" fill="#1a1a1a" font-weight="bold">如何節省空間</text>
<text x="100" y="334" font-size="10" fill="#1a1a1a">修剪舊的歷史資料</text>
<text x="354" y="334" font-size="10" fill="#1a1a1a">只儲存一小部分歷史</text>
<text x="354" y="347" font-size="10" fill="#1a1a1a">分散式的歷史與狀態儲存</text>
<text x="354" y="360" font-size="10" fill="#1a1a1a">通常不需要儲存樹的內部節點</text>
<text x="354" y="373" font-size="10" fill="#1a1a1a">以不同格式儲存不同物件（資料庫、平面檔案等）</text>
<text x="10" y="408" class="cat" font-size="10" fill="#1a1a1a" font-weight="bold">輕客戶端能</text>
<text x="10" y="421" class="cat" font-size="10" fill="#1a1a1a" font-weight="bold">驗證什麼？</text>
<text x="100" y="408" font-size="10" fill="#1a1a1a">共識；有效性需信任誠實多數</text>
<text x="354" y="408" font-size="10" fill="#1a1a1a">共識與有效性（包括資料可用性與計算）</text>
<text x="10" y="456" class="cat" font-size="10" fill="#1a1a1a" font-weight="bold">寫入的隱私</text>
<text x="100" y="456" font-size="10" fill="#1a1a1a">假設 UTXO 圖無法被有效分析</text>
<text x="354" y="456" font-size="10" fill="#1a1a1a">ZK-SNARK</text>
<text x="10" y="491" class="cat" font-size="10" fill="#1a1a1a" font-weight="bold">帳戶策略的隱私</text>
<text x="100" y="491" font-size="10" fill="#1a1a1a">無</text>
<text x="354" y="491" font-size="10" fill="#1a1a1a">ZK-SNARK + 私密帳戶抽象</text>
<text x="10" y="526" class="cat" font-size="10" fill="#1a1a1a" font-weight="bold">讀取的隱私</text>
<text x="100" y="526" font-size="10" fill="#1a1a1a">自己運行全節點，否則毫無隱私</text>
<text x="354" y="526" font-size="10" fill="#1a1a1a">選項 1：運行全節點</text>
<text x="354" y="539" font-size="10" fill="#1a1a1a">（SNARK 免除了計算需求，因此更容易）</text>
<text x="354" y="568" font-size="10" fill="#1a1a1a">選項 2：TEE+ORAM、PIR 等類似技術</text>
<text x="10" y="603" class="cat" font-size="10" fill="#1a1a1a" font-weight="bold">網路層隱私</text>
<text x="100" y="603" font-size="10" fill="#1a1a1a">假設大多數記憶池節點是誠實的，</text>
<text x="100" y="616" font-size="10" fill="#1a1a1a">而且沒有在追蹤你</text>
<text x="354" y="603" font-size="10" fill="#1a1a1a">可使用洋蔥路由、混合網路等</text>
</svg>
</figure>

幾乎所有定義「區塊鏈」的核心特性，不是已經發生根本改變，就是即將發生根本改變：

* **驗證**：下載並重新執行 → PeerDAS 抽樣並驗證 SNARK
* **共識**：PoW → PoS → 經過大幅最佳化的 PoS
* **區塊建構權**：由單一礦工產生區塊 → 多方共同建構區塊

套用 AI 的說法，唯一*誠實*的結論（好啦，是*誠實的笑點*）是：像完成 Lean 升級後的以太坊這樣的現代密碼學網路，之所以被稱為「區塊鏈」，很大程度上是出於歷史原因。實際上，它是一種融合了兩條脈絡的混合構造：

1. 中本聰式的核心理念
2. 從學術界 50 年的研究中誕生的強大新密碼學工具——它們在 2009 年甚至還不存在（或尚未成熟）

<figure data-type="resizable-media" data-align="center">
<img src="../../../../images/the_cryptographic_world_computer/crypto_timeline_zhTW.png" width="600" alt="從學術研究到區塊鏈的密碼學技術時間軸" />
</figure>

<p style="text-align: center"><em class="select-text pointer-events-auto">crypto（加密貨幣）裡有多少 crypto（密碼學）？2009 vs 2020 vs 2030</em></p>

密碼學並不是唯一重要的科學。同樣重要的還有：[形式化驗證](https://vitalik.eth.limo/general/2026/05/18/fv.html)、資料庫理論、點對點網路理論的進步、資訊理論、經濟學等等。但這些都與「每個人都試圖用有效的 PoW 產生下一個區塊，某個人成功了，把它廣播出去，其他人下載並重新執行，如此循環」這個根本核心相容。密碼學帶來的變革則不然。

那麼，這對使用者意味著什麼？

最重要的結論是：使用者所面對的取捨正在發生根本性的變化：

<figure data-type="resizable-media" data-align="center">
<svg xmlns="http://www.w3.org/2000/svg" width="600" height="339" viewBox="0 0 600 339" font-family="Helvetica, Arial, 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif" lang="zh-Hant" class="svg-scope-16p8nd0">
<style>.svg-scope-16p8nd0 text { font-size:10px; fill:#1a1a1a }
.svg-scope-16p8nd0 .hdr { font-size:11px; font-weight:bold }
.svg-scope-16p8nd0 .seclab { font-weight:bold }
.svg-scope-16p8nd0 line { stroke:#999; stroke-width:1 }</style>
<rect width="600" height="339" fill="#fff"/>
<rect x="0" y="24" width="600" height="175" fill="#eef8f0"/>
<rect x="0" y="199" width="600" height="140" fill="#fdf0f0"/>
<rect x="0" y="0" width="600" height="24" fill="#e8e8ee"/>
<text x="34" y="16" class="hdr" font-size="11" fill="#1a1a1a" font-weight="bold">2015 年的以太坊</text>
<text x="321" y="16" class="hdr" font-size="11" fill="#1a1a1a" font-weight="bold">2030 年的以太坊</text>
<line x1="0" y1="0" x2="600" y2="0" stroke="#999" stroke-width="1"/>
<line x1="0" y1="24" x2="600" y2="24" stroke="#999" stroke-width="1"/>
<line x1="26" y1="59" x2="600" y2="59" stroke="#999" stroke-width="1"/>
<line x1="26" y1="94" x2="600" y2="94" stroke="#999" stroke-width="1"/>
<line x1="26" y1="129" x2="600" y2="129" stroke="#999" stroke-width="1"/>
<line x1="26" y1="164" x2="600" y2="164" stroke="#999" stroke-width="1"/>
<line x1="0" y1="199" x2="600" y2="199" stroke="#999" stroke-width="1"/>
<line x1="26" y1="234" x2="600" y2="234" stroke="#999" stroke-width="1"/>
<line x1="26" y1="269" x2="600" y2="269" stroke="#999" stroke-width="1"/>
<line x1="26" y1="304" x2="600" y2="304" stroke="#999" stroke-width="1"/>
<line x1="0" y1="339" x2="600" y2="339" stroke="#999" stroke-width="1"/>
<line x1="0" y1="0" x2="0" y2="339" stroke="#999" stroke-width="1"/>
<line x1="26" y1="0" x2="26" y2="339" stroke="#999" stroke-width="1"/>
<line x1="313" y1="0" x2="313" y2="339" stroke="#999" stroke-width="1"/>
<line x1="600" y1="0" x2="599" y2="339" stroke="#999" stroke-width="1"/>
<text x="13.0" y="118.5" text-anchor="middle" class="seclab" font-size="18" fill="#1a7f37" font-weight="bold">+</text>
<text x="13.0" y="276.0" text-anchor="middle" class="seclab" font-size="18" fill="#b91c1c" font-weight="bold">−</text>
<text x="34" y="39" font-size="10" fill="#1a1a1a">100% 正常運行時間</text>
<text x="321" y="39" font-size="10" fill="#1a1a1a">100% 正常運行時間</text>
<text x="34" y="74" font-size="10" fill="#1a1a1a">抗審查（即保證交易會被納入區塊）</text>
<text x="321" y="74" font-size="10" fill="#1a1a1a">強抗審查：保證交易即時被納入區塊（透過 FOCIL）</text>
<text x="34" y="109" font-size="10" fill="#1a1a1a">保證依照程式設定的規則執行</text>
<text x="321" y="109" font-size="10" fill="#1a1a1a">保證依照程式設定的規則執行</text>
<text x="34" y="144" font-size="10" fill="#1a1a1a">不可逆性</text>
<text x="321" y="144" font-size="10" fill="#1a1a1a">不可逆性</text>
<text x="321" y="179" font-size="10" fill="#1a1a1a">隱私性往往比伺服器更強</text>
<text x="34" y="214" font-size="10" fill="#1a1a1a">成本非常高</text>
<text x="321" y="214" font-size="10" fill="#1a1a1a">通用計算成本高（許多形式的專用計算開銷低得多）</text>
<text x="34" y="249" font-size="10" fill="#1a1a1a">隱私</text>
<text x="321" y="249" font-size="10" fill="#1a1a1a">通用計算的隱私（許多專用應用已具有非常強的隱私）</text>
<text x="34" y="284" font-size="10" fill="#1a1a1a">延遲（出塊約 17 秒，12 次確認約 200 秒）</text>
<text x="321" y="284" font-size="10" fill="#1a1a1a">有些延遲（一個時隙約 4-8 秒，最終確定約 8-32 秒）</text>
<text x="34" y="319" font-size="10" fill="#1a1a1a">要麼運行一個龐大吃資源的節點，要麼信任某人</text>
<text x="321" y="319" font-size="10" fill="#1a1a1a">要獲得最佳保證仍需運行節點，但要求輕得多</text>
</svg>
</figure>

在開發應用時，**計算的結構**開始變得非常重要。在簡單的區塊鏈中，1 位元組就是 1 位元組，1 gas 就是 1 gas。而在未來的架構中，同樣多的計算，如果你把它全部塞進一筆不透明、序列執行的交易裡，成本就會高得多；如果你把它放進封裝良好、可以平行處理或被修剪掉的依賴項中——最好是在交易進入最終區塊之前就處理掉——成本就會低得多。這會影響開發者的激勵，並隨著時間推移影響所有使用以太坊的應用的結構：**也許從長遠來看，我們會收斂到這樣的程式設計模式：只有與描述不可交換的狀態變更及其順序直接相關的資訊會上鏈，其餘的一切都會在被納入區塊之前就先聚合起來**。

<figure data-type="resizable-media" data-align="center">
<svg xmlns="http://www.w3.org/2000/svg" width="866" height="592" viewBox="0 -8 866 592" font-family="system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif" lang="zh-Hant">
  <defs>
    <marker id="arrGray" markerWidth="18" markerHeight="18" refX="14" refY="9" orient="auto" markerUnits="userSpaceOnUse">
      <path d="M2,2 L16,9 L2,16 Z" fill="#475569"/>
    </marker>
  </defs>
  <rect x="0" y="-8" width="866" height="592" fill="#ffffff"/>
  <g stroke="#2563eb" stroke-width="2" fill="#dbeafe">
    <rect x="20" y="20" width="88" height="52" rx="6"/>
    <rect x="20" y="106" width="88" height="52" rx="6"/>
    <rect x="20" y="192" width="88" height="52" rx="6"/>
    <rect x="20" y="278" width="88" height="52" rx="6"/>
    <rect x="20" y="364" width="88" height="52" rx="6"/>
  </g>
  <g font-size="16" font-weight="bold" fill="#1e3a8a" text-anchor="middle">
    <text x="64" y="51" letter-spacing="-1.1">A → B</text>
    <text x="64" y="137" letter-spacing="-1.1">B → C</text>
    <text x="64" y="223" letter-spacing="-1.1">C → D</text>
    <text x="64" y="309" letter-spacing="-1.1">D → E</text>
    <text x="64" y="395" letter-spacing="-1.1">E → F</text>
  </g>
  <g stroke="#475569" stroke-width="2" fill="none" marker-end="url(#arrGray)">
    <path d="M 64,75 V 103"/>
    <path d="M 64,161 V 189"/>
    <path d="M 64,247 V 275"/>
    <path d="M 64,333 V 361"/>
    <path d="M 64,419 V 500"/>
  </g>
  <g fill="#ffedd5" stroke="#ea580c" stroke-width="2">
    <path d="M 632,24 L 632,24 A 4 4 0 0 1 636,20 L 672,20 A 4 4 0 0 1 676,24 L 676,68 A 4 4 0 0 1 672,72 L 592,72 A 4 4 0 0 1 588,68 L 588,50.5 A 4 4 0 0 1 592,46.5 L 628,46.5 A 4 4 0 0 0 632,42.5 Z"/>
    <path d="M 632,110 L 632,110 A 4 4 0 0 1 636,106 L 672,106 A 4 4 0 0 1 676,110 L 676,154 A 4 4 0 0 1 672,158 L 592,158 A 4 4 0 0 1 588,154 L 588,136.5 A 4 4 0 0 1 592,132.5 L 628,132.5 A 4 4 0 0 0 632,128.5 Z"/>
    <path d="M 632,196 L 632,196 A 4 4 0 0 1 636,192 L 672,192 A 4 4 0 0 1 676,196 L 676,240 A 4 4 0 0 1 672,244 L 592,244 A 4 4 0 0 1 588,240 L 588,222.5 A 4 4 0 0 1 592,218.5 L 628,218.5 A 4 4 0 0 0 632,214.5 Z"/>
    <path d="M 632,282 L 632,282 A 4 4 0 0 1 636,278 L 672,278 A 4 4 0 0 1 676,282 L 676,326 A 4 4 0 0 1 672,330 L 592,330 A 4 4 0 0 1 588,326 L 588,308.5 A 4 4 0 0 1 592,304.5 L 628,304.5 A 4 4 0 0 0 632,300.5 Z"/>
    <path d="M 632,368 L 632,368 A 4 4 0 0 1 636,364 L 672,364 A 4 4 0 0 1 676,368 L 676,412 A 4 4 0 0 1 672,416 L 592,416 A 4 4 0 0 1 588,412 L 588,394.5 A 4 4 0 0 1 592,390.5 L 628,390.5 A 4 4 0 0 0 632,386.5 Z"/>
  </g>
  <g font-size="16" fill="#9a3412" text-anchor="middle">
    <text x="654" y="34" font-size="12.5">這就是</text>
    <text x="654" y="49.4" font-size="12.5">為何</text>
    <text x="632" y="64.8" font-size="12.5">允許這麼做</text>
    <text x="654" y="120" font-size="12.5">這就是</text>
    <text x="654" y="135.4" font-size="12.5">為何</text>
    <text x="632" y="150.8" font-size="12.5">允許這麼做</text>
    <text x="654" y="206" font-size="12.5">這就是</text>
    <text x="654" y="221.4" font-size="12.5">為何</text>
    <text x="632" y="236.8" font-size="12.5">允許這麼做</text>
    <text x="654" y="292" font-size="12.5">這就是</text>
    <text x="654" y="307.4" font-size="12.5">為何</text>
    <text x="632" y="322.8" font-size="12.5">允許這麼做</text>
    <text x="654" y="378" font-size="12.5">這就是</text>
    <text x="654" y="393.4" font-size="12.5">為何</text>
    <text x="632" y="408.8" font-size="12.5">允許這麼做</text>
  </g>
  <g fill="#dbeafe" stroke="#2563eb" stroke-width="2">
    <rect x="570" y="2" width="46.2" height="25.5" rx="4"/>
    <rect x="570" y="88" width="46.2" height="25.5" rx="4"/>
    <rect x="570" y="174" width="46.2" height="25.5" rx="4"/>
    <rect x="570" y="260" width="46.2" height="25.5" rx="4"/>
    <rect x="570" y="346" width="46.2" height="25.5" rx="4"/>
  </g>
  <g font-size="16" font-weight="bold" fill="#1e3a8a" text-anchor="middle">
    <text x="592" y="20.25" letter-spacing="-1.1">A → B</text>
    <text x="592" y="106.25" letter-spacing="-1.1">B → C</text>
    <text x="592" y="192.25" letter-spacing="-1.1">C → D</text>
    <text x="592" y="278.25" letter-spacing="-1.1">D → E</text>
    <text x="592" y="364.25" letter-spacing="-1.1">E → F</text>
  </g>
  <path d="M 570,14.75 H 560 V 500" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrGray)"/>
  <g stroke="#475569" stroke-width="2">
    <path d="M 570,100.75 H 560"/>
    <path d="M 570,186.75 H 560"/>
    <path d="M 570,272.75 H 560"/>
    <path d="M 570,358.75 H 560"/>
  </g>
  <g fill="#e5e7eb" stroke="#6b7280" stroke-width="2">
    <rect x="720" y="63" width="52" height="52" rx="6"/>
    <rect x="794" y="192" width="52" height="52" rx="6"/>
    <rect x="720" y="321" width="52" height="52" rx="6"/>
    <rect x="794" y="321" width="52" height="52" rx="6"/>
  </g>
  <g fill="none" stroke="#6b7280" stroke-width="1.6">
    <path d="M 676,46 H 701 V 89 H 720"/>
    <path d="M 676,132 H 701 V 89 H 720"/>
    <path d="M 772,89 H 820 V 192"/>
    <path d="M 676,218 H 794"/>
    <path d="M 820,244 V 321"/>
    <path d="M 676,304 H 701 V 347 H 720"/>
    <path d="M 676,390 H 701 V 347 H 720"/>
    <path d="M 772,347 H 794"/>
  </g>
  <path d="M 820,373 V 509" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrGray)"/>
  <rect x="10" y="502" width="476" height="72" rx="8" fill="#eef2ff" stroke="#4338ca" stroke-width="2"/>
  <g fill="#dbeafe" stroke="#2563eb" stroke-width="2">
    <rect x="20" y="512" width="88" height="52" rx="6"/>
    <rect x="112" y="512" width="88" height="52" rx="6"/>
    <rect x="204" y="512" width="88" height="52" rx="6"/>
    <rect x="296" y="512" width="88" height="52" rx="6"/>
    <rect x="388" y="512" width="88" height="52" rx="6"/>
  </g>
  <g font-size="16" font-weight="bold" fill="#1e3a8a" text-anchor="middle">
    <text x="64" y="544" letter-spacing="-1.1">A → B</text>
    <text x="156" y="544" letter-spacing="-1.1">B → C</text>
    <text x="248" y="544" letter-spacing="-1.1">C → D</text>
    <text x="340" y="544" letter-spacing="-1.1">D → E</text>
    <text x="432" y="544" letter-spacing="-1.1">E → F</text>
  </g>
  <rect x="522" y="502" width="334" height="72" rx="8" fill="#eef2ff" stroke="#4338ca" stroke-width="2"/>
  <g fill="#dbeafe" stroke="#2563eb" stroke-width="2">
    <rect x="532" y="525.25" width="46.2" height="25.5" rx="4"/>
    <rect x="582" y="525.25" width="46.2" height="25.5" rx="4"/>
    <rect x="632" y="525.25" width="46.2" height="25.5" rx="4"/>
    <rect x="682" y="525.25" width="46.2" height="25.5" rx="4"/>
    <rect x="732" y="525.25" width="46.2" height="25.5" rx="4"/>
  </g>
  <g font-size="16" font-weight="bold" fill="#1e3a8a" text-anchor="middle">
    <text x="554" y="543" letter-spacing="-1.1">A → B</text>
    <text x="604" y="543" letter-spacing="-1.1">B → C</text>
    <text x="654" y="543" letter-spacing="-1.1">C → D</text>
    <text x="704" y="543" letter-spacing="-1.1">D → E</text>
    <text x="754" y="543" letter-spacing="-1.1">E → F</text>
  </g>
  <rect x="794" y="512" width="52" height="52" rx="6" fill="#e5e7eb" stroke="#6b7280" stroke-width="2"/>
</svg>
</figure>

<p style="text-align: center"><em class="select-text pointer-events-auto">將計算結構化，能讓區塊鏈更有效地專注於它的本職工作。</em></p>

或許最重要的轉變是：**網路的去中心化特性，正從純粹為了安全性與穩健性而承擔的負擔，轉變為至少有時候、在少數有限的情況下，即使從效能角度來看也是一種優勢**。去中心化網路能讓更大量的資料被平行儲存。它能讓大量計算平行進行，而且在許多情況下是在記憶池內進行。在少數情況下，它還能*提升*隱私，因為只有去中心化網路才能有效隱藏元資料（例如*資料與請求來自何處*）。

早在 2010 年代中期，這就是以太坊早期的夢想之一：我們去中心化不只是為了穩健性，也是為了*提升*規模。既然中心化系統可以把工作分配給不同的參與者來提升效能，我們也應該可以。當時這之所以不可行，主要原因只有一個：缺少的關鍵要素是*驗證*。如果你把工作拆分出去，就必須驗證每一份工作都被正確完成。早期的設計試圖用隨機抽樣的委員會來彌補這一點，但它們都遇到了同樣的瓶頸：第一，委員會的建立既複雜又昂貴，而且會大幅增加延遲；第二，一旦委員會失靈，就沒有任何補救手段。如今，有了現代密碼學，這個問題已經解決，而且這個解決方案的額外開銷正逐月下降。

另一個值得關注、去中心化有可能改善效能特性的領域是延遲。以太坊本身的延遲永遠無法與伺服器匹敵，但圍繞它建立的基礎設施卻有可能做到。

整體而言，在使用者與鏈之間建立一個更強大的、本身並非一條鏈的去中心化中間層，能讓以太坊變得非常強大，同時又不損及鏈的任何根本特性。

在更遙遠的未來，以太坊有可能再經歷一次轉變——[混淆](https://vitalik.eth.limo/general/2026/06/29/obfuscation1.html)（[iO](https://vitalik.eth.limo/general/2026/07/28/obfuscation_part_ii_diamond_io.html)）可能的[興起](https://vitalik.eth.limo/general/2026/08/21/obfuscation_part_iii_local_mixing.html)。這裡的聖杯是：可行的混淆能消除隱私與通用性之間的取捨——你可以用完全安全、加密的形式，進行涉及無限數量（非同步）參與者的完全通用計算。即使是弱版本的混淆，也有許多應用，例如加密記憶池。但早在這些成為現實之前，本文的所有結論就已經適用了。

這就是「密碼學世界電腦」：以太坊從一本單純的帳本——你可以不加區分地把計算與資料倒進去執行——轉變為一種將區塊鏈與密碼學隱私和驗證，以及強大的去中心化鏈下元件結合在一起的架構。

要完整實現這個設計，仍面臨許多挑戰。讓零知識證明足夠高效、足夠安全並不容易，但這屬於[封裝複雜性](https://vitalik.eth.limo/general/2022/02/28/complexity.html)，而且已經在借助 AI 工具大幅最佳化。更困難、也更具系統性複雜度的部分，很可能是如何管理並平行化對極大量狀態的存取。對於如何處理這個問題，已經有許多構想正在醞釀，不過它們仍需要改進，特別是在我們更加了解未來將運行哪些應用之後。

如果你看一下 [Strawmap](https://strawmap.org/)，明年計劃中的分叉 Hegota 很可能是以太坊最後一次「普通」的分叉——它的功能與技術，2015 年的人也能認得出來。此後的一切都將涉及遞迴 STARK、自動化形式化驗證、高度最佳化的共識演算法，以及讓這一切都具備抗量子能力。隨著 PeerDAS 的推出，以太坊已經開始從單純的區塊鏈轉型為強大得多的東西。從 Hegota 之後，這場轉型將成為以太坊的*主線故事*。它的最終成果是：比單靠上一個時代的技術所能實現的，更便宜、更具擴展性、更私密的高安全性計算。這就是密碼學世界電腦。
