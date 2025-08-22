"""RAM Page Replacement Algorithms Toolkit

Provides FIFO, LRU, and Optimal page replacement algorithms for educational and simulation use.

Usage:
    from page_replacement import PageReplacementSimulator
    sim = PageReplacementSimulator(frame_count)
    faults = sim.fifo(page_sequence)
"""

from collections import deque

class PageReplacementSimulator:
    def __init__(self, capacity):
        """
        Initialize the simulator with a number of page frames.

        Args:
            capacity (int): Number of frames in RAM.
        """
        self.capacity = capacity

    def fifo(self, pages):
        """
        FIFO (First-In-First-Out) page replacement algorithm.

        Args:
            pages (list): Sequence of page requests.

        Returns:
            int: Number of page faults.
        """
        memory = deque()
        faults = 0
        for page in pages:
            if page not in memory:
                faults += 1
                if len(memory) == self.capacity:
                    memory.popleft()
                memory.append(page)
        return faults

    def lru(self, pages):
        """
        LRU (Least Recently Used) page replacement algorithm.

        Args:
            pages (list): Sequence of page requests.

        Returns:
            int: Number of page faults.
        """
        memory = []
        faults = 0
        for page in pages:
            if page not in memory:
                faults += 1
                if len(memory) == self.capacity:
                    memory.pop(0)
                memory.append(page)
            else:
                memory.remove(page)
                memory.append(page)
        return faults

    def optimal(self, pages):
        """
        Optimal page replacement algorithm.

        Args:
            pages (list): Sequence of page requests.

        Returns:
            int: Number of page faults.
        """
        memory = []
        faults = 0
        for i, page in enumerate(pages):
            if page not in memory:
                faults += 1
                if len(memory) == self.capacity:
                    future = pages[i + 1:]
                    next_use = [
                        future.index(m) if m in future else float('inf')
                        for m in memory
                    ]
                    idx_to_replace = next_use.index(max(next_use))
                    memory.pop(idx_to_replace)
                memory.append(page)
        return faults
