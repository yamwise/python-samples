def mergeRanges(ranges):

    # Sort by start time
    sorted_ranges = sorted(ranges)

    # Initialize merged_ranges with the earliest meeting
    merged_ranges = [sorted_ranges[0]]

    for current_meeting_start, current_meeting_end in sorted_ranges[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_ranges[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_ranges[-1] = (last_merged_meeting_start,
                                 max(last_merged_meeting_end,
                                     current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_ranges.append(
                (current_meeting_start, current_meeting_end))

    return merged_ranges


print(mergeRanges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
print(mergeRanges([(1, 2), (2, 3)]))
print(mergeRanges([(1, 5), (2, 3)]))
print(mergeRanges([(1, 10), (2, 6), (3, 5), (7, 9)]))
