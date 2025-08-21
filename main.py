def find_missing_ranges(frames: list[int]) -> dict:
    if not frames:
        return {"gaps": [], "longest_gap": None, "missing_count": 0}

    frame_set = set(frames)
    start, end = min(frames), max(frames)

    gaps = []
    missing_count = 0
    longest_gap = None

    i = start
    while i <= end:
        if i not in frame_set:
            gap_start = i
            while i <= end and i not in frame_set:
                i += 1
            gap_end = i - 1
            gaps.append([gap_start, gap_end])

            size = gap_end - gap_start + 1
            missing_count += size
            if not longest_gap or size > (longest_gap[1] - longest_gap[0] + 1):
                longest_gap = [gap_start, gap_end]
        else:
            i += 1

    return {
        "gaps": gaps,
        "longest_gap": longest_gap,
        "missing_count": missing_count
    }