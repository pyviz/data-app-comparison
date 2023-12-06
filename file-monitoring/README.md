# Problem description

Data apps often sit at the end of a larger data processing pipeline, and so it is helpful to have your app update whenever the underlying data files change. An example data generating script can be found in `populate-logs.py` which irregularly appends a row to a data frame.
 
# Requirements
- App should read in and render a csv file as a data frame, whenever that csv file changes the data frame output should rerender.
- The application shouldn't rerender if the csv file is unchanged.
- Othe components should be usable as the data frame rerenders.