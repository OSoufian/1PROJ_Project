import json


def readBoard(name):
    with open("./savedBoard.json", "r+") as js:
        boards = json.loads(js)
        if name in boards:
            return boards[name]

def saveBoard(name, board):
    with open("./savedBoard.json", "w+") as js:
        boards = json.loads(js)
        if name not in boards:
            boards[name] = boards
            json.dump(boards, js)

