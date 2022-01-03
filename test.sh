
conda remove --name gym_mujoco --all -y
conda create --name gym_mujoco python=3.7 -y
conda activate gym_mujoco

which pip

conda install -y -n gym_mujoco patchelf

pip install tqdm
pip install git+git://github.com/openai/gym#egg=gym[mujoco]

python collect.py --outprefix=mujoco

pip uninstall -y gym
pip install git+git://github.com/ikostrikov/gym#egg=gym[mujoco]
python collect.py --outprefix=dmc

python compare.py