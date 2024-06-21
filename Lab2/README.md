# Lab2

Собрать docker образ можно командой

```
make build
```

Протестировать на домене `HOST` можно командой

```
HOST=yandex.ru make run
```

Script help message
```
usage: find_mtu.py [-h] [-m MAX_MTU] host

Find the MTU for host.

positional arguments:
  host                  The host to test MTU against

options:
  -h, --help            show this help message and exit
  -m MAX_MTU, --max-mtu MAX_MTU
                        Upper bound for mtu search
```
