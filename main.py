import time

def open_water_valve(seconds):
		return seconds * 100

def is_temperature_ok(current_temp):
		return 75 <= current_temp <= 80

def add_seasoning(ketchup_ml, sausage_ml, powder_ml):
		return ketchup_ml == 3 and sausage_ml == 2 and powder_ml == 3

def fill_bucket(target_amount):
		return target_amount / 100

def heat_water(current_temp, target_temp):
		diff = target_temp - current_temp
		if diff <= 0:
			return 0
		return diff / 5

def maintain_temperature(current_temp, target_temp):
		if current_temp < target_temp:
			return "INCREASE"
		if current_temp > target_temp:
			return "DECREASE"
		return "MAINTAIN"

def cook_noodle(cooking_seconds):
		return "READY" if cooking_seconds >= 120 else "COOKING"

def dispense_all_seasonings():
		return {"ketchup": 3, "sausage": 2, "powder": 3}

class WaterSystem:
	def __init__(self):
		self.tank_capacity = 5000
		self.current_water_in_tank = 5000
		self.bucket_capacity = 500
		self.current_water_in_bucket = 0
		self.current_temperature = 25
		self.is_valve_open = False


	def open_valve(self, seconds):
		self.is_valve_open = True
		water_to_add = seconds * 100
		print(f"Valve opened for {seconds} seconds...")
		time.sleep(seconds)
		if water_to_add > self.current_water_in_tank:
			water_to_add = self.current_water_in_tank
		if self.current_water_in_bucket + water_to_add > self.bucket_capacity:
			water_to_add = self.bucket_capacity - self.current_water_in_bucket
		self.current_water_in_bucket += water_to_add
		self.current_water_in_tank -= water_to_add
		print(f"Added {water_to_add}ml water to bucket.")
		return water_to_add

	def close_valve(self):
		self.is_valve_open = False
		print("Valve closed. Waiting 2 seconds...")
		time.sleep(2)
		return

	def heat_up(self, seconds):
		increase = seconds * 5
		print(f"Heating up for {seconds} seconds...")
		time.sleep(seconds)
		self.current_temperature += increase
		if self.current_temperature > 100:
			self.current_temperature = 100
		print(f"Temperature increased by {increase}C.")
		return increase

	def cool_down(self, seconds):
		decrease = seconds * 5
		print(f"Cooling down for {seconds} seconds...")
		time.sleep(seconds)
		self.current_temperature -= decrease
		if self.current_temperature < 0:
			self.current_temperature = 0
		print(f"Temperature decreased by {decrease}C.")
		return decrease

	def empty_bucket(self):
		print("Emptying bucket... Waiting 2 seconds...")
		time.sleep(2)
		self.current_water_in_bucket = 0
		print("Bucket emptied.")
		return

	def get_status(self, noodles_portions, ketchup, sausage, powder, noodles_made):
		lines = [
			f"Water Tank: {self.current_water_in_tank}ml / {self.tank_capacity}ml",
			f"Bucket: {self.current_water_in_bucket}ml / {self.bucket_capacity}ml",
			f"Temperature: {self.current_temperature}C",
			f"Noodle Portions: {noodles_portions}",
			f"Ketchup: {ketchup}ml",
			f"Sausage: {sausage}ml",
			f"Powder: {powder}ml",
			f"Noodles Made: {noodles_made}",
		]
		return "\n".join(lines)

class Dispenser:
	def __init__(self, name, capacity, ml_per_trigger=1):
		self.name = name
		self.capacity = capacity
		self.current_amount = capacity
		self.ml_per_trigger = ml_per_trigger

	def trigger(self, times):
		total = times * self.ml_per_trigger
		if total > self.current_amount:
			total = self.current_amount
		self.current_amount -= total
		return total

	def refill(self):
		self.current_amount = self.capacity
		return

	def get_status(self):
		return f"[{self.current_amount} / {self.capacity}]"

class NoodleMachine:
	def __init__(self):
		self.water_system = WaterSystem()
		self.noodle_dispenser = Dispenser("Noodle", capacity=50, ml_per_trigger=1)
		self.ketchup_dispenser = Dispenser("Ketchup", capacity=1000, ml_per_trigger=1)
		self.sausage_dispenser = Dispenser("Sausage", capacity=1000, ml_per_trigger=1)
		self.powder_dispenser = Dispenser("Powder", capacity=1000, ml_per_trigger=1)
		self.noodles_made = 0

	def _delay(self, seconds):
		print(f"Waiting {seconds} seconds...")
		time.sleep(seconds)
		return

	def make_noodle(self):
		self.water_system.current_temperature = 25
		print("Filling water... Need 3 seconds for 300ml")
		self.water_system.open_valve(3)
		self.water_system.close_valve()
		print("Heating water from 25C to 77C... Need 10 seconds")
		self.water_system.heat_up(10)
		print("Dispensing 1 portion of noodle")
		self.noodle_dispenser.trigger(1)
		print("Cooking... Need 15 seconds")
		self._delay(15)
		print("Adding 3ml ketchup")
		for _ in range(3):
			self.ketchup_dispenser.trigger(1)
		print("Adding 2ml sausage")
		for _ in range(2):
			self.sausage_dispenser.trigger(1)
		print("Adding 3ml powder")
		for _ in range(3):
			self.powder_dispenser.trigger(1)
		print("Noodle is ready! Enjoy your meal!")
		print("Cleaning bucket... Need 2 seconds")
		self.water_system.empty_bucket()
		self.noodles_made += 1
		return

	def get_machine_status(self):
		print(self.water_system.get_status(
			self.noodle_dispenser.current_amount,
			self.ketchup_dispenser.current_amount,
			self.sausage_dispenser.current_amount,
			self.powder_dispenser.current_amount,
			self.noodles_made
		))
		return

def main():
	print("INSTANT NOODLE MAKER MACHINE")
	print("="*50)
	machine = NoodleMachine()
	print("\n📊 INITIAL STATUS:")
	print("-"*50)
	machine.get_machine_status()
	print("-"*50)
	print("\n" + "="*50)
	print("🍜 MAKING NOODLE #1...")
	print("="*50)
	machine.make_noodle()
	print("\n" + "="*50)
	print("🍜 MAKING NOODLE #2...")
	print("="*50)
	machine.make_noodle()
	print("\n📊 FINAL STATUS:")
	print("-"*50)
	machine.get_machine_status()
	print("-"*50)

if __name__ == "__main__":
	main()
