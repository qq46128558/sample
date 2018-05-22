## 函数参数总结

### 位置参数(又名必选参数)
```python
def function(name):
    pass
```

### 默认参数
```python
def function(name="Sarah"):
    pass
```

### 可变参数
```python
def function(*name):
    pass
# 调用方式1
function('Sarah','John')
# 调用方式2
name=['Sarah','John']
function(*name)
```

### 关键字参数(任意个)
```python
def function(**kw):
    pass
# 调用方式1
function(city='ZhuHai',gender='M')
# 调用方式2
kw={'city':'ZhuHai','gender':'M'}
function(**kw)
```

### 命名关键字参数
```python
def function(name,*,city):
    pass
def function(name,*change,city):
    pass
```

### 任意函数的调用
```python
function(*args,**kw)
# *args 可变参数,tuple
# **kw 关键字参数,dict
```