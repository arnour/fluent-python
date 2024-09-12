from example_8_4 import Duck, alert, alert_bird, alert_duck


daffy = Duck()

# Valid call, because alert has no type hints
alert(daffy)

# Valid call, because alert_duck takes a Duck argument, and daffy is a Duck
alert_duck(daffy)

# Valid call, because alert_bird takes a Bird argument,
# and daffy is also a Bird—the superclass of Duck
alert_bird(daffy)
