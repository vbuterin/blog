[category]: <> (General,Fun)
[date]: <> (2019/12/24)
[title]: <> (Christmas Special)
[pandoc]: <> (--mathjax)

Since it's Christmas time now, and we're theoretically supposed to be enjoying ourselves and spending time with our families instead of waging endless holy wars on Twitter, this blog post will offer some games that you can play with your friends that will help you have fun _and_ at the same time understand some spooky mathematical concepts!

### 1.58 dimensional chess

<center><br>
[![](../../../../images/christmas-files/chess_tweet.jpg)](https://twitter.com/el33th4xor/status/1138777837320716288)
<br><br>
</center>

This is a variant of chess where the board is set up like this:

<center><br>
![](../../../../images/christmas-files/chess.png)
<br><br>
</center>

The board is still a normal 8x8 board, but there are only 27 open squares. The other 37 squares should be covered up by checkers or Go pieces or anything else to denote that they are inaccessible. The rules are the same as chess, with a few exceptions:

* White pawns move up, black pawns move left. White pawns take going left-and-up or right-and-up, black pawns take going left-and-down or left-and-up. White pawns promote upon reaching the top, black pawns promote upon reaching the left.
* No en passant, castling, or two-step-forward pawn jumps.
* Chess pieces cannot move onto _or through_ the 37 covered squares. Knights cannot move onto the 37 covered squares, but don't care what they move "through".

The game is called 1.58 dimensional chess because the 27 open squares are chosen according to a pattern based on the [Sierpinski triangle](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle). You start off with a single open square, and then every time you double the width, you take the shape at the end of the previous step, and copy it to the top left, top right and bottom left corners, but leave the bottom right corner inaccessible. Whereas in a one-dimensional structure, doubling the width increases the space by 2x, and in a two-dimensional structure, doubling the width increases the space by 4x (4 = 2<sup>2</sup>), and in a three-dimensional structure, doubling the width increases the space by 8x (8 = 2<sup>3</sup>), here doubling the width increases the space by 3x (3 = 2<sup>1.58496</sup>), hence "1.58 dimensional" (see [Hausdorff dimension](https://en.wikipedia.org/wiki/Hausdorff_dimension) for details).

The game is substantially simpler and more "tractable" than full-on chess, and it's an interesting exercise in showing how in [lower-dimensional spaces](https://en.wikipedia.org/wiki/Flatland) defense becomes much easier than offense. Note that the relative value of different pieces may change here, and new kinds of endings become possible (eg. you can checkmate with just a bishop).

### 3 dimensional tic tac toe

<center><br>
![](../../../../images/christmas-files/tic4.png){.padded}
<br><br>
</center>

The goal here is to get 4 in a straight line, where the line can go in any direction, along an axis or diagonal, including between planes. For example in this configuration X wins:

<center><br>
![](../../../../images/christmas-files/tic4_2.png){.padded}
<br><br>
</center>

It's considerably harder than [traditional 2D tic tac toe](https://www.quora.com/Is-there-a-way-to-never-lose-at-Tic-Tac-Toe), and hopefully much more fun!

### Modular tic-tac-toe

Here, we go back down to having two dimensions, except we allow lines to wrap around:

<center><br>
![](../../../../images/christmas-files/tic4_3.png)
<br><small><i>X wins</i></small></center>
<br><br>

Note that we allow diagonal lines with any slope, as long as they pass through all four points. Particularly, this means that lines with slope +/- 2 and +/- 1/2 are admissible:

<center><br>
![](../../../../images/christmas-files/tic4_4.png)
<br><br>
</center>

Mathematically, the board can be interpreted as a 2-dimensional vector space over [integers modulo 4](https://en.wikipedia.org/wiki/Modular_arithmetic), and the goal being to fill in a line that passes through four points over this space. Note that there exists at least one line passing through any two points.

### Tic tac toe over the 4-element binary field

<center><br>
![](../../../../images/christmas-files/tic4_5.png){.padded}
<br><br>
</center>

Here, we have the same concept as above, except we use an even spookier mathematical structure, the [4-element field](https://en.wikipedia.org/wiki/Finite_field#Field_with_four_elements) of polynomials over $Z_2$ modulo $x^2 + x + 1$. This structure has pretty much no reasonable geometric interpretation, so I'll just give you the addition and multiplication tables:

<center><br>
![](../../../../images/christmas-files/tic4_6.png){.padded}
<br><br>
</center>

OK fine, here are all possible lines, excluding the horizontal and the vertical lines (which are also admissible) for brevity:

<center><br>
<img src="../../../../images/christmas-files/tic4_7.png" style="width: 450px" class="padded" />
<br><br>
</center>

The lack of geometric interpretation does make the game harder to play; you pretty much have to memorize the twenty winning combinations, though note that they are _basically_ rotations and reflections of the same four basic shapes (axial line, diagonal line, diagonal line starting in the middle, that weird thing that doesn't look like a line).

### Now play 1.77 dimensional connect four. I dare you.

<center><br>
<img src="../../../../images/christmas-files/tic4_8.png" style="width: 450px" />
<br><br>
</center>

### Modular poker

Everyone is dealt five (you can use whatever variant poker rules you want here in terms of how these cards are dealt and whether or not players have the right to swap cards out). The cards are interpreted as: jack = 11, queen = 12, king = 0, ace = 1. A hand is stronger than another hand, if it contains a longer sequence, with any constant difference between consecutive cards (allowing wraparound), than the other hand.

Mathametically, this can be represented as, a hand is stronger if the player can come up with a line $L(x) = mx+b$ such that they have cards for the numbers $L(0)$, $L(1)$ ... $L(k)$ for the highest $k$.

<center><br>
![](../../../../images/christmas-files/cards1.png)
<br><small><i>Example of a full five-card winning hand. y = 4x + 5.</i></small></center>
<br><br>

To break ties between equal maximum-length sequences, count the number of distinct length-three sequences they have; the hand with more distinct length-three sequences wins.

<center><br>
![](../../../../images/christmas-files/cards2.png)
<br><small><i>This hand has four length-three sequences: K 2 4, K 4 8, 2 3 4, 3 8 K. This is rare.</i></small></center>
<br><br>

Only consider lines of length three or higher. If a hand has three or more of the same denomination, that counts as a sequence, but if a hand has two of the same denomination, any sequences passing through that denomination only count as one sequence.

<center><br>
![](../../../../images/christmas-files/cards3.png)
<br><small><i>This hand has no length-three sequences.</i></small></center>
<br><br>

If two hands are completely tied, the hand with the higher highest card (using J = 11, Q = 12, K = 0, A = 1 as above) wins.

Enjoy!
