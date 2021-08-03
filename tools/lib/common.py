import logging, argparse
from .nrf24 import *

channels = []
args = None
parser = None
radio = None

# Initialize the argument parser - opt: set channels to scan, the verbose of the device, lna for crazy radio
def init_args(description):

  global parser
  parser = argparse.ArgumentParser(description,
    formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=50,width=120))
  parser.add_argument('-c', '--channels', type=int, nargs='+', help='RF channels', default=list(range(2, 84)), metavar='N')
  parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output', default=False)
  parser.add_argument('-l', '--lna', action='store_true', help='Enable the LNA (for CrazyRadio PA dongles)', default=True)
  parser.add_argument('-i', '--index', type=int, help='Dongle index', default=0)

# Parse and process common comand line arguments
def parse_and_init():

  global parser
  global args
  global channels
  global radio

  # Parse the command line arguments
  args = parser.parse_args()

  # Setup logging
  level = logging.DEBUG if args.verbose else logging.INFO
  logging.basicConfig(level=level, format='[%(asctime)s.%(msecs)03d]  %(message)s', datefmt="%Y-%m-%d %H:%M:%S")

  # Set the channels
  channels = args.channels
  logging.debug('Using channels {0}'.format(', '.join(str(c) for c in channels)))

  # Initialize the radio
  radio = nrf24(args.index)
  if args.lna: radio.enable_lna()

