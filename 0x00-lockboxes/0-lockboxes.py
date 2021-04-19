#!/usr/bin/python3
# Lockboxes challenge solution


def canUnlockAll(boxes):
    # Given an array of boxes, returns True if all boxes can be opened
    # Returns False otherwise

    keys = [0]
    pendingBoxes = list(range(len(boxes)))

    # Used to stop the loop if there is no more boxes that can be opened
    control = True

    while control:
        control = False
        for x in range(len(boxes)):
            if (x in keys and x in pendingBoxes):
                keys.extend(boxes[x])
                while(pendingBoxes.count(x)):
                    pendingBoxes.remove(x)
                control = True
    if not pendingBoxes:
        return True
    return False
