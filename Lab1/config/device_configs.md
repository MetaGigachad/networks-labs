### Router

```
Router#show conf
Using 3059 out of 262144 bytes
!
! Last configuration change at 00:33:56 UTC Sun Jun 16 2024
!
version 15.9
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname Router
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
!
!
!
mmi polling-interval 60
no mmi auto-configure
no mmi pvc
mmi snmp-timeout 180
!         
!         
!         
!         
!         
!         
!         
!         
!         
!         
!         
ip cef    
no ipv6 cef
!         
multilink bundle-name authenticated
!         
!         
!         
redundancy
!         
!         
!         
!         
!         
!         
interface GigabitEthernet0/0
 no ip address
 duplex auto
 speed auto
 media-type rj45
!         
interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 10.0.10.1 255.255.255.0
!         
interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 10.0.20.1 255.255.255.0
!         
interface GigabitEthernet0/1
 no ip address
 shutdown 
 duplex auto
 speed auto
 media-type rj45
!         
interface GigabitEthernet0/2
 no ip address
 shutdown 
 duplex auto
 speed auto
 media-type rj45
!         
interface GigabitEthernet0/3
 no ip address
 shutdown 
 duplex auto
 speed auto
 media-type rj45
!         
ip forward-protocol nd
!         
!
no ip http server
!         
ipv6 ioam timestamp
!         
!         
!         
control-plane
!         
banner exec ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
banner incoming ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
banner login ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
!         
line con 0
line aux 0
line vty 0 4
 login    
 transport input none
!         
no scheduler allocate
!         
end       
```

### Switch0

```
Switch#show conf
Using 1523 out of 262144 bytes, uncompressed size = 3151 bytes
!
! Last configuration change at 00:19:50 UTC Sun Jun 16 2024
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname Switch
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
!
!
!
!
!
!         
!         
!         
ip cef    
no ipv6 cef
!         
!         
!         
spanning-tree mode pvst
spanning-tree extend system-id
spanning-tree vlan 10,20 priority 24576
!         
!         
!         
!         
!         
!         
!         
!         
!         
!         
!
!         
!         
!         
!         
interface GigabitEthernet0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
 negotiation auto
!         
interface GigabitEthernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 negotiation auto
!         
interface GigabitEthernet0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 negotiation auto
!         
interface GigabitEthernet0/3
 negotiation auto
!         
interface GigabitEthernet1/0
 negotiation auto
!         
interface GigabitEthernet1/1
 negotiation auto
!         
interface GigabitEthernet1/2
 negotiation auto
!         
interface GigabitEthernet1/3
 negotiation auto
!         
ip forward-protocol nd
!         
ip http server
ip http secure-server
!         
ip ssh server algorithm encryption aes128-ctr aes192-ctr aes256-ctr
ip ssh client algorithm encryption aes128-ctr aes192-ctr aes256-ctr
!         
!         
!         
!         
!
!         
control-plane
!         
banner exec ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
banner incoming ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
banner login ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
!         
line con 0
line aux 0
line vty 0 4
!         
!         
end
```

### Switch1

```
Switch#show conf
Using 1492 out of 262144 bytes, uncompressed size = 3101 bytes
!
! Last configuration change at 00:25:51 UTC Sun Jun 16 2024
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname Switch
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
!
!
!
!
!
!         
!         
!         
ip cef    
no ipv6 cef
!         
!         
!         
spanning-tree mode pvst
spanning-tree extend system-id
!         
!         
!         
!         
!         
!         
!         
!         
!         
!         
!         
!
!         
!         
!         
interface GigabitEthernet0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
 negotiation auto
!         
interface GigabitEthernet0/1
 switchport access vlan 10
 switchport mode access
 negotiation auto
!         
interface GigabitEthernet0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 negotiation auto
!         
interface GigabitEthernet0/3
 negotiation auto
!         
interface GigabitEthernet1/0
 negotiation auto
!         
interface GigabitEthernet1/1
 negotiation auto
!         
interface GigabitEthernet1/2
 negotiation auto
!         
interface GigabitEthernet1/3
 negotiation auto
!         
ip forward-protocol nd
!         
ip http server
ip http secure-server
!         
ip ssh server algorithm encryption aes128-ctr aes192-ctr aes256-ctr
ip ssh client algorithm encryption aes128-ctr aes192-ctr aes256-ctr
!         
!         
!         
!         
!         
!         
control-plane
!         
banner exec ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
banner incoming ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
banner login ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
!         
line con 0
line aux 0
line vty 0 4
!         
!         
end
```

### Switch2

```
Switch#show conf
Using 1495 out of 262144 bytes, uncompressed size = 3101 bytes
!
! Last configuration change at 00:26:45 UTC Sun Jun 16 2024
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname Switch
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
!
!
!
!
!
!         
!         
!         
ip cef    
no ipv6 cef
!         
!         
!         
spanning-tree mode pvst
spanning-tree extend system-id
!         
!         
!         
!         
!         
!         
!         
!         
!         
!         
!         
!
!         
!         
!         
interface GigabitEthernet0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
 negotiation auto
!         
interface GigabitEthernet0/1
 switchport access vlan 20
 switchport mode access
 negotiation auto
!         
interface GigabitEthernet0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 negotiation auto
!         
interface GigabitEthernet0/3
 negotiation auto
!         
interface GigabitEthernet1/0
 negotiation auto
!         
interface GigabitEthernet1/1
 negotiation auto
!         
interface GigabitEthernet1/2
 negotiation auto
!         
interface GigabitEthernet1/3
 negotiation auto
!         
ip forward-protocol nd
!         
ip http server
ip http secure-server
!         
ip ssh server algorithm encryption aes128-ctr aes192-ctr aes256-ctr
ip ssh client algorithm encryption aes128-ctr aes192-ctr aes256-ctr
!         
!         
!         
!
!         
!         
control-plane
!         
banner exec ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
banner incoming ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
banner login ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
!         
line con 0
line aux 0
line vty 0 4
!         
!         
end
```

### Client1

```
VPCS> show ip

NAME        : VPCS[1]
IP/MASK     : 10.0.10.2/24
GATEWAY     : 10.0.10.1
DNS         : 
MAC         : 00:50:79:66:68:04
LPORT       : 20000
RHOST:PORT  : 127.0.0.1:30000
MTU         : 1500
```

### Client2

```
VPCS> show ip

NAME        : VPCS[1]
IP/MASK     : 10.0.20.2/24
GATEWAY     : 10.0.20.1
DNS         : 
MAC         : 00:50:79:66:68:05
LPORT       : 20000
RHOST:PORT  : 127.0.0.1:30000
MTU         : 1500
```
