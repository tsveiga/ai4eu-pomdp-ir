# ai4eu-pomdp-ir

This repository implements a simple interface with the POMDP with Inforamtion Rewards (POMDP-IR) solver.

# Running
## 1) Run the server with the solver
First, the docker container needs to be built.
`cd server && ./docker-build.sh`

Then, we can launch the service
`./docker-run.sh`

## 2) Run the client
Before running the clients, it is needed to copy the protobuf message definitions to its folder and compile locally (the client needs to be aware of the message types)
`cd ../client && ./populate_and_rebuild_protobuf.sh`

There are three client scripts, detailed as follows.

### 2.1) Init the solver

The first script connects to the service which computes the policy. It sends a request with the solver parameters (check the ComputePolicyRequest message definition for which parameters) and waits for the solver to compute the policy.
`python3 pomdp_ir_init_client.py`

### 2.2) Query actions (step)

After the policy is computed, one wants to implement the execution flow. This is a decision loop where the server expects the current observations and returns the best action to execute according to the computed policy.
The current version of the client serves only as an example of the execution flow, therefore the observations are inputed manually by the user in the command line.
`python3 pomdp_ir_step_client.py`

### 2.3) Reset the policy server

If at some point, one wants to restart the execution, this script connects to the reset_execution service which restarts the internal status of the solver (i.e., restarts the step counter, belief state to the initial, etc).
`python3 pomdp_ir_reset_client.py`


**Notes**: 
- the client needs protobuf and grpcio-tools python packages installed.
- the current version of the server is restricted to a patrolling model, which is included in the container. Future works includes to allow the user to pass model files into the container.

