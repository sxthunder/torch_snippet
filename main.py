import time
import os
from utils import print_args, set_seed
from log import Logger
from torch.utils.tensorboard import SummaryWriter
from argparse import ArgumentParser
project_path = ''

# 定义parser
parser = ArgumentParser()
parser.add_argument('-batch_size', default=128, type=int)
parser.add_argument('-output_name', default='', type=str)
parser.add_argument('-k_fold', default=-1, type=int)
parser.add_argument('-seed', default=123456, type=int)
args = parser.parse_args()

#定义时间格式
DATE_FORMAT = "%Y-%m-%d-%H:%M:%S"
#定义输出文件夹，如果不存在则创建,
if args.output_name == '':
    output_path = os.path.join('./output', time.strftime(DATE_FORMAT,time.localtime(time.time())))
else:
    output_path = os.path.join('./output', args.output_name)

if not os.path.exists(output_path):
    os.makedirs(output_path)

#配置tensorboard
tensor_board_log_path = os.path.join(output_path, 'tensor_board_log{}'.format('' if args.k_fold == -1 else args.k_fold))
writer = SummaryWriter(tensor_board_log_path)

#定义log参数
logger = Logger(output_path,'main{}'.format('' if args.k_fold == -1 else args.k_fold)).logger

#打印args
print_args(args, logger, output_path)

#设置seed
logger.info('set seed to {}'.format(args.seed))
set_seed(args)