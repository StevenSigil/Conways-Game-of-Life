# Conways-Game-of-Life

### A zero player game said to represent *emergent complexity* or *self-organizing systems*.

![Random starting demo](https://github.com/StevenSigil/Conways-Game-of-Life/blob/main/demo_img/random_start.gif)
<figcaption>Game of Life with random starting values</figcaption>
<br/>

The idea of The Game of Life has fascinated me for many years. Now that I am able to write decent enough code, I thought
I would try a build.

The basic idea is to show how elaborate patterns (maybe behaviours) can be achieved from very simple rules. By knowing
the rules and observing the outcomes, people have the ability to learn about even more complicated systems (ie: nature,
cells, etc...). For more information on the premise behind the game, check out
this [Wikipedia page](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

My original fascination with this game was two fold. I wanted to observe (and maybe learn more about):

1. Self replicating actions (for lack of a better term) given a basic pattern and applying rules governing the next step
   in the pattern. ie: *"gliders"*
    
 ![Original glider demo](https://github.com/StevenSigil/Conways-Game-of-Life/blob/main/demo_img/glider.gif)
 <figcaption>The original "glider" configuration</figcaption>
 <br/>
    
2. Chaotic initial systems and if they tend to remain in a state of chaos, die out, or (my hunch) eventually become
   orderly.
   - ie: the first gif above - starting the game with random positions.

To not spoil anything, I will let you come to or seek out, your own conclusions on such matters. 

If you would like to give the game a try: 
- Install the requirements.txt on root 
- Run `game/run.py` to start the game
- Draw the initial starting *alive* cells
- Press the window close 'X' button to move to the next run loop and watch the game playout!

Some configuration notes:
- The current configuration is set to use a really large board and random starting values.
   - Adjusting the board size may require adjusting the timing and scale of the random array if used.
- If you want the margin between cells visible, the color that fills the screen (run.py ln: 115) will need to be set to GRAY (or another color).
- I tried leaving comments in the files for other changes you may want to make.
