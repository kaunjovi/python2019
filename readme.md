
# Learning Python

```batch
$ python --version
Python 2.7.10
```

## [Hackerrank](https://www.hackerrank.com/challenges/py-if-else/problem)

### The if else

- The range function goes from x to y-1 by steps of z. range(x, y, z)

### List

- https://www.programiz.com/python-programming/list

```python
# empty list
my_list = []

# list of integers
my_list = [1, 2, 3]

# list with mixed datatypes
my_list = [1, "Hello", 3.4]
```

### Python | List | Negative index

```python
# Negative index
my_list = ['p','r','o','b','e']

# Output: e
print(my_list[-1])

# Output: p
print(my_list[-5])

```

### Python | List | Slicing

```python
my_list = ['p','r','o','g','r','a','m','i','z']
# elements 3rd to 5th
print(my_list[2:5])

# elements beginning to 4th
print(my_list[:-5])

# elements 6th to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])
```

### Python | List | Modify

```python

odd = [2, 4, 6, 8]

# change the 1st item
# Output: [1, 4, 6, 8]
odd[0] = 1

# change 2nd to 4th items
# Output: [1, 3, 5, 7]
odd[1:4] = [3, 5, 7]  

# Output: [1, 3, 5, 7]
odd.append(7)

# Output: [1, 3, 5, 7, 9, 11, 13]
odd.extend([9, 11, 13])

# Output: [1, 3, 5, 9, 7, 5]
odd = [1, 3, 5]
print(odd + [9, 7, 5])

#Output: ["re", "re", "re"]
print(["re"] * 3)

# Insert at a particular location
# Output: [1, 3, 9] 
odd = [1, 9]
odd.insert(1,3)

# Output: [1, 3, 5, 7, 9]
odd[2:2] = [5, 7]

```

### Nested list

```python

# Nested List
n_list = ["Happy", [2,0,1,5]]

# Output: a
print(n_list[0][1])

# Output: 5
print(n_list[1][3])

```

## Stock picking | MRF tyres

- 201805
  - https://www.youtube.com/watch?v=uRQGs3E8U6w
    - 2018 to 2020 - automobile and associated will go up
    - You saw it on Sachin's bat. Idiot. You should have taken notice of then.
    
