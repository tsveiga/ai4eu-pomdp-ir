import time
from concurrent import futures

import grpc

# import the generated classes :
import model_pb2
import model_pb2_grpc

##############
#Specific imports and definitions
from java_factory import *

port = 8061
# create a class to define the server functions, derived from
class POMDPIRServicer(model_pb2_grpc.POMDPIRServicer):
    ####POMDP-IR specific vars
    pomdpfile = 'src/models/patrol.dat'#'/pkg/pomdp-ir/models/patrol.dat'

    pomdp = JClass.POMDP(JClass.JString(pomdpfile))
    
    # nRounds = 1
    # numBelStates = 2000
    # maxBelStates = 10000
    # episodeLength = 50
    # threshold = 0.001
    # explorProb = 0.8
    # nIterations = 2
    # maxAlphaSetSize = 5000
    basename = 'src/models/' #'/pkg/pomdp-ir/models/'
    
    #policyfile = basename + '-' + str(nIterations) + '.pomdp'
    
    belief = None

    execStep = 0

    current_action = 0
    #############

    manager = None

    def compute_policy(self, request, context):

        #This calls the POMDP-IR solver. For now, we assume the model file is hardcoded (ToDO: how to pass a user model file into it?)
        self.pomdp.solve(request.nRounds, request.numBelStates, request.maxBelStates, request.episodeLength, request.threshold, request.explorProb, request.nIterations, request.maxAlphaSetSize, JClass.JString(self.basename))
        
        response = model_pb2.ComputePolicyResponse()     
        response.some_output = 1
        
        return response

    #This method is intended to reset the execution of the POMDP, i.e., return belief to initial and step counter to 0. For a scenario where the user wants to start from the beginning without going throught the policy computation process again.
    def reset_execution(self, request, context):

        # We start by fetching the initial belief
        self.belief = self.pomdp.initialBelState

        self.execStep = 0
            
        response = model_pb2.ResetExecutionResponse()     
        response.some_output = True
        
        return response

    def step(self, request, context):
        if self.execStep == 0:
            print('Initial step')
            self.execStep += 1
            self.belief = self.pomdp.initialBelState

            self.current_action = self.pomdp.policyQuery(self.belief)
            action_name = self.pomdp.actions[self.current_action].name
        
            response = model_pb2.StepResponse()     
            response.action = self.current_action
            response.action_name = action_name

            return response

        self.execStep += 1
        print('Executing step ' + str(self.execStep))

        ###Get observations

        obs = [0]*self.pomdp.nObsVars
        for i in range(0,self.pomdp.nObsVars):
            obs[i] = request.observations[i]
            
        print('Observations = {}, {}'.format(obs,type(obs)))


        ###Update belief
        self.belief = self.pomdp.beliefUpdate(self.belief,self.current_action,obs)
        
        ##Get action from policy with udpated belief
        self.current_action = self.pomdp.policyQuery(self.belief)
        #__import__("pdb").set_trace()
        action_name = self.pomdp.actions[self.current_action].name
        
        response = model_pb2.StepResponse()     
        response.action = self.current_action
        response.action_name = action_name
        
        return response

# creat a grpc server :
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

model_pb2_grpc.add_POMDPIRServicer_to_server(POMDPIRServicer(), server)

print("Starting server. Listening on port : " + str(port))
server.add_insecure_port("[::]:{}".format(port))
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
