import numpy as np
e = np.exp(1)

def sigmoid(x):
    print("a:", 1 / (1 + e**(-x)))
    print(type(x))
    return 1 / (1 + e**(-x))

def Dsigmoid(x):
    return sigmoid(x) * (1.0 - sigmoid(x))  




def binaryStepDemo(x):
  if x >= 0.0:
      return 1.0
  else:
      return 0.0

def binaryStep(x):
  y = []
  for i in range(len(x)):
    if x[i] >= [0.0]:
      y.append([1.0])
    else:
      y.append([0.0])
  return np.array(y)
  
        
def DbinaryStep(x):
    return np.array([[1.0] for row in range(0,len(x))])





def softplus(x):
    return np.log(1+((e)**x))
 
def Dsoftplus(x):
    return 1/(1+((e)**-x))





def johnStep(x):
  return 1 / (1 + e**((-50*x)))

def DjohnStep(x):
  return johnStep(x)*(1.0*johnStep(x))


"""

def ReLUDemo(x):
  if x > 0:
      return x
  else:
      return 0

def ReLU(x):
  y = []
  for i in range(len(x)):
    if x[i] > [0.0]:
      y.append([x])
    else:
      y.append([0.0])
  return np.array(y)

    
def DReLU(x):
  if x < 0:
    return 0
  else:
    return 1
  # y = []
  # for i in range(len(x)):
  #   if x[i] < [0.0]:
  #     y.append([0.0])
  #   else:
  #     y.append([1.0])
  # return np.array(y)




# SoftExponential:
def softex(x,a=0.01):
  if a < 0:
    return -((np.log(1-a*(x+a)))/a)
  elif a == 0:
    return x
  elif a > 0:
    return (((e)**(a*x))/a)+a
  
# SoftExponential derivative:
def Dsoftex(x,a=0.01):
  return 1/(1-a*(a+x)) if a < 0 else (e)**(a*x)



# Soft Clipping:
def softclip(x,a=0.01):
  return (1/a)*(np.log10((1+((e)**(a*x)))/(1+(e)**(a*(x-1)))))
  
# Soft Clipping derivative.
def Dsoftclip(x,a=0.01,p=1):
  def sech(x):
    return np.cosh(x)**(-1)
  return (0.5)*(np.sinh(p/2))*(sech((p*x)/2))*sech((p/2)*(1-x))


  # Gaussian: 
def gaussian(x):
  return (e)**((-x)**2)
   
# Gaussian derivative:
def Dgaussian(x):
    return -2*x*(e)**((-x)**2)


def x(x):
    return x

def Dx(x):
    return 1


# Inverse square root LINEAR unit (ISRLU):
def isrlu(x,a=0.01):
   return x/np.sqrt(1+(a*(x**2))) if x < 0 else x

# ISRLU derivative:
def Disrlu(x,a=0.01):
  return (1/np.sqrt(1+(a*(x**2))))**3 if x < 0 else 1


  # Soft Clipping:
def softclip(x,a=0.01):
  return (1/a)*(np.log10((1+((e)**(a*x)))/(1+(e)**(a*(x-1)))))
  
# Soft Clipping derivative.
def Dsoftclip(x,a=0.01,p=1):
  def sech(x):
    return np.cosh(x)**(-1)
  return (0.5)*(np.sinh(p/2))*(sech((p*x)/2))*sech((p/2)*(1-x))
"""