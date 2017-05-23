# Answer to notes.md Questions
### 5/23/2017


### How would you use this algorithm?
Since we are looking at a smoothed in signal; it can be used to compare the fluctuation of the signal
to see how similar or different they might. For instance in the case of a straight time series where

_n_1 + n_2 +…+ n_k when n = 1_

we would not see any signal other than a flatline at 0. In the case of stock data; I'd use
the output and find a threshold to BUY or SELL depending on the trade strategy.
One could also run the data through an anomaly detection algorithm to identify out of the
norm events as Google Finance may use a similar method to trigger correlation between news events.

### How would you improve it?
That depends:

 * Create a comprehensive CLI
 * Input any time series data and giving user ability to define their own parameter of choice
 * Create unit tests to ensure the data input would identify informal
 * Add more data validation around the user input so that if / when the user adds a non-numeric character to the input; the script will not choke and spit up everywhere.


