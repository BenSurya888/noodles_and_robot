import time

# TASK 1
capacity_water = 500  # ml
time_stamp = 100  # second

def open_water_valve(seconds):
		total_water = time_stamp * seconds
		if total_water > capacity_water:
			total_water = capacity_water
		return int(total_water)

def is_temperature_ok(current_temp):
		if 75 <= current_temp <= 80:
			return True
		else:
			return False

def add_seasoning(ketchup_ml, sausage_ml, powder_ml):
		if ketchup_ml == 3 and sausage_ml == 2 and powder_ml == 3:
			return True
		else:
			return False

def fill_bucket(target_amount):
		total_filled = 0
		seconds = 0
		while total_filled < target_amount:
			total_filled += open_water_valve(5)
			seconds += 1
		return seconds

seconds_needed = fill_bucket(500)
print(f"Seconds needed to fill bucket: {seconds_needed} seconds")

def heat_water(current_temp, target_temp):
		if current_temp >= target_temp:
			return 0
		temp_diff = target_temp - current_temp
		seconds_needed = temp_diff / 5
		return int(seconds_needed)

seconds_to_heat = heat_water(25, 80)
print(f"Seconds needed to heat water: {seconds_to_heat} seconds")

min_temp = 75
max_temp = 80

def maintain_temperature(current_temp, target_temp):
		if current_temp < min_temp:
			return "increase"
		elif current_temp > max_temp:
			return "decrease"
		else:
			return "maintain"

cooking_seconds = 120

def cook_noodle(cooking_seconds):
		if cooking_seconds >= 120:
			return "ready"
		elif cooking_seconds < 120:
			return "cooking"

def dispense_all_seasonings():
	ketchup_dispensed = 3
	sausage_dispensed = 2
	powder_dispensed = 3

	result = {
		'ketchup': ketchup_dispensed,
		'sausage': sausage_dispensed,
		'powder': powder_dispensed
	}

print(f"Dispensed seasonings: {dispense_all_seasonings()}ml")

# TASK 2
class WaterSystem:
	def __init__(self):
		self.tank_capacity = 5000
		self.bucket_capacity = 500
		self.current_water_in_bucket = 0
		self.current_temperature = 25
		self.is_valve_open = False


	def open_valve(self, seconds):
		water_add = 0
		seconds_per_time = 0

		while self.current_water_in_bucket < self.bucket_capacity and seconds_per_time < seconds:
			water_add = open_water_valve(1)
			self.current_water_in_bucket += water_add
			if self.current_water_in_bucket > self.bucket_capacity:
				self.current_water_in_bucket = self.bucket_capacity
			seconds_per_time += 1
			print(f"Filling... Current water in bucket: {self.current_water_in_bucket}ml")
			time.sleep(1)

	def close_valve(self, target_fill=500):
		seconds_per_time = 0
		while self.current_water_in_bucket > target_fill:
			self.current_water_in_bucket -= 100
			if self.current_water_in_bucket < target_fill:
				self.current_water_in_bucket = target_fill
			seconds_per_time += 1
			print(f"Closing valve... Current water in bucket: {self.current_water_in_bucket}ml")
			time.sleep(1)
		print(f"Valve closed. Final water in bucket: {self.current_water_in_bucket}ml")
		return seconds_per_time
		
		
	def heat_up(self, target_temp):
		seconds_per_time = 0
		while self.current_temperature < target_temp:
			self.current_temperature += 5
			if self.current_temperature > target_temp:
				self.current_temperature = target_temp
			seconds_per_time += 1
			print(f"Heating... Current temperature: {self.current_temperature}C")
			time.sleep(1)
		print(f"Target temperature {target_temp}C reached.")
		return seconds_per_time

	def cool_down(self, target_temp):
		seconds_per_time = 0
		while self.current_temperature > target_temp:
			self.current_temperature -= 5
			if self.current_temperature < target_temp:
				self.current_temperature = target_temp
			seconds_per_time += 1
			print(f"Cooling... Current temperature: {self.current_temperature}C")
			time.sleep(1)
		print(f"Target temperature {target_temp}C reached.")
		return seconds_per_time

	def empty_bucket(self):
		print("Emptying bucket...")
		seconds_per_time = 0
		while self.current_water_in_bucket > 0:
			self.current_water_in_bucket -= 100
			if self.current_water_in_bucket < 0:
				self.current_water_in_bucket = 0
			seconds_per_time += 1
			print(f"Emptying... Current water in bucket: {self.current_water_in_bucket}ml")
			time.sleep(1)
		print("Bucket emptied.")
		return seconds_per_time

	def get_status(self, noodles_portions, ketchup, sausage, powder, noodles_made):
		lines = [
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
		dispensed = 0
		for i in range(times):
			if self.current_amount > 0:
				self.current_amount -= self.ml_per_trigger
				dispensed += self.ml_per_trigger
				print(f"Dispensing {self.name}... {dispensed}{self.name if self.name != 'Noodle' else ' portion'} dispensed")
				time.sleep(1)
			else:
				print(f"{self.name} out of stock!")
				break
		return dispensed

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
		for i in range(seconds):
			print(f"Cooking... {i+1}s")
			time.sleep(1)
		return

	def make_noodle(self):
		self.water_system.current_temperature = 25
		print("Filling water... Need 3 seconds for 300ml")
		self.water_system.open_valve(3)
		print("="*50)
		print("Closing valve to keep 300ml water in bucket...")
		self.water_system.close_valve(1)
		print("="*50)
		print("Heating water from 25C to 77C... Need 10 seconds")
		self.water_system.heat_up(77)
		print("="*50)
		print("Dispensing 1 portion of noodle")
		self.noodle_dispenser.trigger(1)
		print("="*50)
		print("Cooking... Need 15 seconds")
		self._delay(15)
		print("="*50)
		print("Adding 3ml ketchup")
		self.ketchup_dispenser.trigger(3)
		print("="*50)
		print("Adding 2ml sausage")
		self.sausage_dispenser.trigger(2)
		print("="*50)
		print("Adding 3ml powder")
		self.powder_dispenser.trigger(3)
		print("="*50)
		print("Noodle is ready! Enjoy your meal!")
		print("="*50)
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
