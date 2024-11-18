x = float(input())
eta=float(input())
step=int(input())

for t in range(1, step + 1):
  new_x = x - eta * (2 * x - 4)
  dist = abs(new_x - x)
  if dist < 1e-3:
    print("x_min = " + str(new_x) + ", loss_function = " + str(new_x**2 - 4*x + 4) + ", after " + str(t) + " step")
    break
  else:
    x = new_x

if dist >= 1e-3:
  print("Cannot find x_min after", step, "step with learning rate eta =", eta)
