# Import deque from the collections library, which is a list-like container with fast appends and pops on either end.
from collections import deque


# the First-In, First-Out (FIFO) page replacement algorithm.
def fifo(reference_string, num_frames):
    """FIFO Page Replacement Algorithm"""
    # Use a deque as a queue to easily add to the right and remove from the left.
    frames = deque()
    # Use a set for fast checking of whether a page is currently in a frame.
    page_set = set()
    # Initialize the count of page faults to zero.
    page_faults = 0

    # Loop through each page in the user-provided reference string.
    for page in reference_string:
        # Check if the current page is NOT in memory (a page fault).
        if page not in page_set:
            # If it's a fault, increase the counter.
            page_faults += 1
            # If the frames are already full...
            if len(frames) == num_frames:
                # ...remove the oldest page from the left of the deque (queue).
                oldest_page = frames.popleft()
                # Also remove it from the set for consistency.
                page_set.remove(oldest_page)
            # Add the new page to the right of the deque (end of the queue).
            frames.append(page)
            # Add the new page to the set.
            page_set.add(page)
    # Return the total number of page faults.
    return page_faults

# Defines the Least Recently Used (LRU) page replacement algorithm.
def lru(reference_string, num_frames):
    """LRU Page Replacement Algorithm"""
    # Use a list to store the frames. The least recently used will be at the front (index 0).
    frames = []
    # A dictionary to check for a page's existence quickly.
    page_map = {}
    # Initialize the count of page faults to zero.
    page_faults = 0

    # Loop through each page in the user-provided reference string.
    for page in reference_string:
        # Check if the page is already in memory (a page hit).
        if page in page_map:
            # If it's a hit, move the page to the end of the list to mark it as most recently used.
            frames.remove(page)
            frames.append(page)
        # This block executes if the page is NOT in memory (a page fault).
        else:
            # If it's a fault, increase the counter.
            page_faults += 1
            # If the frames are already full...
            if len(frames) == num_frames:
                # ...remove the least recently used page, which is at the front of the list.
                lru_page = frames.pop(0)
                # Also remove it from the map.
                del page_map[lru_page]
            # Add the new page to the end of the list (making it the most recently used).
            frames.append(page)
            # Add the new page to the map.
            page_map[page] = True
    # Return the total number of page faults.
    return page_faults

# Defines the Optimal page replacement algorithm.
def optimal(reference_string, num_frames):
    """Optimal Page Replacement Algorithm"""
    # Use a list to store the frames.
    frames = []
    # Use a set for fast checking of whether a page is currently in a frame.
    page_set = set()
    # Initialize the count of page faults to zero.
    page_faults = 0

    # Loop through each page and its index in the reference string.
    for i, page in enumerate(reference_string):
        # Check if the current page is NOT in memory (a page fault).
        if page not in page_set:
            # If it's a fault, increase the counter.
            page_faults += 1
            # If the frames are already full...
            if len(frames) == num_frames:
                # ...we need to find the best page to replace.
                farthest_next_use = -1
                victim_page = -1
                victim_idx = -1
                # Look at each page currently in the frames.
                for frame_idx, frame_page in enumerate(frames):
                    try:
                        # Find the next time this frame_page will be used by searching the rest of the reference_string.
                        next_use = reference_string[i+1:].index(frame_page) + i + 1
                        # If this page is used further in the future than the current "farthest" page, it becomes the new candidate for replacement.
                        if next_use > farthest_next_use:
                            farthest_next_use = next_use
                            victim_page = frame_page
                            victim_idx = frame_idx
                    # This error means the page is never used again in the reference string.
                    except ValueError:
                        # If a page is never used again, it's the perfect one to replace.
                        victim_page = frame_page
                        victim_idx = frame_idx
                        # Break the inner loop because we've found the best victim.
                        break
                # If a victim page was chosen...
                if victim_page != -1:
                    # ...remove it from the frames list and the set.
                    frames.pop(victim_idx)
                    page_set.remove(victim_page)
            # Add the new page to the frames.
            frames.append(page)
            page_set.add(page)
    # Return the total number of page faults.
    return page_faults

# Defines the Clock (also called Second-Chance) page replacement algorithm.
def clock(reference_string, num_frames):
    """Clock (Second-Chance) Page Replacement Algorithm"""
    # Create the frames, initialized to None.
    frames = [None] * num_frames
    # Create a parallel list for the reference bits, all start at 0.
    ref_bits = [0] * num_frames
    # The "hand" of the clock, which points to the next frame to check.
    hand = 0
    # A map to quickly find a page's index in the frames.
    page_to_frame = {}
    # Initialize the count of page faults to zero.
    page_faults = 0

    # Loop through each page in the user-provided reference string.
    for page in reference_string:
        # Check if the page is already in memory (a page hit).
        if page in page_to_frame:
            # If it's a hit, set its reference bit to 1, giving it a "second chance".
            ref_bits[page_to_frame[page]] = 1
        # This block executes if the page is NOT in memory (a page fault).
        else:
            # If it's a fault, increase the counter.
            page_faults += 1
            # Start the clock algorithm to find a victim frame.
            while True:
                # If the frame the hand is pointing to is empty, we can use it.
                if frames[hand] is None:
                    victim_idx = hand
                    break
                # If the reference bit is 0, we've found our victim.
                if ref_bits[hand] == 0:
                    victim_idx = hand
                    break
                # If the reference bit is 1, give it a second chance by setting the bit to 0.
                ref_bits[hand] = 0
                # Move the clock hand to the next frame (and wrap around if necessary).
                hand = (hand + 1) % num_frames
            # If the victim frame we chose was not empty...
            if frames[victim_idx] is not None:
                # ...remove the old page from our map.
                del page_to_frame[frames[victim_idx]]
            # Place the new page into the victim frame.
            frames[victim_idx] = page
            # Set the new page's reference bit to 1.
            ref_bits[victim_idx] = 1
            # Add the new page and its frame index to the map.
            page_to_frame[page] = victim_idx
            # Move the hand to the next position for the next fault.
            hand = (victim_idx + 1) % num_frames
    # Return the total number of page faults.
    return page_faults

# --- User Input Section ---

# Function to get the required inputs from the user.
def get_user_input():
    print("=== Virtual Memory Page Replacement Simulation ===\n")
    # Ask the user for the total number of pages in their reference string.
    n = int(input("Enter number of pages: "))
    # Ask the user to enter the page numbers.
    print(f"Enter {n} page numbers (space-separated): ", end="")
    ref_string = list(map(int, input().split()))
    # Validate that the user entered the correct number of pages.
    while len(ref_string) != n:
        print(f"Please enter exactly {n} numbers: ", end="")
        ref_string = list(map(int, input().split()))
    # Ask the user for the number of available frames in memory.
    num_frames = int(input("Enter number of frames: "))
    # Return the reference string and number of frames.
    return ref_string, num_frames

# --- Run Simulation ---

# Function to run a single algorithm and print its results.
def run_simulation(algo_name, algo_func, ref_str, num_frames):
    # Call the algorithm function (e.g., fifo, lru) to get the number of faults.
    faults = algo_func(ref_str, num_frames)
    # Calculate the number of hits.
    hits = len(ref_str) - faults
    # Calculate the hit ratio percentage.
    hit_ratio = (hits / len(ref_str)) * 100 if len(ref_str) > 0 else 0
    # Print the results in a formatted table row.
    print(f"{algo_name:<10} | {faults:<12} | {hits:<10} | {hit_ratio:<15.2f}")
    # Return a dictionary containing the results.
    return {"name": algo_name, "faults": faults, "hit_ratio": hit_ratio}

# --- Belady's Anomaly Detection ---

# A special function to test for Belady's Anomaly using the FIFO algorithm.
def test_belady(ref_str):
    print("\n--- Demonstrating Belady's Anomaly with FIFO ---")
    # Calculate page faults for FIFO with 3 frames.
    f3 = fifo(ref_str, 3)
    # Calculate page faults for FIFO with 4 frames.
    f4 = fifo(ref_str, 4)
    # Print the results.
    print(f"FIFO (3 Frames): {f3} page faults")
    print(f"FIFO (4 Frames): {f4} page faults")
    # Check if the faults increased when the number of frames increased.
    if f4 > f3:
        print("Belady's Anomaly Demonstrated: Faults increased with more frames!")
    else:
        print("Belady's Anomaly not observed in this case.")

# --- Main Execution ---

# This standard Python construct ensures the code inside only runs when the script is executed directly.
if __name__ == "__main__":
    # Get the reference string and number of frames from the user.
    ref_string, num_frames = get_user_input()

    # Print the header for the results table.
    print("\n--- Summary of Results ---")
    print("-" * 50)
    print(f"{'Algorithm':<10} | {'Page Faults':<12} | {'Page Hits':<10} | {'Hit Ratio (%)':<15}")
    print("-" * 50)

    # A list to store the results from each simulation.
    results = []
    # Run the simulation for each of the four algorithms.
    results.append(run_simulation("FIFO", fifo, ref_string, num_frames))
    results.append(run_simulation("LRU", lru, ref_string, num_frames))
    results.append(run_simulation("Optimal", optimal, ref_string, num_frames))
    results.append(run_simulation("Clock", clock, ref_string, num_frames))

    # Print a closing line for the table.
    print("-" * 50)

    # Run the special test for Belady's Anomaly.
    test_belady(ref_string)
#1 2 3 4 1 2 5 1 2 3 4 5
