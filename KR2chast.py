import matplotlib.pyplot as plt
from scipy import interpolate

a = 0.5
b = 0.3
N = [1000000]
S = [990000]
I = [7000]
R = [3000]
t = [0.25]

i = 0
dif = 10
while dif >= 1:
    math = S[i] - S[i]*a
    S.append(math)
    dif = S[i] - S[i+1]
    t.append(t[i] + 0.25)

    math = I[-1] + S[i]*a - I[-1] * b
    I.append(math)

    math = N[-1] - S[-1] - I[-1]
    R.append(math)
    i += 1

Sf = interpolate.interp1d(t, S, kind='cubic')
If = interpolate.interp1d(t, I, kind='cubic')
Rf = interpolate.interp1d(t, R, kind='cubic')

fig = plt.figure()
plt.title('Sf(t)')
plt.plot(t, Sf(t))
plt.grid()
fig = plt.figure()
plt.title('If(t)')
plt.plot(t, If(t))
plt.grid()
fig = plt.figure()
plt.title('Rf(t)')
plt.plot(t, Rf(t))
plt.grid()

fig = plt.figure()
plt.title('S(t),I(t),R(t)')

plt.plot(t, Sf(t), 'g', label = 'S(t)')
plt.plot(t, If(t), 'r',label = 'I(t)')
plt.plot(t, Rf(t), 'y',label = 'R(t)')
plt.legend(loc='upper right')
plt.grid()

print("S:",S)
print("I:",I)
print("R:",R)
print("T:",t)
plt.show()