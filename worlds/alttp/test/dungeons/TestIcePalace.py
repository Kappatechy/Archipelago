from .TestDungeon import TestDungeon


class TestIcePalace(TestDungeon):

    def testIcePalace(self):
        self.starting_regions = ['Ice Palace (Entrance)']
        self.run_tests([
            ["Ice Palace - Icebreaker Chest", False, []],
            ["Ice Palace - Icebreaker Chest", False, [], ['Hammer']],
            ["Ice Palace - Icebreaker Chest", False, [], ['Progressive Glove']],
            ["Ice Palace - Icebreaker Chest", False, [], ['Fire Rod', 'Bombos']],
            ["Ice Palace - Icebreaker Chest", False, [], ['Fire Rod', 'Progressive Sword']],
            ["Ice Palace - Icebreaker Chest", False, [], ['Bomb Upgrade (+5)', 'Bomb Upgrade (+10)', 'Bomb Upgrade (50)']],
            ["Ice Palace - Icebreaker Chest", True, ['Bomb Upgrade (+5)', 'Progressive Glove', 'Fire Rod', 'Hammer', 'Hookshot', 'Small Key (Ice Palace)']],
            ["Ice Palace - Icebreaker Chest", True, ['Bomb Upgrade (+5)', 'Progressive Glove', 'Bombos', 'Progressive Sword', 'Hammer', 'Hookshot', 'Small Key (Ice Palace)']],
            #@todo: Change from item randomizer - Right side key door is only in logic if big key is in there
            #["Ice Palace - Icebreaker Chest", True, ['Progressive Glove', 'Cane of Byrna', 'Fire Rod', 'Hammer', 'Small Key (Ice Palace)', 'Small Key (Ice Palace)']],
            #["Ice Palace - Icebreaker Chest", True, ['Progressive Glove', 'Cane of Byrna', 'Bombos', 'Progressive Sword', 'Hammer', 'Small Key (Ice Palace)', 'Small Key (Ice Palace)']],
            #["Ice Palace - Icebreaker Chest", True, ['Progressive Glove', 'Cape', 'Fire Rod', 'Hammer', 'Small Key (Ice Palace)', 'Small Key (Ice Palace)']],
            #["Ice Palace - Icebreaker Chest", True, ['Progressive Glove', 'Cape', 'Bombos', 'Progressive Sword', 'Hammer', 'Small Key (Ice Palace)', 'Small Key (Ice Palace)']],

            ["Ice Palace - Pengator Chest", False, []],
            ["Ice Palace - Pengator Chest", False, [], ['Fire Rod', 'Bombos']],
            ["Ice Palace - Pengator Chest", False, [], ['Fire Rod', 'Progressive Sword']],
            ["Ice Palace - Pengator Chest", True, ['Fire Rod']],
            ["Ice Palace - Pengator Chest", True, ['Bombos', 'Progressive Sword']],

            ["Ice Palace - Tongue Pull Chest", False, []],
            ["Ice Palace - Tongue Pull Chest", False, [], ['Hammer']],
            ["Ice Palace - Tongue Pull Chest", False, [], ['Progressive Glove']],
            ["Ice Palace - Tongue Pull Chest", False, [], ['Fire Rod', 'Bombos']],
            ["Ice Palace - Tongue Pull Chest", False, [], ['Fire Rod', 'Progressive Sword']],
            ["Ice Palace - Tongue Pull Chest", False, [], ['Bomb Upgrade (+5)', 'Bomb Upgrade (+10)', 'Bomb Upgrade (50)']],
            ["Ice Palace - Tongue Pull Chest", True, ['Bomb Upgrade (+5)', 'Progressive Glove', 'Fire Rod', 'Hammer', 'Hookshot', 'Small Key (Ice Palace)']],
            ["Ice Palace - Tongue Pull Chest", True, ['Bomb Upgrade (+5)', 'Progressive Glove', 'Bombos', 'Progressive Sword', 'Hammer', 'Hookshot', 'Small Key (Ice Palace)']],
            #["Ice Palace - Tongue Pull Chest", True, ['Progressive Glove', 'Cane of Byrna', 'Fire Rod', 'Hammer', 'Small Key (Ice Palace)', 'Small Key (Ice Palace)']],
            #["Ice Palace - Tongue Pull Chest", True, ['Progressive Glove', 'Cane of Byrna', 'Bombos', 'Progressive Sword', 'Hammer', 'Small Key (Ice Palace)', 'Small Key (Ice Palace)']],
            #["Ice Palace - Tongue Pull Chest", True, ['Progressive Glove', 'Cape', 'Fire Rod', 'Hammer', 'Small Key (Ice Palace)', 'Small Key (Ice Palace)']],
            #["Ice Palace - Tongue Pull Chest", True, ['Progressive Glove', 'Cape', 'Bombos', 'Progressive Sword', 'Hammer', 'Small Key (Ice Palace)', 'Small Key (Ice Palace)']],

            ["Ice Palace - Spike Room", False, []],
            ["Ice Palace - Spike Room", False, [], ['Fire Rod', 'Bombos']],
            ["Ice Palace - Spike Room", False, [], ['Fire Rod', 'Progressive Sword']],
            ["Ice Palace - Spike Room", False, [], ['Bomb Upgrade (+5)', 'Bomb Upgrade (+10)', 'Bomb Upgrade (50)']],
            ["Ice Palace - Spike Room", True, ['Bomb Upgrade (+5)', 'Fire Rod', 'Hookshot', 'Small Key (Ice Palace)']],
            ["Ice Palace - Spike Room", True, ['Bomb Upgrade (+5)', 'Bombos', 'Progressive Sword', 'Hookshot', 'Small Key (Ice Palace)']],
            #["Ice Palace - Spike Room", True, ['Cape', 'Fire Rod', 'Small Key (Ice Palace)', 'Small Key (Ice Palace)']],
            #["Ice Palace - Spike Room", True, ['Cape', 'Bombos', 'Progressive Sword', 'Small Key (Ice Palace)', 'Small Key (Ice Palace)']],
            #["Ice Palace - Spike Room", True, ['Cane of Byrna', 'Fire Rod', 'Small Key (Ice Palace)', 'Small Key (Ice Palace)']],
            #["Ice Palace - Spike Room", True, ['Cane of Byrna', 'Bombos', 'Progressive Sword', 'Small Key (Ice Palace)', 'Small Key (Ice Palace)']],

            ["Ice Palace - Freezor Chest", False, []],
            ["Ice Palace - Freezor Chest", False, [], ['Fire Rod', 'Bombos']],
            ["Ice Palace - Freezor Chest", False, [], ['Fire Rod', 'Progressive Sword']],
            ["Ice Palace - Freezor Chest", False, [], ['Bomb Upgrade (+5)', 'Bomb Upgrade (+10)', 'Bomb Upgrade (50)']],
            ["Ice Palace - Freezor Chest", True, ['Bomb Upgrade (+5)', 'Fire Rod']],
            ["Ice Palace - Freezor Chest", True, ['Bomb Upgrade (+5)', 'Bombos', 'Progressive Sword']],

            ["Ice Palace - Iced T Room", False, []],
            ["Ice Palace - Iced T Room", False, [], ['Fire Rod', 'Bombos']],
            ["Ice Palace - Iced T Room", False, [], ['Fire Rod', 'Progressive Sword']],
            ["Ice Palace - Iced T Room", False, [], ['Bomb Upgrade (+5)', 'Bomb Upgrade (+10)', 'Bomb Upgrade (50)']],
            ["Ice Palace - Iced T Room", True, ['Bomb Upgrade (+5)', 'Fire Rod']],
            ["Ice Palace - Iced T Room", True, ['Bomb Upgrade (+5)', 'Bombos', 'Progressive Sword']],

            ["Ice Palace - Big Chest", False, []],
            ["Ice Palace - Big Chest", False, [], ['Big Key (Ice Palace)']],
            ["Ice Palace - Big Chest", False, [], ['Fire Rod', 'Bombos']],
            ["Ice Palace - Big Chest", False, [], ['Fire Rod', 'Progressive Sword']],
            ["Ice Palace - Big Chest", False, [], ['Bomb Upgrade (+5)', 'Bomb Upgrade (+10)', 'Bomb Upgrade (50)']],
            ["Ice Palace - Big Chest", True, ['Bomb Upgrade (+5)', 'Big Key (Ice Palace)', 'Fire Rod']],
            ["Ice Palace - Big Chest", True, ['Bomb Upgrade (+5)', 'Big Key (Ice Palace)', 'Bombos', 'Progressive Sword']],

            ["Ice Palace - Boss", False, []],
            ["Ice Palace - Boss", False, [], ['Hammer']],
            ["Ice Palace - Boss", False, [], ['Progressive Glove']],
            ["Ice Palace - Boss", False, [], ['Big Key (Ice Palace)']],
            ["Ice Palace - Boss", False, [], ['Fire Rod', 'Bombos']],
            ["Ice Palace - Boss", False, [], ['Fire Rod', 'Progressive Sword']],
            ["Ice Palace - Boss", False, [], ['Bomb Upgrade (+5)', 'Bomb Upgrade (+10)', 'Bomb Upgrade (50)']],
            # need hookshot now to reach the right side for the 6th key
            ["Ice Palace - Boss", True, ['Bomb Upgrade (+5)', 'Progressive Glove', 'Big Key (Ice Palace)', 'Fire Rod', 'Hammer', 'Small Key (Ice Palace)', 'Small Key (Ice Palace)', 'Hookshot']],
            ["Ice Palace - Boss", True, ['Bomb Upgrade (+5)', 'Progressive Glove', 'Big Key (Ice Palace)', 'Fire Rod', 'Hammer', 'Cane of Somaria', 'Small Key (Ice Palace)', 'Hookshot']],
            ["Ice Palace - Boss", True, ['Bomb Upgrade (+5)', 'Progressive Glove', 'Big Key (Ice Palace)', 'Bombos', 'Progressive Sword', 'Hammer', 'Small Key (Ice Palace)', 'Small Key (Ice Palace)', 'Hookshot']],
            ["Ice Palace - Boss", True, ['Bomb Upgrade (+5)', 'Progressive Glove', 'Big Key (Ice Palace)', 'Bombos', 'Progressive Sword', 'Hammer', 'Cane of Somaria', 'Small Key (Ice Palace)', 'Hookshot']],
        ])