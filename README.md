# net-scan

Yerel ağdaki cihazları keşfetmek için kullanılır.

## Gereksinimler

net-scan aşağıdaki kütüphaneleri kullanır.

* Colorama
* Scapy

## Kurulumu

Projeyi klonlamak için;

```python
git clone https://github.com/thealper2/net-scan.git
```
Gerekli kütüphaneleri kurmak için;

```python
python -m pip install -r requirements.txt
```

## Kullanımı

| Parametre | Kullanımı |
| --------- | --------- |
| -t        | Target. Hedef IP aralığını belirtmek için kullanılır |

```bash
usage: net-scan.py [-h] -t T

Network scanner

options:
  -h, --help  show this help message and exit
  -t T        target
```

## Örnekler

```python
python3 net-scan.py -t 192.168.1.1/24
```
