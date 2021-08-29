[category]: <> (General,Gitcoin)
[date]: <> (2020/10/18)
[title]: <> (Gitcoin Grants Round 7 Retrospective)
[pandoc]: <> (--mathjax)

Round 7 of Gitcoin Grants has successfully completed! This round has seen an unprecedented growth in interest and contributions, with $274,830 in contributions and $450,000 in matched funds distributed across 857 projects.

The category structure was once again changed; this time was had a split between "dapp tech", "infrastructure tech" and "community". Here are the results:

<center>
<img src="../../../../images/round_7_files/results1.jpg" style="width: 360px" />
<img src="../../../../images/round_7_files/results2.jpg" style="width: 360px" />
<img src="../../../../images/round_7_files/results3.jpg" style="width: 360px" />
</center>

## Defi joins the matching!

In this round, we were able to have much higher matching values than before. This was because the usual matchings, provided by the Ethereum Foundation and a few other actors, were supplemented for the first time by a high level of participation from various defi projects:

![](../../../../images/round_7_files/matching.jpg)

The matchers were:

* [Chainlink](https://chain.link/), a smart contract oracle project
* [Optimism](https://optimism.io/), a layer-2 optimistic rollup
* The [Ethereum Foundation](http://ethereum.org)
* [Balancer](https://balancer.exchange/), a decentralized exchange
* [Synthetix](https://synthetix.io/), a synthetic assets platform
* [Yearn](https://yearn.finance/), a collateralized-lending platform
* [Three Arrows Capital](https://www.threearrowscap.com/about-us/), an investment fund
* [Defiance Capital](https://twitter.com/defiancecapital), another investment fund
* [Future Fund](https://twitter.com/future_fund_), which is totally not an investment fund! (/s)
* $MEME, a memecoin
* [Yam](https://yam.finance/), a defi project
* Some individual contributors: ferretpatrol, [bantg](https://twitter.com/bantg/), [Mariano Conti](https://twitter.com/nanexcool/), [Robert Leshner](https://twitter.com/rleshner/), [Eric Conner](twitter.com/econoar/), [10b576da0](https://twitter.com/10b57e6da0)

The projects together contributed a large amount of matching funding, some of which was used this round and some of which is reserved as a "rainy day fund" for future rounds in case future matchers are less forthcoming.

This is a significant milestone for the ecosystem because it shows that Gitcoin Grants is expanding beyond reliance on a very small number of funders, and is moving toward something more sustainable. But it is worth exploring, what exactly is driving these matchers to contribute, and is it sustainable?

There are a few possibile motivations that are likely all in play to various extents:

1. People are naturally altruistic to some extent, and this round defi projects got unexpectedly wealthy for the first time due to a rapid rise in interest and token prices, and so donating some of that windfall felt like a natural "good thing to do"
2. Many in the community are critical of defi projects by default, viewing them as unproductive casinos that create a negative image of what Ethereum is supposed to be about. Contributing to public goods is an easy way for a defi project to show that they want to be a positive contributor to the ecosystem and make it better
3. Even in the absence of such negative perceptions, defi is a competitive market that is heavily dependent on community support and network effects, and so it's very valuable to a project to win friends in the ecosystem
4. The largest defi projects capture enough of the benefit from these public goods that it's in their own interest to contribute
5. There's a high degree of common-ownership between defi projects (holders of one token also hold other tokens and hold ETH), and so even if it's not strictly in a _project's_ interest to donate a large amount, _token holders of that project_ push the project to contribute because they as holders benefit from the gains to both that project but also to the other projects whose tokens they hold.

The remaining question is, of course: how sustainable will these incentives be? Are the altruistic and public-relations incentives only large enough for a one-time burst of donations of this size, or could it become more sustainable? Could we reliably expect to see, say, $2-3 million per year spent on quadratic funding matching from here on? If so, it would be excellent news for public goods funding diversification and democratization in the Ethereum ecosystem.

### Where did the troublemakers go?

One curious result from the previous round and this round is that the "controversial" community grant recipients from previous rounds seem to have dropped in prominence on their own. In theory, we should have seen them continue to get support from their supporters with their detractors being able to do nothing about it. In practice, though, the top media recipients this round appear to be relatively uncontroversial and universally beloved mainstays of the Ethereum ecosystem. Even the [Zero Knowledge Podcast](https://www.zeroknowledge.fm/), an excellent podcast but one aimed for a relatively smaller and more highly technical audience, has received a large contribution this round.

What happened? Why did the distribution of media recipients improve in quality all on its own? Is the mechanism perhaps more self-correcting than we had thought?

### Overpayment

This round is the first round where top recipients on all sides received quite a large amount. On the infrastructure side, the White Hat Hacking project (basically a fund to donate to [samczsun](https://samczsun.com/)) received a total of $39,258, and the [Bankless podcast](http://podcast.banklesshq.com/) got $47,620. We could ask the question: are the top recipients getting too much funding?

To be clear, I do think that it's very improper to try to create a moral norm that public goods contributors should only be earning salaries up to a certain level and should not be able to earn much more than that. People launching coins earn huge windfalls all the time; it is completely natural and fair for public goods contributors to also get that possibility (and furthermore, the numbers from this round translate to about ~$200,000 per year, which is not even that high).

However, one can ask a more limited and pragmatic question: given the current reward structure, is putting an extra $1 into the hands of a top contributor _less valuable_ than putting $1 into the hands of one of the other very valuable projects that's still underfunded? Turbogeth, Nethermind, RadicalXChange and many other projects could still do quite a lot with a marginal dollar. For the first time, the matching amounts are high enough that this is actually a significant issue.

Especially if matching amounts increase even further, is the ecosystem going to be able to correctly allocate funds and avoid overfunding projects? Alternatively, if it fails to avoid over-concentrating funds, is that all that bad? Perhaps the possibility of becoming the center of attention for one round and earning a $500,000 windfall will be part of the incentive that motivates independent public goods contributors!

We don't know; but these are the yet-unknown facts that running the experiment at its new increased scale is for the first time going to reveal.

### Let's talk about categories...

The concept of categories as it is currently implemented in Gitcoin Grants is a somewhat strange one. Each category has a fixed total matching amount that is split between projects within that category. What this mechanism basically says is that the community can be trusted to choose between projects _within_ a category, but we need a separate technocratic judgement to judge how the funds are split between the different categories in the first place.

But it gets more paradoxical from here. In Round 7, a ["collections" feature](https://gitcoin.co/grants/collections) was introduced halfway through the round:

![](../../../../images/round_7_files/categories.jpg)

If you click "Add to Cart" on a collection, you immediately add everything in the collection to your cart. This is strange because this mechanism seems to send the exact _opposite_ message: users that don't understand the details well can choose to allocate funds to entire categories, but (unless they manually edit the amounts) they should not be making many active decisions _within_ each category.

Which is it? Do we trust the radical quadratic fancy democracy to allocate within categories but not between them, do we trust it to allocate between categories but nudge people away from making fine-grained decisions within them, or something else entirely? I recommend that for Round 8 we think harder about the philosophical challenges here and come up with a more principled approach.

One option would be to have one matching pool and have _all_ the categories just be a voluntary UI layer. Another would be to experiment with _even more_ "affirmative action" to bootstrap particular categories: for example, we could split the Community matching into a $25,000 matching pool for each major world region (eg. North America + Oceania, Latin America, Europe, Africa, Middle East, India, East + Southeast Asia) to try to give projects in more neglected areas a leg up. There are many possibilities here! One hybrid route is that the "focused" pools could _themselves_ be quadratic funded in the previous round!

### Identity verification

As collusion, fake accounts and other attacks on Gitcoin Grants have been recently increasing, Round 7 added an additional verification option with the decentralized social-graph-based [BrightID](https://www.brightid.org/), and single-handedly boosted the project's userbase by a factor of ten:

![](../../../../images/round_7_files/brightid.jpg)

This is good, because along with helping BrightID's growth, it also subjects the project to a trial-by-fire: there's now a large incentive to try to create a large number of fake accounts on it! BrightID is going to face a tough challenge making it reasonably easy for regular users to join but at the same time resist attacks from fake and duplicate accounts. I look forward to seeing them try to meet the challenge!

### ZK rollups for scalability

Finally, Round 7 was the first round where Gitcoin Grants experimented with using the [ZkSync](https://wallet.zksync.io/) ZK rollup to decrease fees for payments:

<center>
<img src="../../../../images/round_7_files/zkrollups.png" style="width:450px" />
</center><br>

The main thing to report here is simply that the ZK rollup successfully did decrease fees! The user experience worked well. Many optimistic and ZK rollup projects are now looking at [collaborating with wallets](https://www.theblockcrypto.com/linked/80744/coinbase-wallet-optimisms-layer-2-rollup) on direct integrations, which should increase the usability and security of such techniques further.

### Conclusions

Round 7 has been a pivotal round for Gitcoin Grants. The matching funding has become much more sustainable. The levels of funding are now large enough to successfully fund quadratic freelancers to the point where a project getting "too much funding" is a conceivable thing to worry about! Identity verification is taking steps forward. Payments have become much more efficient with the introduction of the [ZkSync](https://wallet.zksync.io/) ZK rollup. I look forward to seeing the grants continue for many more rounds in the future.
