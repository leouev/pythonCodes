import sys
g = 9.81
try:
    v0 = float(sys.argv[1])
except:
    print("forgot to input the v0")
    sys.exit(1)

try:
    t = float(sys.argv[2])
except:
    print("forgot to input the t")
    sys.exit(1)

if t > 0 and t < (2.0 * v0 / g):
    y = v0 * t - 0.5 * g * t ** 2
else:
    print("the time is invalid")
    sys.exit(1)
print(y)