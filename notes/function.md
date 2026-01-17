Functions are like mini-programs inside your program.
They help you **organize code**, **avoid repetition**, and **make your code reusable**.

💡 Imagine you need to greet 100 users —

Would you write `print("Hello")` 100 times? ❌

No! You’d just call one **function** again and again ✅

---

## 🚀 **1️⃣ What is a Function?**

A **function** is a block of code that runs **only when called**.

We define it using the keyword `def`.

```python
def function_name():
    # code to execute

```
### **Example: Basic Function**

```python
def greet():
    print("Hello, welcome to Python! 👋")

# Calling the function
greet()

```

Output:Hello, welcome to Python! 👋
🧠 *Note:* You must **call** the function — it won’t run automatically!

---

## ⚙️ **2️⃣ Function with Parameters**

Functions can take **inputs** called **parameters** (or **arguments**) to work with dynamic values.

```python
def greet(name):
    print("Hello", name)

```

Calling:
```python
greet("Vaibhav")
greet("Riya")

```

Output:

```
Hello Vaibhav
Hello Riya

```

---

## 🧮 **3️⃣ Function with Return Value**

Sometimes, you want a function to **send a result back**.

Use the `return` keyword.

```python
def add(a, b):
```
```python
return a + b

result = add(10, 20)
print("Sum:", result)

```

Output:

```
Sum: 30

```

💡 `*return` ends the function immediately and passes the value back.*

---

## 🧱 **4️⃣ Default Parameters**

If the caller doesn’t pass a value, Python uses the **default**.

```python
def greet(name="Guest"):
    ```python
print("Hello", name)

greet()          # uses default
greet("Vaibhav") # overrides default

```

Output:

```
Hello Guest
Hello Vaibhav

```

---

## 🔢 **5️⃣ Keyword Arguments**

You can pass arguments **by name**, not just order.

```python
def student(name, age):
    print(f"Name: {name}, Age
```
```