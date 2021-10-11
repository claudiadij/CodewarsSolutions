# Speedcubing is the hobby involving solving a variety of twisty puzzles, the most famous being the 3x3x3 puzzle or Rubik's Cube, as quickly as possible.
# In the majority of Speedcubing competitions, a Cuber solves a scrambled cube 5 times, and their result is found by taking the average of the middle 3 solves (ie. the slowest and fastest times are disregarded, and an average is taken of the remaining times).
# In some competitions, the unlikely event of a tie situation is resolved by comparing Cuber's fastest times.
# Write a function cube_times(times) that, given an array of floats times returns an array / tuple with the Cuber's result (to 2 decimal places) AND their fastest solve.



def cube_times(times):
    times.remove(max(times))
    mini = times.index(min(times))
    byemini = times.pop(mini)
    mean = sum(times)/3
    return (round(mean,2), byemini)