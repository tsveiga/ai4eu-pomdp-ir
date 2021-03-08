# ai4eu-pomdp-ir

This repository implements a simple interface with the POMDP with Inforamtion Rewards (POMDP-IR) solver.

# Running
## 1) Run the server with the solver
First, the docker container needs to be built.
`cd server && ./docker-build.sh`

Then, we can launch the service
`./docker-run.sh`

## 2) Run the client
Before running the client, it is needed to copy the protobuf message definitions to its folder and compile locally (the client needs to be aware of the message types)
`cd ../client && ./populate_and_rebuild_protobuf.sh`

# 2.1) Init the solver

# 2.2) Query actions (step)

# 2.3) Reset the policy server


**Note**: the client needs protobuf and grpcio-tools python packages installed.
