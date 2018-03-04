# -*- coding: utf-8 -*-

import random

def start():
    '''
    지뢰찾기 시작 함수
    '''

    # 사각형 가로
    mapX = 10

    # 사각형 세로
    mapY = 10

    # 게임맵 2차원 배열 초기화
    gameMap = [[0 for col in range(mapX)] for row in range(mapY)]

    # 지뢰 개수
    mine = 10

    # 배치된 지뢰 개수
    mineSet = 0

    # 배치된 지뢰 좌표
    mineSetList = []

    # 지뢰 배치
    while mineSet < mine:
        # 랜덤 가로, 세로 좌표
        randX = random.randrange(0, mapX-1)
        randY = random.randrange(0, mapY-1)

        # 지뢰가 이미 배치되어 있으면 좌표 재생성
        if gameMap[randX][randY] == '*':
            continue

        gameMap[randX][randY] = '*'
        mineXY = [randX, randY]
        mineSetList.append(mineXY)
        mineSet = mineSet + 1

    # 모든 사각형에 대한 숫자 구하기
    # 지뢰 주변 8개 사각형에 포함된 폭탄 개수 구하기
    for i in mineSetList:
        setMineX = i[0]
        setMineY = i[1]

        leftTopX = setMineX - 1
        leftTopY = setMineY - 1
        if not leftTopX < 0 or leftTopY < 0:
            if not gameMap[leftTopX][leftTopY] == '*':
                gameMap[leftTopX][leftTopY] = gameMap[leftTopX][leftTopY] + 1

        centerTopX = setMineX - 1
        centerTopY = setMineY
        if not centerTopX < 0 or centerTopY < 0:
            if not gameMap[centerTopX][centerTopY] == '*':
                gameMap[centerTopX][centerTopY] = gameMap[centerTopX][centerTopY] + 1

        rightTopX = setMineX - 1
        rightTopY = setMineY + 1
        if not rightTopX < 0 or rightTopY < 0:
            if not rightTopY == mapY:
                if not gameMap[rightTopX][rightTopY] == '*':
                    gameMap[rightTopX][rightTopY] = gameMap[rightTopX][rightTopY] + 1

        leftMiddleX = setMineX
        leftMiddleY = setMineY - 1
        if not leftMiddleX < 0 or leftMiddleY < 0:
            if not gameMap[leftMiddleX][leftMiddleY] == '*':
                gameMap[leftMiddleX][leftMiddleY] = gameMap[leftMiddleX][leftMiddleY] + 1

        rightMiddleX = setMineX
        rightMiddleY = setMineY + 1
        if not rightMiddleX < 0 or rightMiddleY < 0:
            if not rightMiddleY == mapY:
                if not gameMap[rightMiddleX][rightMiddleY] == '*':
                    gameMap[rightMiddleX][rightMiddleY] = gameMap[rightMiddleX][rightMiddleY] + 1

        leftBottomX = setMineX + 1
        leftBottomY = setMineY - 1
        if not leftBottomX < 0 or leftBottomY < 0:
            if not leftBottomX == mapX:
                if not gameMap[leftBottomX][leftBottomY] == '*':
                    gameMap[leftBottomX][leftBottomY] = gameMap[leftBottomX][leftBottomY] + 1

        centerBottomX = setMineX + 1
        centerBottomY = setMineY
        if not centerBottomX < 0 or centerBottomY < 0:
            if not centerBottomX == mapX:
                if not gameMap[centerBottomX][centerBottomY] == '*':
                    gameMap[centerBottomX][centerBottomY] = gameMap[centerBottomX][centerBottomY] + 1

        rightBottomX = setMineX + 1
        rightBottomY = setMineY + 1
        if not rightBottomX < 0 or rightBottomY < 0:
            if not rightBottomX == mapX or rightBottomY == mapY:
                if not gameMap[rightBottomX][rightBottomY] == '*':
                    gameMap[rightBottomX][rightBottomY] = gameMap[rightBottomX][rightBottomY] + 1

    # 최종 맵 출력
    for i in gameMap:
        print i

start()
