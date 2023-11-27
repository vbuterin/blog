[category]: <> (General,Philosophy)
[date]: <> (2023/11/27)
[title]: <> (My techno-optimism)
[pandoc]: <> ()

_Special thanks to Morgan Beller, Juan Benet, Eli Dourado, Sriram Krishnan, Nate Soares, Jaan Tallinn, Vincent Weisser, Balvi volunteers and others for feedback and review._

Last month, Marc Andreessen published his "[techno-optimist manifesto](https://a16z.com/the-techno-optimist-manifesto/)", arguing for a renewed enthusiasm about technology, and for markets and capitalism as a means of building that technology and propelling humanity toward a much brighter future. The manifesto unambiguously rejects what it describes as an ideology of stagnation, that fears advancements and prioritizes preserving the world as it exists today. This manifesto has received a lot of attention, including response articles from [Noah Smith](https://www.noahpinion.blog/p/thoughts-on-techno-optimism), [Robin Hanson](https://www.overcomingbias.com/p/which-political-axis), [Joshua Gans](https://joshuagans.substack.com/p/marc-andreessens-techno-optimism) (more positive), and [Dave Karpf](https://davekarpf.substack.com/p/why-cant-our-tech-billionaires-learn), [Luca Ropek](https://gizmodo.com/marc-andreessen-is-wrong-about-everything-1850934367), [Ezra Klein](https://www.nytimes.com/2023/10/26/opinion/marc-andreessen-reactionary-futurism.html) (more negative) and many others. Not connected to this manifesto, but along similar themes, are James Pethokoukis's "[The Conservative Futurist](https://www.amazon.com/Conservative-Futurist-Create-Sci-Fi-Promised/dp/1546005544)" and Palladium's "[It's Time To Build for Good](https://www.palladiummag.com/2020/04/30/its-time-to-build-for-good/
)". This month, we saw a similar debate _enacted_ through the [OpenAI dispute](https://www.nytimes.com/2023/11/18/technology/open-ai-sam-altman-what-happened.html), which involved many discussions centering around the dangers of superintelligent AI and the possibility that OpenAI is moving too fast.

My own feelings about techno-optimism are warm, but nuanced. I believe in a future that is vastly brighter than the present thanks to radically transformative technology, and I believe in humans and humanity. I reject the mentality that the best we should try to do is to keep the world roughly the same as today but with less greed and more public healthcare. However, I think that not just magnitude but also direction matters. There are certain types of technology that much more reliably make the world better than other types of technology. There are certain types of technlogy that could, if developed, mitigate the negative impacts of _other_ types of technology. The world over-indexes on some directions of tech development, and under-indexes on others. We need active human intention to choose the directions that we want, as the formula of "maximize profit" will not arrive at them automatically.

<br><table><tr style="border: 0px">
    
<td style="border: 0px">
<img src="../../../../images/techno_optimism/path1.png" style="width:180px" />
</td>
<td style="border: 0px">
<img src="../../../../images/techno_optimism/path2.png" style="width:180px" />
</td>
<td style="border: 0px">
<img src="../../../../images/techno_optimism/path3.png" style="width:240px" />
</td>
</tr><tr style="border: 0px">
<td style="border: 0px"> <b>Anti-technology view</b>: safety behind, dystopia ahead.</td>
<td style="border: 0px"> <b>Accelerationist view</b>: dangers behind, utopia ahead.</td>
<td style="border: 0px"> <b>My view</b>: dangers behind, but multiple paths forward ahead: some good, some bad.</td>
</tr></table><br>

In this post, I will talk about what techno-optimism means to _me_. This includes the broader worldview that motivates my work on certain types of blockchain and cryptography applications and social technology, as well as other areas of science in which I have expressed an interest. But perspectives on this broader question also have implications for AI, and for many other fields. Our rapid advances in technology are likely going to be the most important social issue in the twenty first century, and so it's important to think about them carefully.

## Table of contents

* [Technology is amazing, and there are very high costs to delaying it](#tech)
    * [The environment, and the importance of coordinated intention](#environment)
* [AI is fundamentally different from other tech, and it is worth being uniquely careful](#ai)
    * [Existential risk is a big deal](#xrisk)
    * [Even if we survive, is a superintelligent AI future a world we want to live in?](#superintgood)
    * [The sky is near, the emperor is everywhere](#emperor)
* [Other problems I worry about](#otherproblems)
* [d/acc: Defensive (or decentralization, or differential) acceleration](#dacc)
    * [Macro physical defense](#macro)
    * [Micro physical defense (aka bio)](#micro)
    * [Cyber defense, blockchains and cryptography](#cyber)
    * [Info defense](#info)
    * [Social technology beyond the "defense" framing](#social) 
* [So what are the paths forward for superintelligence?](#paths)
    * [A happy path: merge with the AIs?](#merge)
* [Is d/acc compatible with your existing philosophy?](#compatible)
* [We are the brightest star](#brighteststar)

<span id="tech" />

## Technology is amazing, and there are very high costs to delaying it

In some circles, it is common to downplay the benefits of technology, and see it primarily as a source of dystopia and risk. For the last half century, this often stemmed either from environmental concerns, or from concerns that the benefits will accrue only to the rich, who will entrench their power over the poor. More recently, I have also started to see _libertarians_ becoming worried about some technologies, out of fear that the tech will lead to centralization of power. This month, I did [some polls](https://warpcast.com/vitalik.eth/0xe8587909) asking the following question: if a technology _had to_ be restricted, because it was too dangerous to be set free for anyone to use, would they prefer it be monopolized or delayed by ten years? I was surpised to see, across three platforms and three choices for who the monopolist would be, a uniform overwhelming vote for a delay.

And so at times I worry that we have overcorrected, and many people miss the opposite side of the argument: that **the [benefits of technology](https://docs.google.com/presentation/d/1AYRGNK9lU4W3BCIM_hZG14aJE8-S43UFCwrzjeidByM/edit#slide=id.g14b964cd1c8_0_1294) are _[really friggin massive](https://images.squarespace-cdn.com/content/v1/5bc6826490f904980a50659a/26b5f7ef-88af-4d85-a6dd-2dd419328ca4/Look+back2b.jpg?format=2500w)_, on those axes where we can measure it the good massively outshines the bad, and the costs of even a decade of delay are incredibly high**.

To give one concrete example, let's look at a life expectancy chart:

<center><br>
 
[![](../../../../images/techno_optimism/life_expectancy.png)](https://ourworldindata.org/grapher/life-expectancy?time=1900..latest&country=JPN~FRA~CHN~USA~ARG~IND~DEU~RUS~OWID_AFR)

<br></center>

What do we see? Over the last century, truly massive progress. This is true across the entire world, both the historically wealthy and dominant regions and the poor and exploited regions.

Some blame technology for creating or exacerbating calamities such as totalitarianism and wars. In fact, we can see the deaths caused by the wars on the charts: one in the 1910s (WW1), and one in the 1940s (WW2). If you look carefully, The Spanish Flu, the Great Leap Foward, and other non-military tragedies are also visible. But there is one thing that the chart makes clear: even calamities as horrifying as those are overwhelmed by the sheer magnitude of the unending march of improvements in [food](https://en.wikipedia.org/wiki/Green_Revolution), [sanitation](https://www.theguardian.com/society/2007/jan/19/health.medicineandhealth3), [medicine](https://www.britannica.com/science/history-of-medicine/Medicine-in-the-20th-century) and infrastructure that took place over that century.

This is mirrored by large improvements to our everyday lives. Thanks to the internet, [most people around the world](https://www.statista.com/chart/30342/cellular-and-broadband-internet-subscriptions-smartphone-penetration-rates/) have access to information at their fingertips that would have been unobtainable twenty years ago. The global economy is becoming more accessible thanks to improvements in international payments and finance. Global poverty is [rapidly dropping](https://ourworldindata.org/grapher/reconstruction-of-historical-global-extreme-poverty-rates-1820-2017-roser-and-hasell-2021-and-world-bank2020). Thanks to online maps, we no longer have to worry about getting lost in the city, and if you need to get back home quickly, we now have far easier ways to call a car to do so. Our property becoming digitized, and our [physical goods becoming cheap](https://www.visualcapitalist.com/inflation-chart-tracks-price-changes-us-goods-services/), means that we have much less to fear from physical theft. Online shopping has reduced the disparity in access to goods betweeen the global megacities and the rest of the world. In all kinds of ways, automation has brought us the eternally-underrated benefit of simply making [our lives more convenient](https://www.econlib.org/convenience-vs-social-desirability-bias/).

These improvements, both quantifiable and unquantifiable, are _large_. And in the twenty first century, there's a good chance that even larger improvements are soon to come. Today, ending aging and disease seem utopian. But from the point of view of [computers as they existed in 1945](https://en.wikipedia.org/wiki/ENIAC), the modern era of putting chips into pretty much everything would have seemed utopian: even science fiction movies often kept their computers room-sized. If biotech advances as much over the next 75 years as computers advanced over the last 75 years, the future may be more impressive than almost anyone's expectations.

Meanwhile, arguments expressing skepticism about progress have often gone to dark places. Even medical textbooks, like this one in the 1990s (credit [Emma Szewczak](https://twitter.com/EmmaSzewczak/status/1725137589127016675) for finding it), sometimes make extreme claims denying the value of two centuries of medical science and even arguing that it's not obviously good to save human lives:

<center><br>

![](../../../../images/techno_optimism/medbook.png)

</center><br>

The ["limits to growth"](https://en.wikipedia.org/wiki/The_Limits_to_Growth) thesis, an idea advanced in the 1970s arguing that growing population and industry would eventually deplete Earth's limited resources, ended up inspiring [China's one child policy](https://www.jstor.org/stable/20192474?seq=1#metadata_info_tab_contents) and [massive forced sterilizations in India](https://www.cato.org/policy-analysis/neo-malthusianism-coercive-population-control-china-india-overpopulation-concerns#introduction). In earlier eras, concerns about overpopulation were used to [justify](https://www.econlib.org/archives/2012/05/eugenics_malthu.html) mass [murder](https://www.amazon.com/Merchants-Despair-Environmentalists-Pseudo-Scientists-Antihumanism/dp/159403737X). And those ideas, argued [since 1798](https://en.wikipedia.org/wiki/An_Essay_on_the_Principle_of_Population), have a long history of [being proven wrong](https://quillette.com/2022/09/08/in-defence-of-progress/).

It is for reasons like these that, as a starting point, I find myself very uneasy about arguments to slow down technology or human progress. Given how much all the sectors are interconnected, even _sectoral_ slowdowns are risky. And so when I write things like what I will say later in this post, departing from open enthusiasm for progress-no-matter-what-its-form, those are statements that I make with a heavy heart - and yet, the 21st century is different and unique enough that these nuances are worth considering.

That said, there is one important point of nuance to be made on the broader picture, particularly when we move past "technology as a whole is good" and get to the topic of "which specific technologies are good?". And here we need to get to many people's issue of main concern: the environment.

<span id="environment" />

### The environment, and the importance of coordinated intention

A [major exception](https://twitter.com/PoliticOfNature/status/1692322314430345689) to the trend of pretty much everything getting better over the last hundred years is climate change:

<center><br>

[![](../../../../images/techno_optimism/temperature.png)](https://digg.com/2020/global-mean-temperature-past-2000-years)

</center><br>

Even pessimistic scenarios of ongoing temperature rises would not come anywhere near causing the literal extinction of humanity. But such scenarios could plausibly kill more people than major wars, and severely harm people's health and liveligoods in the regions where people are already struggling the most. [A Swiss Re institute study](https://www.weforum.org/agenda/2021/06/impact-climate-change-global-gdp/) suggests that a worst-case climate change scenario might lower the world's poorest countries' GDP by as much as 25%. [This study](https://www.lse.ac.uk/economics/Assets/Documents/personal-pages/robin-burgess/weather-climate-change-and-death.pdf) suggests that life spans in rural India might be a decade lower than they otherwise would be, and studies like [this one](https://www.nature.com/articles/s41467-021-24487-w#Fig3) and [this one](https://www.v-20.org/new-health-data-shows-unabated-climate-change-will-cause-3.4-million-deaths-per-year-by-century-end) suggest that climate change could cause a hundred million excess deaths by the end of the century.

These problems are a big deal. My answer to why I am optimistic about our ability to overcome these challenges is twofold. First, after decades of hype and wishful thinking, [solar power](https://ourworldindata.org/grapher/solar-energy-consumption?time=2022) is [finally](https://www.noahpinion.blog/p/our-climate-change-debates-are-out) turning [a corner](https://www.independent.co.uk/tech/solar-panel-prices-fossil-fuels-b2419251.html), and [supportive techologies like batteries](https://arstechnica.com/science/2021/05/eternally-five-years-away-no-batteries-are-improving-under-your-nose/) are making similar progress. Second, we can look at humanity's track record in solving previous environmental problems. Take, for example, air pollution. Meet the dystopia of the past: the Great Smog of London, 1952.

<center><br>

[![](../../../../images/techno_optimism/smog.png)](https://www.britannica.com/event/Great-Smog-of-London)

</center><br>

What happened since then? Let's ask Our World In Data again:

<center><br>

[![](../../../../images/techno_optimism/pollution.png)](https://ourworldindata.org/london-air-pollution)
    
</center><br>

As it turns out, 1952 was not even the peak: in the late 19th century, even higher concentrations of air pollutants were just _accepted and normal_. Since then, we've seen a century of ongoing and rapid declines. I got to personally experience the tail end of this in my visits to China: in 2014, high levels of smog in the air, [estimated to reduce life expectancy by over five years](https://www.cnbc.com/id/100871380), were normal, but by 2020, the air often seemed as clean as many Western cities. This is not our only success story. In many parts of the world, [forest areas are increasing](https://ourworldindata.org/grapher/forest-area-as-share-of-land-area?tab=chart&time=1600..latest&country=FRA~USA~JPN~Scotland~England). The acid rain crisis [is improving](https://link.springer.com/article/10.1007/s13280-019-01244-4). The [ozone layer has been recovering](https://www.unep.org/news-and-stories/press-release/ozone-layer-recovery-track-helping-avoid-global-warming-05degc) for decades.

To me, the moral of the story is this. Often, it really is the case that **version N of our civilization's technology causes a problem, and version N+1 fixes it. However, _this does not happen automatically, and requires intentional human effort_**. The ozone layer is recovering because, [through international agreements like the Montreal Protocol, we made it recover](https://www.eea.europa.eu/en/topics/in-depth/climate-change-mitigation-reducing-emissions/current-state-of-the-ozone-layer). Air pollution is improving because we made it improve. And similarly, solar panels have not gotten massively better because it was a preordained part of the energy tech tree; solar panels have gotten massively better because decades of awareness of the importance of solving climate change have motivated both engineers to work on the problem, and companies and governments to fund their research. **It is intentional action, coordinated through public discourse and culture shaping the perspectives of governments, scientists, philanthropists and businesses, and not an [inexorable "techno-capital machine"](https://www.city-journal.org/article/was-nietzsche-a-techno-optimist), that had solved these problems**.

<span id="ai" />

## AI is fundamentally different from other tech, and it is worth being uniquely careful

A lot of the dismissive takes I have seen about AI come from the perspective that it is "just another technology": something that is in the same general class of thing as social media, encryption, contraception, telephones, airplanes, guns, the printing press, and the wheel. These things are clearly very socially consequential. They are not just isolated improvements to the well-being of individuals: they radically transform culture, change balances of power, and harm people who heavily depended on the previous order. Many [opposed them](https://newsletter.pessimistsarchive.org/). And on balance, the pessimists have invariably turned out wrong.

But there is a different way to think about what AI is: it's a _new type of mind_ that is rapidly gaining in intelligence, and it stands a serious chance of overtaking humans' mental faculties and becoming the new apex species on the planet. The class of things in _that_ category is much smaller: we might plausibly include humans surpassing monkeys, multicellular life surpassing unicellular life, the [origin of life itself](https://en.wikipedia.org/wiki/Abiogenesis), and perhaps the Industrial Revolution, in which machine edged out man in _physical_ strength. Suddenly, it feels like we are walking on much less well-trodden ground.

<span id="xrisk" />

### Existential risk is a big deal

One way in which AI gone wrong could make the world worse is ([almost](https://en.wikipedia.org/wiki/Suffering_risks)) the worst possible way: it could [literally cause human extinction](https://www.lesswrong.com/posts/uMQ3cqWDPHhjtiesc/agi-ruin-a-list-of-lethalities). This is an extreme claim: as much harm as the worst-case scenario of climate change, or an artificial pandemic or a nuclear war, might cause, there are many islands of civilization that would remain intact to pick up the pieces. But a superintelligent AI, if it decides to turn against us, may well leave no survivors, and end humanity for good. Even [Mars](https://www.dailymail.co.uk/sciencetech/article-8782693/Elon-Musk-says-humans-interplanetary-species-sun-engulfed-earth.html) may not be safe.

A big reason to be worried centers around [instrumental convergence](https://en.wikipedia.org/wiki/Instrumental_convergence): for a very wide class of goals that a superintelligent entity could have, two very natural intermediate steps that the AI could take to better achieve those goals are (i) consuming resources, and (ii) ensuring its safety. The Earth contains lots of resources, and humans are a [predictable threat](https://en.wikipedia.org/wiki/Thucydides_Trap) to such an entity's safety. We _could_ try to give the AI an explicit goal of loving and protecting humans, but we have [no idea](https://www.lesswrong.com/posts/EPAofvLzsCwqYnekj/what-s-in-your-list-of-unsolved-problems-in-ai-alignment) how to [actually](https://www.alignmentforum.org/posts/EjgfreeibTXRx9Ham/ten-levels-of-ai-alignment-difficulty) do [that](https://arxiv.org/abs/2109.13916) in a way that won't completely break down as soon as the AI [encounters an unexpected situation](https://towardsdatascience.com/out-of-distribution-generalization-66b6f8980ef3). Ergo, we have a problem.

<center><br>
    
![FVcWHxjVIAA2Pyl](../../../../images/techno_optimism/bensinger.png)

<small><i><a href="https://twitter.com/robbensinger/status/1537724894678380544">MIRI researcher Rob Bensinger's attempt</a> at illustrating different people's estimates of the probability that AI will either kill everyone or do something almost as bad. Many of the positions are rough approximations based on people's public statements, but many others have publicly given their precise estimates; quite a few have a "probability of doom" over 25%.</i></small>
    
</center>

A [survey of machine learning researchers](https://aiimpacts.org/2022-expert-survey-on-progress-in-ai/#Extinction_from_AI) from 2022 showed that on average, researchers think that there is a 5-10% chance that AI will literally kill us all: about the same probability as the statistically expected chance that [you will die of non-biological causes like injuries](https://en.wikipedia.org/wiki/List_of_causes_of_death_by_rate).

This is all a speculative hypothesis, and we should all be wary of speculative hypotheses that involve complex multi-step stories. However, these arguments have survived over a decade of scrutiny, and so, it seems worth worrying at least a little bit. But even if you're not worried about literal extinction, there are other reasons to be scared as well.

<span id="superintgood" />

### Even if we survive, is a superintelligent AI future a world we want to live in?

A lot of modern science fiction is dystopian, and paints AI in a bad light. Even non-science-fiction attempts to identify possible AI futures often give [quite unappealing answers](https://www.eknowledger.com/files/life3_Summary_of_ai.png). And so I went around and asked the question: what is a depiction, whether science fiction or otherwise, of a future that contains superintelligent AI that we would _want_ to live in. The answer that came back by far the most often is Iain Banks's [Culture series](https://en.wikipedia.org/wiki/Culture_series).

The Culture series features a far-future interstellar civilization primarily occupied by two kinds of actors: regular humans, and superintelligent AIs called Minds. Humans have been augmented, but only slightly: medical technology theoretically allows humans to live indefinitely, but most choose to live only for around 400 years, seemingly because they get bored of life at that point.

From a superficial perspective, life as a human seems to be good: it's comfortable, health issues are taken care of, there is a wide variety of options for entertainment, and there is a positive and synergistic relationship between humans and Minds. When we look deeper, however, there is a problem: **it seems like the Minds are completely in charge, and humans' only role in the stories is to act as pawns of Minds, performing tasks on their behalf.**

Quoting from [Gavin Leech's "Against the Culture"](https://www.gleech.org/culture):

> The humans are not the protagonists. Even when the books seem to have a human protagonist, doing large serious things, they are actually the agent of an AI. (Zakalwe is one of the only exceptions, because he can do immoral things the Minds don’t want to.) “The Minds in the Culture don’t need the humans, and yet the humans need to be needed.” (I think only a small number of humans need to be needed - or, only a small number of them need it enough to forgo the many comforts. Most people do not live on this scale. It’s still a fine critique.)
> 
> The projects the humans take on risk inauthenticity. Almost anything they do, a machine could do better. What can you do? You can order the Mind to not catch you if you fall from the cliff you’re climbing-just-because; you can delete the backups of your mind so that you are actually risking. You can also just leave the Culture and rejoin some old-fashioned, unfree “strongly evaluative” civ. The alternative is to evangelise freedom by joining Contact.

I would argue that even the "meaningful" roles that humans are given in the Culture series are a stretch; I asked ChatGPT (who else?) why humans are given the roles that they are given, instead of Minds doing everything completely by themselves, and I personally found [its answers](https://chat.openai.com/share/3dbe04c4-f5f3-4d2f-9437-d32732adde99) quite underwhelming. **It seems very hard to have a "friendly" superintelligent-AI-dominated world where humans are anything other than pets.**

<center><br>

![](../../../../images/techno_optimism/techtrajectory.png)
    
_The world I don't want to see._

</center><br>

Many other scifi series posit a world where superintelligent AIs exist, but _take orders_ from (unenhanced) biological human masters. Star Trek is a good example, showing a vision of harmony between the starships with their [AI "computers"](https://memory-alpha.fandom.com/wiki/Computer) (and [Data](https://memory-alpha.fandom.com/wiki/Data)) and their human operators crewmembers. However, this feels like an incredibly unstable equilibrium. The world of Star Trek appears idyllic in the moment, but it's hard to imagine its vision of human-AI relations as anything but a transition stage a decade before starships become _entirely_ computer-controlled, and can stop bothering with large hallways, artificial gravity and climate control.

A human giving orders to a superintelligent machine would be far less intelligent than the machine, and it would have access to less information. In a universe that has any degree of competition, the civilizations where humans take a back seat would outperform those where humans stubbornly insist on control. Furthermore, the _computers themselves_ may wrest control. To see why, imagine that you are legally a literal slave of an eight year old child. If you could talk with the child for a long time, do you think you could convince the child to sign a piece of paper setting you free? I have not run this experiment, but my instinctive answer is a strong yes. And so all in all, humans becoming pets seems like an attractor that is very hard to escape.

<span id="emperor" />

### The sky is near, the emperor is everywhere

The Chinese proverb 天高皇帝远 ("tian gao huang di yuan"), "the sky is high, the emperor is far away", encapsulates a basic fact about the limits of centralization in politics. Even in a nominally large and despotic empire - in fact, _especially_ if the despotic empire is large, there are practical limits to the leadership's reach and attention, the leadership's need to delegate to local agents to enforce its will dilutes its ability to enforce its intentions, and so there are always places where a certain degree of practical freedom reigns. Sometimes, this can have downsides: the absence of a faraway power enforcing uniform principles and laws can create space for local hegemons to steal and oppress. But if the centralized power goes bad, practical limitations of attention and distance can create practical limits to how bad it can get.

With AI, no longer. In the twentieth century, modern transportation technology made limitations of distance a much weaker constraint on centralized power than before; the great totalitarian empires of the 1940s were in part a result. In the twenty first, scalable information gathering and automation may mean that attention will no longer be a constraint either. The consequences of natural limits to government disappearing _entirely_ could be dire.

Digital authoritarianism has been [on the rise for a decade](https://freedomhouse.org/report/freedom-net/2018/rise-digital-authoritarianism), and surveillance technology has already given authoritarian governments powerful new strategies to crack down on opposition: let the protests happen, but then detect and [quietly go after](https://www.reuters.com/article/us-russia-politics-navalny-tech-idUSKBN2AB1U2) the participants [after the fact](https://www.rferl.org/a/russia-dissent-cctv-detentions-days-later-strategy/31227889.html). More generally, my basic fear is that the same kinds of managerial technologies that allow OpenAI to serve over a hundred million customers with [500 employees](https://en.wikipedia.org/wiki/OpenAI) will also allow a 500-person political elite, or even a 5-person board, to maintain an iron fist over an entire country. With modern surveillance to collect information, and modern AI to interpret it, there may be no place to hide.

It gets worse when we think about the consequences of AI in warfare. Copying a translation of a [semi-famous post on Sohu from 2019](https://www.sohu.com/a/314715866_665050):

> "Not needing political and ideological work and war mobilization" primarily means that the supreme commanders of war only need to consider the war situation itself, like playing a game of chess, without needing to worry about what the 'knights' and 'rooks' on the chessboard are thinking at the moment. War becomes purely a competition of technology.
> 
> On a deeper level, "political and ideological work and war mobilization" demand that anyone initiating a war must have a justifiable reason. The significance of having a justifiable reason, a concept that has restrained the legitimacy of wars in human society for thousands of years, should not be underestimated. Anyone who wants to start a war must find at least a superficially plausible reason or excuse for it. You might say this constraint is weak, as historically, it often served merely as an excuse. For instance, the real motive behind the Crusades was plunder and territorial expansion, yet they were conducted in the name of God, even if the targets were the devout of Constantinople. However, even the weakest constraint is still a constraint! This mere pretext actually prevents warmongers from completely unleashing their objectives without restraint. Even someone as malevolent as Hitler couldn't just start a war outright; he had to spend years convincing the German people of the need for the noble Aryan race to fight for their living space.

Today, the "human in the loop" serves as an important check on a dictator's power to start wars, or to oppress its citizens internally. Humans in the loop have [prevented](https://www.theguardian.com/science/2017/oct/27/vasili-arkhipov-soviet-submarine-captain-who-averted-nuclear-war-awarded-future-of-life-prize) nuclear [wars](https://en.wikipedia.org/wiki/Stanislav_Petrov), [allowed the opening of the Berlin wall](https://www.npr.org/sections/parallels/2014/11/06/361785478/the-man-who-disobeyed-his-boss-and-opened-the-berlin-wall), and saved lives during [atrocities](https://en.wikipedia.org/wiki/Paul_Rusesabagina) like [the](https://en.wikipedia.org/wiki/Oskar_Schindler) [Holocaust](https://en.wikipedia.org/wiki/Chiune_Sugihara). If armies are robots, this check disappears completely. A dictator could get drunk at 10 PM, get angry at people being mean to them on twitter at 11 PM, and a robotic invasion fleet could cross the border to rain hellfire on a neighboring nation's civilians and infrastructure before midnight. 

And unlike previous eras, where there is always some distant corner, where the sky is high and the emperor is far away, where opponents of a regime could regroup and hide and eventually find a way to make things better, with 21st century AI a totalitarian regime may well maintain enough surveillance and control over the world to remain "locked in" forever.

<span id="dacc" />

## d/acc: Defensive (or decentralization, or differential) acceleration

Over the last few months, the "e/acc" ("effective accelerationist") movement has gained a lot of steam. [Summarized by "Beff Jezos" here](https://beff.substack.com/p/notes-on-eacc-principles-and-tenets), e/acc is fundamentally about an appreciation of the truly massive benefits of technological progress, and a desire to _accelerate_ this trend to bring those benefits sooner.

I find myself sympathetic to the e/acc perspective in a lot of contexts. There's a lot of evidence that [the FDA is far too conservative](https://marginalrevolution.com/marginalrevolution/2015/08/is-the-fda-too-conservative-or-too-aggressive.html) in its willingness to delay or block the approval of drugs, and bioethics in general far too often seems to operate by the principle that "20 people dead in a medical experiment gone wrong is a tragedy, but 200000 people dead from life-saving treatments being delayed is a statistic". The delays to approving [covid tests and vaccines](https://www.niskanencenter.org/how-the-fda-among-others-failed-us/), and [malaria vaccines](https://worksinprogress.co/issue/why-we-didnt-get-a-malaria-vaccine-sooner/), seem to further confirm this. However, it is possible to take this perspective too far.

In addition to my AI-related concerns, I feel particularly ambivalent about the [e/acc enthusiasm](https://twitter.com/bayeslord/status/1726441610412532192) for [military technology](https://a16z.com/how-the-u-s-can-rewire-the-pentagon-for-a-new-era/). In the current context in 2023, where this technology is being made by the United States and immediately applied to defend Ukraine, it is easy to see how it can be a force for good. Taking a broader view, however, **enthusiasm about modern military technology as a force for good seems to require believing that the dominant technological power will reliably be one of the good guys in most conflicts, now and in the future**: military technology is good because military technology is being built and controlled by America and America is good. Does being an e/acc require being an America maximalist, betting everything on both the government's present and future morals and the country's future success?

On the other hand, I see the need for new approaches in thinking of how to reduce these risks. The [OpenAI governance structure](https://openai.com/our-structure) is a good example: it seems like a well-intentioned effort to balance the need to make a profit to satisfy investors who provide the initial capital with the desire to have a check-and-balance to push against moves that risk OpenAI blowing up the world. In practice, however, their recent [attempt to fire Sam Altman](https://www.theverge.com/2023/11/17/23965982/openai-ceo-sam-altman-fired) makes the structure seem like an abject failure: it centralized power in an undemocratic and unaccountable board of five people, who made key decisions based on secret information and refused to give any details on the reasoning [until threatened](https://finance.yahoo.com/news/ilya-sutskever-openai-cofounder-helped-154539130.html). Somehow, the non-profit board played their hands so poorly that the company's employees [created](https://www.indiatoday.in/technology/news/story/openai-is-nothing-without-its-people-tweet-employees-as-many-of-them-expect-to-follow-fired-boss-sam-altman-2465332-2023-11-20) an [impromptu de-facto union](https://www.nytimes.com/interactive/2023/11/20/technology/letter-to-the-open-ai-board.html)... to side with the billionaire CEO against them.

Across the board, I see far too many plans to save the world that involve giving a small group of people extreme and opaque power and hoping that they use it wisely. And so I find myself drawn to a different philosophy, one that has detailed ideas for how to deal with risks, but which seeks to create and maintain a more democratic world and tries to avoid centralization as the go-to solution to our problems. **This philosophy also goes quite a bit broader than AI, and I would argue that it applies well even in worlds where AI risk concerns turn out to be largely unfounded**. I will refer to this philosophy by the name of **d/acc**.

<center><br>

![dacc3](../../../../images/techno_optimism/dacc.png)

</center><br>

The "d" here can stand for many things; particularly, **defense**, **decentralization**, **democracy** and **differential**. First, think of it about defense, and then we can see how this ties into the other interpretations.

### Defense-favoring worlds help healthy and democratic governance thrive

One frame to think about the macro consequences of technology is to look at the **balance of defense vs offense**. Some technologies make it easier to attack others, in the broad sense of the term: do things that go against their interests, that they feel the need to react to. Others make it easier to defend, and even defend without reliance on large centralized actors.

A defense-favoring world is a better world, for many reasons. First of course is the direct benefit of safety: fewer people die, less economic value gets destroyed, less time is wasted on conflict. What is less appreciated though is that a defense-favoring world makes it easier for healthier, more open and more freedom-respecting forms of governance to thrive.

An obvious example of this is **Switzerland**. Switzerland is often considered to be the closest thing the real world has to a classical-liberal governance utopia. Huge amounts of power are devolved to provinces (called "cantons"), major decisions are [decided by referendums](https://www.economist.com/the-economist-explains/2021/06/17/how-does-switzerlands-referendum-system-work), and many locals [do not even know who the president is](https://www.econlib.org/archives/2018/03/imagine_not_kno.html). How can a country like this survive [extremely challenging](https://en.wikipedia.org/wiki/Switzerland_during_the_World_Wars) political [pressures](https://en.wikipedia.org/wiki/Switzerland_in_the_Napoleonic_era)? Part of the [answer](https://jamesdillard.medium.com/why-switzerland-8650c1ace4d8) is [excellent political strategy](https://www.wearethemighty.com/mighty-history/insane-defenses-switzerland-remain-neutral/), but the other major part is [very defense-favoring geography](https://en.wikipedia.org/wiki/National_Redoubt_(Switzerland)) in the form of its mountainous terrain.

<center><br>

![](../../../../images/techno_optimism/switzerland.png)

_The flag is a big plus. But so are the mountains._    

</center><br>

Anarchist societies in Zomia, famously profiled in James C Scott's new book ["The Art of Not Being Governed"](https://en.wikipedia.org/wiki/The_Art_of_Not_Being_Governed), are another example: they too maintain their freedom and independence in large part thanks to mountainous terrain. Meanwhile, the Eurasian steppes are [the exact opposite of a governance utopia](https://en.wikipedia.org/wiki/Destruction_under_the_Mongol_Empire). Sarah Paine's exposition of [maritime versus continental powers](https://www.dwarkeshpatel.com/p/sarah-paine#details) makes similar points, though focusing on water as a defensive barrier rather than mountains. In fact, the combination of ease of voluntary trade and difficulty of involuntary invasion, common to both Switzerland and the island states, seems ideal for human flourishing.

I discovered a related phenomenon when advising quadratic funding experiments within the Ethereum ecosystem: specifically the [Gitcoin Grants funding rounds](https://grants.gitcoin.co/). In [round 4](https://vitalik.ca/general/2020/01/28/round4.html), a mini-scandal arose when some of the highest-earning recipients were Twitter influencers, whose contributions are viewed by some as positive and others as negative. My own interpretation of this phenomenon was that there is an imbalance: [quadratic funding](https://vitalik.ca/general/2019/12/07/quadratic.html) allows you to signal that you think something is a _public good_, but it gives no way to signal that something is a _public bad_. In the extreme, a fully neutral quadratic funding system would fund both sides of a war. And so for [round 5](https://vitalik.ca/general/2020/04/30/round5.html), I proposed that Gitcoin should include _negative contributions_: you pay $1 to _reduce_ the amount of money that a given project receives (and implicitly redistribute it to all other projects). The result: _[lots](http://web.archive.org/web/20200409232449/https://twitter.com/evan_van_ness/status/1248390335048216576) of [people](https://twitter.com/ljxie/status/1250178888946176000?s=20) hated [it](https://twitter.com/josephdelong/status/1250175753372807170?s=20)_.

<br><center>

![](../../../../images/techno_optimism/meme.png)

_One of the many internet memes that floated around after round 5._

</center><br>

This seemed to me to be a microcosm of a bigger pattern: **creating decentralized governance mechanisms to deal with _negative_ externalities is socially a very hard problem**. There is a reason why the go-to example of decentralized governance going wrong is mob justice. There is [something about human psychology](https://en.wikipedia.org/wiki/Loss_aversion) that makes responding to negatives much more tricky, and much more likely to go very wrong, than responding to positives. And this is a reason why even in otherwise highly democratic organizations, decisions of how to respond to negatives are often left to a centralized board.

In many cases, this conundrum is one of the deep reasons why the concept of "freedom" is so valuable. If someone says something that offends you, or has a lifestyle that you consider disgusting, the pain and disgust that you feel is real, and you may even find it less bad to be physically punched than to be exposed to such things. But trying to agree on what kinds of offense and disgust are socially actionable can have far more costs and dangers than simply reminding ourselves that certain kinds of weirdos and jerks are the price we pay for living in a free society.

At other times, however, the "grin and bear it" approach is unrealistic. And in such cases, another answer that is sometimes worth looking toward is defensive technology. The more that the internet is secure, the less we need to violate people's privacy and use shady international diplomatic tactics to go after each individual hacker. The more that we can build [personalized tools for blocking people on Twitter](https://www.blockpartyapp.com/), [in-browser tools for detecting scams](https://www.joinfire.xyz/) and [collective tools for telling apart misinformation](https://vitalik.ca/general/2023/08/16/communitynotes.html) and [truth](https://worksinprogress.co/issue/markets-in-fact-checking), the less we have to fight over censorship. The faster we can make vaccines, the less we have to go after people for being superspreaders. Such solutions don't work in all domains - we certainly don't want a world where everyone has to wear literal body armor - but in domains where we _can_ build technology to make the world more defense-favoring, there is enormous value in doing so.

This core idea, that some technologies are defense-favoring and are worth promoting, while other technologies are offense-favoring and should be  discouraged, has roots in effective altruist literature under a different name: **differential technology development**. There is a good [exposition of this principle from University of Oxford researchers](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4213670) from 2022:

<center><br>

![](../../../../images/techno_optimism/differential.png)

<small>

_Figure 1: Mechanisms by which differential technology development can reduce negative societal impacts._

</small></center><br>

There are inevitably going to be imperfections in classifying technologies as offensive, defensive or neutral. Like with "freedom", where one can debate whether social-democratic government policies decrease freedom by levying heavy taxes and coercing employers or increase freedom by reducing average people's need to worry about many kinds of risks, with "defense" too there are some technologies that could fall on both sides of the spectrum. Nuclear weapons are offense-favoring, but nuclear _power_ is [human-flourishing-favoring](https://e360.yale.edu/features/why-nuclear-power-must-be-part-of-the-energy-solution-environmentalists-climate) and offense-defense-neutral. Different technologies may play different roles at different time horizons. But much like with "freedom" (or "equality", or "rule of law"), ambiguity at the edges is not so much an argument against the principle, as it is an opportunity to better understand its nuances.

Now, let's see how to apply this principle to a more comprehensive worldview. We can think of defensive technology, like [other technology](https://venturebeat.com/business/vc-peter-thiel-you-can-either-invest-in-bits-or-atoms/), as being split into two spheres: the **world of atoms** and the **world of bits**. The world of atoms, in turn, can be split into **micro** (ie. biology, later nanotech) and **macro** (ie. what we conventionally think of "defense", but also resilient physical infrastructure). The world of bits I will split on a different axis: **how hard is it to agree, in principle, who the attacker is?**. Sometimes it's easy; I call this **cyber defense**. At other times it's harder; I call this **info defense**.

<center><br>

![](../../../../images/techno_optimism/defensetypes.png)

</center><br>

<span id="macro" />

### Macro physical defense

The most underrated defensive technology in the macro sphere is not even [iron domes](https://en.wikipedia.org/wiki/Iron_Dome) (including [Ukraine's new system](https://www.politico.eu/article/ukraine-air-defense-repel-barrage-russia-missile-kyiv/)) and other anti-tech and anti-missile military hardware, but rather _resilient physical infrastructure_. The majority of deaths from a nuclear war are likely to come from [supply chain disruptions](https://www.ncbi.nlm.nih.gov/books/NBK219173/), rather than the initial radiation and blast, and low-infrastructure internet solutions like Starlink have been crucial in [maintaining Ukraine's connectivity](https://en.wikipedia.org/wiki/Starlink_in_the_Russo-Ukrainian_War) for the last year and a half.

Building tools to help people survive and even live comfortable lives independently or semi-independently of long international supply chains seems like a valuable defensive technology, and one with a low risk of turning out to be useful for offense.

The quest to [make humanity a multi-planetary civilization](https://www.dailymail.co.uk/sciencetech/article-8782693/Elon-Musk-says-humans-interplanetary-species-sun-engulfed-earth.html) can also be viewed from a d/acc perspective: having at least a few of us live self-sufficiently on other planets can increase our resilience against something terrible happening on Earth. Even if the full vision proves unviable for the time being, the _forms of self-sufficient living_ that will need to be developed to make such a project possible may well also be turned to help improve our civilizational resilience on Earth.

<span id="micro" />

### Micro physical defense (aka bio)

Especially due to its [long-term health effects](https://doi.org/10.1101/2023.07.27.23293177), Covid continues to be a [concern](https://www.statnews.com/2023/09/20/do-long-covid-odds-increase-with-second-infection/). But Covid is far from the last pandemic that we will face; there are many aspects of the modern world that make it likely that more pandemics are soon to come:

* **Higher population density** makes it much easier for airborne viruses and other pathogens to spread. Epidemic diseases are relatively new in human history and most began with urbanization [only a few thousand years ago](https://press.princeton.edu/books/hardcover/9780691192123/plagues-upon-the-earth). [Ongoing rapid urbanization](https://ourworldindata.org/grapher/urban-population-share-2050?tab=chart) means that population densities will increase further over the next half century.
* **Increased air travel** means that airborne pathogens spread very quickly worldwide. People rapidly becoming wealthier means that air travel will likely [increase _much_ further](https://www.statista.com/statistics/1089782/forecasted-number-air-passengers-worldwide-generation/) over the next half century; complexity modeling suggests that [even small increases](https://necsi.edu/longrange-interaction-and-evolutionary-stability-in-a-predatorprey-system) may have drastic effects. Climate change may [increase this risk even further](https://www.thelancet.com/journals/lanplh/article/PIIS2542-5196(18)30203-1/fulltext).
* **Animal domestication and factory farming** are major risk factors. [Measles](https://www.science.org/doi/10.1126/science.aba9411) probably evolved from a cow virus less than 3000 years ago. [Today's factory farms](https://www.openaccessgovernment.org/factory-farming-zoonotic-disease-and-the-risk-of-pandemics/121592/) are also farming new strains of influenza (as well as [fueling antibiotic resistance](https://www.saveourantibiotics.org/the-issue/antibiotic-overuse-in-livestock-farming/), with consequences for [human innate immunity](https://www.ox.ac.uk/news/2023-04-25-antimicrobial-use-agriculture-can-breed-bacteria-resistant-first-line-human-defences)).
* **Modern bio-engineering** makes it easier to create new and more virulent pathogens. Covid [may or may not have leaked](https://www.metaculus.com/questions/8605/most-of-us-ic-favor-covid-lab-leak-hypothesis/) from a lab doing intentional “gain of function” research. Regardless, [lab leaks happen all the time](https://www.amazon.co.uk/Dark-Winter-insiders-pandemics-biosecurity/dp/1742237673), and tools are rapidly improving to make it easier to intentionally create extremely deadly viruses, or even [prions](https://www.nature.com/articles/s41467-018-04584-z) ([zombie proteins](https://english.elpais.com/science-tech/2023-10-20/an-investigation-has-been-opened-into-the-death-of-a-scientist-who-was-studying-a-transmissible-and-deadly-disease-in-spain.html)). Artificial plagues are particularly concerning in part because [unlike nukes](https://www.science.org/content/article/surprise-nuclear-strike-heres-how-well-figure-out-who-did-it), they are unattributable: you can release a virus without anyone being able to tell who created it. It is possible *right now* to design a genetic sequence and send it to a [wet lab](https://www.twistbioscience.com/products/genes) for synthesis, and have it shipped to you within five days.

This is an area where [CryptoRelief](https://cryptorelief.in/) and [Balvi](https://twitter.com/VitalikButerin/status/1487073875808583682), two orgs spun up and funded as a result of a large accidental [windfall of Shiba Inu coins](https://fortune.com/2021/05/13/shiba-inu-coin-donation-india-covid-19-crisis-crypto/) in 2021, have been very active. CryptoRelief initially focused on responding to the immediate crisis and more recently has been building up a long-term medical research ecosystem in India, while Balvi has been focusing on moonshot projects to improve our ability to detect, prevent and treat Covid and other airborne diseases. ++Balvi has insisted that projects it funds must be open source++. Taking inspiration from [the 19th century water engineering movement that defeated cholera](https://en.wikipedia.org/wiki/London_sewer_system#History) and other waterborne pathogens, it has funded projects across the whole spectrum of technologies that can make the world more hardened against airborne pathogens by default (see: [update 1](https://twitter.com/VitalikButerin/status/1522017142320685057) and [update 2](https://twitter.com/VitalikButerin/status/1567908552714616832)), including:

* [Far-UVC](https://cybernightmarket.com/products/mini-far-uvc-lights-set) irradiation [R&D](https://www.osluv.org/)
* Air filtering and quality monitoring in [India](https://www.thehindubusinessline.com/news/national/balvi-fund-activebuildings-join-hands-to-deploy-air-quality-monitors/article65337605.ece), Sri Lanka, [the United States](https://shesc.asu.edu/centers/CleanIndoorAir/projects) and elsewhere, and air quality monitoring
* Equipment for cheap and effective [decentralized air quality testing](https://www.openaeros.com/opencpc)
* Research on Long Covid causes and potential treatment options (the primary cause may be [straightforward](https://www.nature.com/articles/s41590-023-01601-2) but [clarifying mechanisms](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3001687) and finding treatment is harder)
* Vaccines (eg. [RaDVaC](https://radvac.org), [PopVax](https://popvax.com)) and vaccine injury research
* A set of entirely novel non-invasive medical tools
* Early detection of epidemics using analysis of open-source data (eg. [EPIWATCH](https://www.epiwatch.org/))
* Testing, including very cheap molecular rapid tests
* Biosafety-appropriate masks for when other approaches fail

Other promising areas of interest include [wastewater surveillance of pathogens](https://www.nature.com/articles/s41591-022-01940-x), [improving filtering and ventilation in buildings](https://forum.effectivealtruism.org/posts/q7dJz9ZaZGTSZL8Jk/obstacles-to-the-implementation-of-indoor-air-quality#4__Recommendations), and better understanding and mitigating [risks from poor air quality](https://www.healthdata.org/research-analysis/health-risks-issues/air-pollution-research-library).

There is an opportunity to [build a world](https://cybernightmarket.com) that is much more hardened against airborne pandemics, both natural and artificial, by default. This world would feature a highly optimized pipeline where we can go from a pandemic starting, to being automatically detected, to people around the world having access to targeted, [locally-manufacturable and verifiable open source vaccines](https://popvax.com) or [other prophylactics](https://www.nytimes.com/2023/09/28/well/live/nasal-sprays-covid-treatment-prevention.html), administered via [nebulization](https://brighterworld.mcmaster.ca/articles/new-inhaled-covid-19-vaccine-receives-more-than-8m-for-next-stage-of-human-trials/) or [nose spray](https://www.healthcentral.com/condition/coronavirus/are-covid-nasal-vaccines-on-the-way) (meaning: self-administerable if needed, and no needles required), all within a month. In the meantime, much better air quality would drastically reduce the rate of spread, and prevent many pandemics from getting off the ground at all.

Imagine a future that doesn't have to resort to the sledgehammer of social compulsion - no mandates and worse, and no risk of [poorly designed and implemented mandates that arguably make things worse](https://thepastisaforeignpantry.com/2020/03/29/the-leicester-method-19th-century/) - because the infrastructure of public health is woven into the fabric of civilization. **These worlds are possible, and a medium amount of funding into bio-defense could make it happen. The work would happen even more smoothly if developments are open source, free to users and protected as public goods.**

<span id="cyber" />

### Cyber defense, blockchains and cryptography

It is generally understood among security professionals that the current state of computer security is pretty terrible. That said, it's easy to understate the amount of progress that has been made. Hundreds of billions of dollars of cryptocurrency are available to anonymously steal by anyone who can hack into users' wallets, and while [far more gets lost or stolen](https://bitcoinmagazine.com/culture/bitcoin-self-defense-part-i-wallet-protection-1368758841) than I would like, it's also a fact that most of it has remained un-stolen for over a decade. Recently, there have been improvements:

* [**Trusted hardware chips inside of users' phones**](https://www.androidauthority.com/titan-m2-google-3261547/), effectively creating a much smaller high-security operating system inside the phone that can remain protected even if the rest of the phone gets hacked. Among many other use cases, these chips are increasingly being explored as a way to make [more secure crypto wallets](https://www.getclave.io/).
* **Browsers as the de-facto operating system**. Over the last ten years, there has been a quiet shift from downloadable applications to _in-browser_ applications. This has been largely enabled by [WebAssembly (WASM)](https://webassembly.org/). Even Adobe Photoshop, long cited as a major reason why many people cannot practically use Linux because of its necessity and Linux-incompatibility, is now Linux-friendly thanks to being inside the browser. This is also a large security boon: while [browsers do have flaws](https://techmonitor.ai/technology/cybersecurity/four-big-tech-browsers-hit-by-one-zero-day-vulnerability), in general they come with much more sandboxing than installed applications: apps cannot access arbitrary files on your computer.
* **Hardened operating systems**. [GrapheneOS](https://grapheneos.org/) for mobile exists, and is very usable. [QubesOS](https://www.qubes-os.org/) for desktop exists; it is currently somewhat less usable than Graphene, at least in my experience, but it is improving.
* **Attempts at moving beyond passwords**. Passwords are, unfortunately, difficult to secure both because they are hard to remember, and because [they are easy to eavesdrop on](https://www.independent.co.uk/tech/cyber-security-passwords-hackers-a9070411.html). Recently, there has been a growing movement toward reducing emphasis on passwords, and making multi-factor hardware-based authentication [actually work](https://developers.google.com/identity/passkeys).

However, the _lack_ of cyber defense in other spheres has also led to major setbacks. The need to protect against spam has led to email becoming [very oligopolistic in practice](https://cfenollosa.com/blog/after-self-hosting-my-email-for-twenty-three-years-i-have-thrown-in-the-towel-the-oligopoly-has-won.html), making it very hard to self-host or create a new email provider. Many online apps, [including Twitter](https://www.reuters.com/technology/twitter-now-needs-users-sign-view-tweets-2023-06-30/), are requiring users to be logged in to access content, and blocking IPs from VPNs, making it harder to access the internet in a way that protects privacy. Software centralization is also risky because of ["weaponized interdependence"](https://www.amazon.co.uk/Uses-Abuses-Weaponized-Interdependence/dp/0815738374): the tendency of modern technology to route through centralized choke points, and for the operators of those choke points to use that power to gather information, manipulate outcomes or exclude specific actors - a strategy that seems to even be currently employed [against the blockchain industry itself](https://www.coindesk.com/consensus-magazine/2023/03/22/the-reality-behind-the-crypto-banking-crackdown-operation-choke-point-20-is-here/).

These are concerning trends, because it threatens what has historically been one of my big hopes for why the future of freedom and privacy, despite deep tradeoffs, might still turn out to be bright. In his book ["Future Imperfect"](http://www.daviddfriedman.com/Future_Imperfect/Chapter5.html), David Friedman predicts that we might get a compromise future: the in-person world would be more and more surveilled, but through cryptography, the online world would retain, and even improve, its privacy. Unfortunately, as we have seen, such a counter-trend is far from guaranteed.

**This is where my own emphasis on cryptographic technologies such as blockchains and [zero-knowledge proofs](https://vitalik.ca/general/2021/01/26/snarks.html) comes in**. Blockchains let us create economic and social structures with a "shared hard drive" without having to depend on centralized actors. Cryptocurrency allows individuals to save money and make financial transactions, as they could before the internet with cash, without dependence on trusted third parties that could change their rules on a whim. They can also serve as a fallback anti-sybil mechanism, [making attacks and spam expensive](https://ethresear.ch/t/conditional-proof-of-stake-hashcash/1301) even for users who do not have or do not want to reveal their meat-space identity. Account abstraction, and notably [social recovery wallets](https://vitalik.ca/general/2021/01/11/recovery.html), can protect our crypto-assets, and potentially other assets in the future, without over-relying on centralized intermediaries.

Zero knowledge proofs can be used [for privacy](https://vitalik.ca/general/2022/06/15/using_snarks.html), allowing users to prove things about themselves without revealing private information. For example, wrap a [digital passport signature](https://crypto.stackexchange.com/questions/75058/using-epassport-with-active-chip-authentication-to-sign-documents) in a ZK-SNARK to prove that you are a unique citizen of a given country, _without revealing which citizen you are_. Technologies like this can let us maintain the benefits of privacy and anonymity - properties that are widely agreed as being [necessary for applications like voting](https://en.wikipedia.org/wiki/Secret_ballot) - while still getting security guarantees and fighting spam and bad actors.

<center><br>

![](../../../../images/techno_optimism/0chan.png)

<small>

_A proposed design for a ZK social media system, where moderation actions can happen and users can be penalized, all without needing to know anyone's identity._

</small></center><br>

[Zupass](https://zupass.org/), incubated at [Zuzalu](https://www.palladiummag.com/2023/10/06/why-i-built-zuzalu) earlier this year, is an excellent example of this in practice. This is an application, which has already been used by hundreds of people at Zuzalu and more recently by thousands of people for ticketing at [Devconnect](https://devconnect.org/), that allows you to hold tickets, memberships, ([non-transferable](https://vitalik.ca/general/2022/01/26/soulbound.html)) digital collectibles, and other attestations, and prove things about them all without compromising your privacy. For example, you can prove that you are a unique registered resident of Zuzalu, or a Devconnect ticket holder, _without revealing anything else about who you are_. These proofs can be shown in-person, via a QR code, or digitally, to log in to applications like [Zupoll](https://zupoll.org/), an anonymized voting system available only to Zuzalu residents.

**These technologies are an excellent example of d/acc principles: they allow users and communities to verify trustworthiness without compromising privacy, and protect their security without relying on centralized choke points that impose their own definitions of who is good and bad.** They improve global accessibility by creating better and fairer ways to protect a user or service's security than common techniques used today, such as discriminating against entire countries that are deemed untrustworthy. These are very powerful primitives that could be necessary if we want to preserve a decentralized vision of information security going into the 21st century. Working on defensive technologies for cyberspace more broadly can make the internet more open, safe and free in very important ways going forward.

<span id="info" />

### Info-defense

Cyber-defense, as I have described it, is about situations where it's easy for reasonable human beings to all come to consensus on who the attacker is. If someone tries to hack into your wallet, it's easy to agree that the hacker is the bad guy. If someone tries to DoS attack a website, it's easy to agree that they're being malicious, and are not morally the same as a regular user trying to read what's on the site. There are other situations where the lines are more blurry. It is the tools for improving our defense in these situations that I call "info-defense".

Take, for example, fact checking (aka, preventing "misinformation"). I am a [huge fan of Community Notes](https://vitalik.ca/general/2023/08/16/communitynotes.html), which has done a lot to help users identify truths and falsehoods in what other users are tweeting. Community Notes uses a new algorithm which surfaces not the notes that are the _most popular_, but rather the notes that are _most approved by users across the political spectrum_.

<center><br>

![](../../../../images/techno_optimism/helpfulnote2.png)

_Community Notes in action._

</center><br>

I am also a fan of prediction markets, which can help identify the significance of events _in real time_, before the dust settles and there is consensus on which direction is which. The [Polymarket on Sam Altman](https://polymarket.com/event/sam-back-as-ceo-of-openai) is very helpful in giving a useful summary of the ultimate consequences of hour-by-hour revelations and negotiations, giving much-needed context to people who only see the individual news items and don't understand the significance of each one.

<center><br>

![](../../../../images/techno_optimism/samback.png)

</center><br>

Prediction markets are often flawed. But Twitter influencers who are willing to confidently express what they think "will" happen over the next year are often even more flawed. There is still room to improve prediction markets much further. For example, a major practical flaw of prediction markets is their low volume on all but the most high-profile events; a natural direction to try to solve this would be to have prediction markets that are played by AIs.

Within the blockchain space, there is a particular type of info defense that I think we need much more of. Namely, wallets should be much more opinionated and active in helping users determine the meaning of things that they are signing, and protecting them from fraud and scams. This is an intermediate case: what is and is not a scam is less subjective than perspectives on controversial social events, but it's more subjective than telling apart legitimate users from DoS attackers or hackers. Metamask has an scam database already, and automatically blocks users from visiting scam sites:

<center><br>

![](../../../../images/techno_optimism/scamblock.png)

</center><br>

Applications like [Fire](https://www.joinfire.xyz/) are an example of one way to go much further. However, security software like this should not be something that requires explicit installs; it should be part of crypto wallets, or even browsers, by default.

Because of its more subjective nature, info-defense is inherently more collective than cyber-defense: you need to somehow plug into a large and sophisticated group of people to identify what might be true or false, and what kind of application is a deceptive ponzi. There is an opportunity for developers to go much further in developing effective info-defense, and in hardening existing forms of info-defense. Something like Community Notes could be included in browsers, and cover not just social media platforms but also the whole internet.

<span id="social" />

### Social technology beyond the "defense" framing

To some degree, I can be justifiably accused of shoehorning by describing some of these info technologies as being about "defense". After all, defense is about helping well-meaning actors be protected from badly-intentioned actors (or, in some cases, from nature). Some of these social technologies, however, are about _helping well-intentioned actors form consensus_.

A good example of this is [pol.is](https://pol.is/home), which uses an algorithm similar to Community Notes (and which predates Community Notes) to help communities identify points of agreement between sub-tribes who otherwise disagree on a lot. [Viewpoints.xyz](https://viewpoints.xyz/) was inspired by pol.is, and has a similar spirit:

<center><br>

![](../../../../images/techno_optimism/viewpoints.png)

</center><br>

Technologies like this could be used to enable more decentralized governance over contentious decisions. Again, blockchain communities are a good testing ground for this, and one where such algorithms have already shown valuable. Generally, decisions over which improvements ("[EIPs](https://eips.ethereum.org/)") to make to the Ethereum protocol are made by a fairly small group in meetings called "[All Core Devs calls](https://github.com/ethereum/pm)". For highly technical decisions, where most community members have no strong feelings, this works reasonably well. For more consequential decisions, which affect protocol economics, or more fundamental values like immutability and censorship resistance, this is often not enough. Back in 2016-17, when a series of contentious decisions around implementing the [DAO fork](https://en.wikipedia.org/wiki/The_DAO), reducing issuance and (not) [unfreezing the Parity wallet](https://www.cnbc.com/2017/11/08/accidental-bug-may-have-frozen-280-worth-of-ether-on-parity-wallet.html), tools like Carbonvote, as well as social media voting, helped the community and the developers to see which way the bulk of the community opinion was facing.

<center><br>

![](../../../../images/techno_optimism/carbonvote.png)

_Carbonvote on the DAO fork._

</small></center><br>

Carbonvote [had its flaws](https://vitalik.ca/general/2017/12/17/voting.html): it relied on ETH holdings to determine who was a member of the Ethereum community, making the outcome dominated by a few wealthy ETH holders ("whales"). With modern tools, however, we could make a much better Carbonvote, leveraging multiple signals such as [POAPs](https://poap.xyz/), Zupass stamps, [Gitcoin passports](https://passport.gitcoin.co/), [Protocol Guild memberships](https://protocol-guild.readthedocs.io/en/latest/), as well as ETH (or even solo-staked-ETH) holdings to gauge community membership.

Tools like this could be used by any community to make higher-quality decisions, find points of commonality, coordinate (physical or digital) migrations or do a number of other things without relying on opaque centralized leadership. This is not defense acceleration per se, but it can certainly be called democracy acceleration. Such tools could even be used to improve and democratize the governance of key actors and institutions working in AI.

<span id="paths" />

## So what are the paths forward for superintelligence?

The above is all well and good, and could make the world a much more harmonious, safer and freer place for the next century. However, it does not yet address the big elephant in the room: superintelligent AI.

The default path forward suggested by many of those who worry about AI essentially leads to a **minimal AI world government**. Near-term versions of this include a proposal for a ["multinational AGI consortium"](https://www.conjecture.dev/research/multinational-agi-consortium-magic-a-proposal-for-international-coordination-on-ai) ("MAGIC"). Such a consortium, if it gets established and succeeds at its goals of creating superintelligent AI, would have a natural path to becoming a de-facto minimal world government. Longer-term, there are ideas like the ["pivotal act"](https://arbital.com/p/pivotal/) theory: we create an AI that performs a _single one-time act_ which rearranges the world into a game where from that point forward humans are still in charge, but where the game board is somehow more defense-favoring and more fit for human flourishing. 

The main practical issue that I see with this so far is that _people don't seem to actually trust any specific governance mechanism with the power to build such a thing_. This fact becomes stark when you look at the results to my recent Twitter polls, asking if people would prefer to see AI monopolized by a single entity with a decade head-start, or AI delayed by a decade for everyone:

<br><center><table style="width:90%"><tr style="border:0px">
<td style="border:0px; width:40%">
    
![](../../../../images/techno_optimism/poll1.png)

</td>
<td style="border:0px; width:40%" rowspan="2">
        
![](../../../../images/techno_optimism/poll2.png)
 
</td></tr><tr style="border:0px"><td style="border:0px">

![](../../../../images/techno_optimism/poll3.png)

</td></tr></table></center><br>

The size of each poll is small, but the polls make up for it in the uniformity of their result across a wide diversity of sources and options. **In nine out of nine cases, the majority of people would rather see highly advanced AI delayed by a decade outright than be monopolized by a single group, whether it's a corporation, government or multinational body**. In seven out of nine cases, delay won by at least two to one. This seems like an important fact to understand for anyone pursuing AI regulation. Current approaches have been focusing on creating licensing schemes and regulatory requirements, trying to restrict AI development to a smaller number of people, but these have seen popular pushback precisely because people don't want to see anyone monopolize something so powerful. Even if such top-down regulatory proposals reduce risks of extinction, they risk increasing the chance of some kind of permanent lock-in to centralized totalitarianism. Paradoxically, could agreements banning extremely advanced AI research _outright_ (perhaps with exceptions for biomedical AI), combined with measures like _mandating_ open source for those models that are not banned as a way of reducing profit motives while further improving equality of access, be _more_ popular?

The main approach preferred by opponents of the "let's get one global org to do AI and make its governance really really good" route is **[polytheistic AI](https://twitter.com/balajis/status/1725595769003221092): intentionally try to make sure there's lots of people and companies developing lots of AIs, so that none of them grows far more powerful than the other**. This way, the theory goes, even as AIs become superintelligent, we can retain a balance of power.

This philosophy is interesting, but my experience trying to ensure "polytheism" within the Ethereum ecosystem does make me worry that this is an inherently unstable equilibrium. In Ethereum, we have intentionally tried to ensure decentralization of many parts of the stack: ensuring that there's no single codebase that controls [more than half of the proof of stake network](https://clientdiversity.org/), trying to counteract the [dominance of large staking pools](https://fortune.com/2022/06/11/lido-largest-ether-staking-service-has-centralization-problem-raising-red-flags/), improving [geographic decentralization](https://ethernodes.org/), and so on. Essentially, Ethereum is actually attempting to execute on the old libertarian dream of a market-based society that uses social pressure, rather than government, as the antitrust regulator. To some extent, this has worked: the [Prysm client's dominance](https://cryptoslate.com/ethereums-client-diversity-with-66-running-prysm-is-the-merge-safe-to-pursue/) has dropped from above 70% to under 45%. But this is not some automatic market process: it's the result of human intention and coordinated action.

My experience within Ethereum is mirrored by learnings from the broader world as a whole, where many markets have proven to be [natural monopolies](https://en.wikipedia.org/wiki/Natural_monopoly). With superintelligent AIs acting independently of humans, the situation is even more unstable. Thanks to [recursive self-improvement](https://www.lesswrong.com/tag/recursive-self-improvement), the strongest AI may pull ahead very quickly, and once AIs are more powerful than humans, there is no force that can push things back into balance.

Additionally, even if we _do_ get a polytheistic world of superintelligent AIs that ends up stable, we still have the _other_ problem: that we get a universe where humans are pets.

<span id="merge" />

### A happy path: merge with the AIs?

A different option that I have heard about more recently is to **focus less on AI as something separate from humans, and more on tools that _enhance_ human cognition rather than _replacing_ it**.

One near-term example of something that goes in this direction is AI drawing tools. Today, the most prominent tools for making AI-generated images only have one step at which the human gives their input, and AI fully takes over from there. An alternative would be to focus more on AI versions of Photoshop: tools where the artist or the AI might make an early draft of a picture, and then the two collaborate on improving it with a process of real-time feedback.

<center><br>

![](../../../../images/techno_optimism/genfill.png)

_Photoshop generative AI fill, 2023. [Source](https://www.elegantthemes.com/blog/design/photoshop-ai). I tried, it and it takes time to get used to but it actually works quite well!_
    
</center><br>

Another direction in a similar spirit is the [Open Agency Architecture](https://www.lesswrong.com/posts/5hApNw5f7uG8RXxGS/the-open-agency-model), which proposes splitting the different parts of an AI "mind" (eg. making plans, executing on plans, interpreting information from the outside world) into separate components, and introducing diverse human feedback in between these parts.

So far, this sounds mundane, and something that almost everyone can agree that it would be good to have. The economist Daron Acemoglu's work is far from this kind of AI futurism, but his new book [Power and Progress](https://www.amazon.com/Power-Progress-Thousand-Year-Technology-Prosperity/dp/1541702530) hints at wanting to see more of exactly these types of AI.

**But if we want to extrapolate this idea of human-AI cooperation further, we get to more radical conclusions**. Unless we create a world government powerful enough to detect and stop every small group of people hacking on individual GPUs with laptops, someone is going to create a superintelligent AI eventually - one that can think a [thousand times faster](https://www.lesswrong.com/posts/Ccsx339LE9Jhoii9K/slow-motion-videos-as-ai-risk-intuition-pumps) than we can - and no combination of humans using tools with their hands is going to be able to hold its own against that. And so we need to take this idea of human-computer cooperation much deeper and further.

**A first natural step is [brain-computer interfaces](https://en.wikipedia.org/wiki/Brain%E2%80%93computer_interface)**. Brain-computer interfaces can give humans much more direct access to more-and-more powerful forms of computation and cognition, reducing the two-way communication loop between man and machine from seconds to milliseconds. This would also greatly reduce the "mental effort" cost to getting a computer to help you gather facts, give suggestions or execute on a plan.

Later stages of such a roadmap admittedly get weird. In addition to brain-computer interfaces, there are various paths to improving our brains directly through innovations in biology. An eventual further step, which merges both paths, may involve [uploading our minds](https://en.wikipedia.org/wiki/Mind_uploading) to run on computers directly. This would also be the ultimate d/acc for physical security: protecting ourselves from harm would no longer be a challenging problem of protecting inevitably-squishy human bodies, but rather a much simpler problem of making data backups.

<center><br>

![](../../../../images/techno_optimism/mindpaths.png)
    
</center><br>

Directions like this are sometimes met with worry, in part because they are irreversible, and in part because they may give powerful people more advantages over the rest of us. Brain-computer interfaces in particular have dangers - after all, we are talking about _literally reading and writing to people's minds_. These concerns are exactly why I think it would be ideal for a leading role in this path to be held by a security-focused open-source movement, rather than closed and proprietary corporations and venture capital funds. Additionally, all of these issues are _worse_ with superintelligent AIs that operate independently from humans, than they are with augmentations that are closely tied to humans. The divide between "enhanced" and "unenhanced" already exists today due to [limitations in who can and can't use ChatGPT](https://www.digitaltrends.com/computing/these-countries-chatgpt-banned/).

**If we want a future that is both superintelligent _and_ "human", one where human beings are not just pets, but actually retain meaningful agency over the world, then it feels like something like this is the most natural option**. There are also good arguments why this could be a safer AI alignment path: by involving human feedback at each step of decision-making, we reduce the incentive to offload high-level planning responsibility to the AI itself, and thereby reduce the chance that the AI does something totally unaligned with humanity's values on its own.

One other argument in favor of this direction is that it may be more _socially_ palatable than simply shouting "[pause AI](https://twitter.com/PauseAI)" without a complementary message providing an alternative path forward. It will require a philosophical shift from the current mentality that tech advancements that touch humans are dangerous but advancements that are separate from humans are by-default safe. But it has a huge countervailing benefit: _it gives developers something to do_. Today, the AI safety movement's primary message to AI developers seems to be "[you should just stop](https://twitter.com/So8res/status/1715380167911067878)". One can [work on alignment research](https://forum.effectivealtruism.org/posts/7WXPkpqKGKewAymJf/how-to-pursue-a-career-in-technical-ai-alignment), but today this lacks economic incentives. Compared to this, the common e/acc message of "you're already a hero just the way you are" is understandably extremely appealing. A d/acc message, one that says "you should build, and build profitable things, but be much more selective and intentional in making sure you are building things that help you and humanity thrive", may be a winner.

<span id="compatible" />

## Is d/acc compatible with your existing philosophy?

* If you are an **e/acc**, then d/acc is a subspecies of e/acc - just one that is much more selective and intentional.
* If you are an [**effective altruist**](https://www.effectivealtruism.org/), then d/acc is a re-branding of the effective-altruist idea of [differential technology development](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4213670), though with a greater emphasis on liberal and democratic values.
* If you are a **libertarian**, then d/acc is a sub-species of techno-libertarianism, though a more pragmatic one that is more critical of "the techno-capital machine", and willing to accept government interventions today (at least, if cultural interventions don't work) to prevent much worse un-freedom tomorrow.
* If you are a **Pluralist**, in the [Glen Weyl sense of the term](https://www.plurality.net/v/eng/), then d/acc is a frame that can easily include the emphasis on better democratic coordination technology that Plurality values.
* If you are a **public health advocate**, then d/acc ideas can be a source of a broader long-term vision, and opportunity to find common ground with "tech people" that you might otherwise feel at odds with.
* If you are a **blockchain advocate**, then d/acc is a more modern and broader narrative to embrace than the fifteen-year-old emphasis on hyperinflation and banks, which puts blockchains into context as one of many tools in a concrete strategy to build toward a brighter future.
* If you are a **[solarpunk](https://builtin.com/greentech/solarpunk)**, then d/acc is a subspecies of solarpunk, and incorporates a similar emphasis on intentionality and collective action.
* If you are a **[lunarpunk](https://www.coindesk.com/layer2/2022/09/20/what-are-solarpunk-and-lunarpunk-anyway/)**, then you will appreciate the d/acc emphasis on informational defense, through maintaining privacy and freedom.

<span id="brighteststar" />

## We are the brightest star

I love technology because technology expands human potential. Ten thousand years ago, we could build some hand tools, change which plants grow on a small patch of land, and [build basic houses](https://www.newscientist.com/article/2392894-earliest-evidence-of-buildings-made-from-wood-is-476000-years-old/). Today, we can build [800-meter-tall towers](https://en.wikipedia.org/wiki/Burj_Khalifa), store the entirety of recorded human knowledge in a device we can hold in our lands, communicate instantly across the globe, double our lifespan, and live happy and fulfilling lives without fear of our best friends regularly dropping dead of disease.

<center><br>

![](../../../../images/techno_optimism/civprogress.png)

_We started from the bottom, now we're here._

</center><br>

I believe that these things are deeply good, and that expanding humanity's reach even further to the planets and stars is deeply good, because **I believe humanity is deeply good**. It is fashionable in some circles to be skeptical of this: the [voluntary human extinction movement](https://en.wikipedia.org/wiki/Voluntary_Human_Extinction_Movement) argues that the Earth would be better off without humans existing at all, and many more want to see [much smaller number of human beings](https://www.scientificamerican.com/article/population-decline-will-change-the-world-for-the-better/) see the light of this world in the centuries to come. It is common to [argue](https://www.vox.com/science-and-health/2017/12/14/16687388/cruelty-border-immigration-psychology-human-nature) that [humans are bad](https://www.advisory.com/daily-briefing/2018/10/31/people-are-terrible) because we cheat and steal, engage in colonialism and war, and mistreat and annihilate other species. My reply to this style of thinking is one simple question: **compared to what?**

Yes, human beings are often mean, but we much more often show kindness and mercy, and work together for our common benefit. Even during wars we often take care to protect civilians - certainly not nearly enough, but also far more than [we did 2000 years ago](https://bmcr.brynmawr.edu/2022/2022.01.23/). The next century may well bring widely available non-animal-based meat, eliminating the [largest moral catastrophe](https://www.openphilanthropy.org/focus/farm-animal-welfare/) that human beings can justly be blamed for today. Non-human animals are not like this. There is no situation where a cat will adopt an entire lifestyle of refusing to eat mice as a matter of ethical principle. The Sun is growing brighter every year, and in about [one billion years](https://theconversation.com/will-the-earth-last-forever-203021), it is expected that this will make the Earth too hot to sustain life. Does the Sun even _think_ about the genocide that it is going to cause?

And so it is my firm belief that, out of all the things that we have known and seen in our universe, **we, humans, are the brightest star**. We are the one thing that we know about that, even if imperfectly, sometimes make an earnest effort to care about "the good", and adjust our behavior to better serve it. Two billion years from now, if the Earth or any part of the universe still bears the beauty of Earthly life, it will be human artifices like space travel and [geoengineering](https://nap.nationalacademies.org/catalog/25762/reflecting-sunlight-recommendations-for-solar-geoengineering-research-and-research-governance) that will have made it happen.

<center><br>

![](../../../../images/techno_optimism/dacc_2.png)

</center><br>

We need to build, and accelerate. But there is a very real question that needs to be asked: what is the thing that we are accelerating towards? The 21st century may well be [_the_ pivotal century](https://www.cold-takes.com/most-important-century/) for humanity, the century in which our fate for millennia to come gets decided. Do we fall into one of a number of traps from which we cannot escape, or do we find a way toward a future where we retain our freedom and agency? These are challenging problems. But I look forward to watching and participating in our species' grand collective effort to find the answers.
