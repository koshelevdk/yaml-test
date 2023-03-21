# yaml-test

We want to create YAML file that can be processed by test_yaml.py script.

Initila content:
```
a:
  value1: foo
  value2: bar

b:
  value3: baz
```

Desired content:
```
a:
  value1: foo
  value2: bar

b:
  value3: baz

c:
  key1: #Here goes all keys from ".a"
  key2: #Here goes the value of ".b.value3"
```

Result example:
```
a:
  value1: foo
  value2: bar

b:
  value3: baz

c:
  key1:
    value1: foo
    value2: bar
  key2: baz
```