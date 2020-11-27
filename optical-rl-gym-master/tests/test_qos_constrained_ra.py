import gym
import optical_rl_gym
from optical_rl_gym.utils import Path
from optical_rl_gym.envs.rwa_env import shortest_path, shortest_available_path, least_loaded_path
from optical_rl_gym.utils import evaluate_heuristic, random_policy

import pickle
import logging
import numpy as np

import matplotlib.pyplot as plt

load = 250
logging.getLogger('qosconstrainedenv').setLevel(logging.INFO)

seed = 20
episodes = 10
episode_length = 1000

monitor_files = []
policies = []
k_paths = 5
num_service_classes=2
classes_arrival_probabilities=[.5, .5]
classes_reward=[10., 1.]
num_spectrum_resources = 16
load = 50

# topology_name = 'gbn'
# topology_name = 'nobel-us'
# topology_name = 'germany50'
with open(f'../examples/topologies/nsfnet_chen_5-paths.h5', 'rb') as f:
    topology = pickle.load(f)

env_args = dict(topology=topology, seed=10, allow_rejection=True, load=load, mean_service_holding_time=25,
                episode_length=episode_length, num_service_classes=num_service_classes,
                classes_arrival_probabilities=classes_arrival_probabilities,
                classes_reward=classes_reward, num_spectrum_resources=num_spectrum_resources, k_paths=k_paths)

env_rnd = gym.make('QoSConstrainedRA-v0', **env_args)
mean_reward_rnd, std_reward_rnd = evaluate_heuristic(env_rnd, random_policy, n_eval_episodes=episodes)
print('Rnd:', mean_reward_rnd, std_reward_rnd)

env_sp = gym.make('QoSConstrainedRA-v0', **env_args)
mean_reward_sp, std_reward_sp = evaluate_heuristic(env_sp, shortest_path, n_eval_episodes=episodes)
print('SP:', mean_reward_sp, std_reward_sp, env_sp.actions_output)

env_sap = gym.make('QoSConstrainedRA-v0', **env_args)
mean_reward_sap, std_reward_sap = evaluate_heuristic(env_sap, shortest_available_path, n_eval_episodes=episodes)
print('SAP:', mean_reward_sap, std_reward_sap, env_sap.actions_output)

env_llp = gym.make('QoSConstrainedRA-v0', **env_args)
mean_reward_llp, std_reward_llp = evaluate_heuristic(env_llp, least_loaded_path, n_eval_episodes=episodes)
print('LLP:', mean_reward_llp, std_reward_llp, env_llp.actions_output)
