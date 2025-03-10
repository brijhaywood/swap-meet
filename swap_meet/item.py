class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
            return "Poor"
        elif self.condition <= 1:
            return "Fair"
        elif self.condition <= 2:
            return "Gently Used"
        elif self.condition <= 3:
            return "Good Condition"
        elif self.condition <= 4:
            return "Excellent Condition"
        elif self.condition <= 5:
            return "Like Brand New"
        else:
            return "Invalid Number"