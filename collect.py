import copy
import os
import pickle

import gym
import numpy as np
from absl import app, flags
from tqdm import tqdm

from common import env_names

FLAGS = flags.FLAGS

flags.DEFINE_string('outprefix', 'mujoco', '')


def main(_):
    for env_name in env_names:
        env = gym.make(env_name)

        data = dict(states=[],
                    actions=[],
                    next_states=[],
                    rewards=[],
                    dones=[],
                    infos=[])

        env.seed(42)
        env.action_space.seed(42)

        done = True
        for i in tqdm(range(10000)):
            if done:
                state = np.copy(env.reset())

            action = env.action_space.sample()
            next_state, reward, done, info = env.step(action)

            data['states'].append(np.copy(state))
            data['actions'].append(np.copy(action))
            data['next_states'].append(np.copy(next_state))
            data['rewards'].append(reward)
            data['dones'].append(done)
            data['infos'].append(copy.deepcopy(info))

        save_folder = 'data'
        os.makedirs(save_folder, exist_ok=True)

        save_file = os.path.join(save_folder, f'{FLAGS.outprefix}_{env_name}')
        with open(save_file, 'wb') as f:
            pickle.dump(data, f)


if __name__ == '__main__':
    app.run(main)
