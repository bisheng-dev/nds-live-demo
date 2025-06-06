package nds_live_tile;

struct Lane {
    uint32 id;
    float64 coordinates[];
    string type;
};

struct Tile {
    uint16 level;
    uint64 mortonCode;
    Lane lanes[];
};