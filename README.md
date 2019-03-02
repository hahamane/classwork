# classwork 7
Homework PseudoCode
1. Load data
  a. Get file name from the user(using argparse)
    i. Check whether header file provided
  b. Ensure file exists
  c. Read first lines -- enough so we can see the outliners
  d. check type of each row in each column, and see if consistent
 
2. Organize data (adding header)
  a. if we have a header in our data file:
    i. load it, tell pandas to look in the first row for a header
  b. otherwise:
    i. if header file provided:
      - load header file ("open()" and "read()" of the file)
      - load the data and add header (pandas can except the list of column names)
    ii. otherwise:
      - throw an exception and exit
      - move on without a header
1/2:
  a. try: 
    i. load data with pandas, enforcing that things are numbers while assuming there is no header
  b. except Exception or ValueError or ValueError, FileNotFoundEror - Depending on what you want as e:
   ii. print (e)

3. Summary statistics
  a. np.mean(data axis=0) - look it up.
  b. np.std(data axis=0)

4. Plot (1 feature)
  a. for column in dataframe.columns:
    i. data = dataframe[column]
   ii. newfig = creating a new figure
  iii. plot histogram on newfig
   iv. title "column name"
    v. name y axis "count" and x axis "bin/column name"
   vi. save newfig with name determined by column.name
       -  "histogram_column:{0}".format(name)
  vii. clear/reset the figure

## seaborn, plotly
5. Plot (2 features)
  a. for idx, column1 in enumerate(dataframe):
    i. for jdx column2 in dataframe.iloc[:,idex+1]:
      - data1 = dataframe[column1]
      - data2 = dataframe[column2]
      - plt.scater(data1,data2)
      - save the plot ("sctter_{0}_{1}.png".format(column1, column2))

6. Plot (2+ features)
  a. correlation relation
  b. 3D plots


docker
docker run -ti -v ${PWD}:${PWD} -w {$PWD}  newImage ## to mount the volume of the current directory to the same directory inside the docker. Then start from the location



