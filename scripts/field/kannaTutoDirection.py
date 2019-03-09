# Created by MechAviv
# Map ID :: 807100110
# Unknown : Unknown

if sm.getFieldID() == 807100110:
    sm.curNodeEventEnd(True)
    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(True, False, False, False)
    sm.setStandAloneMode(True)
    sm.giveSkill(40020000, 1, 1)
    sm.giveSkill(40020001, 1, 1)
    sm.removeSkill(40020002)
    sm.giveSkill(40020109, 1, 1)
    sm.showFieldEffect("JPKanna/text0", 0)
    sm.sendDelay(7000)


    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(False, True, False, False)
    sm.warp(807100100, 1)
elif sm.getFieldID() == 807100100:
    sm.curNodeEventEnd(True)
    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(True, False, False, False)
    sm.forcedInput(2)
    sm.sendDelay(2500)


    sm.forcedInput(0)
    sm.setSpeakerID(9131003)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendNext("I can already feel the dark energy burning my skin.")


    sm.setSpeakerID(9131003)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.flipSpeaker()
    sm.flipDialoguePlayerAsSpeaker()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendSay("This place gives me goosebumps.")


    sm.setSpeakerID(9131003)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.flipSpeaker()
    sm.flipDialoguePlayerAsSpeaker()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendSay("There's a lot of noise.")


    sm.setSpeakerID(9131003)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendSay("We may not be the only intruders.")


    sm.setSpeakerID(9131003)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.flipSpeaker()
    sm.flipDialoguePlayerAsSpeaker()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendSay("Whatever's going on, I don't like it. Do you think someone else could have received the same orders?")


    sm.setSpeakerID(9131006)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendSay("Leave the worrying to me, Kanna. You hurry and stop the ritual.")


    sm.setSpeakerID(9131003)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendSay("The others have gone to the Northern Wing or the southwestern area. Kenshin's right. You need to focus on stopping the ritual.")


    sm.setSpeakerID(9131003)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendSay("We think it's taking place in the Western Wing. If you can somehow disrupt it, the power flowing into the Temple will be cut off. You'll have to destroy the altar in the basement to fully stop the ritual.")


    sm.setSpeakerID(9131003)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.flipSpeaker()
    sm.flipDialoguePlayerAsSpeaker()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendSay("Got it.")


    sm.setSpeakerID(9131003)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendSay("You must hurry, Kanna!")


    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(False, True, False, False)
    # Unhandled Field Effect [ObjectStateByString] Packet: 02 06 00 67 75 69 64 65 31
    # Unhandled Field Effect [ObjectStateByString] Packet: 02 06 00 67 75 69 64 65 32
    # Unhandled Field Effect [ObjectStateByString] Packet: 02 06 00 67 75 69 64 65 33
elif sm.getFieldID() == 807100111:
    sm.curNodeEventEnd(True)
    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(True, False, False, False)
    sm.showFieldEffect("JPKanna/text1", 0)
    sm.sendDelay(7000)


    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(False, True, False, False)
    sm.warp(807100101, 1)
elif sm.getFieldID() == 807100111:
    sm.curNodeEventEnd(True)
    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(True, False, False, False)
    sm.showFieldEffect("JPKanna/text2", 0)
    sm.sendDelay(7000)

    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(False, True, False, False)
    sm.warp(807100102, 1)
elif sm.getFieldID() == 807100102:
    sm.curNodeEventEnd(True)
    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(True, False, False, False)
    sm.showEffect("Effect/DirectionJP3.img/effect/kannaTuto/balloonMsg/1", 0, 0, -120, -2, -2, False, 0)
    sm.sendDelay(2000)


    sm.showEffect("Effect/DirectionJP3.img/effect/kannaTuto/balloonMsg/2", 0, 0, -120, -2, -2, False, 0)
    sm.sendDelay(2000)


    sm.showEffect("Effect/DirectionJP3.img/effect/kannaTuto/balloonMsg/3", 0, 0, -120, -2, -2, False, 0)
    sm.sendDelay(2000)


    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(False, True, False, False)
    sm.addPopUpSay(9130081, 5000, "#eEliminate the enemies!#n\r\n", "")
    sm.chatScript("Eliminate the enemies!")
    sm.showFieldEffect("aran/tutorialGuide2", 0)
    sm.removeSkill(40021183)
    sm.removeSkill(40021184)
    sm.removeSkill(40021185)
    sm.removeSkill(40021186)
elif sm.getFieldID() == 807100103:
    sm.curNodeEventEnd(True)
    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(True, False, False, False)
    sm.forcedInput(2)
    sm.sendDelay(1500)


    sm.forcedInput(6)
    sm.sendDelay(1000)


    sm.forcedInput(0)
    sm.showEffect("Effect/DirectionJP3.img/effect/kannaTuto/balloonMsg/4", 0, 0, -120, -2, -2, False, 0)
    sm.sendDelay(2000)


    sm.showEffect("Effect/DirectionJP3.img/effect/kannaTuto/balloonMsg/5", 0, 0, -120, -2, -2, False, 0)
    sm.sendDelay(2000)


    sm.forcedAction(1767, 0)
    sm.showEffect("Skill/4212.img/skill/42121005/tile/begin", 0, 0, 0, -2, -2, False, 0)
    sm.sendDelay(1400)


    sm.showEffect("Skill/4212.img/skill/42121005/tile/0", 0, 0, 0, -2, -2, False, 0)
    sm.showEffect("Effect/DirectionJP3.img/effect/kannaTuto/balloonMsg/6", 0, 0, -120, -2, -2, False, 0)
    sm.sendDelay(1440)


    sm.showEffect("Skill/4212.img/skill/42121005/tile/end", 0, 0, 0, -2, -2, False, 0)
    sm.sendDelay(960)


    sm.forcedInput(2)
    sm.sendDelay(1000)


    sm.forcedInput(0)
    sm.sendDelay(500)


    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(False, True, False, False)
    sm.warp(807100104, 0)
elif sm.getFieldID() == 807100104:
    sm.curNodeEventEnd(True)
    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(True, False, False, False)
    sm.showNpcSpecialActionByTemplateId(9131004, "back", 0)
    sm.forcedInput(2)
    sm.sendDelay(3500)


    sm.forcedInput(3)
    sm.showEffect("Effect/DirectionJP3.img/effect/kannaTuto/balloonMsg/7", 0, 0, -100, -2, -2, False, 0)
    sm.sendDelay(2000)


    sm.showEffect("Effect/DirectionJP3.img/effect/kannaTuto/balloonMsg/8", 0, 0, -100, -2, -2, False, 0)
    sm.sendDelay(2000)


    sm.showEffect("Effect/DirectionJP3.img/effect/kannaTuto/balloonMsg/9", 0, 250, -150, -2, -2, False, 0)
    sm.sendDelay(2000)


    sm.showEffect("Effect/DirectionJP3.img/effect/kannaTuto/balloonMsg/10", 0, 0, -100, -2, -2, False, 0)
    sm.sendDelay(2000)


    sm.forcedAction(1769, 0)
    sm.showEffect("Skill/4200.img/skill/42001000/effect", 0, 0, 0, -2, -2, False, 0)
    sm.sendDelay(270)


    sm.forcedAction(1770, 0)
    sm.showEffect("Skill/4200.img/skill/42001005/effect", 0, 0, 0, -2, -2, False, 0)
    sm.sendDelay(330)


    sm.showEffect("Skill/4212.img/skill/42121008/effect", 0, 0, 0, -2, -2, False, 0)
    sm.sendDelay(200)


    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(False, True, False, False)
    sm.warp(807100105, 0)
elif sm.getFieldID() == 807100105:
    if "1" not in sm.getQRValue(57376):
        sm.curNodeEventEnd(True)
        sm.setTemporarySkillSet(0)
        sm.setInGameDirectionMode(True, False, False, False)
        sm.sendDelay(1000)

        sm.createQuestWithQRValue(57376, "1")
        # Unhandled Stat Changed [MMP] Packet: 00 00 00 20 00 00 00 00 00 00 64 00 00 00 FF 00 00 00 00
        sm.setJob(4200)
        # Unhandled Stat Changed [STR] Packet: 00 00 40 00 00 00 00 00 00 00 04 00 FF 00 00 00 00
        # Unhandled Stat Changed [DEX] Packet: 00 00 80 00 00 00 00 00 00 00 04 00 FF 00 00 00 00
        # Unhandled Stat Changed [INTE] Packet: 00 00 00 01 00 00 00 00 00 00 23 00 FF 00 00 00 00
        # Unhandled Stat Changed [AP] Packet: 00 00 00 40 00 00 00 00 00 00 17 00 FF 00 00 00 00
        # Unhandled Stat Changed [HP] Packet: 00 00 00 04 00 00 00 00 00 00 DF 00 00 00 FF 00 00 00 00
        # Unhandled Stat Changed [MHP] Packet: 00 00 00 08 00 00 00 00 00 00 C2 00 00 00 FF 00 00 00 00
        sm.addSp(6, True)
        # Unhandled Stat Changed [MHP] Packet: 00 00 00 08 00 00 00 00 00 00 EE 01 00 00 FF 00 00 00 00
        # [INVENTORY_GROW] [01 1C ]
        # [INVENTORY_GROW] [02 1C ]
        # [INVENTORY_GROW] [03 1C ]
        # [INVENTORY_GROW] [04 1C ]
        sm.removeSkill(40021227)
        sm.giveSkill(40021227, 1, 1)
        # Unhandled Stat Changed [HP] Packet: 00 00 00 04 00 00 00 00 00 00 38 02 00 00 FF 00 00 00 00
        # Inventory Operation with 1 operations.
        # Unhandled Stat Changed [INSIGHT_EXP] Packet: 00 00 00 00 20 00 00 00 00 00 20 2B 00 00 FF 00 00 00 00
        # Unhandled Message [INC_NON_COMBAT_STAT_EXP_MESSAGE] Packet: 14 00 00 20 00 00 00 00 00 20 2B 00 00
        sm.playURLVideoByScript("http://nxcache.nexon.net/maplestory/video/yt/JPKanna.html")


    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(False, True, False, False)
    sm.setStandAloneMode(False)
    sm.startQuest(57471)
    sm.completeQuest(57471)
    sm.warp(807040000, 0)
