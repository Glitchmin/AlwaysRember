import Logic.Item as Items

class QuestList:
    def __init__(self):
        self.current = 0
        self.quests: list[Items.AbstractItem] = [
            [Items.sticks, Items.pickaxe],
            [Items.rubber, Items.metal_scraps, Items.sticks],
            [Items.sticks, Items.rubber, Items.metal_scraps, Items.radio]
        ]

    def deliver(self, item: Items.AbstractItem):
        if item in self.quests[self.current]:
            self.quests[self.current].remove(item)
        if len(self.quests[self.current]) == 0:
            self.urrent += 1

    def done(self) -> bool:
        return self.current == len(self.quests)