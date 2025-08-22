from page_replacement import PageReplacementSimulator

pages = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
frame_capacity = 4

sim = PageReplacementSimulator(frame_capacity)

print("RAM Page Replacement Results")
print("--------------------------------")
print("Page sequence:", pages)
print("Frame capacity:", frame_capacity)
print()
print("   FIFO page faults:", sim.fifo(pages))
print("    LRU page faults:", sim.lru(pages))
print("Optimal page faults:", sim.optimal(pages))