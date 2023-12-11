def init(N):
    global id2score;
    global id2team;
    global teamsize
    id2score = [0] * (N + 1)
    id2team = [i for i in range(N + 1)]
    teamsize = [1 for i in range(N + 1)]


def findBaseTeam(player):
    while player != id2team[player]:
        player = id2team[player]
    return player


def updateScore(mWinnerID, mLoserID, mScore):
    player_team = findBaseTeam(mWinnerID)
    id2score[player_team] += mScore

    player_team = findBaseTeam(mLoserID)
    id2score[player_team] -= mScore


def unionTeam(mPlayerA, mPlayerB):
    player_teamA = findBaseTeam(mPlayerA)
    player_teamB = findBaseTeam(mPlayerB)

    if teamsize[player_teamA] > teamsize[player_teamB]:
        teamsize[player_teamA] += teamsize[player_teamB]
        id2team[player_teamB] = player_teamA
        id2score[player_teamB] -= id2score[player_teamA]
    else:
        teamsize[player_teamB] += teamsize[player_teamA]
        id2team[player_teamA] = player_teamB
        id2score[player_teamA] -= id2score[player_teamB]


def getScore(mID):
    score = 0
    while True:
        score += id2score[mID]
        if mID == id2team[mID]:
            return score
        mID = id2team[mID]
    return score