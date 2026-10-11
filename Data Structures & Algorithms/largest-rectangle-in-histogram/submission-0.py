class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        # Monotonic stack: heights in the stack are always non-decreasing from bottom to top.
        # Each entry is (start_index, height): the rectangle of this height can extend
        # LEFT back to start_index, and keeps extending right until a shorter bar shows up.
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            # By default, a rectangle of height h starts at the current index
            start = i

            # If the bar on top of the stack is TALLER than the current bar,
            # that taller rectangle can't extend past index i (the current bar blocks it).
            # So it's "finished": pop it and compute its area.
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Width = from where it started (index) up to, but not including, i
                maxArea = max(maxArea, height * (i - index))
                # Key trick: since the popped bar was taller than h, a rectangle of
                # height h can extend back to where the popped bar started.
                start = index

            # Push the current bar with its (possibly extended-left) start index
            stack.append((start, h))

        # Whatever is left in the stack never hit a shorter bar on its right,
        # so each of these rectangles extends all the way to the end of the array.
        for i, h in stack:
            # Width = from its start index to the end of the array
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea