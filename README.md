# Bin packing problem

## Author
Wojciech Moczydłowski 296258

## Usage
```
cd ./BinPacking
python -m BinPacking.main
```

## Input data
User can input data using console for small tests or generate random data for bigger one.

## Algorithms
Program includes two algorithms:
1) Brutal algorithm computes necessary boxes using all permutations of items. This algorithm is accurate, but totally slow.
2) Best fit algorithm approximates brutal algorithm.It is not accurate, but quite fast.

## Project structure
Project is divided into two parts:
1) algorithms: this part includes two algorithms: brutal and first fit.
2) view: this part includes View class which manages displaying results.
3) dataController: this part includes DataController class which manages input data.

