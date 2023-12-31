# Advent of Code 2023

I'm using [Advent of Code 2023](https://adventofcode.com/2023) to learn some new
programming languages, python being one of them. Don't expect this to be very good code,
I'm still learning.

---

### Day 1: Trebuchet?!
This one was as expected very straight forward.
There was a small gotcha if you just replaced each number-as-word with the number itself,
but it was pretty obvious once you see it.

### Day 2: Cube Conundrum
This was all about parsing the input. I used regular expressions for one other language,
but I believe just doing string splitting is better and more efficient.
Maybe regular expressions can be slightly more readable. 

### Day 3: Gear Ratios
I always find working with 2D maps like this awkward.
Especially if you don't know exactly what you're going to be doing with it.
I chose to do nothing more than just split it into lines, for easy access based on coordinates.

If I were to keep adding functionality to this kind of system, I would probably create something
that returns a list of adjacent squares to objects. Then I could iterate over them to find
if we are touching this or that. By the time I realized I might need something like that, I was too
far into the task to bother with it.

### Day 4: Scratchcards
Pretty straight forward problem today, not much to comment on.

### Day 5: Scratchcards
This one was a bit more difficult, and just terrible to work with in Python.
Idk, but I feel the code I wrote was just a mess and unreadable, and I was confusing myself.
This despite me just porting over the solution that I first did in C#.
Part 1 works, I might come back and fix Part 2 later.

### Day 6: Wait For It
This one I'm pretty happy with. It was pretty simple, and it's a direct
port of the Rust implementation. Maybe it's because of how simple it is,
but I feel it reads well, and is elegant enough.

### Day 7: Camel Cards
Fun problem. One small change I made from my Rust implementation is that
I stopped passing if we wanted to use J as joker or not as a parameter,
and instead just replaced `J` with `?`. That way I could have one
logic for both parts, just one input with jacks, and one with jokers.

### Day 8: Haunted Wasteland
Of all the implementations I did, I like this one the best.
I think it's mostly because of how quick and compact the parsing was.
I did not go for any graph or anything this time, just a dictionary
holding all the nodes. Turned out fine, and actually ran faster than I expected.

### Day 9: Mirage Maintenance
I like all the implementations I did of this problem. There is something
satisfying about breaking a problem like this into 3-6 line functions,
where each has a very specific, well-defined task. When we have code like this,
even if some of the functions were to be very complex and a bit difficult
to understand, the fact that they are isolated, very specific, and so short,
those things makes it easy to reason about the whole code without understanding each part.

### Day 10: Pipe Maze
Fun problem. Pretty easy to implement.
This is the first problem where I did the Python implementation first.
No special reason for this, I just wanted to mix things up.
Only real problem I had was I manually entered the result of part 2, and
accidentally flipped two of the digits. Debugged for a while before I
realized I had the correct solution all along :D
Code ended up a bit long, and somewhat messy, but it read ok I guess.
