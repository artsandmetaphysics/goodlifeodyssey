---
title: 'Altera: Physical Laws'
description: 'A detailed description of the physical laws of Altera.'
status: incomplete
order: 501
---

## Physical Laws

Unlike our universe, where we do not have definite knowledge of its physical laws, we *do* have definite knowledge of Altera's physical laws because we have contrived them.  In fact, Altera's physical laws are designed so that we could easily simulate them on a computer in our universe.

Altera has two finite spatial dimensions that wrap around on themselves.  If an entity moves beyond the edge of Altera, it reappears at the opposing end.  Because each dimension is finite, Altera has a definite and fixed size.  There exist two types of entities in Altera.  Entities exist at particular discrete locations along each dimension.  The first type of entity is a "creature", which we shall call a Nook.  The second type of entity we shall call "food".

Altera is a dynamic world, with a temporal dimension.  Nooks can sense their surroundings and can move.  Time progresses in discrete steps.  During each time step, Nooks may decide to move onto any of the four immediately adjacent locations, do nothing, or perform one of a small number of other actions which we will introduce shortly.

Nooks have a single externally observable property, which we refer to as its "weight".  We may represent a weight as a number between 1 and 255.  Food has a weight of 1.  Nooks may decide to "eat" the contents of any one of the four squares immediately adjacent to its current location.  If that square contains food, the Nook's weight increases by 1, up until it reaches a maximum weight of 255.  We call a Nook whose weight is 255 a "fat" Nook.  If on the other hand, that square contains another Nook, it will eat it so long as its weight is less its own.  Finally, if the square is empty, nothing will occur.  When a Nook eats another Nook, its weight becomes the sum of its previous weight and the weight of the Nook that it ate, unless the resulting weight would be greater than 255, in which case the Nook's weight would simply be 255.

If a Nook moves into a location containing food or another Nook that weights less than itself that other Nook is "pushed" into the opposing square.  If the opposing square also contains an object, the Nook is still able to push it, so long as the sum of the weights is less than itself, and so on.

Nooks have one sense which we shall call "vision".  Their vision is discrete, and they can see in all directions simultaneously.  At any given moment, their vision allows them to "see" a 7x7 grid centered on their location.  At each location, they can sense the weight of the being at that location, including themselves at the central square.  Thus, food and Nooks with a weight of 1 will appear the same.

Nooks may decide to "reproduce"---to split themselves into two Nooks.  If a Nook decides to reproduce, they must choose which of the adjacent four squares the new Nook will emerge onto.  The weight of the parent Nook is split in two; if its original weight was an even number, the parent and child will both have half the original weight; if the original weight was an odd number, the parent will keep the indivisible extra portion.  The child Nook will be a nearly identical replica of the parent Nook, but it may undergo a "mutation" during the reproductive process.  We will discuss this more in the next section.

Every 65,536 moments in time each Nook's weight drops by 1.  This event is called a "starvation".  If a Nook's weight is 1 when this occurs, they will "die" and the grid location that it had occupied will become empty.

Altera has a single "conservation law"---the sum of the weights of all Nooks and food is always equal to the number of spatial locations in the universe.  Food appears on squares throughout Altera so as to ensure this is true.  The locations are pseudo-random, but new food is always placed on empty squares.  Food never moves or decays.  Once it has appeared, it occupies its location indefinitely until a Nook eats it or nudges it into another square.  There are two events that occur new food to be "grown" in Altera.  The first is during a starvation.  The second occurs when a Nook eats something such that its weight exceeds 255.

There are several details of Altera's physical laws that we have omitted.  In particular, the order in which Nook actions occurs, which can be important in certain situations.  For example, if two Nooks of similar weight move into a square at the same time or if a Nook attempts to reproduce but is surrounded by other Nooks.

## Mind

There is an essential aspect of Altera that we have not discussed---the means by which Nooks "decide" how to act.  At each moment in time Nooks decide between doing nothing, moving in any of four directions, eating in any of four directions, or reproducing in any of four directions.  Hence a Nook must decide between thirteen alternatives at each moment.  If a Nook decides to take an action that it is physically incapable of making (for example reproducing when its weight is 1), it will instead do nothing.

When making these decisions, Nooks will have available their immediate sensory data---their view of the surroundings and their knowledge of their weight.  They also will have some "memory" and "knowledge" derived from their past interactions with their surroundings.  These memory and knowledge is encoded in the Nook's "mind".

The Nook mind changes over time in two different manners.  It changes over the course of a particular Nook's existence, which we refer to as "acclimatization", and it changes each time a Nook reproduces, which we refer to as "evolution".  The "evolution" process is pseudo-random.

We will avoid discussing the structure of the Nook mind, because it is not clear what it would be, and because it would be complicated and likely irrelevant to the purposes of this thought experiment.  It is worth noting that the state of the mind may be very large.  For example, it may have as much information content as the human brain is in our universe.  It is likely that evolutionary change would involve altering the structure of the mind---how much data must be retained and what the data means, while acclimatization would involve changing the particular data without altering its structure or meaning.

It is important to note that the Nook mind would be finite, i.e. it could be represented as a (perhaps very long) series of numbers.

## Comments on Physical Laws

Let's compare our current understanding of our physical laws to Altera's.

Our universe has one time and three spatial dimensions.  All of these dimensions appear continuous to us, however, they may be discrete at a small enough scale.  Space, time, matter, and energy are intertwined according to general relativity.  Altera has time and two spatial dimensions.  All are discrete.  Matter occupies space and time, but does not affect it; time passes consistently for all Nooks.

In our universe, motion is an interaction between particles that can be described with mathematical equations.  In Altera, movement is an algorithmic phenomena governed by the minds of the Nooks.  It is natural, given the nomenclature we are using, to conceive of the Nooks as having a "will" that motivates their movements.  It is also possible to conceive of the Nooks as "particles".

Our universe has a variety of particles that interact to form atoms, molecules, and organic beings of substantial complexity.  Our particles have several properties---a mass and spin, and sometimes a color, flavor, or charge.  Their interactions with each other can be described using mathematical equations.  Altera has two types of particles---food and Nook.  They both have a single property---their weight.  They interact with each other in a direct algorithmic manner via the Nook's ability to eat and see other particles.  Unlike our universe, where complexity only arises through the composition of simple particles, in Altera, complexity can arise in the individual Nook as well as through composition of many Nooks.

In our universe, beings sense their surroundings using complex organs built from many particles.  These organs have evolved over time, and transmit and amplify the interactions of the constituent particles.  Humans have since constructed even more complex sensing tools.  Nooks have a sense of vision "built" into them directly, or, this is seen as their.  If we conceptualize the Nook as a being with a will, then this feels oddly specific.  If we conceptualize the Nook as a particle, it seems less odd.

## Determinism

Altera is a completely deterministic world.  If a given world state were re "played" it would always evolve in an identical manner.

The Nooks would likely not be aware of this, and it is not even clear that they *could ever* prove whether the world was deterministic.
