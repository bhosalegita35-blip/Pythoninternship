### **1. Comments in Python**

Used to explain your code.

Python completely ignores comments.

Non-executable code

# Single-line comment
'''Multi-line comment'''


✅ Comments make your code clean and readable.

✅ Useful for debugging and documentation.



### ✅ **Identifiers**
Also called Variables

Identifiers =Unique name to identify that variable. / Names we use for variables, functions, classes, etc.

✔ Must start with a letter or underscore

✔ Cannot start with numbers

✔ No spaces or special characters

✔ Case-sensitive (`Name` ≠ `name`)

✅ Valid:
student_name = "Riya"
_age = 20

#camel Case-start with lowercase  and ends with uppercase
eg.userName,empId,empRole
#pascal-case-start and end with capital
eg.UserName,EmpId,EmpRole
### ** Varieables in Python**

A variable is simply a container that stores some value. or used to hold/store the data in  a memory 
1 Byte (B) = 8 Bits (b) 

We can store any type of data in a variable, i.e , Number / String / Boolean / Array / Object / Function

We can use variables multiple times, i.e, Reusability

👉 In Python, you do NOT need to declare the type.

👉 Python automatically understands it (dynamic typing).

```python
name = "Pratik"
address = 'lorem ipsum lorem ipsum, lorem ipsum' // String

details="""
				lorem ipsum lorem ipsum, lorem ipsum
				lorem ipsum lorem ipsum, lorem ipsum
				lorem ipsum lorem ipsum, lorem ipsum

				"""
age=24 //Int
height=5.8 //Float 
is_student=True //Bool
```
### **3. Dynamic Typing**

Python allows the same variable to hold different types at different times:

```python
x = 10
x = "Now I'm text"

```

✅ Very flexible

✅ But be careful — can cause confusion in big programs.

---

### 🧩 **4. Multiple Variable Assignment**

Assign multiple values in one line:
```python
a,b,c=10,20,30
```
Assign one value to multiple variables:
```python
x=y=z=5
```
### **5. Data Types in Python**

```python
# PDT - primitive Data Types  - built in data types

# int 
# float
# String 
# Boolean 
# None 

# NPDT - Non-PDT - User  Defined Data Typs  i.e Derived from PDT

# List (Array)
#Tuple(Like Array but immutable -we cant change value )
#Dictionary(Object)
#sets
```
Type  Example           Description
int   10                Whole number
float 5.5               Decimal number
str   "Hello"           Text
bool  True/False        Boolean
list  [1,2,3]           Ordered+changable
tuple (1,2,3)           Ordered+NOT changable
dict  {"name":"Pratik"} Key-value pair
None  None              Represents"no value"

✅ Example:

```python
age=30
empCTC=20.5
isElgible=True
name="Pratik"
empRole=None

```

✅ Use `type()` to check:
```python
print(type(items))  # list
```
### ✅ **Extra Point: Escape Sequences**

Used inside strings:

| Escape | Meaning |

| `\n` | new line |
| `\t` | tab space |
| `\"` | double quote inside string |

Example:

```python
print("Hello\nPython")

```
