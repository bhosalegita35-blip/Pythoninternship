### **1. Operators in Python**

Used to perform actions on variables or values.

Types        Operator              Example          Description
Arithmetic   +,-,*,/,//,%,**       a+b              Math operations
Comparision  ==,!=,>,<,>=,<=       a>b              compare values
Logical      and,or,not            a>5 and b<10     combine conditions
Assignment   =,+=,-=,*=,/=         x+=2             update variable
Membership   in, not in            "a"in "apple"    check presence
Identify     is,is not              a is b          compare object identity

1️⃣ Arithmetic Operators:+,-,*,/,//,%,**
Example:
a=10
b=3
print(a+b)
print(a%b)

2️⃣ Comparison Operators:==,!=,>,<,>=,<=
Example:
x=10
y=20
print(x< y)

### **3️⃣ Bitwise Operators**

Bitwise operators work on binary values (0s and 1s).

✅ 8421 Rule (Binary Place Values)

Each bit has a fixed value:

| Bit | 8 | 4 | 2 | 1 |
| --- | --- | --- | --- | --- |
| Value | 8 | 4 | 2 | 1 |

`&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<`, `>>`

Example:
print(5&3) #1

### **4️⃣ Ternary Operator (Conditional Expression)**

Super useful for real projects

**Syntax**

```
= value_if_true  if  condition  else  value_if_false

```
result = "Pass" if score >= 40 else "Fail"

### **Operator Precedence (Priority Order)**:
High->low
(),**,* / // %,+ -,comparision,Logical