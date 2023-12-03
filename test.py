from main.model import AtariNet
from main.agent import Agent
from main.environment import *
import torch
import os

# This is the testing script (epsilon value to something very low
# and load the model)

if __name__ == "__main__":

    os.environ['KMP_DUPLICATE_LIB_OK'] = "TRUE"

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    environment = DQNPong(device = device)

    model = AtariNet(nb_actions = 6)

    model.to(device)

    model.load_the_model()

    agent = Agent(model = model, 
                device = device,
                epsilon = 0.05,
                min_epsilon = 0.1,
                nb_warmup = 2000,
                nb_actions = 6,
                learning_rate = 0.00025,
                memory_capacity = 100000,
                batch_size = 32)

    # Change games_amount to based on what game you choose, as 
    # one game may not be enough for some games
    agent.test(env = environment, games_amount = 3)