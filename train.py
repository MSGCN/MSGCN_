from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import yaml
import numpy as np

from lib.utils import load_graph_data
from model.msgcn_supervisor import MSGCNSupervisor


def main(args):
    with open(args.config_filename) as f:
        supervisor_config = yaml.load(f)

        graph_pkl_filename = supervisor_config['data'].get('graph_pkl_filename')
        adj_mx, mask = load_graph_data(graph_pkl_filename)

        supervisor = MSGCNSupervisor(adj_mx=adj_mx, mask=mask, **supervisor_config)

        supervisor.train()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_filename', default=None, type=str,
                        help='Configuration filename for restoring the model.')
    parser.add_argument('--use_cpu_only', default=False, type=bool, help='Set to true to only use cpu.')
    args = parser.parse_args()
    main(args)
