import os

script_dir = os.path.dirname(
    os.path.abspath(__file__)
)  # Get the absolute dir the script is in
os.chdir(script_dir)
base_hockey_path = os.path.normpath(os.path.join(script_dir, '../simulation/hockey/2025/'))
base_simulation_path = os.path.normpath(os.path.join(script_dir, '../simulation/BBA/2024/'))
base_nfl_simulation_path = os.path.normpath(os.path.join(script_dir, '../simulation/NFL Games/'))
base_cfb_simulation_path = os.path.normpath(os.path.join(script_dir, '../simulation/CFB Games/'))
base_superb_owl_path = os.path.normpath(os.path.join(script_dir, '../simulation/Superb Owl/'))