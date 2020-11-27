from gym.envs.registration import register

register(
    id='RMSCA-v0',
    entry_point='optical_rl_gym.envs:RMSCAEnv',
)

register(
    id='DeepRMSCA-v0',
    entry_point='optical_rl_gym.envs:DeepRMSCAEnv',
)

register(
    id='RWA-v0',
    entry_point='optical_rl_gym.envs:RWAEnv',
)

register(
    id='QoSConstrainedRA-v0',
    entry_point='optical_rl_gym.envs:QoSConstrainedRA',
)
