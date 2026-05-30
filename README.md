# Python Basics — Explained Step by Step (Beginner Edition)

A plain-language, line-by-line walkthrough of all 30 problems. The same handful of building blocks — **loops**, **`if` decisions**, **slicing**, **comprehensions**, and a few helper functions — solve every problem here, so once these click the rest get much easier.

---

## 🔤 Strings

### 1. First three characters

```python
def first_three(s):
    return s[:3]
```

**Line 1** — `def` means "define a function." We're creating a reusable mini-machine called `first_three`. The `s` in parentheses is the **parameter**: a placeholder for whatever string we hand it. So when we later call `first_three('python')`, the `s` *becomes* `'python'` inside the function.

**Line 2** — `return` sends a value back out of the function. `s[:3]` is a **slice**. Think of the string as a row of boxes, each with a position number starting at 0:

```
 p   y   t   h   o   n
 0   1   2   3   4   5
```

`s[:3]` means "start at the beginning, stop *before* position 3" — so you get positions 0, 1, 2 → `pyt`. The neat part: if the string only has 2 letters, slicing doesn't crash, it just gives you the 2 it has. That's why we don't need an `if` check for short strings.

---

### 2. Caesar cipher

```python
def caesar_encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            result += ch
    return result
```

**`result = ""`** — we start with an empty string. We'll glue each shifted letter onto this as we go, like building a word bead by bead.

**`for ch in text:`** — this is a **loop**. It runs the indented code once for every character in `text`, and each time, `ch` holds the current character. So for `"Hi"`, the loop runs twice: first `ch` is `'H'`, then `ch` is `'i'`.

**`if ch.isupper():`** — `.isupper()` is a question that answers `True` or `False`: "is this character a capital letter?" If yes, we run the line beneath it.

Now the core trick. Computers store letters as numbers (the ASCII system). `A` is 65, `B` is 66… and `a` is 97, `b` is 98. Two functions flip between them:
- `ord('A')` gives `65` (letter → number)
- `chr(65)` gives `'A'` (number → letter)

So reading `chr((ord(ch) - 65 + shift) % 26 + 65)` from the inside out:
- `ord(ch)` — get the letter's number, e.g. `'H'` → 72
- `- 65` — slide it down so `A` becomes 0, `B` becomes 1… `H` becomes 7. Now we're working with a clean 0–25 scale.
- `+ shift` — move it along the alphabet (shift of 3: `H`'s 7 becomes 10)
- `% 26` — the **wrap-around**. `%` gives the remainder after dividing. If shifting pushes us past `Z` (past 25), `% 26` loops us back to the start, so `Z` shifted by 1 becomes `A` instead of falling off the end.
- `+ 65` — slide back up into real letter-number territory
- `chr(...)` — turn that final number back into a letter

**`elif ch.islower():`** — `elif` means "else, if." Only checked when the first `if` was `False`. Same maths but with 97 because lowercase letters start there.

**`else: result += ch`** — for anything that isn't a letter (spaces, commas, `!`), just keep it unchanged.

**`result += ch`** — `+=` means "add this onto the end of what's already there." `result += 'K'` turns `""` into `"K"`.

To *decrypt*, you call it with a negative shift (`-3`), which slides letters backward.

---

### 3. Remove duplicate characters

```python
def remove_duplicates(s):
    seen = ""
    for ch in s:
        if ch not in seen:
            seen += ch
    return seen
```

`seen` starts empty and collects characters we've already met. For each character, `if ch not in seen:` asks "have we *not* met this one yet?" `in` checks membership — `'a' in 'cat'` is `True`. If the character is new, we add it; if it's a repeat, we skip it. For `"programming"`, the second `g`, `r`, and `m` get skipped → `progamin`.

---

### 4. Delete all occurrences of a character

```python
def delete_char(s, c):
    return s.replace(c, "")
```

`.replace(old, new)` swaps every copy of `old` for `new` in a string. By replacing with `""` (nothing), we're effectively deleting it. `delete_char("banana", "a")` → `"bnn"`.

---

### 5. Count leap years in a range

```python
def is_leap(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

def count_leap(span):
    start, end = span.split("-")
    count = 0
    for y in range(int(start), int(end) + 1):
        if is_leap(y):
            count += 1
    return count
```

**The leap rule** — `is_leap` returns `True` or `False`. A year is a leap year if it's divisible by 4 (`y % 4 == 0`, meaning "remainder is zero") **and** either it's not a century year (`y % 100 != 0`) **or** it's divisible by 400. That second part is why 1900 wasn't a leap year but 2000 was.

**`span.split("-")`** — the input is one string like `"1981-1991"`. `.split("-")` cuts it at the dash into a list `["1981", "1991"]`, and `start, end = ...` unpacks those two pieces into two variables in one go.

**`range(int(start), int(end) + 1)`** — `int(...)` converts the text `"1981"` into the actual number `1981` (you can't count with text). `range(a, b)` produces numbers from `a` up to *but not including* `b`, so we add `+ 1` to include the final year.

**`count += 1`** — each time we find a leap year, bump the counter up by one. At the end we return the total.

---

### 6. Insert a space before each capital letter

```python
def add_spaces(word):
    result = word[0]
    for ch in word[1:]:
        if ch.isupper():
            result += " "
        result += ch
    return result
```

**`result = word[0]`** — `word[0]` grabs just the first character (position 0). We seed our result with it directly, because we never want a space *before* the very first letter even if it's a capital.

**`for ch in word[1:]:`** — `word[1:]` is everything *from* position 1 onward (skipping the first character we already handled). We loop over the rest.

For each character: `if ch.isupper():` — if it's a capital, first tack on a space, then add the character. If it's lowercase, we skip the space line and just add the character. So `PythonExercises` flows as `P` → `y,t,h,o,n` (no spaces) → hit capital `E`, add space then `E` → `Python E...`.

---

## 📋 Lists

### 1. First and last 5 square numbers

```python
squares = [x * x for x in range(1, 31)]
print("First 5:", squares[:5])
print("Last 5:", squares[-5:])
```

**Line 1** is a **list comprehension** — a compact way to build a list with a loop tucked inside it. Read it right-to-left: `for x in range(1, 31)` walks through the numbers 1 to 30 (remember `range` stops *before* 31), and for each `x`, the `x * x` at the front says "square it and put it in the list." So `squares` ends up holding `[1, 4, 9, 16, 25, ...]`.

The same thing written the long way would be:

```python
squares = []
for x in range(1, 31):
    squares.append(x * x)
```

Both do exactly the same job — the comprehension is just shorter.

**`squares[:5]`** slices the first five (positions 0–4). **`squares[-5:]`** uses negative positions: `-1` is the last item, `-5` is the fifth from the end, so `[-5:]` means "the last five."

---

### 2. Difference between two lists

```python
list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 4, 6]
diff = [x for x in list1 if x not in list2]
print(diff)  # [1, 3, 5]
```

Another comprehension, but this one has a **filter** on the end. For each `x` in `list1`, the `if x not in list2` decides whether it's allowed into the new list. If `x` is missing from `list2`, it gets kept. So `1`, `3`, `5` survive (they're not in `list2`), and `2`, `4`, `6` get dropped.

---

### 3. Concatenate a list with a range 1..n

```python
def concat_range(items, n):
    result = []
    for i in range(1, n + 1):
        for item in items:
            result.append(item + str(i))
    return result

print(concat_range(['p', 'q'], 5))
```

This is a **nested loop** — a loop inside a loop. The outer loop picks a number `i` (1, then 2, then 3…). For each of those numbers, the inner loop runs fully through every letter in `items`.

`item + str(i)` glues the letter to the number — but you can't add a letter to a number directly, so `str(i)` first converts the number `1` into the text `"1"`. Then `'p' + "1"` gives `"p1"`.

`.append(...)` adds one item onto the end of the list. Because the number loop is on the *outside*, the output groups by number: `p1, q1`, then `p2, q2`, and so on.

---

### 4. List → list of dictionaries

```python
names = ["Black", "Red", "Maroon", "Yellow"]
codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]

result = []
for name, code in zip(names, codes):
    result.append({"color_name": name, "color_code": code})
print(result)
```

`zip(names, codes)` is the star here. It zips the two lists together like a zipper, pairing them up by position: `("Black", "#000000")`, then `("Red", "#FF0000")`, and so on. The `for name, code in ...` unpacks each pair into two variables at once.

Inside the loop we build a small **dictionary** — `{"key": value}` — where each piece of data has a label. `{"color_name": name, "color_code": code}` makes something like `{"color_name": "Black", "color_code": "#000000"}`, and we append it to the result.

---

### 5. Move all zeros to the end

```python
def move_zeros(nums):
    non_zeros = [n for n in nums if n != 0]
    zeros = [n for n in nums if n == 0]
    return non_zeros + zeros
```

Two filtered comprehensions split the work. The first keeps everything that *isn't* zero (`n != 0`). The second keeps *only* the zeros (`n == 0`). Then `non_zeros + zeros` — using `+` to join two lists end to end — sticks all the zeros after all the non-zeros. The order of the non-zeros stays exactly as it was.

---

### 6. Round, min/max, ×5, unique ascending

```python
nums = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
rounded = [round(n) for n in nums]

print("Minimum value:", min(rounded))
print("Maximum value:", max(rounded))

times5 = [n * 5 for n in rounded]
unique_sorted = sorted(set(times5))
print("Result:", " ".join(str(n) for n in unique_sorted))
```

Step by step: `[round(n) for n in nums]` rounds every number to the nearest whole one (`22.4` → `22`, `16.22` → `16`). `min()` and `max()` are built-in functions that find the smallest and largest in a list.

`[n * 5 for n in rounded]` multiplies each rounded number by 5.

Then the last line does two clean-up jobs at once:
- `set(times5)` throws away duplicates — a **set** can't hold the same value twice.
- `sorted(...)` puts what's left in ascending order and hands back a list.

`" ".join(...)` glues the numbers into one string with a space between each. But `join` only works on text, so `str(n)` converts each number to text first. The result is `"20 25 45 ..."`.

---

### 7. Count the lists inside a list

```python
def count_lists(data):
    count = 0
    for item in data:
        if isinstance(item, list):
            count += 1
    return count
```

We loop through each item and use `isinstance(item, list)` — a check that asks "is this thing a list?" — to decide whether to count it. We only count items that are *themselves* lists, and we don't peek inside them. So in `[[2,4], [[6,8],[4,5,8]], [10,12,14]]` there are three top-level lists, even though one of them has lists nested deeper inside.

---

## 📖 Dictionaries

A dictionary stores data as **key → value** pairs, like a real dictionary maps a word to its definition. You look things up by key, not by position.

### 1. Concatenate dictionaries

```python
dic1 = {1:10, 2:20}; dic2 = {3:30, 4:40}; dic3 = {5:50, 6:60}

combined = {}
combined.update(dic1)
combined.update(dic2)
combined.update(dic3)
print(combined)
```

`combined = {}` starts an empty dictionary. `.update(other)` pours all the pairs from `other` into `combined`. Doing it three times merges all three into one.

---

### 2. Print all distinct values

```python
data = [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},
        {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]

unique = set()
for d in data:
    for value in d.values():
        unique.add(value)
print("Unique Values:", unique)
```

`data` is a list of tiny dictionaries. The outer loop grabs one dictionary at a time (`d`). `d.values()` gives just the values of that dictionary (ignoring the keys), and the inner loop adds each one to our `set`. Because a set automatically refuses duplicates, repeated codes like `S001` and `S005` only appear once at the end.

---

### 3. Combine by adding values for common keys

```python
from collections import Counter

d1 = {'a':100, 'b':200, 'c':300}
d2 = {'a':300, 'b':200, 'd':400}
print(Counter(d1) + Counter(d2))
```

`Counter` is a special dictionary from Python's `collections` toolbox. The `import` line brings it in. Its superpower: when you add two `Counter`s with `+`, matching keys get their values *added together* instead of one overwriting the other. So `'a'` (100 + 300) becomes 400, while `'c'` and `'d'` (which appear in only one) carry over as-is.

---

### 4. Top three items by value

```python
items = {'item1':45.50, 'item2':35, 'item3':41.30, 'item4':55, 'item5':24}

top3 = sorted(items.items(), key=lambda x: x[1], reverse=True)[:3]
for name, price in top3:
    print(name, price)
```

`items.items()` turns the dictionary into a list of pairs: `[('item1', 45.5), ('item2', 35), ...]`.

`sorted(..., key=lambda x: x[1], reverse=True)` sorts those pairs. The `key` tells Python *what to sort by* — `lambda x: x[1]` is a throwaway one-line function meaning "for each pair `x`, look at position 1 (the price)." `reverse=True` puts the biggest first. Finally `[:3]` slices off the top three. The loop then unpacks each pair into `name` and `price` to print them.

---

### 5. Filter a dictionary by value

```python
marks = {'Cierra Vega':175, 'Alden Cantrell':180,
         'Kierra Gentry':165, 'Pierre Cox':190}
print({k: v for k, v in marks.items() if v > 170})
```

This is a **dictionary comprehension** — same idea as a list comprehension but it builds a dictionary. `for k, v in marks.items()` walks through every key-value pair, and `if v > 170` only keeps the pairs whose value clears 170. `{k: v ...}` rebuilds those survivors into a new dictionary.

---

### 6. Extract values for one subject

```python
records = [{'Math':90,'Science':92},
           {'Math':89,'Science':94},
           {'Math':92,'Science':88}]

print([d['Science'] for d in records])
print([d['Math'] for d in records])
```

`d['Science']` looks up the value stored under the key `'Science'` in dictionary `d`. The comprehension does that lookup for every dictionary in the list, collecting just those values into a new list.

---

## 🔒 Tuples

A tuple is like a list but **locked** — once created, you can't change its contents. You write them with round brackets: `(1, 2, 3)`.

### 1. Replace the last value of each tuple

```python
lst = [(10,20,40),(40,50,60),(70,80,90)]
print([t[:-1] + (100,) for t in lst])
```

Since tuples can't be edited in place, we build new ones. `t[:-1]` slices off everything *except* the last item (`(10, 20, 40)` → `(10, 20)`). Then `+ (100,)` sticks a fresh tuple holding `100` onto the end. The comma in `(100,)` is essential — it's what makes it a tuple rather than just the number `100` in brackets.

---

### 2. Remove empty tuples

```python
data = [(), (), ('',), ('a','b'), ('a','b','c'), ('d')]
print([t for t in data if t])
```

The filter here is simply `if t`. In Python, an empty tuple `()` counts as `False` ("falsy") while a tuple with anything in it counts as `True`. So `if t` quietly drops the empties. Note `('',)` survives — it holds an empty *string*, so it's not empty. And `('d')` is sneaky: with no comma it's just the string `'d'`, not a tuple, so it stays too.

---

### 3. Sort tuples by their float element

```python
data = [('item1','12.20'),('item2','15.10'),('item3','24.5')]
print(sorted(data, key=lambda x: float(x[1]), reverse=True))
```

The numbers are stored as *text* (`'12.20'`), and sorting text doesn't sort numerically. So `key=lambda x: float(x[1])` says "for each pair, take position 1 and convert it to a real decimal number with `float()` before comparing." `reverse=True` sorts largest first.

---

### 4. Tuple of integers → one integer

```python
def tuple_to_int(t):
    return int("".join(str(n) for n in t))
```

Read inside out: `str(n) for n in t` turns each number into text. `"".join(...)` glues those texts together with nothing between them, so `(1, 2, 3)` becomes `"123"`. Then `int(...)` converts that whole string back into the single number `123`.

---

### 5. Sum of each tuple

```python
data = [(1,2,6),(2,3,-6),(3,4),(2,2,2,2)]
print([sum(t) for t in data])
```

`sum(t)` adds up all the numbers in one tuple. The comprehension applies it to every tuple in the list, giving a list of totals.

---

### 6. Average by position (column average)

```python
data = ((10,10,10,12),(30,45,56,45),(81,80,39,32),(1,2,3,4))
print([sum(col)/len(col) for col in zip(*data)])
```

This is the tricky one. The averages run *down the columns*, not across each tuple. `zip(*data)` does the magic: the `*` unpacks the four tuples and feeds them to `zip`, which then groups them by position — all the first elements together `(10, 30, 81, 1)`, all the second elements together, and so on. For each of those columns, `sum(col) / len(col)` is the average (total divided by how many there are).

---

## 🎯 Sets

A set holds **unique, unordered** items — no duplicates, no positions.

```python
s = {1, 2, 3, 4}
print(len(s))            # 4 — how many items

s.add(5)                 # add one item
s.update([6, 7])         # add several at once
s.discard(7)             # remove an item (no error if it's missing)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)             # intersection: items in BOTH  -> {3, 4}
print(a | b)             # union: items in EITHER        -> {1,2,3,4,5,6}
print(a - b)             # difference: in a but NOT b    -> {1, 2}
print(max(a), min(a))    # largest and smallest          -> 4 1
```

The three symbols are worth memorizing: `&` keeps what's shared, `|` combines everything, and `-` subtracts one set from another. `len`, `max`, and `min` are the same built-in functions you've already seen with lists.

---

## 🧠 The Big Picture

A handful of building blocks recombine to solve every single problem here:

- **Loops** (`for`) — do something for each item
- **Decisions** (`if` / `elif` / `else`) — choose what to do
- **Slicing** (`[:]`) — grab parts of a string or list
- **Comprehensions** (`[... for ...]`) — build a collection in one line
- **Helper functions** — `sum`, `len`, `min`, `max`, `round`, `sorted`, `zip`, and the converters `str` / `int` / `float`

Once those feel familiar, you're not really learning 30 separate things — you're remixing the same dozen ideas.
