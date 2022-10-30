def judgeCircle(moves):
    Origin = [0, 0]
    for i in range(len(moves)):
        if moves[i] == "R":
            Origin[0] = Origin[0] - 1
        elif moves[i] == "L":
            Origin[0] = Origin[0] + 1
        elif moves[i] == "U":
            Origin[1] = Origin[1] + 1
        else:
            moves[1] = Origin[1] - 1
    return True if Origin == [0, 0] else False


def judgeCircle2(moves):
    import re
    return False if (len(re.findall("R", moves)) != len(re.findall("L", moves))) \
                    or (len(re.findall("U", moves)) != len(re.findall("D", moves))) else True