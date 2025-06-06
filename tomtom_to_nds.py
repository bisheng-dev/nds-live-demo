#transform the supplier map into the format of nds.live
import sys
import os
sys.path.insert(0, os.path.abspath("generated"))

import json
import argparse

from nds_live_tile.tile import Tile
from nds_live_tile.lane import Lane
import zserio

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to input JSON file")
    parser.add_argument("--output", required=True, help="Path to output binary file")
    args = parser.parse_args()

    # 读取 JSON 文件
    with open(args.input, "r") as f:
        data = json.load(f)

    # 构造 Lane 对象列表
    lanes = []
    for lane_data in data["lanes"]:
        lane = Lane(
            id_=lane_data["id"],
            coordinates_=lane_data["coordinates"],
            type_=lane_data["type"]
        )
        lanes.append(lane)

    # 构造 Tile 对象
    tile = Tile(
        level_=data["level"],
        morton_code_=data["mortonCode"],
        lanes_=lanes
    )

    # 计算偏移并写入二进制文件
    bitstream = zserio.BitStreamWriter()
    tile.initialize_offsets()
    tile.write(bitstream)

    with open(args.output, "wb") as f:
        f.write(bitstream.byte_array)


    print(f"✅ 成功写入: {args.output}")

if __name__ == "__main__":
    main()
