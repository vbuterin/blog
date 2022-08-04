[category]: <> (General,Blockchains,Philosophy,Economics)
[date]: <> (2017/07/27)
[title]: <> (A Note on Metcalfe's Law, Externalities and Ecosystem Splits)
[pandoc]: <> (--mathjax)

Looks like it's blockchain split season [again](http://bitcoincash.org/). For background of various people discussing the topic, and whether such splits are good or bad:

* Power laws and network effects (arguing the BTC/BCC split may destroy value due to network effect loss): [https://medium.com/crypto-fundamental/power-laws-and-network-effects-why-bitcoincash-is-not-a-free-lunch-5adb579972aa](https://medium.com/crypto-fundamental/power-laws-and-network-effects-why-bitcoincash-is-not-a-free-lunch-5adb579972aa)
* Brian Armstrong on the Ethereum Hard Fork (last year): [https://blog.coinbase.com/on-the-ethereum-hard-fork-780f1577e986](https://blog.coinbase.com/on-the-ethereum-hard-fork-780f1577e986)
* Phil Daian on the ETH/ETC split: [http://pdaian.com/blog/stop-worrying-love-etc/](http://pdaian.com/blog/stop-worrying-love-etc/)

Given that ecosystem splits are not going away, and we may well see more of them in the crypto industry over the next decade, it seems useful to inform the discussion with some simple economic modeling. With that in mind, let's get right to it.
<br>
<hr />
<br>

Suppose that there exist two projects A and B, and a set of users of total size $N$, where A has $N_a$ users and B has $N_b$ users. Both projects benefit from network effects, so they have a utility that increases with the number of users. However, users also have their own differing taste preferences, and this may lead them to choose the smaller platform over the bigger platform if it suits them better.

We can model each individual's private utility in one of four ways:

|                           |                            |
|---------------------------|----------------------------|
| 1. $U(A) = p + N_a$ | $U(B) = q + N_b$           |
| 2. $U(A) = p \cdot N_a$ | $U(B) = q \cdot N_b$      |
| 3. $U(A) = p + \ln{N_a}$ | $U(B) = q + \ln{N_b}$      |
| 4. $U(A) = p \cdot \ln{N_a}$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| $U(B) = q \cdot \ln{N_b}$ |

$p$ and $q$ are private per-user parameters that you can think of as corresponding to users' distinct preferences. The difference between the first two approaches and the last two reflects differences between interpretations of Metcalfe's law, or more broadly the idea that the per-user value of a system grows with the number of users. The [original formulation](https://en.wikipedia.org/wiki/Metcalfe%27s_law) suggested a per-user value of $N$ (that is, a total network value of $N^{2}$), but other analysis (see [here](http://spectrum.ieee.org/computing/networks/metcalfes-law-is-wrong)) suggests that above very small scales $N\log{N}$ usually dominates; there is a controversy over which model is correct. The difference between the first and second (and between the third and fourth) is the extent to which utility from a system's intrinsic quality and utility from network effects are complementary - that is, are the two things good in completely separate ways that do not interact with each other, like social media and coconuts, or are network effects an important part of letting the intrinsic quality of a system shine?

We can now analyze each case in turn by looking at a situation where $N_a$ users choose A and $N_b$ users choose B, and analyze each individual's decision to choose one or the other from the perspective of economic externalities - that is, does a user's choice to switch from A to B have a positive net effect on others' utility or a negative one? If switching has a positive externality, then it is virtuous and should be socially nudged or encouraged, and if it has a negative externality then it should be discouraged. We model an "ecosystem split" as a game where to start off $N_a = N$ and $N_b = 0$ and users are deciding for themselves whether or not to join the split, that is, to move from A to B, possibly causing $N_a$ to fall and $N_b$ to rise.

Switching (or not switching) from A to B has externalties because A and B both have network effects; switching from A to B has the negative externality of reducing A's network effect, and so hurting all remaining A users, but it also has the positive externality of increasing B's network effect, and so benefiting all B users.

#### Case 1

Switching from A to B gives $N_a$ users a negative externality of one, so a total loss of $N_a$, and it gives $N_b$ users a positive externality of one, so a total gain of $N_b$. Hence, the total externality is of size $N_b - N_a$; that is, switching from the smaller to the larger platform has positive externalities, and switching from the larger platform to the smaller platform has negative externalities.

#### Case 2

Suppose $P_a$ is the sum of $p$ values of $N_a$ users, and $Q_b$ is the sum of $q$ values of $N_b$ users. The total negative externality is $P_a$ and the total positive externality is $Q_b$. Hence, switching from the smaller platform to the larger has positive social externalities if the two platforms have equal intrinsic quality to their users (ie. users of A intrinsically enjoy A as much as users of B intrinsically enjoy B, so $p$ and $q$ values are evenly distributed), but if it is the case that A is bigger but B is better, then there are positive externalities in switching to B.

Furthermore, notice that if a user is making a switch from a larger A to a smaller B, then this itself is revealed-preference evidence that, for that user, and for all existing users of B, $\frac{q}{p} > \frac{N_a}{N_b}$. However, if the split stays as a split, and does not proceed to become a full-scale migration, then that means that users of A hold different views, though this could be for two reasons: (i) they intrinsically dislike A but not by enough to justify the switch, (ii) they intrinsically like A more than B. This could arise because (a) A users have a higher opinion of A than B users, or (b) A users have a lower opinion of B than B users. In general, we see that moving from a system that makes its average user less happy to a system that makes its average user more happy has positive externalities, and in other situations it's difficult to say.

#### Case 3

The derivative of $\ln{x}$ is $\frac{1}{x}$. Hence, switching from A to B gives $N_a$ users a negative externality of $\frac{1}{N_a}$, and it gives $N_b$ users a positive externality of $\frac{1}{N_b}$. Hence, the negative and positive externalities are both of total size one, and thus cancel out. Hence, switching from one platform to the other imposes no social externalities, and it is socially optimal if all users switch from A to B if and only if they think that it is a good idea for them personally to do so.

#### Case 4

Let $P_a$ and $Q_b$ are before. The negative externality is of total size $\frac{P_a}{N_a}$ and the positive externality is of total size $\frac{Q_b}{N_b}$. Hence, if the two systems have equal intrinsic quality, the externality is of size zero, but if one system has higher intrinsic quality, then it is virtuous to switch to it. Note that as in case 2, if users _are_ switching from a larger system to a smaller system, then that means that they find the smaller system to have higher intrinsic quality, although, also as in case 2, if the split remains a split and does not become a full-scale migration, then that means other users see the intrinsic quality of the larger system as higher, or at least not lower by enough to be worth the network effects.

The existence of users switching to B suggests that for them, $\frac{q}{p} \geq \frac{log{N_a}}{log{N_b}}$, so for the $\frac{Q_B}{N_b} > \frac{P_a}{N_a}$ condition to not hold (ie. for a move from a larger system to a smaller system not to have positive externalities) it would need to be the case that users of A have similarly high values of $p$ - an approximate heuristic is, the users of A would need to love A so much that if _they_ were the ones in the minority that would be willing to split off and move to (or stay with) the smaller system. In general, it thus seems that moves from larger systems to smaller systems that actually do happen will have positive externalities, but it is far from ironclad that this is the case.

<br>
<hr />
<br>

Hence, if the first model is true, then to maximize social welfare we should be trying to nudge people to switch to (or stay with) larger systems over smaller systems, and splits should be discouraged. If the fourth model is true, then we should be at least slightly trying to nudge people to switch to smaller systems over larger systems, and splits should be slightly encouraged. If the third model is true, then people will choose the socially optimal thing all by themselves, and if the second model is true, it's a toss-up.

It is my personal view that the truth lies somewhere between the third and fourth models, and the first and second greatly overstate network effects above small scales. The first and second model (the $N^{2}$ form of Metcalfe's law) essentially state that a system growing from 990 million to 1 billion users gives the same increase in per-user utility as growing from 100,000 to 10.1 million users, which seems very unrealistic, whereas the $N\log{N}$ model (growing from 100 million to 1 billion users gives the same increase in per-user utility as growing from 100,000 to 10 million users) intuitively seems much more correct.

And the third model says: if you see people splitting off from a larger system to create a smaller system because they want something that more closely matches their personal values, then the fact that these people have already shown that they value this switch enough to give up the comforts of the original system's network effects is by itself enough evidence to show that the split is socially beneficial. Hence, unless I can be convinced that the first model is true, or that the second model is true and the specific distributions of $p$ and $q$ values make splits make negative negative externalities, I maintain my existing view that those splits that actually do happen (though likely not _hypothetical_ splits that end up not happening due to lack of interest) are in the long term socially beneficial, value-generating events.
