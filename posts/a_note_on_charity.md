[category]: <> (General,Economics)
[date]: <> (2017/03/11)
[title]: <> (A Note On Charity Through Marginal Price Discrimination)
[pandoc]: <> (--mathjax)

**Updated 2018-07-28. See end note.**

The following is an interesting idea that I had two years ago that I personally believe has promise and could be easily implemented in the context of a blockchain ecosystem, though if desired it could certainly also be implemented with more traditional technologies (blockchains would help get the scheme network effects by putting the core logic on a more neutral platform).

Suppose that you are a restaurant selling sandwiches, and you ordinarily sell sandwiches for $7.50. Why did you choose to sell them for $7.50, and not $7.75 or $7.25? It clearly can’t be the case that the cost of production is exactly $7.49999, as in that case you would be making no profit, and would not be able to cover fixed costs; hence, in most normal situations you would still be able to make _some_ profit if you sold at $7.25 or $7.75, though less. Why less at $7.25? Because the price is lower. Why less at $7.75? Because you get fewer customers. It just so happens that $7.50 is the point at which the balance between those two factors is optimal for you.

<center>
<img src="../../../../images/a-note-on-charity-files/pic1.png" style="width: 330px" />
<img src="../../../../images/a-note-on-charity-files/pic2.png" style="width: 330px; margin-left: 20px" class="padded" />
</center>
<br>

Notice one consequence of this: if you make a _slight_ distortion to the optimal price, then even compared to the magnitude of the distortion the losses that you face are minimal. If you raise prices by 1%, from $7.50 to $7.575, then your profit declines from $6750 to $6733.12 - a tiny 0.25% reduction. And that’s _profit_ - if you had instead donated 1% of the price of each sandwich, it would have reduced your profit by 5%. The smaller the distortion the more favorable the ratio: raising prices by 0.2% only cuts your profits down by 0.01%.

Now, you could argue that stores are not perfectly rational, and not perfectly informed, and so they may not _actually_ be charging at optimal prices, all factors considered. However, if you don’t know what direction the deviation is in for any given store, then even still, _in expectation_, the scheme works the same way - except instead of losing $17 it’s more like flipping a coin where half the time you gain $50 and half the time you lose $84. Furthermore, in the more complex scheme that we will describe later, we'll be adjusting prices in both directions simultaneously, and so there will not even be any extra risk - no matter how correct or incorrect the original price was, the scheme will give you a predictable small net loss.

Also, the above example was one where marginal costs are high, and customers are picky about prices - in the above model, charging $9 would have netted you no customers at all. In a situation where [marginal costs are much lower](http://www.thezeromarginalcostsociety.com/), and customers are less price-sensitive, the losses from raising or lowering prices would be even lower.

So what is the point of all this? Well, suppose that our sandwich shop changes its policy: it sells sandwiches for $7.55 to the general public, but lowers the prices to $7.35 for people who volunteered in some charity that maintains some local park (say, this is 25% of the population). The store’s new profit is $\$6682.5 \cdot 0.25+\$6742.5 \cdot 0.75=\$6727.5$ (that’s a $22.5 loss), but the result is that you are now paying all 4500 of your customers 20 cents each to volunteer at that charity - an incentive size of $900 (if you just count the customers who actually do volunteer, $225). So the store loses a bit, but gets a huge amount of leverage, de-facto contributing at least $225 depending on how you measure it for a cost of only $22.5.

<center>
<img src="../../../../images/a-note-on-charity-files/pic3.png" class="padded" />
</center>
<br>

Now, what we can start to do is build up an ecosystem of “stickers”, which are non-transferable digital “tokens” that organizations hand out to people who they think are contributing to worthy causes. Tokens could be organized by category (eg. poverty relief, science research, environmental, local community projects, open source software development, writing good blogs), and merchants would be free to charge marginally lower prices to holders of the tokens that represent whatever causes they personally approve of.

The next stage is to make the scheme recursive - being or working for a merchant that offers lower prices to holders of green stickers is itself enough to merit you a green sticker, albeit one that is of lower potency and gives you a lower discount. This way, if an entire community approves of a particular cause, it may actually be profit-maximizing to start offering discounts for the associated sticker, and so economic and social pressure will maintain a certain level of spending and participation toward the cause in a stable equilibrium.

As far as implementation goes, this requires:

* A standard for stickers, including wallets where people can hold stickers
* Payment systems that have support for charging lower prices to sticker holders included
* At least a few sticker-issuing organizations (the lowest overhead is likely to be issuing stickers for charity donations, and for easily verifiable online content, eg. open source software and blogs)

So this is something that can certainly be bootstrapped within a small community and user base and then let to grow over time.

Update 2017.03.14: [here](https://github.com/vbuterin/research/blob/master/charity_sim.py) is an economic model/simulation showing the above implemented as a Python script.

Update 2018.07.28: after discussions with others (Glen Weyl and several Reddit commenters), I realized a few extra things about this mechanism, some encouraging and some worrying:

* The above mechanism could be used not just by charities, but also by centralized corporate actors. For example, a large corporation could offer a bribe of $40 to any store that offers the 20-cent discount to customers of its products, gaining additional revenue much higher than $40. So it's empowering but potentially dangerous in the wrong hands... (I have not researched it but I'm sure this kind of technique is used in various kinds of loyalty programs already)
* The above mechanism has the property that a merchant can "donate" $\$x$ to charity at a cost of $\$x^{2}$ (note: $x^{2}<x$ at the scales we're talking about here). This gives it a structure that's economically optimal in certain ways (see [quadratic voting](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2003531)), as a merchant that feels twice as strongly about some public good will be inclined to offer twice as large a subsidy, whereas most other social choice mechanisms tend to either undervalue (as in traditional voting) or overvalue (as in buying policies via lobbying) stronger vs weaker preferences.
