from neural import *

inputs = [1, 1, 1, 1, \
          0, 1, 0, 1, \
          1, 0, 0, 1, \
          1, 1, 1, 1]    

print("Output: ", predict(np.array(inputs)))


from graphics import *

# output = graph("X", 0.000324, [2, 1, .3, .2, .1, .0])
output = graph()

print(output)

