# Answer to notes.md Questions
### 5/23/2017


### How would you use this algorithm?
Since we are looking at a change in signal; it can be used to compare the fluctuation of the signal
to see how similar or different they might. For instance in the case of a straight time series where

$$ n_1 + n_2 +…+ n_k $$
where of  n = 1;

we would not see any signal other than a flatline at 0. In the case of stock data; I'd use
the output and run the data through an anomaly detection algorithm to identify out of the
norm events that may trigger a buy/sell scenario.

### How would you improve it?
That depends:
* Create a comprehensive CLI for the program.
* Input any time series data and giving user ability to define their own parameter of choice
* Create unit tests to ensure the data input would identify informal
* Add more data validation


