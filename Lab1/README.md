# Lab1

В директории `config` находится [экспортированная топология](./config/_Exports_unetlab_export-20240616-031624.zip) и вывод [конфигураций устройств](./config/device_configs.md).

### Выводы клиентов

Оба клиента удачно пингуют друг друга, в том числе при отключении любой из трёх связей между свитчами.

#### Client1 pings Client2

```
VPCS> ping 10.0.20.2

84 bytes from 10.0.20.2 icmp_seq=1 ttl=63 time=24.566 ms
84 bytes from 10.0.20.2 icmp_seq=2 ttl=63 time=10.233 ms
84 bytes from 10.0.20.2 icmp_seq=3 ttl=63 time=15.255 ms
84 bytes from 10.0.20.2 icmp_seq=4 ttl=63 time=10.289 ms
84 bytes from 10.0.20.2 icmp_seq=5 ttl=63 time=10.430 ms
```

### Client2 pings Client1

```
VPCS> ping 10.0.10.2

84 bytes from 10.0.10.2 icmp_seq=1 ttl=63 time=32.176 ms
84 bytes from 10.0.10.2 icmp_seq=2 ttl=63 time=22.543 ms
84 bytes from 10.0.10.2 icmp_seq=3 ttl=63 time=8.381 ms
84 bytes from 10.0.10.2 icmp_seq=4 ttl=63 time=8.568 ms
84 bytes from 10.0.10.2 icmp_seq=5 ttl=63 time=7.491 ms
```
