# CSV recipes
This folder contain some useful solutions for common problems


* How to read a large CSV file in chunks with Pandas in Python
https://www.kite.com/python/answers/how-to-read-a-large-csv-file-in-chunks-with-pandas-in-python

``` 
for chunk in pd.read_csv("large.csv", chunksize=10):
    print(chunk)
```    
    

* Writing an iterator to load data in chunks
http://cs996.icu/2016/10/11/loading-data-case-using-generators-and-chunks/#Writing-an-iterator-to-load-data-in-chunks


* Difference between Python's Generators and Iterators
https://stackoverflow.com/questions/2776829/difference-between-pythons-generators-and-iterators

```
def foo():
     print "begin"
     for i in range(3):
         print "before yield", i
         yield i
         print "after yield", i
     print "end"

f = foo()
f.next()
```



* How to iterate over consecutive chunks of Pandas dataframe efficiently
Chunks generator function for iterating pandas Dataframes and Series
https://stackoverflow.com/questions/25699439/how-to-iterate-over-consecutive-chunks-of-pandas-dataframe-efficiently


* How to convert a pandas DataFrame into a list of tuples in Python

https://www.kite.com/python/answers/how-to-convert-a-pandas-dataframe-into-a-list-of-tuples-in-python





