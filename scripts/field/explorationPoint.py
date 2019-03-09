# Victoria Island Explorer Medal  |  Used for that Explore Medal Quest
if sm.getFieldID() == 105000000 and sm.hasQuest(30004):
    sm.setPlayerAsSpeaker()
    sm.sendNext("Welp, this thing is ancient, but seems to be working. Guess I should head back.")
    sm.warp(910700200, 0) # Root Abyss Quest Line Map
    sm.completeQuest(30004)

elif sm.getFieldID() == 104000000:
    sm.showEffect("Map/Effect.img/maplemap/enter/104000000")

elif sm.getFieldID() == 220080000 and sm.hasQuest(1662):
    sm.chatScript("Enter papulatus.")
elif sm.getFieldID() == 120000100 and "1" in sm.getQRValue(5675):
    sm.createQuestWithQRValue(2945, "1")
    sm.createQuestWithQRValue(17902, "1")
    sm.completeQuest(17902)
    sm.systemMessage("You cleared the Adventure Journal mission.")
    sm.avatarOriented("Effect/OnUserEff.img/RecordClear_BT/clear")
    # Update Quest Record EX | Quest ID: [51236] | Data: StageKey=0
