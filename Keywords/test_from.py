#from
#"from" is a keyword, used to import 'specified section from the module'.

#datetime is a module and we just importing specified section "time"
from datetime import time

x = time(minute=30)
print("Prints minute: ", x)

y = time(hour=12)
print("Prints hours: ", y)

z = time(second=12)
print("Prints seconds: ", z)