# 5.2 Saving and loading the model  

## Notes

After training the model, save it as a file, to use it for making predictions in future.  


### **Functions and methods:**  
  
* `with` - ensure file export content is complete without explicit closing  
* `open([file name],[flag])` - Open a file and return a stream.  
    Flag character Meaning:  
    'w'       open for writing, truncating the file first  
    'r'       open for reading the file
    'b'       file is binary, return contents as bytes objects without any decoding  
* `[open stream].close()`- Close a file to complete stream.  
* `pickle.dump([object], [file])` - Write a pickled representation of object to the open file object.  
* `pickle.load([file])` - Read and return an object from the pickle data stored in a file.  
* `f"some text {expression}"` - f-string (formatted string literal) is created by prefixing a string with the letter 'f' or 'F', allowing you to embed expressions inside curly braces {} 

  
### **Futher Reading**  
* [Compound statements | Python official](https://docs.python.org/3/reference/compound_stmts.html) details on `with`.  
* [Python's F-String for String Interpolation and Formatting | Real Python Tutorial](https://realpython.com/python-f-strings/)