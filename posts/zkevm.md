[category]: <> (General,Blockchains)
[date]: <> (2022/08/04)
[title]: <> (The different types of ZK-EVMs)
[pandoc]: <> ()

_Special thanks to the PSE, Polygon Hermez, Zksync, Scroll, Matter Labs and Starkware teams for discussion and review._

There have been many "ZK-EVM" projects making flashy announcements recently. [Polygon](https://blog.polygon.technology/the-future-is-now-for-ethereum-scaling-introducing-polygon-zkevm) open-sourced their ZK-EVM project, [ZKSync](https://matterlabs.medium.com/100-days-to-mainnet-6f230893bd73) released their plans for ZKSync 2.0, and the relative newcomer [Scroll](https://mirror.xyz/scroll.eth/XQyXDgyxoefag6hcBgGJFz8qrb10rmSU-zUBvY3Q9_A) announced their ZK-EVM recently. There is also the ongoing effort from the [Privacy and Scaling Explorations team](https://github.com/privacy-scaling-explorations/zkevm-circuits), [Nicolas Liochon et al's team](https://ethresear.ch/t/a-zk-evm-specification/11549), an [alpha compiler](https://medium.com/starkware/starknet-alpha-2-4aa116f0ecfc) from the EVM to Starkware's ZK-friendly language [Cairo](https://starkware.co/cairo/), and certainly at least a few others I have missed.

The core goal of all of these projects is the same: to use [ZK-SNARK](https://vitalik.ca/general/2021/01/26/snarks.html) technology to make cryptographic proofs of execution of Ethereum-like transactions, either to make it much easier to verify the Ethereum chain itself or to build [ZK-rollups](https://vitalik.ca/general/2021/01/05/rollup.html) that are (close to) equivalent to what Ethereum provides but are much more scalable. But there are subtle differences between these projects, and what tradeoffs they are making between practicality and speed. This post will attempt to describe a taxonomy of different "types" of EVM equivalence, and what are the benefits and costs of trying to achieve each type.

## Overview (in chart form)

![](../../../../images/zkevm/chart.png)

## Type 1 (fully Ethereum-equivalent)

Type 1 ZK-EVMs strive to be fully and uncompromisingly Ethereum-equivalent. They do not change any part of the Ethereum system to make it easier to generate proofs. They do not replace hashes, state trees, transaction trees, precompiles or any other in-consensus logic, no matter how peripheral.

#### <span style="color:#008800">Advantage: perfect compatibility</span>

The goal is to be able to verify Ethereum blocks as they are today - or at least, verify the [execution-layer side](https://hackmd.io/@n0ble/the-merge-terminology) (so, beacon chain consensus logic is not included, but all the transaction execution and smart contract and account logic is included).

Type 1 ZK-EVMs are what we ultimately need make the Ethereum layer 1 itself more scalable. In the long term, modifications to Ethereum tested out in Type 2 or Type 3 ZK-EVMs might be introduced into Ethereum proper, but such a re-architecting comes with its own complexities.

Type 1 ZK-EVMs are also ideal for rollups, because they allow rollups to re-use a lot of infrastructure. For example, Ethereum execution clients can be used as-is to generate and process rollup blocks (or at least, they can be once [withdrawals are implemented](https://github.com/ethereum/consensus-specs/blob/dev/specs/capella/beacon-chain.md) and that functionality can be re-used to support ETH being deposited into the rollup), so tooling such as block explorers, block production, etc is very easy to re-use.

#### <span style="color:#cc0000">Disadvantage: prover time</span>

Ethereum was not originally designed around ZK-friendliness, so there are _many_ parts of the Ethereum protocol that take a large amount of computation to ZK-prove. Type 1 aims to replicate Ethereum exactly, and so it has no way of mitigating these inefficiencies. At present, proofs for Ethereum blocks take many hours to produce. This can be mitigated either by clever engineering to massively parallelize the prover or in the longer term by ZK-SNARK ASICs.

#### <span style="color:#880088">Who's building it?</span>

The [ZK-EVM Community Edition](https://github.com/privacy-scaling-explorations/zkevm-specs) (bootstrapped by community contributors including [Privacy and Scaling Explorations](https://github.com/privacy-scaling-explorations/), the Scroll team, [Taiko](https://github.com/taikochain) and others) is a Tier 1 ZK-EVM.

## Type 2 (fully EVM-equivalent)

Type 2 ZK-EVMs strive to be exactly EVM-equivalent, but not quite Ethereum-equivalent. That is, they look exactly like Ethereum "from within", but they have some differences on the outside, particularly in data structures like the block structure and [state tree](https://medium.com/@eiki1212/ethereum-state-trie-architecture-explained-a30237009d4e).

The goal is to be fully compatible with existing applications, but make some minor modifications to Ethereum to make development easier and to make proof generation faster.

#### <span style="color:#008800">Advantage: perfect equivalence at the VM level</span>

Type 2 ZK-EVMs make changes to data structures that hold things like the Ethereum state. Fortunately, these are structures that the EVM itself cannot access directly, and so applications that work on Ethereum would almost always still work on a Type 2 ZK-EVM rollup. You would not be able to use Ethereum execution clients as-is, but you could use them with some modifications, and you would still be able to use EVM debugging tools and most other developer infrastructure.

There are a small number of exceptions. One incompatibility arises for applications that verify Merkle proofs of [historical Ethereum blocks](https://github.com/aragon/evm-storage-proofs) to verify claims about historical transactions, receipts or state (eg. bridges sometimes do this). A ZK-EVM that replaces Keccak with a different hash function would break these proofs. However, I usually recommend against building applications this way anyway, because future Ethereum changes (eg. [Verkle trees](https://notes.ethereum.org/@vbuterin/verkle_tree_eip)) will break such applications even on Ethereum itself. A better alternative would be for Ethereum itself to add [future-proof history access precompiles](https://ethresear.ch/t/future-proof-shard-and-history-access-precompiles/9781).

#### <span style="color:#cc0000">Disadvantage: improved but still slow prover time</span>

Type 2 ZK-EVMs provide faster prover times than Type 1 mainly by removing parts of the Ethereum stack that rely on needlessly complicated and ZK-unfriendly cryptography. Particularly, they might change Ethereum's Keccak and RLP-based Merkle Patricia tree and perhaps the block and receipt structures. Type 2 ZK-EVMs might instead use a different hash function, eg. [Poseidon](https://www.poseidon-hash.info/). Another natural modification is modifying the state tree to store the code hash and keccak, removing the need to verify hashes to process the `EXTCODEHASH` and `EXTCODECOPY` opcodes.

These modifications significantly improve prover times, but they do not solve every problem. The slowness from having to prove the EVM as-is, with all of the inefficiencies and ZK-unfriendliness inherent to the EVM, still remains. One simple example of this is memory: because an `MLOAD` can read any 32 bytes, including "unaligned" chunks (where the start and end are not multiples of 32), an MLOAD can't simply be interpreted as reading one chunk; rather, it might require reading two consecutive chunks and performing bit operations to combine the result.

#### <span style="color:#880088">Who's building it?</span>

[Scroll's ZK-EVM](https://mirror.xyz/scroll.eth/XQyXDgyxoefag6hcBgGJFz8qrb10rmSU-zUBvY3Q9_A) project is building toward a Type 2 ZK-EVM, as is [Polygon Hermez](https://blog.polygon.technology/the-future-is-now-for-ethereum-scaling-introducing-polygon-zkevm). That said, neither project is quite there yet; in particular, a lot of the more complicated precompiles have not yet been implemented. Hence, at the moment both projects are better considered [Type 3](#type-3-almost-evm-equivalent).

## Type 2.5 (EVM-equivalent, except for gas costs)

One way to <span style="color:#008800">significantly improve worst-case prover times</span> is to greatly increase the gas costs of specific operations in the EVM that are very difficult to ZK-prove. This might involve precompiles, the KECCAK opcode, and possibly specific patterns of calling contracts or accessing memory or storage or reverting.

Changing gas costs <span style="color:#cc0000">may reduce developer tooling compatibility and break a few applications</span>, but it's generally considered less risky than "deeper" EVM changes. Developers should take care to not require more gas in a transaction than fits into a block, to never make calls with hard-coded amounts of gas (this has already been standard advice for developers for a long time).

An alternative way to manage resource constraints is to simply set hard limits on the number of times each operation can be called. This is easier to implement in circuits, but plays much less nicely with EVM security assumptions. I would call this approach Type 3 rather than Type 2.5.

## Type 3 (almost EVM-equivalent)

Type 3 ZK-EVMs are _almost_ EVM-equivalent, but make a few sacrifices to exact equivalence to further improve prover times and make the EVM easier to develop.

#### <span style="color:#008800">Advantage: easier to build, and faster prover times</span>

Type 3 ZK-EVMs might remove a few features that are exceptionally hard to implement in a ZK-EVM implementation. [Precompiles](https://docs.moonbeam.network/builders/build/canonical-contracts/precompiles/eth-mainnet/) are often at the top of the list here;. Additionally, Type 3 ZK-EVMs sometimes also have minor differences in how they treat contract code, memory or stack.

#### <span style="color:#cc0000">Disadvantage: more incompatibility</span>

The goal of a Type 3 ZK-EVM is to be compatible with _most_ applications, and require only minimal re-writing for the rest. That said, there will be some applications that would need to be rewritten either because they use pre-compiles that the Type 3 ZK-EVM removes or because of subtle dependencies on edge cases that the VMs treat differently.

#### <span style="color:#880088">Who's building it?</span>

Scroll and Polygon are both Type 3 in their current forms, though they're expected to improve compatibility over time. Polygon has a unique design where they are ZK-verifying their own internal language called [zkASM](https://github.com/0xPolygonHermez/zkevm-doc/blob/main/mkdocs/docs/zkEVM/zkASM/Introduction.md), and they interpret ZK-EVM code using the zkASM implementation. Despite this implementation detail, I would still call this a genuine Type 3 ZK-EVM; it can still verify EVM code, it just uses some different internal logic to do it.

Today, no ZK-EVM team _wants_ to be a Type 3; Type 3 is simply a transitional stage until the complicated work of adding precompiles is finished and the project can move to Type 2.5. In the future, however, Type 1 or Type 2 ZK-EVMs may become Type 3 ZK-EVMs voluntarily, by adding in _new_ ZK-SNARK-friendly precompiles that provide functionality for developers with low prover times and gas costs.

## Type 4 (high-level-language equivalent)

A Type 4 system works by taking smart contract source code written in a high-level language (eg. [Solidity](https://docs.soliditylang.org/en/v0.8.15/), [Vyper](https://vyper.readthedocs.io/en/stable/), or some intermediate that both compile to) and compiling _that_ to some language that is explicitly designed to be ZK-SNARK-friendly.

#### <span style="color:#008800">Advantage: very fast prover times</span>

There is a _lot_ of overhead that you can avoid by not ZK-proving all the different parts of each EVM execution step, and starting from the higher-level code directly.

I'm only describing this advantage with one sentence in this post (compared to a big bullet point list below for compatibility-related disadvantages), but that should not be interpreted as a value judgement! Compiling from high-level languages directly really can greatly reduce costs and help decentralization by making it easier to be a prover.

#### <span style="color:#cc0000">Disadvantage: more incompatibility</span>

A "normal" application written in Vyper or Solidity can be compiled down and it would "just work", but there are some important ways in which very many applications are not "normal":

* **Contracts may not have the same addresses** in a Type 4 system as they do in the EVM, because CREATE2 contract addresses depend on the exact bytecode. This breaks applications that rely on not-yet-deployed "counterfactual contracts", ERC-4337 wallets, [EIP-2470 singletons](https://eips.ethereum.org/EIPS/eip-2470) and many other applications.
* **Handwritten EVM bytecode** is more difficult to use. Many applications use handwritten EVM bytecode in some parts for efficiency. Type 4 systems may not support it, though there are ways to implement limited EVM bytecode support to satisfy these use cases without going through the effort of becoming a full-on Type 3 ZK-EVM.
* **Lots of debugging infrastructure cannot be carried over**, because such infrastructure runs over the EVM bytecode. That said, this disadvantage is mitigated by the _greater_ access to debugging infrastructure from "traditional" high-level or intermediate languages (eg. LLVM).

Developers should be mindful of these issues.

#### <span style="color:#880088">Who's building it?</span>

[ZKSync](https://matterlabs.medium.com/100-days-to-mainnet-6f230893bd73) is a Type 4 system, though it may add compatibility for EVM bytecode over time. Nethermind's [Warp](https://github.com/NethermindEth/warp) project is building a compiler from Solidity to Starkware's Cairo, which will turn StarkNet into a de-facto Type 4 system.

## The future of ZK-EVM types

The types are not unambiguously "better" or "worse" than other types. Rather, they are different points on the tradeoff space: lower-numbered types are more compatible with existing infrastructure but slower, and higher-numbered types are less compatible with existing infrastructure but faster. In general, it's healthy for the space that all of these types are being explored.

Additionally, ZK-EVM projects can easily start at higher-numbered types and jump to lower-numbered types (or vice versa) over time. For example:

* A ZK-EVM could start as Type 3, deciding not to include some features that are especially hard to ZK-prove. Later, they can add those features over time, and move to Type 2.
* A ZK-EVM could start as Type 2, and later become a hybrid Type 2 / Type 1 ZK-EVM, by providing the possibility of operating either in full Ethereum compatibility mode or with a modified state tree that can be proven faster. Scroll is considering moving in this direction.
* What starts off as a Type 4 system could become Type 3 over time by adding the ability to process EVM code later on (though developers would still be encouraged to compile direct from high-level languages to reduce fees and prover times)
* A Type 2 or Type 3 ZK-EVM can become a Type 1 ZK-EVM if Ethereum itself adopts its modifications in an effort to become more ZK-friendly.
* A Type 1 or Type 2 ZK-EVM can become a Type 3 ZK-EVM by adding a precompile for verifying code in a very ZK-SNARK-friendly language. This would give developers a choice between Ethereum compatibility and speed. This would be Type 3, because it breaks perfect EVM equivalence, but for practical intents and purposes it would have a lot of the benefits of Type 1 and 2. The main downside might be that some developer tooling would not understand the ZK-EVM's custom precompiles, though this could be fixed: developer tools could add universal precompile support by supporting a config format that includes an EVM code equivalent implementation of the precompile.

Personally, my hope is that everything becomes Type 1 over time, through a combination of improvements in ZK-EVMs and improvements to Ethereum itself to make it more ZK-SNARK-friendly. In such a future, we would have multiple ZK-EVM implementations which could be used both for ZK rollups and to verify the Ethereum chain itself. Theoretically, there is no need for Ethereum to standardize on a single ZK-EVM implementation for L1 use; different clients could use different proofs, so we continue to benefit from code redundancy.

However, it is going to take quite some time until we get to such a future. In the meantime, we are going to see a lot of innovation in the different paths to scaling Ethereum and Ethereum-based ZK-rollups.
