
class Bread:
    pass

    def __init__(self, slices: int, **nutrition):
        self.slices = slices
        self.nutrition_per_slice = nutrition
        self.total_nutrition = { k: v * slices for k, v in nutrition.items()}

    def get_nutrition(self, slices: int) -> dict[str, float]:
        """Calculate the total nutrition for a given number of slices."""
        return { k: v * slices for k, v in self.nutrition_per_slice.items() }

class WholeWheatBread(Bread):
    pass

class RyeBread(Bread):
    pass


"""
| Bread type            | Calories | Carbs     | Sugar   | Protein    | Fat       | Fiber     | Sodium |
| --------------------- | -------- | --------- | ------- | ---------- | --------- | --------- | ------ |
| Bread, standard white | 67–77    | 13–19 g   |  6-8 g  |  2–3.5 g   | 0.8–1.2 g | 0.6–1.2 g | 170 mg |
| Whole wheat bread     | 69–92    | 13.8–17 g |  1-2 g  |  2.7–4.0 g | 1.1–2.0 g | 1.9–2.8 g | 138 mg |
| Rye bread             | 82–85    | 15–15.5 g |  4-6 g  |  2.7–3.0 g | 1.0–1.1 g | 1.8–2.0 g | 211 mg |
"""
print('White bread:')
wb = Bread(12, calories=77, carbs=19, sugar=8, protein=3.5, fat=1.2, fiber=1.2, sodium=170)
print(wb.nutrition_per_slice)
print(wb.slices)
print(wb.total_nutrition)
print(wb.get_nutrition(2))
print()
print('Wholewheat bread:')
wwb = Bread(12, calories=92, carbs=17, sugar=2, protein=4, fat=2, fiber=2.8, sodium=138)
print(wwb.nutrition_per_slice)
print(wwb.slices)
print(wwb.total_nutrition)
print(wwb.get_nutrition(2))
print()
print('Rye bread:')
rb = Bread(12, calories=85, carbs=15.5, sugar=6, protein=3, fat=1.1, fiber=2, sodium=211)
print(rb.nutrition_per_slice)
print(rb.slices)
print(rb.total_nutrition)
print(rb.get_nutrition(2))

"""
Claude's fix to my solution:
This preserves your **nutrition idea as an extension point while satisfying the spec: 
each subclass has a fixed identity, get_nutrition is inherited, and no stale slice count is stored.

class Bread:
    def __init__(self, **nutrition):
        self.calories = nutrition.get('calories', 66)
        self.carbs    = nutrition.get('carbs', 12)
        self.sodium   = nutrition.get('sodium', 170)
        self.sugar    = nutrition.get('sugar', 1)
        self.fat      = nutrition.get('fat', 0.8)

    def get_nutrition(self, slices: int) -> dict[str, float]:
        return {k: v * slices for k, v in vars(self).items()}


class WholeWheatBread(Bread):
    def __init__(self):
        super().__init__(calories=67, carbs=12, sodium=138, sugar=1.4, fat=1)


class RyeBread(Bread):
    def __init__(self):
        super().__init__(calories=67, carbs=12, sodium=172, sugar=1, fat=0.8)
        
        
Which is the recommended best practice Lerner's or your fix?
The **nutrition flexibility in the fix is solving a problem the spec doesn't have. 
If nutritional values are fixed per bread type — which they are, a WholeWheatBread 
always has the same values — then accepting arbitrary keyword arguments adds indirection 
without benefit. It also obscures what the class actually expects; a reader has to 
trace through get() calls with defaults to understand the data model.
Lerner's version is more direct: the attributes are plainly listed in __init__, 
there's nothing to trace, and vars(self) just works. It's also slightly more honest 
about the design — super().__init__() isn't called in the subclasses because the 
subclasses are replacing the parent's data entirely, not extending it. 
That's a reasonable choice when the subclass has nothing to add behaviorally.
The one thing worth noting: Lerner's subclasses don't call super().__init__(), 
which is a pattern that can cause subtle bugs if the hierarchy grows (e.g., 
if Bread later gains non-nutritional setup logic). But for a flat, stable hierarchy 
like this one, it's a pragmatic tradeoff.
Rule of thumb: flexibility mechanisms (**kwargs, get() with defaults) earn their 
place when variation comes from the caller. When variation is fixed per class, 
encode it directly in the class.

"""