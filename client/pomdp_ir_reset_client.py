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

resetExecInit = model_pb2.Empty()

response = stub.reset_execution(resetExecInit)

print('Success, reset execution')

print('Done!')
