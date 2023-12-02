# Problem description

This exercise illustrates the common problem of sampling from a dataset and interrogating that dataset with matplotlib plots.
You could imaging the sample being taken from a database, or larger than memory dataset, but in this case it's based on a small sample of the NYC Taxi data.

## Requirements

1.  The application should have the following components:

    -   A proportion input which selects the proportion of the dataset to sample

    -   A log-scale input which selects whether the tip plot is on a log scale

    -   A plot showing the relationship between tips and prices

    -   A plot showing a histogram of prices

2.  The app should use matplotlib plots (which can be found in `plots.py`

3.  The histogram plot should not rerender if the log-scale selector is changed

4.  The sample should only be retaken if the proportion slider changes

5.  Each time the proportion slider changes the app should take a new sample

# 
