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
y = v0 * t - 0.5 * g * t ** 2
print(y)