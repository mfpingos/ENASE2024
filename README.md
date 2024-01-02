
# TTL Data Processing, Generation, and Querying Scripts

These scripts, written in Python and Bash, serve three main purposes: organizing existing TTL data `final.py`, generating random TTL data `europeanagenerator.py, paradisiotisgenerator.py`, and running performance tests on querying TTL data `runQ.sh`.


## Features

**final.py**
- Organizes TTL data into nested folders based on user-defined tags.
- Displays execution time, CPU, and memory usage.
- Creates or replaces folders for data storage.


**europeanagenerator.py, paradisiotisgenerator.py**
- Generates random data entries for flock management.
- Customizable source count.
- Saves generated data to a specified TTL file.
- Prints execution time.

**runQ.sh**
- Automates the execution of an ARQ query 100 times.
- Records CPU and memory usage, execution time, and row counts.
- Calculates and displays average execution time.


## Requirements
- Python 2.7 or later for final.py; Python 3.x for `europeanagenerator.py and paradisiotisgenerator.py`
- Bash shell for `runQ.sh`
- The psutil module for `final.py`
- The faker module for `europeanagenerator.py and paradisiotisgenerator.py`
- Apache Jena ARQ for `runQ.sh`
## How to run 
**final.py**
- Run the script in a Python environment.
- Input the required tags and file path for TTL data when prompted.
- Check the output in the specified folder structure.

**europeanagenerator.py and paradisiotisgenerator.py**
- Run the script in a Python environment.
- Enter the number of sources to generate and the TTL file name when prompted.
- Check the generated data in the specified TTL file.

**runQ.sh**
- Run the script in a Bash shell.
- The script executes an ARQ query 100 times and outputs performance metrics to 100_lv2_100.txt.

### Output Details
- `final.py` generates a main folder named after the concatenated tags with nested subfolders.
- `europeanagenerator.py and paradisiotisgenerator.py` produces a TTL file with randomly generated data entries.
- `runQ.sh` produces a text file with detailed performance metrics for each run and the average execution time.

## Example

**final.py**

```
Enter the tags separated by spaces: tag1 tag2
Enter the file path for the TTL data: path/to/your/ttlfile.ttl
```

**europeanagenerator.py and paradisiotisgenerator.py** 
```
Enter the number of sources to generate: 10
Enter the TTL file name to save the data (e.g., output.ttl): output.ttl
```



