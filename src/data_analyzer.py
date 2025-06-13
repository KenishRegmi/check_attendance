from src.utils import parse_date, time_diff_minutes
from datetime import timedelta

def analyze_hourly_blocks_with_gap_check(data_list, max_gap=15):
    valid_data = [d for d in data_list if 'data' in d and 'date' in d]
    for d in valid_data:
        d['parsed_date'] = parse_date(d['date'])
        d['data'] = float(d['data'])

    sorted_data = sorted(valid_data, key=lambda x: x['parsed_date'])

    usage_blocks = []
    total_consumed = 0

    n = len(sorted_data)
    i = 0

    while i < n:
        start_time = sorted_data[i]['parsed_date']
        block = [sorted_data[i]]

        j = i + 1
        # Collect points within 1 hour from start_time
        while j < n and (sorted_data[j]['parsed_date'] - start_time) <= timedelta(hours=1):
            block.append(sorted_data[j])
            j += 1

        # Check gaps between consecutive points in the block
        gaps_ok = True
        for k in range(1, len(block)):
            gap = time_diff_minutes(block[k-1]['parsed_date'], block[k]['parsed_date'])
            if gap > max_gap:
                gaps_ok = False
                break

        if gaps_ok and len(block) > 1:
            consumption = abs(block[-1]['data'] - block[0]['data'])
            usage_blocks.append({
                "start": block[0]['date'],
                "end": block[-1]['date'],
                "consumed": round(consumption, 2),
                "samples": len(block)
            })
            total_consumed += consumption
            # Slide window by 1 index only (to catch overlapping blocks)
            i += 1
        else:
            # Slide window by 1 index if not valid block
            i += 1

    return usage_blocks, round(total_consumed, 2)
