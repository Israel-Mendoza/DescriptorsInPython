class Countdown:

    def __init__(self, start):
        self.start = start + 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        self.start -= 1
        return self.start


class Rocket:
    # The countdown class attribute will be shared
    # amont the Rocket class instances
    countdown = Countdown(10)


r1 = Rocket()
r2 = Rocket()

print(f"Rocket 1 value: {r1.countdown}")
print(f"Rocket 2 value: {r2.countdown}")
print(f"Rocket 1 value: {r1.countdown}")
print(f"Rocket 2 value: {r2.countdown}")
print(f"Rocket 1 value: {r1.countdown}")
print(f"Rocket 2 value: {r2.countdown}")
print(f"Rocket 1 value: {r1.countdown}")
print(f"Rocket 2 value: {r2.countdown}")
print(f"Rocket 1 value: {r1.countdown}")
print(f"Rocket 2 value: {r2.countdown}")
