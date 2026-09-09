class BSPNode:
    """Binary Space Partitioning tree node for 2D line hyperplanes."""
    def __init__(self, partition_segment: tuple[tuple[float, float], tuple[float, float]] = None):
        self.partition = partition_segment
        self.front = None
        self.back = None

    def classify_point(self, pt: tuple[float, float]) -> int:
        if not self.partition:
            return 0
        (x1, y1), (x2, y2) = self.partition
        # Cross product (x2 - x1)*(py - y1) - (y2 - y1)*(px - x1)
        cross = (x2 - x1) * (pt[1] - y1) - (y2 - y1) * (pt[0] - x1)
        if abs(cross) < 1e-7:
            return 0 # ON line
        return 1 if cross > 0 else -1 # FRONT vs BACK

    def build_tree(self, segments: list[tuple[tuple[float, float], tuple[float, float]]]):
        if not segments:
            return
        self.partition = segments[0]
        front_segments = []
        back_segments = []

        for seg in segments[1:]:
            p1_side = self.classify_point(seg[0])
            p2_side = self.classify_point(seg[1])

            if p1_side >= 0 and p2_side >= 0:
                front_segments.append(seg)
            else:
                back_segments.append(seg)

        if front_segments:
            self.front = BSPNode()
            self.front.build_tree(front_segments)
        if back_segments:
            self.back = BSPNode()
            self.back.build_tree(back_segments)

    def depth_order(self, eye: tuple[float, float]) -> list:
        """Returns segments in back-to-front painter's order relative to eye position."""
        if not self.partition:
            return []
        side = self.classify_point(eye)
        order = []
        if side >= 0:
            if self.back: order.extend(self.back.depth_order(eye))
            order.append(self.partition)
            if self.front: order.extend(self.front.depth_order(eye))
        else:
            if self.front: order.extend(self.front.depth_order(eye))
            order.append(self.partition)
            if self.back: order.extend(self.back.depth_order(eye))
        return order
