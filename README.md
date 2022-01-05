# Preparation

```bash
mkdir ~/.mujoco/
cd ~/.mujoco/

wget https://roboti.us/download/mjpro150_linux.zip
sudo apt install unzip
unzip mjpro150_linux.zip
wget https://roboti.us/file/mjkey.txt
rm mjpro150_linux.zip
echo "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:$HOME/.mujoco/mjpro150/bin" >> ~/.bashrc
source ~/.bashrc 

wget https://github.com/deepmind/mujoco/releases/download/2.1.0/mujoco210-linux-x86_64.tar.gz
tar xvf mujoco-2.1.0-linux-x86_64.tar.gz
tm mujoco-2.1.0-linux-x86_64.tar.gz
```

# Run collection and comparison
```bash
sh test.sh
```
