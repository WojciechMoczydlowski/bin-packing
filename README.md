# bin packing problem

## Author
Wojciech Moczydłowski 296258

## Usage
```
cd ./BinPacking
python -m BinPacking.main
```

## Input data
User can input data using console for small tests or generate random data for bigger one

## Algorithms
Program includes two algorithms:
1) Brutal algorithm computes necessary boxes using all permutations of items. This algorithm is accurate, but totally slow.
2) Best fit algorithm approximates brutal algorithm.It is not accurate, but quite fast.

## Files
Project is divied into two parts:
1) Algorithms: this part includes two algoritms: brutal and first fit. 
2) View: tihs  class manages input and output data.

