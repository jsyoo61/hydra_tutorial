# 1. simple

Recommend running the following on the shell script as a tutorial.\
You should notice that `outputs/` directory is created when the scripts are single-run, and `multirun/` directory is created when the scripts are multi-run.\
Also, each directory that is created contains `.hydra/` directory which has:
- the current user configurations (`.hydra/config.yaml`) for the process
- the current hydra configurations (`.hydra/hydra.yaml`) for the process
- the current overridden configurations (`.hydra/overrides.yaml`) for the process

The followings are example runs:

- `python hydra_sample.py` # basic functionality
- `python hydra_sample.py -m run.random_seed=0,1,2,3,4` # [multirun](https://hydra.cc/docs/tutorials/basic/running_your_app/multi-run/) parameter sweep with `-m` flag
- `python hydra_sample.py -m "run.random_seed=range(0,5)` # multirun sweep with [predefined command line hydra syntax](https://hydra.cc/docs/advanced/override_grammar/extended/)
- `python hydra_sample.py +new_variable=0` # [Inserting new config values](https://hydra.cc/docs/tutorials/basic/your_first_app/simple_cli/) (you could also add predefined config_groups that was not included in the main config)
- `python hydra_sample.py -m +new_variable=0,1,2,3,4` # Insert new config & sweep

configs that start with `hydra` are internal hydra configs that changes the behavior of the runs. They are internally defined so you have to refer to the [documents](https://hydra.cc/docs/configure_hydra/intro/).\
Single run examples:

- `python hydra_sample.py hydra.job.chdir=True` # [Change working directory](https://hydra.cc/docs/tutorials/basic/running_your_app/working_directory/) (directory of process) when run. You can change this behavior to be the default by setting `hydra.job.chdir: True` in the `config/train_cfg.yaml` file
- `python hydra_sample.py hydra.job.chdir=True hydra.run.dir=outputs/custom_directory` # Specifying custom directory by overriding (hidden) hydra configuration
- `python hydra_sample.py hydra.run.dir=outputs/custom_directory` # Note that this does not change the working directory, but the logging file (`hydra_sample.log`) & `.hydra/` files are generated in the `hydra.run.dir`.

Multirun examples:
- `python hydra_sample.py -m hydra.job.chdir=True +random_seed=0,1,2,3,4` # Multirun with changing working directory
- `python hydra_sample.py -m hydra.job.chdir=True hydra.sweep.dir=multirun/custom_directory +random_seed=0,1,2,3,4` # Specifying custom multirun directory by overriding (hidden) hydra configuration
- `python hydra_sample.py -m hydra.sweep.dir=multirun/custom_directory +random_seed=0,1,2,3,4` # Specifying custom multirun directory to store `hydra_sample.log` & `.hydra/`, but does not change working direcotry
- `python hydra_sample.py -m hydra.job.chdir=True hydra.sweep.dir=multirun/custom_directory hydra.sweep.subdir=run_${random_seed} +random_seed=0,1,2,3,4` # Specifying custom multirun directory & subdir
- `python hydra_sample.py -m hydra.job.chdir=True hydra/launcher=joblib hydra.launcher.n_jobs=2 "+random_seed=range(0,5)"` # Multirun sweep with parallel processes & n_job limit. Need to install `hydra-joblib-launcher` first! (`pip install hydra-joblib-launcher`)

Debug mode:
- `python hydra_sample.py hydra.verbose=True` # Run using different [logging](https://hydra.cc/docs/tutorials/basic/running_your_app/logging/) levels

<!--
- `python hydra_sample.py -c job`
- `python hydra_sample.py -c hydra`
- `python hydra_sample.py -c all` -->
