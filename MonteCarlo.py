import datetime
from random import gauss
import math
#S(T)=S(0)*e^(r-.5*v^2)
def generate_asset_price(S,v,r,T):
    return S * math.exp((r - 0.5 * v**2) * T + v * math.sqrt(T) * gauss(0,1.0)) #gauss = normal distribtion bellshape

def call_payoff(S_T,K):
    return max(0.0,S_T-K)

def put_payoff(S_T,K):
    return max(0.0,K-S_T)

S = 857.29 # underlying price
v = 0.2076 # vol of 20.76%
r = 0.0014 # rate of 0.14% assume constant
T = (datetime.date(2013,9,21) - datetime.date(2013,9,3)).days / 365.0
K = 860. #struck price
simulations = 100000
payoffs = []

discount_factor = math.exp(-r * T)#devidence??

for i in range(simulations):
    S_T = generate_asset_price(S,v,r,T)
    payoffs.append(
        call_payoff(S_T, K)
    )

call_price = discount_factor * (sum(payoffs) / float(simulations))

print ('Option Price is %.4f' % call_price)

