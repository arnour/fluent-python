# fluent-python
Fluent Python: Clear, Concise, and Effective Programming Exercises

## Chapter 1 - The Python Data Model

- [Example 1.1: French deck emulating a collection](chapters/1/example_1_1.py)
- [Example 1.2: How Special Methods Are Used](chapters/1/example_1_2.py)

## Chapter 2 - An Array of Sequences

- [Example 2.1: Build a list of Unicode code points from a string](chapters/2/example_2_1.py)
- [Example 2.2: Build a list of Unicode code points from a string, using a listcomp](chapters/2/example_2_2.py)
- [Example 2.3: Listcomps Versus map and filter](chapters/2/example_2_3.py)
- [Example 2.4: Cartesian product using a list comprehension](chapters/2/example_2_4.py)
- [Example 2.5: Initializing a tuple and an array from a generator expression](chapters/2/example_2_5.py)
- [Example 2.6: Cartesian product in a generator expression](chapters/2/example_2_6.py)
- [Example 2.7: Tuples used as records](chapters/2/example_2_7.py)
- [Example 2.8: Nested Unpacking](chapters/2/example_2_8.py)
- [Example 2.9: Pattern Matching with Sequences](chapters/2/example_2_9.py)
- [Example 2.10: Destructuring nested tuples](chapters/2/example_2_10.py)
- [Example 2.11: Matching patterns without match/case](chapters/2/example_2_11.py)
- [Example 2.12: Pattern matching with match/case](chapters/2/example_2_12.py)
- [Example 2.13: Assigning names to slices](chapters/2/example_2_13.py)
- [Example 2.14: A list with three lists of length 3 can represent a tic-tac-toe board](chapters/2/example_2_14.py)
- [Example 2.15: A list with three references to the same list is useless](chapters/2/example_2_15.py)
- [Example 2.16: A riddle: A += Assignment Puzzler](chapters/2/example_2_16.py)
- [Example 2.17: The unexpected result: item t2 is changed and an exception is raised](chapters/2/example_2_17.py)
- [Example 2.18: Bytecode for the expression s[a] += b](chapters/2/example_2_18.py)
- [Example 2.19: Creating, saving, and loading a large array of floats](chapters/2/example_2_19.py)
- [Example 2.20: Handling 6 bytes of memory as 1×6, 2×3, and 3×2 views](chapters/2/example_2_20.py)
- [Example 2.21: Changing the value of a 16-bit integer array item by poking one of its bytes](chapters/2/example_2_21.py)
- [Example 2.22: Basic operations with rows and columns in a numpy.ndarray](chapters/2/example_2_22.py)
- [Example 2.23: Working with a deque](chapters/2/example_2_23.py)

## Chapter 3 - Dictionaries and Sets

- [Example 3.1: Examples of dict comprehensions](chapters/3/example_3_1.py)
- [Example 3.2: Pattern Matching with Mappings](chapters/3/example_3_2.py)
- [Example 3.3: Inserting or Updating Mutable Values](chapters/3/example_3_3.py)
- [Example 3.4: Uses dict.get to fetch and update a list](chapters/3/example_3_4.py)
- [Example 3.5: Uses dict.setdefault to fetch and update a list](chapters/3/example_3_5.py)
- [Example 3.6: Uses defaultdict to fetch and update a list](chapters/3/example_3_6.py)
- [Example 3.8: Subclassing dict](chapters/3/example_3_8.py)
- [Example 3.9: Subclassing UserDict Instead of dict](chapters/3/example_3_9.py)
- [Example 3.10: MappingProxyType builds a read-only mappingproxy instance from a dict](chapters/3/example_3_10.py)
- [Example 3.11: Dictionary Views](chapters/3/example_3_11.py)
- [Example 3.12: Count occurrences of needles in a haystack](chapters/3/example_3_12.py) 

## Chapter 4 - Unicode Text Versus Bytes

- [Example 4.1: Encoding and decoding](chapters/4/example_4_1.py)
- [Example 4.2: Sequence as bytes and as bytearray](chapters/4/example_4_2.py)
- [Example 4.3: Initializing bytes from the raw data of an array](chapters/4/example_4_3.py)
- [Example 4.4: Same text encoded as three different byte sequences](chapters/4/example_4_4.py)
- [Example 4.5: Encoding and decoding](chapters/4/example_4_5.py)
- [Example 4.6: Decoding from str to bytes: success and error handling](chapters/4/example_4_6.py)
- [Example 4.7: SyntaxError When Loading Modules with Unexpected Encoding](chapters/4/example_4_7.py)
- [Example 4.10: Exploring encoding defaults](chapters/4/example_4_10.py)
- [Example 4.14: Extreme “Normalization”: Taking Out Diacritics](chapters/4/example_4_14.py)
- [Example 4.19: # Sorting Unicode Text](chapters/4/example_4_19.py)

## Chapter 5 - Data Class Builders

- [Example 5.1: Simple class](chapters/5/example_5_1.py)
- [Example 5.2: Using typing.NamedTuple](chapters/5/example_5_2.py)
- [Example 5.3: Using @dataclass](chapters/5/example_5_3.py)
- [Example 5.4: Defining and using a named tuple type](chapters/5/example_5_4.py)
- [Example 5.5: Named tuple attributes and methods](chapters/5/example_5_5.py)
- [Example 5.6: Named tuple attributes and methods](chapters/5/example_5_6.py)
- [Example 5.8: Typed Named Tuples](chapters/5/example_5_8.py)
- [Example 5.9: Python does not enforce type hints at runtime](chapters/5/example_5_9.py)
- [Example 5.10: The Meaning of Variable Annotations: a plain class with type hints](chapters/5/example_5_10.py)
- [Example 5.11: Inspecting a typing.NamedTuple](chapters/5/example_5_11.py)
- [Example 5.12: Inspecting a class decorated with dataclass](chapters/5/example_5_12.py)
- [Example 5.13: Mutable Types as Parameter Defaults: Bad Idea](chapters/5/example_5_13.py)
- [Example 5.14: Field Options ](chapters/5/example_5_14.py)
- [Example 5.15: parameterized generic type](chapters/5/example_5_15.py)
- [Example 5.17: focusing on the handle field declaration and ____post_init____ validation](chapters/5/example_5_17.py)
- [Example 5.18: Example from the dataclasses module documentation](chapters/5/example_5_18.py)
- [Example 5.19: : code for Resource, a class based on Dublin Core terms](chapters/5/example_5_19.py)
- [Example 5.22: Pattern Matching Class Instances](chapters/5/example_5_22.py)

## Chapter 6 - Object References, Mutability, and Recycling

- [Example 6.1: Variables as boxes](chapters/6/example_6_1.py)
- [Example 6.2: Variables are bound to objects only after the objects are created](chapters/6/example_6_2.py)
- [Example 6.3: Identity, Equality, and Aliases](chapters/6/example_6_3.py)
- [Example 6.4: value x identity check](chapters/6/example_6_4.py)
- [Example 6.5: The Relative Immutability of Tuples](chapters/6/example_6_5.py)
- [Example 6.6: Making a shallow copy of a list containing another list](chapters/6/example_6_6.py)
- [Example 6.8: Deep and Shallow Copies of Arbitrary Objects](chapters/6/example_6_8.py)
- [Example 6.10: Cyclic references](chapters/6/example_6_10.py)
- [Example 6.11: Function Parameters as References](chapters/6/example_6_11.py)
- [Example 6.12: Mutable Types as Parameter Defaults: Bad Idea](chapters/6/example_6_12.py)
- [Example 6.15: Mutating received arguments](chapters/6/example_6_15.py)
- [Example 6.16: The end of an object’s life](chapters/6/example_6_16.py)
- [Example 6.17: A tuple built from another is actually the same exact tuple](chapters/6/example_6_17.py)
- [Example 6.18: String literals may create shared objects](chapters/6/example_6_18.py)


## Chapter 7 - Functions as First-Class Objects

- [Example 7.1: Create and test a function](chapters/7/example_7_1.py)
- [Example 7.2: Use function through a different name](chapters/7/example_7_2.py)
- [Example 7.3: pass function as an argument](chapters/7/example_7_3.py)
- [Example 7.4: pass function as an argument 2](chapters/7/example_7_4.py)
- [Example 7.5: map and filter compared to alternatives coded as list comprehensions](chapters/7/example_7_5.py)
- [Example 7.6: reduce and sum](chapters/7/example_7_6.py)
- [Example 7.7: using lambda](chapters/7/example_7_7.py)
- [Example 7.8: callable user-defined class's instance](chapters/7/example_7_8.py)
- [Example 7.9: From Positional to Keyword-Only Parameters](chapters/7/example_7_9.py)
- [Example 7.11: Packages for Functional Programming](chapters/7/example_7_11.py)
- [Example 7.13: Demo of itemgetter](chapters/7/example_7_13.py)
- [Example 7.14: Demo of attrgetter](chapters/7/example_7_14.py)
- [Example 7.15: Demo of methodcaller](chapters/7/example_7_15.py)
- [Example 7.16: Using partial](chapters/7/example_7_16.py)
- [Example 7.17: Using partial 2](chapters/7/example_7_17.py)
- [Example 7.18: Demo of partial applied to a function](chapters/7/example_7_18.py)
