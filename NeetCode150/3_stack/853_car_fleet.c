typedef struct Item {
    int pos;
    float time;
} Item;

int cmp(const void* a, const void* b) {
    const Item* ia = (const Item*)a;
    const Item* ib = (const Item*)b;

    return ib->pos - ia->pos;  // descending order
}

int carFleet(int target, int* position, int positionSize, int* speed, int speedSize) {
    if (positionSize == 0) {
        return 0;
    }

    Item* items = malloc(positionSize * sizeof(Item));

    for (int i = 0; i< positionSize; i++) {
        items[i].pos = position[i];
        items[i].time = (float) (target - position[i]) / speed[i];
    }

    qsort(items, positionSize, sizeof(Item), cmp);

    float curr_fleet_time = items[0].time;
    int fleets = 1;

    for (int i = 1; i< positionSize; i++) {
        if (items[i].time > curr_fleet_time) {
            curr_fleet_time = items[i].time;
            fleets++;
        }
    }

    free(items);

    return fleets;
}