from random import randint
from timeit import default_timer as timer

import grpc

# import the generated classes
import model_pb2
import model_pb2_grpc

start_ch = timer()
port_addr = "localhost:8061"

# open a gRPC channel
channel = grpc.insecure_channel(port_addr)

# create a stub (client)
stub = model_pb2_grpc.POMDPIRStub(channel)

# First, call the service to compute policy
policyInit = model_pb2.ComputePolicyRequest()

policyInit.nRounds = 1
policyInit.numBelStates = 2000
policyInit.maxBelStates = 10000
policyInit.episodeLength = 50
policyInit.threshold = 0.001
policyInit.explorProb = 0.8
policyInit.nIterations = 2
policyInit.maxAlphaSetSize = 5000

response = stub.compute_policy(policyInit)

print('Success, computed policy')

print('Done!')
