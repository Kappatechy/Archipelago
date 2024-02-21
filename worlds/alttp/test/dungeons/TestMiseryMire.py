from .TestDungeon import TestDungeon


class TestMiseryMire(TestDungeon):

    def testMiseryMire(self):
        self.starting_regions = ['Misery Mire (Entrance)']
        self.run_tests([
            ["Misery Mire - Bridge Chest", False, []],
            ["Misery Mire - Bridge Chest", False, [], ['Pegasus Boots', 'Hookshot']],
            ["Misery Mire - Bridge Chest", False, [], ['Progressive Sword', 'Hammer', 'Fire Rod', 'Cane of Somaria', 'Progressive Bow', 'Ice Rod']],  #Ice Rod works!
            ["Misery Mire - Bridge Chest", True, ['Progressive Sword', 'Pegasus Boots']],
            ["Misery Mire - Bridge Chest", True, ['Progressive Sword', 'Hookshot']],
            ["Misery Mire - Bridge Chest", True, ['Hammer', 'Pegasus Boots']],
            ["Misery Mire - Bridge Chest", True, ['Hammer', 'Hookshot']],
            ["Misery Mire - Bridge Chest", True, ['Fire Rod', 'Pegasus Boots']],
            ["Misery Mire - Bridge Chest", True, ['Fire Rod', 'Hookshot']],
            ["Misery Mire - Bridge Chest", True, ['Cane of Somaria', 'Pegasus Boots']],
            ["Misery Mire - Bridge Chest", True, ['Cane of Somaria', 'Hookshot']],
            ["Misery Mire - Bridge Chest", True, ['Progressive Bow', 'Pegasus Boots']],
            ["Misery Mire - Bridge Chest", True, ['Progressive Bow', 'Hookshot']],
            ["Misery Mire - Bridge Chest", True, ['Ice Rod', 'Pegasus Boots']],
            ["Misery Mire - Bridge Chest", True, ['Ice Rod', 'Hookshot']],

            ["Misery Mire - Big Chest", False, []],
            ["Misery Mire - Big Chest", False, [], ['Big Key (Misery Mire)']],
            ["Misery Mire - Big Chest", False, [], ['Pegasus Boots', 'Hookshot']],
            ["Misery Mire - Big Chest", False, [], ['Progressive Sword', 'Hammer', 'Fire Rod', 'Cane of Somaria', 'Progressive Bow', 'Ice Rod']],
            ["Misery Mire - Big Chest", True, ['Big Key (Misery Mire)', 'Pegasus Boots', 'Progressive Sword']],
            ["Misery Mire - Big Chest", True, ['Big Key (Misery Mire)', 'Hookshot', 'Progressive Sword']],

            ["Misery Mire - Main Lobby", False, []],
            ["Misery Mire - Main Lobby", False, [], ['Pegasus Boots', 'Hookshot']],
            ["Misery Mire - Main Lobby", False, [], ['Small Key (Misery Mire)', 'Big Key (Misery Mire)']],
            ["Misery Mire - Main Lobby", True, ['Small Key (Misery Mire)', 'Hookshot', 'Progressive Sword']],
            ["Misery Mire - Main Lobby", True, ['Small Key (Misery Mire)', 'Pegasus Boots', 'Progressive Sword']],
            ["Misery Mire - Main Lobby", True, ['Big Key (Misery Mire)', 'Hookshot', 'Progressive Sword']],
            ["Misery Mire - Main Lobby", True, ['Big Key (Misery Mire)', 'Pegasus Boots', 'Progressive Sword']],

            ["Misery Mire - Cutscene Chest", False, []],
            ["Misery Mire - Cutscene Chest", False, [], ['Fire Rod', 'Lamp']],
            ["Misery Mire - Cutscene Chest", False, [], ['Pegasus Boots', 'Hookshot']],
            ["Misery Mire - Cutscene Chest", False, ['Small Key (Misery Mire)', 'Small Key (Misery Mire)'], ['Small Key (Misery Mire)']],
            ["Misery Mire - Cutscene Chest", True, ['Small Key (Misery Mire)', 'Small Key (Misery Mire)', 'Small Key (Misery Mire)', 'Lamp', 'Progressive Sword', 'Pegasus Boots']],
            ["Misery Mire - Cutscene Chest", True, ['Small Key (Misery Mire)', 'Small Key (Misery Mire)', 'Small Key (Misery Mire)', 'Lamp', 'Progressive Sword', 'Hookshot']],
            ["Misery Mire - Cutscene Chest", True, ['Small Key (Misery Mire)', 'Small Key (Misery Mire)', 'Small Key (Misery Mire)', 'Fire Rod', 'Progressive Sword', 'Pegasus Boots']],
            ["Misery Mire - Cutscene Chest", True, ['Small Key (Misery Mire)', 'Small Key (Misery Mire)', 'Small Key (Misery Mire)', 'Fire Rod', 'Progressive Sword', 'Hookshot']],

            ["Misery Mire - Torch Tiles Chest", False, []],
            ["Misery Mire - Torch Tiles Chest", False, [], ['Fire Rod', 'Lamp']],
            ["Misery Mire - Torch Tiles Chest", False, [], ['Pegasus Boots', 'Hookshot']],
            ["Misery Mire - Torch Tiles Chest", False, ['Small Key (Misery Mire)', 'Small Key (Misery Mire)'], ['Small Key (Misery Mire)']],
            ["Misery Mire - Torch Tiles Chest", True, ['Small Key (Misery Mire)', 'Small Key (Misery Mire)', 'Small Key (Misery Mire)', 'Lamp', 'Progressive Sword', 'Pegasus Boots']],
            ["Misery Mire - Torch Tiles Chest", True, ['Small Key (Misery Mire)', 'Small Key (Misery Mire)', 'Small Key (Misery Mire)', 'Lamp', 'Progressive Sword', 'Hookshot']],
            ["Misery Mire - Torch Tiles Chest", True, ['Small Key (Misery Mire)', 'Small Key (Misery Mire)', 'Small Key (Misery Mire)', 'Fire Rod', 'Progressive Sword', 'Pegasus Boots']],
            ["Misery Mire - Torch Tiles Chest", True, ['Small Key (Misery Mire)', 'Small Key (Misery Mire)', 'Small Key (Misery Mire)', 'Fire Rod', 'Progressive Sword', 'Hookshot']],

            ["Misery Mire - Switch Block Chest", False, []],
            ["Misery Mire - Switch Block Chest", False, [], ['Small Key (Misery Mire)', 'Big Key (Misery Mire)']],
            ["Misery Mire - Switch Block Chest", False, [], ['Pegasus Boots', 'Hookshot']],
            ["Misery Mire - Switch Block Chest", True, ['Small Key (Misery Mire)', 'Progressive Sword', 'Pegasus Boots']],
            ["Misery Mire - Switch Block Chest", True, ['Small Key (Misery Mire)', 'Progressive Sword', 'Hookshot']],
            ["Misery Mire - Switch Block Chest", True, ['Big Key (Misery Mire)', 'Progressive Sword', 'Pegasus Boots']],
            ["Misery Mire - Switch Block Chest", True, ['Big Key (Misery Mire)', 'Progressive Sword', 'Hookshot']],

            ["Misery Mire - Spike Chest", False, []],
            ["Misery Mire - Spike Chest", False, [], ['Pegasus Boots', 'Hookshot']],
            ["Misery Mire - Spike Chest", True, ['Progressive Sword', 'Pegasus Boots', 'Cape']],
            ["Misery Mire - Spike Chest", True, ['Progressive Sword', 'Hookshot', 'Cape']],
            ["Misery Mire - Spike Chest", True, ['Progressive Sword', 'Pegasus Boots', 'Cane of Byrna']],
            ["Misery Mire - Spike Chest", True, ['Progressive Sword', 'Hookshot', 'Cane of Byrna']],
            ["Misery Mire - Spike Chest", True, ['Progressive Sword', 'Pegasus Boots', 'Boss Heart Container']],
            ["Misery Mire - Spike Chest", True, ['Progressive Sword', 'Hookshot', 'Boss Heart Container']],

            ["Misery Mire - Boss", False, []],
            ["Misery Mire - Boss", False, [], ['Lamp']],
            ["Misery Mire - Boss", False, [], ['Cane of Somaria']],
            ["Misery Mire - Boss", False, [], ['Progressive Sword', 'Hammer', 'Progressive Bow']],
            ["Misery Mire - Boss", False, [], ['Big Key (Misery Mire)']],
            ["Misery Mire - Boss", False, [], ['Pegasus Boots', 'Hookshot']],
            ["Misery Mire - Boss", False, [], ['Bomb Upgrade (+5)', 'Bomb Upgrade (+10)', 'Bomb Upgrade (50)']],
            ["Misery Mire - Boss", True, ['Bomb Upgrade (+5)', 'Big Key (Misery Mire)', 'Lamp', 'Cane of Somaria', 'Progressive Sword', 'Pegasus Boots']],
            ["Misery Mire - Boss", True, ['Bomb Upgrade (+5)', 'Big Key (Misery Mire)', 'Lamp', 'Cane of Somaria', 'Hammer', 'Pegasus Boots']],
            ["Misery Mire - Boss", True, ['Bomb Upgrade (+5)', 'Big Key (Misery Mire)', 'Lamp', 'Cane of Somaria', 'Progressive Bow', 'Pegasus Boots']],
        ])