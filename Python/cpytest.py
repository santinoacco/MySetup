import configargparse
import os
import configparser
import yaml
import sys
sys.path.append('src/')
from cnn_photon_id_parser import set_parser

# print(parser.__dir__())
# p_yaml= configargparse.ArgParser(
        # config_file_parser_class=configargparse.YAMLConfigFileParser)
# p_yaml.add('-c','--config', is_config_file=True)
# p_yaml.add('-gO','--G_OutDir',type=yaml.safe_load,required=True)
# # p_yaml.add('-IO','--IOdirs',type=yaml.safe_load,action="append")
# # p_yaml.add('-InDir_DP',required=False)
# p_yaml.add('-metrics','--Metrics',type=yaml.safe_load)

p_ini = configargparse.ArgParser(
        config_file_parser_class=configargparse.ConfigparserConfigFileParser
        )
p_ini.add('-c','--config',is_config_file=True)
# p_ini.add('-gO','--IOdirs')
# p_ini.add('--g_outdir')
p_ini.add('--g_outdir',env_var='GLOBAL_OUTDIR')
# IF EXPECTED ARG IS A DICT THEN, ADD IT WITH `add_argument` and add `type=yaml.safe_load`
p_ini.add_argument('--metrics',type=yaml.safe_load)

# p_ini.add('-metrics','--Metrics')


def main(argv):

    args = set_parser()
    # args = p_yaml.parse_args()
    print(args)
    print("train out is ", args.train_out)
    print("train out is ", type(args.train_out))
    print("train out is is false?", args.train_out is False)
    print("train out is is None?", args.train_out is None)
    print("train out exists?", os.path.exists(args.train_out))

    # args = p_ini.parse_args()

    # print(args)
    # print(os.path.exists(args.g_outdir))
    # print(os.path.exists(args.IOdirs))

    # cfg = configparser.ConfigParser()
    # cfg.read('config.ini')
    # print(cfg.sections())
    # print(os.path.exists(cfg['IOdirs']['G_OutDir']))

    # print(type(args.IOdirs))
    # print(type(args.IOdirs['DataProcessing_OUT']))

    # print(args.IOdirs.items())

    # args=p_ini.parse_args()
    # print(args)
    # cfg = args.config.ConfigParser()
    # print(cfg)


    # print(args['IOdirs'])

    return
if __name__ == '__main__':
    main(sys.argv[1:])


