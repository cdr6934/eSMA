## ODH Python Project

Attached is GOOG stock price data.

Write a well-documented, clear Python script with a nice 'style' that implements the following algorithm using the closing price of the stock:

1. Create an exponentially smoothed long term moving average  (smoothing window = 4 weeks, though flexible based on user input). Call it lt_av.
2. Create an exponentially smoothed short term moving average (smoothing window = 2 weeks, though flexible based on user input). Call it st_av.
3. Create a variable that is the difference between ltav and stav (ltav -stav). Call it diff_ltst.
4. Create an exponentially smoothed moving average of diff_ltst (smoothing window = 1.5 weeks). Call it diff_ltst_av.
5. Create a variable that is difference between 3 and 4. Call it: diff_av_diff.

Explain in 250--500 words (shorter is better as we don't want stuff we all know and understand) + graph what information this algorithm captures (focus on the information in step 5).

How would you use this algorithm?
How would you improve it?

Also provide clear instruction for how a user would run your script including details about any dependencies, etc.

