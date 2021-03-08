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

# Finally, execute the act/observe/update belief loop

# First, get observation from somewhere (here, just a user input)
obs = print("Enter observation ids: ")
#obs = int(obs)
try: 
    obs = [] 
      
    while True: 
        obs.append(int(input())) 
          
# if the input is not-integer, just print the list 
except: 
    print(obs) 

stepInit = model_pb2.StepRequest(observations = obs)

response = stub.step(stepInit)

print('Policy returned action: '+str(response.action_name)+' with id: '+str(response.action))

print('Done!')
