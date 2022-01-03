import os
import pickle

import numpy as np
from absl import app, flags
from common import env_names

FLAGS = flags.FLAGS

flags.DEFINE_string('outprefix', 'mujoco', '')


def main(_):
    data_folder = 'data'

    for env_name in env_names:
        print(f'Checking {env_name}')
        mujoco_file_name = os.path.join(data_folder, f'mujoco_{env_name}')
        with open(mujoco_file_name, 'rb') as f:
            mujoco_data = pickle.load(f)
        
        dmc_file_name = os.path.join(data_folder, f'dmc_{env_name}')
        with open(dmc_file_name, 'rb') as f:
            dmc_data = pickle.load(f)
    
        for key in mujoco_data.keys():
            for i in range(len(mujoco_data[key])):
                if key in ['states', 'actions', 'next_states']:
                    assert np.all(np.equal(mujoco_data[key][i], dmc_data[key][i]))
                elif key in ['rewards', 'dones']:
                    assert mujoco_data[key][i] == dmc_data[key][i]
                elif key == 'infos':
                    for k, v in mujoco_data[key][i].items():
                        if type(v) in [float, np.float64, bool]:
                            assert mujoco_data[key][i][k] == dmc_data[key][i][k]
                        else:
                          raise ValueError
                else:
                    raise ValueError
            print(f'{env_name} {key}: OK')
if __name__ == '__main__':
    app.run(main)
