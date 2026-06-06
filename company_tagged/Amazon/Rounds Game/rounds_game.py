class SOlution:
    def solve(self, power, armor):

        #the maximum armor we can spend is min(armor, max(power))
        #then we want to have at least 1 heart when all power - max_armor happens

        max_armor = min(armor, max(power))
        lives = sum(power) - max_armor + 1
        return lives