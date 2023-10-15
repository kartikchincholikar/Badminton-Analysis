# About
An attempt to collect and use data to find a player's "Patterns of Play". These can be exploited in a match.\
Here is a sample report:

![Sample report](https://i.imgur.com/K9qGB9z.jpg)

## Rally Simulator
![Rally Simulator](https://i.imgur.com/jXJhdYy.png)


# Data
Here is an example rally :
> b 7 d 3 a 7b g 3 plafowon 

We can read this as :

**b**    : position on court\
**7**    : position on court ( an overhead has been hit )\
**d**    : position on court\
**3**    : position on court\
**a**    : position on court\
**7b**  : position on court ( a backhand has been hit )\
**g**    : position on court\
**3**    : position on court\
**pla**  : end of the rally because the shuttle was hit "OUT"\
**fo**   : the error was forced\
**won**  : the rally was won by the player.

##

Each of these tokens are represented as vectors (distributed or one hot) and can be fed as input to an RNN.
The RNN can predict where the next shot is most likely to be hit, by looking at the previous shots.

"Patterns of Play" can also be found by simply describing the sequence of events as a Markov Chain.
