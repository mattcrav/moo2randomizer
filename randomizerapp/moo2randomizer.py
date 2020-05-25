import random


class Result:
    def __init__(self):
        self.difficulty = None
        self.galaxy_size = None
        self.galaxy_age = None
        self.players = None
        self.tech_level = None
        self.tactical_combat = None
        self.random_events = None
        self.antarans_attack = None
        self.picks = []
        self.randomize()

    @staticmethod
    def valid_picks(removed, base, pnts, neg, gl, mn):
        v = [x for x in base if x[2] <= pnts]
        v = [x for x in v if x[2] >= neg]
        v = [x for x in v if pnts - x[2] >= gl]
        if pnts == gl and mn:
            v = [x for x in v if x[2] == 0]
        v = [x for x in v if x not in removed]
        return v

    def make_picks(self, pcks, pnts, neg, gl, mn):
        removed_picks = []
        picks = []
        available_picks = self.valid_picks(removed_picks, pcks, pnts, neg, gl, mn)

        while len(available_picks) > 0:
            pick = random.choice(available_picks)
            removed_picks += [x for x in pcks if x[1] == pick[1]]
            pnts -= pick[2]
            if pick[2] < 0:
                neg -= pick[2]
            picks.append(pick)
            available_picks = self.valid_picks(removed_picks, pcks, pnts, neg, gl, mn)

        return picks, pnts > gl

    def randomize(self):
        result = '----NEW GAME----'
        difficulty = ['Tutor', 'Easy', 'Average', 'Hard', 'Impossible']
        self.difficulty = f'DIFFICULTY: {random.choice(difficulty)}\n'
        result += self.difficulty
        galaxy_size = ['Small', 'Medium', 'Large', 'Cluster', 'Huge']
        self.galaxy_size = f'GALAXY SIZE: {random.choice(galaxy_size)}\n'
        result += self.galaxy_size
        galaxy_age = ['Organic Rich', 'Mineral Rich', 'Average']
        self.galaxy_age = f'GALAXY AGE: {random.choice(galaxy_age)}\n'
        result += self.galaxy_age
        players = [2, 3, 4, 5, 6, 7, 8]
        self.players = f'PLAYERS: {random.choice(players)}\n'
        result += self.players
        tech_level = ['Pre Warp', 'Post Warp', 'Advanced', 'Average']
        self.tech_level = f'TECH LEVEL: {random.choice(tech_level)}\n'
        result += self.tech_level
        tactical_combat = ['Yes', 'No']
        self.tactical_combat = f'TACTICAL COMBAT: {random.choice(tactical_combat)}\n'
        result += self.tactical_combat
        random_events = ['Yes', 'No']
        self.random_events = f'RANDOM EVENTS: {random.choice(random_events)}\n'
        result += self.random_events
        antarans_attack = ['Yes', 'No']
        self.antarans_attack = f'ANTARANS ATTACK: {random.choice(antarans_attack)}\n'
        result += self.antarans_attack
        result += '\n'

        result += '---SELECT RACE---\n'
        races = [
            'Alkari',
            'Bulrathi',
            'Darlocks',
            'Elerians',
            'Gnolams',
            'Humans',
            'Klackons',
            'Meklars',
            'Mrrshan',
            'Psilons',
            'Sakkra',
            'Silicoids',
            'Trilarians'
        ]
        result += f'RACE: {random.choice(races)}\n'
        all_picks = [
            ['-50% Growth', 'Population', -4],
            ['+50% Growth', 'Population', 3],
            ['+100% Growth', 'Population', 6],
            ['-1/2 Food', 'Farming', -3],
            ['+1 Food', 'Farming', 4],
            ['+2 Food', 'Farming', 7],
            ['-1 Production', 'Industry', -3],
            ['+1 Production', 'Industry', 3],
            ['+2 Production', 'Industry', 6],
            ['-1 Research', 'Science', -3],
            ['+1 Research', 'Science', 3],
            ['+2 Research', 'Science', 6],
            ['-0.5 BC', 'Money', -4],
            ['+0.5 BC', 'Money', 5],
            ['+1.0 BC', 'Money', 8],
            ['-20', 'Ship Defense', -2],
            ['+25', 'Ship Defense', 3],
            ['+50', 'Ship Defense', 7],
            ['-20', 'Ship Attack', -2],
            ['+20', 'Ship Attack', 2],
            ['+50', 'Ship Attack', 4],
            ['-10', 'Ground Combat', -2],
            ['+10', 'Ground Combat', 2],
            ['+20', 'Ground Combat', 4],
            ['-10', 'Spying', -3],
            ['+10', 'Spying', 3],
            ['+20', 'Spying', 6],
            ['Feudal', 'Governments', -4],
            ['Dictatorship', 'Governments', 0],
            ['Democracy', 'Governments', 7],
            ['Unification', 'Governements', 6],
            ['Low-G World', 'Special Abilities (Gravity)', -5],
            ['High-G World', 'Special Abilities (Gravity)', 6],
            ['Aquatic', 'Special Abilities (Aquatic)', 5],
            ['Subterranean', 'Special Abilities (Subterranean)', 6],
            ['Large Home World', 'Special Abilities (Size)', 1],
            ['Rich Home World', 'Special Abilities (Wealth)', 2],
            ['Poor Home World', 'Special Abilities (Wealth)', -1],
            ['Artifacts World', 'Special Abilities (Artifacts)', 3],
            ['Cybernetic', 'Special Abilities (Life)', 4],
            ['Lithovore', 'Special Abilities (Life)', 10],
            ['Repulsive', 'Special Abilities (Diplomacy)', -6],
            ['Charismatic', 'Special Abilities (Diplomacy)', 3],
            ['Uncreative', 'Special Abilities (Creativity)', -4],
            ['Creative', 'Special Abilities (Creativity)', 8],
            ['Tolerant', 'Special Abilities (Tolerant)', 10],
            ['Fantastic Traders', 'Special Abilities (Traders)', 4],
            ['Telepathic', 'Special Abilities (Telepathic)', 6],
            ['Lucky', 'Special Abilities (Lucky)', 3],
            ['Omniscient', 'Special Abilities (Omniscient)', 3],
            ['Stealthy Ships', 'Special Abilities (Stealth)', 4],
            ['Trans Dimensional', 'Special Abilities (Trans Dimensional)', 5],
            ['Warlord', 'Special Abilities (Warlord)', 4],
        ]
        neg_min = -10
        goal = 0
        points = 10
        min_possible = True
        leftover_points = True
        final_picks = []
        while leftover_points:
            final_picks, leftover_points = self.make_picks(all_picks, points, neg_min, goal, min_possible)

        result += 'PICKS:\n'
        labels = []
        for p in all_picks:
            if p in final_picks:
                self.picks.append(f'{p[1]}: {p[0]}')
                t = p[1]
                if 'Special Abilities' in p[1]:
                    t = 'Special Abilities'
                if t not in labels:
                    result += f'{t}\n'
                    labels.append(t)
                result += f'\t{p[0]}\n'

        return result


if __name__ == '__main__':
    r = Result()
    print(r.randomize())
