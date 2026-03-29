# word_constraint_comparator

The repository contains all implementation files, the word list datasets, timing scripts, and result data used to generate the figures and tables in this paper. Instructions for reproducing the experiments are provided in the repository README.

The Python files are named according to which algorithm they use and which constraints they fulfil. For example, `algoA_c1.py` uses algorithm A and fulfils constraint 1. 

`words_alpha.txt` is the word file used in the programs, and `read_english_dictionary.py` describes how to access words from the file. 

Our results per run are stored in the `results_word_constraints.xlsx` Excel file. 

Finally, a JSON format file of the word file is in the `words_dictionary.json` file.

To run any of the programs, have (the latest version of) Python installed. Next, ensure you have `random` and `time` installed within your Python environment, and that you have the `words_alpha.txt` file in the same directory.


