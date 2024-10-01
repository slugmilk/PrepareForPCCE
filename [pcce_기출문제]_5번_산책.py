# -*- coding: utf-8 -*-
"""[PCCE 기출문제] 5번 / 산책.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13KBO8K2iHZOViz2Ao1n0HcmvbCFWMcIr

### 문제 설명
여름이는 강아지를 산책시키려고 합니다. 여름이는 2차원 좌표평면에서 동/서/남/북 방향으로 1m 단위로 이동하면서 강아지를 산책시킵니다. 산책루트가 담긴 문자열 route가 주어질 때, 도착점의 위치를 return하도록 빈칸을 채워 solution함수를 완성해 주세요.

* route는 "N", "S", "E", "W"로 이루어져 있습니다.
  * "N"은 북쪽으로 1만큼 움직입니다.
  * "S"는 남쪽으로 1만큼 움직입니다.
    * 북쪽으로 -1만큼 움직인 것과 같습니다.
  * "E"는 동쪽으로 1만큼 움직입니다.
  * "W"는 서쪽으로 1만큼 움직입니다.
    * 동쪽으로 -1만큼 움직인 것과 같습니다.
* 출발점으로부터 [동쪽으로 떨어진 거리, 북쪽으로 떨어진 거리]형태로 강아지의 최종 위치를 구해서 return해야 합니다.
* 출발점을 기준으로 서쪽, 남쪽에 있는 경우는 동쪽, 북쪽으로 음수만큼 떨어진 것으로 표현합니다.
  * 출발점으로부터 동쪽으로 2, 북쪽으로 3만큼 떨어졌다면 [2, 3]을 return 합니다.
  * 출발점으로부터 서쪽으로 1, 남쪽으로 4만큼 떨어졌다면 [-1, -4]를 return 합니다.

### 제한 사항
* 1 ≤ route의 길이 ≤ 20
* route는 "N", "S", "E", "W"로만 이루어져 있습니다.
"""

def solution(route):
    east = 0
    north = 0
    for i in route:
        if i == "N":
            north += 1
        elif i == "S" :
            north -= 1
        elif i == "E" :
            east += 1
        elif i == "W":
            east -= 1

    return [east, north]