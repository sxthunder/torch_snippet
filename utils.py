import random
import torch
import numpy as np

def print_args(args, logger, output_path):
    logger.info('#'*20 + 'Arguments' + '#'*20)
    arg_dict = vars(args)
    for k, v in arg_dict.items():
        logger.info('{}:{}'.format(k, v))
    logger.info('output path is {}'.format(output_path))

def set_seed(args):
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)