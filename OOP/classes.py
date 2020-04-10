class Weapon:
	def __init__(self, level_w, range_w, durability_w):
		self.level_w = level_w
		self.range_w = range_w
		self.durability_w = durability_w

	def description(self):
		print("Weapon [lv:",self.level_w,"/rg:",self.range_w,"/du:",self.durability_w,"] : ", end='')

class Sword(Weapon):
	def __init__(self, level_w, range_w, durability_w, alloy_s, blade_length_s):
		super().__init__(level_w, range_w, durability_w)
		self.alloy_s = alloy_s
		self.blade_length_s = blade_length_s

	def power(self):
		return self.level_w * self.blade_length_s;

	def strike(foe_distance):
		if (self.durability_w > 0 and foe_distance < self.range_w):
			self.durability_w-=1;
			return self.power(self)

	def description(self):
		super().description()
		print("A great sword made with ",self.alloy_s, " !")

class Bow(Weapon):
	def __init__(self, level_w, range_w, durability_w, elasticity_b, arrows_b):
		super().__init__(level_w, range_w, durability_w)
		self.elasticity_b = elasticity_b
		self.arrows_b = arrows_b

	def power(self):
		return self.level_w * self.elasticity_b;

	def description(self):
		super().description()
		print("A super-precise bow, very useful for hunting !")


if __name__ == '__main__':
	exacalibur = Sword(100, 10, 1000, 'Steal', 2)
	yumi = Bow(10, 100, 100, 50, 500)

	yumi.description();
	exacalibur.description();
	print ("The power of Excalibur is : ", exacalibur.power())
