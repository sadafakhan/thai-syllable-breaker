# thai-syllable-breaker. 
This program takes a text file of Thai text as input and runs it through an FSA designed to accept licit Thai syllables.
It then returns a file with the input text segmented on syllable breaks.

Args:
    categoryfile (str): path to text file delineating syllabic categories for every character
    inputfile (str):  path to text file with Thai character input

Returns:
    output.txt: text file of syllabically segmented Thai characters.

To run: 
```
python3 ./main.py category.txt input.txt output.txt
```

PROJECT 3 OF LING473 (08/24/2021)
