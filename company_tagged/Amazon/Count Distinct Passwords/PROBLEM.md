## 2. Code Question 2

Weak passwords are likely to be hacked and misused. Due to this, developers at Amazon regularly come up with new algorithms to check the health of user passwords. A new algorithm estimates the variability of a password as the number of distinct password strings that can be obtained by reversing any one substring of the original password. Given the original password that consists of lowercase English characters, find its variability.

> **Note:** A substring is a contiguous sequence of characters within a string. For example 'bcd', 'a', 'abcd' are substrings of the string 'abcd' whereas the strings 'bd', 'acd' are not.

---

### Example

The following strings can be formed from `password = 'abc'` (as visualized in **image_8a86c1.jpg**):

* Reversing any substring of length 1 gives the original string `"abc"`.
* Reversing the substring `"ab"` gives a new string `"bac"`.
* Reversing the substring `"bc"` gives a new string `"acb"`.
* Reversing the substring `"abc"` gives a new string `"cba"`.

There are 4 distinct password strings that can be obtained from `password`. Return 4.

---

### Function Description

Complete the function `countDistinctPasswords` in the editor below.

`countDistinctPasswords` has the following parameter:

* `string password`: the original password

**Returns**

* `long_int`: the number of distinct password strings that can be formed

---

### Constraints

* All characters in `password` are lowercase English letters `ascii[a-z]`
* 1 ≤ length of `password` ≤ 10⁵

---

### Input Format For Custom Testing

Refer to the layout shown in **image_8a86bd.jpg**.

---

### Sample Case 0

#### Sample Input For Custom Testing

```text
abaa

```

*(In the interactive environment, this assigns `password = "abaa"`)*

#### Sample Output

```text
4

```

#### Explanation

The strings that can be formed are `"abaa"`, `"aaba"`, `"baaa"` and `"aaab"`.

---

### Sample Case 1

*(Header visible at the bottom of **image_8a86bd.jpg**)*