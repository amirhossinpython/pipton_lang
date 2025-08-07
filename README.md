# PiptonLang - Documentation / مستندات زبان پیپتون

---

## 🇮🇷 مستندات زبان برنامه‌نویسی پیپتون

### مقدمه:

Pipton یک زبان برنامه‌نویسی تفسیری (Interpreter Based) است که با استفاده از پایتون ساخته شده و سینتکسی ساده، روان، و شبیه به زبان‌های سطح بالا دارد. این زبان با هدف آموزش آسان، توسعه سریع، و کدنویسی شخصی‌سازی‌شده طراحی شده است.

---

### 🎯 اهداف زبان:

* ساده‌سازی آموزش برنامه‌نویسی برای مبتدیان
* نزدیک بودن سینتکس به تفکر منطقی فارسی و انگلیسی
* اجرای سریع و آسان کدها در محیط ترمینال
* توسعه‌پذیری بالا با قابلیت افزودن ماژول‌ها

---

### 📌 ساختار دستورات زبان Pipton:

```pipton
var name = entry("نام شما: ")
print>>"سلام " + name

var x = 10
while x < 13 {
    print>>x
    x = x + 1
}

for i in range(0, 3) {
    print>>i
}

fun greet(n) {
    print>>"سلام " + n
}
greet("پایتون")

class A {
    def __init__(self) {
        print>>"کلاس مقداردهی شد"
    }
}

import time
print>>time.ctime()
```

---

### 🧠 دستورها و قواعد:

#### 1. تعریف متغیر:

```pipton
var x = 5
```

#### 2. حلقه‌ها:

```pipton
while x < 10 {
    print>>x
    x = x + 1
}

for i in range(0, 5) {
    print>>i
}
```

#### 3. تابع:

```pipton
fun hello(name) {
    print>>"Hello " + name
}
hello("Amir")
```

#### 4. کلاس:

```pipton
class A {
    def __init__(self) {
        print>>"Init"
    }
}
```

#### 5. دریافت ورودی:

```pipton
var name = entry("Your name: ")
```

#### 6. چاپ خروجی:

```kod
print>>"Welcome to Pipton!"
```

#### 7. وارد کردن کتابخانه‌های پایتون:

```pipton
import math
print>>math.sqrt(25)
```

---

## 🇬🇧 PiptonLang Documentation

### Introduction:

Pipton is a lightweight interpreted language designed for simplicity and readability. It is powered by Python and supports a custom Persian-English hybrid syntax to make it intuitive for Persian speakers.

---

### 🎯 Language Goals:

* Beginner-friendly structure
* Customizable syntax
* Support for Python libraries
* Terminal-based execution

---

### 📌 Syntax Highlights:

```pipton
var name = entry("Your name: ")
print>>"Hello " + name

var x = 10
while x < 13 {
    print>>x
    x = x + 1
}

for i in range(0, 3) {
    print>>i
}

fun greet(n) {
    print>>"Hi " + n
}
greet("Pipton")

class A {
    def __init__(self) {
        print>>"Class initialized"
    }
}

import time
print>>time.ctime()
```

---

### 🔧 How to Use Pipton:

1. Install locally:

```bash
pip install .
```

2. Run a file:

```bash
pipton examples/test.pipton
```






