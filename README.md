# Assignment 1

### Part 1
![Part 1](https://github.com/DylanCrooks/personal/blob/main/Pasted%20image%2020240128143658.png?raw=true)
```Echo``` takes in an input, and then selects the minimum between the length of the input string and the repetitions. Because I'm dumb, I didn't do it recursively.
### Part 2
![Part 2a](https://github.com/DylanCrooks/personal/blob/main/Pasted%20image%2020240128143404.png?raw=true)
```Timer``` wrapper allows us to measure the function's execution time. ```Dictstore``` is used to store the results for plotting - it's not necessary otherwise.

![Part 2b](https://github.com/DylanCrooks/personal/blob/main/Pasted%20image%2020240128143545.png?raw=true)
```Plotting``` takes the x-values from ```dictstore```'s keys and the y-values from ```dictstore```'s values. I later realized x1 wasn't necessary, but could be used 
by iterating through the dictionary.
### Graph
![Graph](https://github.com/DylanCrooks/personal/blob/main/Figure_1.png?raw=true)
I'm not sure why it steps up according to that pattern, likely some hidden rounding operation, or caching. 
