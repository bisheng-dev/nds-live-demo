#simulate the vehicle request aws for map data
import boto3
import sys
import os
sys.path.insert(0, os.path.abspath("generated"))
from generated.nds_live_tile.tile import Tile
from zserio import BitStreamReader


s3 = boto3.client('s3')
response = s3.get_object(Bucket='nds-live-raw-data-bx', Key='input/tile_1.bin')
data = response['Body'].read()

# 方法1：使用BitStreamReader
reader = BitStreamReader(data)
tile = Tile.from_reader(reader)
print(f"Received Tile with {len(tile.lanes)} lanes")