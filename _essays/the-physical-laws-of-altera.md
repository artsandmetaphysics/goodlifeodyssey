---
title: 'The Physical Laws of Altera'
description: 'An introduction to the workings of Altera---a 2D world within which we will investigate many philosophical questions.'
status: incomplete
order: 500
---

## Motivation

I have found it helpful, when asking questions about our universe, to consider how analogous questions could be asked and answered by beings in an alternate, simpler universe.  I call this universe Altera.  Answers to many questions, when asked in our universe, are obscured by its complex nature and our uncertain place within it.  Analogous questions, when asked in Altera, are often plainly answered.  We may then be able to generalize these answers to our universe more clearly than if we had pursued them directly.

Imagining an alternate universe such as Altera is difficult because our minds continually pull us back into our own.  We must remember that to the beings within it Altera is real.  Our sense of normality is biased by our familiarity with, and existence in, our universe.  But we have no firm reason to believe that our universe couldn't have been different, or that alternate universes couldn't exist.

Our ability to imagine alternate universes is obstructed because we must describe them using familiar language.  This difficulty could have been helped somewhat by using made-up words. However, it was burdensome to keep track of them so I repurposed words from our universe.  I indicate when I am repurposing a word by placing it in quotes the first time it is used as such.

Despite these difficulties, I have been able to clarify my thoughts using this approach, and I hope that others find similar success.  At least it may be a clear exposition of many questions previously asked and answered by philosophers.  At most, it may lead to new insights.

This sort of thought experiment has been performed before.  The book *Flat Land*, written by Edwin Abbott Abbott, is the earliest example of which I am aware.  In *Flat Land*, Abbott investigates the limitations of two-dimensional beings understanding a third dimension.  With this regard, the book was successful, however, the extent of his investigation was limited.  There are more questions to explore---especially questions about knowledge, metaphysics, and ethics.

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

## Evolution

Altera's physical laws were designed so that the Nook's minds could evolve.  The Nook's are competing for scare Food to avoid starving to death.  Nooks that reproduce more frequently are better adapted for their environment.  They will propogate their Mind more then less adapted Nooks.  Beneficial random mutations will accumulate.

## Conciousness

Imagine that, after a long period of time, the Nooks became concious.  They developed language, which could be transmitted from one Nook to another via a series of pauses and movements.  The developed civilization, wherein different Nooks played different roles.  Some Nooks were responsible for gathering food and stockpiling it.  Other Nooks were responsible for defense and protection of the food.  Some Nooks were kings or priests.  Others were dancers and poets.  A wealthy civilization could encode knowledge using food, placed at regular intervals corresponding to their "spoken" language.  In order to transmit information more quickly across their world, they could form communication chains, perhaps by having heavy Nooks push long chains of food.

It is also quite possible, even likely, that conciousness would never develop.  Just because the elements necessary for evolution to occur are present, does not necessitate the development of consciousness.  Perhaps the laws of physics that have been contrived are too simplistic to support conciousness.  Or perhaps they lead evolution inevitably to a local maximum, or a dead world state wherein all of the Nooks perish.

## Science

The Nooks could perform scientific experiments to better understand the physical laws of Altera.  Some laws would be easier to understand than others.  They could learn when certain actions would be "allowed".  Perhaps, if all of the Nooks in the universe collaborated together, they could somehow deduce the equation for the pseudo random number generator that governs food placement.

Well before they developed conciousness, their minds would evolve to account for the physical laws of their universe.  Thus in a sense they would "know" the physical laws without consciously knowing them.  In the same way that insects have evolved to account for gravity despite not being aware of knowing the physical laws of gravity.

Perhaps the early concious Nooks would form some sort of religion to explain their existence.  It seems likely that food, and its random placement, would be central to their early religions.

## Determinism

Altera is a completely deterministic world.  If a given world state were re "played" it would always evolve in an identical manner.

The Nooks would likely not be aware of this, and it is not even clear that they *could ever* prove whether the world was deterministic.

## Philosophy

These are three central questions I ask myself.  To a first approximation, each of these questions corresponds to a branch of philosophy.

1. How can one know things? (Epistemology)
2. What is the nature of reality? (Metaphysics)
3. What should one do? (Ethics)

I believe that these questions are interdependent, and they can not be answered in isolation from one another.  In the remainder of this essay we will consider these questions from a concious Nook's point of view.

## Appearance and Reality

Is there any knowledge in Altera that is so certain that no reasonable Nook could deny it?

Lets begin with Nook's sense of sight.  They see the weights of the discrete objects surrounding them.  Can they be certain of their sensory knowledge?

In our world, we describe the appearance of objects using vague language.  We say an object is red, but what we mean is the object is red under usual lighting conditions.  Apart from describing our personal sensory experiences, it is difficult to state much about the "color" of the physical object.  Precisely describing the object's color and appearance would require knowledge of our current scientific theory.

We sense particles in our universe slowly and in aggregate.  This may be because our minds and sense organs are constructed out of particles too.  Perhaps, to achieve the complex structure required for conscious sensing, our minds and senses must operate above the dimension of particles.

The Nook's sense of sight is simpler than ours, and it is embedded in the Alteran physical laws.  The complexity of Nook minds can increase without requiring them to increase in space or using more resources.  For this reason, it is possible that highly evolved, concious Nooks would still be aware of their bare sensory input.

It is also possible that they would not be aware of their immediate sensory input.  Perhaps, like is likely in our universe, it is not evolutionarily beneficial to be aware of small details like this, and their minds abstract and condense their sensory input for their minds to consider and react to.

Since Nook's physical size is fixed, I suspect that even highly evolved Nooks will continue to be aware of the discrete locations in Altera, but I can imagine their minds blending many individual sets of 7x7 weights sensed at each timestep, into larger views.  This would be similar to how our eyes, visual cortex, abstract objects.  Optical illusions occur when these abstractions occur at a low level in our sensory chain, causing us to perceive things that are not there.

If this sort of abstraction were to occur, the

- senses abstracting low-level inputs; we are unaware of the individual neural inputs; we are also unaware of individual quantum events.  Not necessarily brcause we *couldn't* be (our eyes may be able to detect single photons), but because our relatively vast size makes individual particles less interesting or relevant to our survival.  We require a lot of food to keep the apparatus going, if we thought and operated on the level of individual particles, we would never aggregate enough food to sustain ourselves at the timescales we need to.
- the fundamentally discrete nature of our universe, and Altera, both anchor the size of things (although differently bc Nooks prob stay at the bottom while we are just far enough up to support the correct level of complexity); imagine a universe where the laws of physics did not provide any size-anchoring (i.e. they are scale invariant); you could got infinitely smaller or infinitely larger.  You could shrink humans to 1/10th of their current size.

## Free Will

Nookian minds are deterministic, but the Nooks probably wouldn't know this.  The minds of conscious Nook are likely so complex that they would not be able perfectly predict how they would they themselves or other Nooks would react to a situation.  Furthermore, they would be unable to devise an experiment to test whether their minds were deterministic, since they would be unable to establish the same "situation" twice.  By "situation", we mean the complete state relevant to a Nook making a "choice".  In other words, the Nook's mind would have to have identical state, and the sensory input that they are deciding on would need to be the same.  Establishing identical sensory input would not be too difficult, but it would be impossible for them to establish that a Nook's mind's state has the same state twice in a row.  The state of a Nook's mind is complex and would likely have a long history.  The Nook being experimented on would remember earlier renditions of the experiment.  A Nook's child's mind would be very similar to the parent, but not exactly the same due to the mutation---thus experimenting on a parent-child pair would also be unfeasible.

Thus, the Nooks are in a similar situation to ourselves with regards to free will and determinism.  They may suspect that their world is perfectly deterministic, but they would be unable to prove it.  As a result, they may wonder, like we do, whether they have "free will."

What do we mean by "free will?"  A standard definition is: the ability to choose between different possible courses of action.  This definition begs the question---what does it mean for a being to choose?  At each time-step, the Nook mind is presented with sensory input and outputs an "action" that determines what the Nook will do (nothing, move, eat, or reproduce).  If this process is what we mean by choosing, then the Nooks have free will despite being deterministic.

Some would say that, for the Nooks to truly make a "choice"---and, by extension, to have "free will"---a different outcome must be possible, given the same situation.

In the case of Altera, one way to accomplish this would be to add randomness into the algorithm that "runs" a Nook's decision making process.

The simplest way we could do this is to alter our program so that each Nook's mind's state has a slight random perturbation applied to its state just before it makes a choice.  This introduces another issue, how we will arrive at this "randomness"?  Computers in our world are deterministic.  The only way to introduce true randomness into a computer is using randomness from outside the computer (e.g. from mouse movements, or network traffic delays).  By introducing true randomness from our universe into the computer so that we can truly randomly perturb the Nook's mind, we are coupling our universes state to the Nooks state.  If our own universe is deterministic, it is entirely possible that the Nook's choices are still deterministic (in the sense that no other outcome was possible).  Of course, the Nook's can't tell the difference in either case.

Lets assume that our universe is not deterministic, and that we can randomly perturb the Nook's mind's state before they make choices.  Now, alternate outcomes would be possible, given the same situation.  Do the Nooks now have free will?  One may object for a few different reasons, which we will consider in turn.

One may object because this randomness is added to the Nook's mind from the "outside".  Imagine that we are running each Nook's mind on a separate computer, and that each computer has its own randomness which it injects into each mind.  Clearly where there randomness comes from is not relevant.

Another objection is that we are adding randomness that is outside of the "control" of the Nook, so it is not possible that this randomness could give the Nook free will.  Well, what do we mean by "control"?  Do we mean that the Nook has the "will" to make it act one way or another?  Clearly this is begging the question, for we are debating what free will means in the first place.  "No, but really, I don't know how the mechanism would work, but surely there is some way that the Nook could have control over the outcome while not being deterministic!"  When considered in our universe, with its huge complexity and its unknowns, some of us may find this argument convincing.  However, when considered in the context of Altera it is clearly silly.  There is no mechanism within Altera that would circumvent this problem.  To this one may argue that Altera is too simple a world to have free will!  In fact, one may argue that, for the same reason, our assumption that consciousness could develop in Altera is also not possible.  I will call this the mystical metaphysical argument, because it is arguing that free will is beyond our ability to understand.  It is impossible to argue against the mystic---because they can always throw up their hands and say "it just is---it's impossible for us to understand, its beyond reason, its outside space and time, but it just is.  I believe it."  

We can not argue against the mystic, but it is worth noting that, from the outside, a being that has free will via this mystical metaphysical substance would be externally indistinguishable from a being that has the random perturbations.  In both cases, they would be unpredictable for us.

Thus, if your mother has free-will, but your father does not, you would not be able to tell the difference.

In conclusion, either:

1. our actions are deterministic
2. our actions are not deterministic, because randomness is injected from an internal or external sources
3. our actions are not deterministic, because of some mystical metaphysical "stuff" that we can not understand, however, this situation would be impossible to distinguish from the previous possibility.

The meaning of free-will in any case feels different from what we intuitively feel it should mean, but ultimately we must recognize that our intuition is wrong.  Nooks (and ourselves) do make choices, so in this sense they have free will.  These choices are deterministic, but they are so complicated that no Nook can predict them.

There is no reason why this result can not be extended to our universe.  We also make choices in that no one (not even ourselves) can predict what we will do.  If our world is deterministic, than clearly our choices are also deterministic.  If our world is not deterministic, then but our choices may be deter
