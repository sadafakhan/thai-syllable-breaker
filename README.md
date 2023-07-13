# thai-syllable-breaker
This program takes a text file of Thai text as input and runs it through an FSA designed to accept licit Thai syllables.
It then returns a file with the input text segmented on syllable breaks.

Args:
* ```categoryfile```: path to text file delineating syllabic categories for every character
* ```inputfile```: path to text file with Thai character input

Returns:
* ```output.txt```: text file of syllabically segmented Thai characters.

To run: 
```
src/run.sh input/category.txt input/input.txt output/output.txt
```

PROJECT 3 OF LING473 (08/24/2021)
