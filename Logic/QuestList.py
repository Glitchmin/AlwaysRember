from Logic.Item import AbstractItem, Quests

class QuestList:
    def __init__(self):
        self.current = 0
        self.quests: list[list[AbstractItem]] = [
            [Quests.sticks, Quests.poop],
            [Quests.rubber, Quests.metal_scraps, Quests.sticks],
            [Quests.sticks, Quests.rubber, Quests.metal_scraps, Quests.bucket]
        ]

    def deliver(self, item: AbstractItem):
        if item in self.quests[self.current]:
            self.quests[self.current].remove(item)
        if len(self.quests[self.current]) == 0:
            self.current += 1

    def done(self) -> bool:
        return self.current == len(self.quests)
