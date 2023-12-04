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
