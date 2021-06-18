import json


def readBoard(nb_player, name):
    with open("./savedBoard.json", "r+") as js:
        boards = json.loads(js.read())
        if int(nb_player) > 1 and int(nb_player) < 7: 
            if name in boards[nb_player]:
                return boards[nb_player][name]

def saveBoard(nb_player, name, board):
    with open("./savedBoard.json", "w+") as js:
        boards = json.loads(js)
        if name not in boards:
            boards[nb_player][name] = boards
            json.dump(boards, js)