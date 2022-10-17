import hydra
from omegaconf import OmegaConf, DictConfig
import logging

import os

log = logging.getLogger(__name__)

# %%
@hydra.main(config_path='config', config_name='train_cfg', version_base=None)
def main(cfg: DictConfig) -> None:
    log.info(OmegaConf.to_yaml(cfg))
    log.info(os.getcwd())
    log.debug('Debug level message')

if __name__=='__main__':
    main()
