import sys
from twocaptcha import TwoCaptcha

image = sys.argv[1]
### casesensitive = sys.argv[2]

solver = TwoCaptcha('2e76b87ebfb0c83b4aa02d14f6043d71')

res = solver.normal(image)

time.sleep(15)

print(res)
  
