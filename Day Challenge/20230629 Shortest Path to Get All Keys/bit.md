# 비트 연산

위 문제에서 사용된 비트 연산은 열쇠의 상태를 비트 플래그로 표현하는 데에 활용되었습니다. 이 비트 플래그는 각 열쇠에 대해 하나의 비트를 할당하여 획득 여부를 표시합니다.

아래는 기본 비트 논리 연산 예제입니다.

```
>>> bin(0b1101 & 0b1001)    # 비트 AND
'0b1001'
>>> 13 & 9                  # 비트 AND
9
>>> bin(0b1101 | 0b1001)    # 비트 OR
'0b1101'
>>> 13 | 9                  # 비트 OR
13
>>> bin(0b1101 ^ 0b1001)    # 비트 XOR
'0b100'
>>> 13 ^ 9                  # 비트 XOR
4
>>> bin(~0b1101)            # 비트 NOT
'-0b1110'
>>> ~13                     # 비트 NOT
-14

>>> 0b0011 << 2    # 비트를 왼쪽으로 2번 이동
12
>>> bin(12)
'0b1100'
>>> 0b1100 >> 2    # 비트를 오른쪽으로 2번 이동
3
>>> bin(3)
'0b11'
```

예를 들어, a부터 f까지의 열쇠가 있다고 가정하면, 이를 비트 플래그로 표현하면 다음과 같습니다:

```
a: 000001 (2진수)
b: 000010 (2진수)
c: 000100 (2진수)
d: 001000 (2진수)
e: 010000 (2진수)
f: 100000 (2진수)
```

각 비트는 열쇠의 획득 여부를 나타내며, 1은 획득한 것을 의미하고 0은 획득하지 않은 것을 의미합니다. 비트 연산을 사용하여 열쇠의 획득 여부를 효율적으로 처리할 수 있습니다.

위 코드에서는 keys 변수가 열쇠의 비트 표현을 나타내며, 획득한 열쇠를 나타내는 비트를 해당 위치에 1로 설정합니다. 이렇게 비트 연산을 통해 열쇠의 획득 여부를 추적하고 검사할 수 있습니다.

또한, k & (1 << (ord(grid[ni][nj]) - ord('A')))와 같은 비트 연산을 사용하여 열쇠가 필요한 문에 대한 열쇠의 획득 여부를 확인할 수 있습니다. 이 연산은 열쇠가 필요한 문에 해당하는 비트가 1인지 확인하여 열쇠를 가지고 있는지를 판단합니다.