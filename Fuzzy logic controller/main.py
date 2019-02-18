from Membership import sad,memberships
import defuzzify
import rule
import itertools


class FLC:
    def __init__(self, speed, acc, dist):
        self.s = speed
        self.a = acc
        self.d = dist
        self.s_index = list()
        self.a_index = list()
        self.d_index = list()

    def evaluate(self):
        spd = sad.speed(self.s)
        acc = sad.acceleration(self.a)
        dist = sad.distance(self.d)
        self.s_index = [i for i in range(len(spd)) if spd[i] > 0]
        self.a_index = [i for i in range(len(acc)) if acc[i] > 0]
        self.d_index = [i for i in range(len(dist)) if dist[i] > 0]
        print(self.sum_of_area())
        print(self.weighted_sum())

    def sum_of_area(self):
        sum_area = 0
        sum_product = 0
        for combination in itertools.product(self.s_index, self.a_index, self.d_index):
            centre, area = defuzzify.get_area(rule.get_rule(combination[0], combination[1], combination[2]))
            sum_area += area
            sum_product += area * centre
        return sum_product / sum_area

    def weighted_sum(self):
        sum_memb = 0
        sum_product = 0
        for combination in itertools.product(self.s_index, self.a_index, self.d_index):
            centre, _ = defuzzify.get_area(rule.get_rule(combination[0], combination[1], combination[2]))
            memb = sad.fuel(rule.get_rule(combination[0], combination[1], combination[2]), centre)
            sum_product += memb * centre
            sum_memb += memb
        return sum_product / sum_memb


if __name__ == "__main__":
    x = FLC(70, 15, 30)
    x.evaluate()
