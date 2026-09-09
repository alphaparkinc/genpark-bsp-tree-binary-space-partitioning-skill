from client import BSPNode

def main():
    print("=== Binary Space Partitioning (BSP) Tree ===")
    bsp = BSPNode()
    walls = [
        ((0, 0), (10, 0)),
        ((0, 5), (10, 5)),
        ((0, -5), (10, -5))
    ]
    bsp.build_tree(walls)

    eye = (5, 10)
    order = bsp.depth_order(eye)
    print("Painter's Render Order (Back to Front):", order)
    assert len(order) == 3

    print("BSP Tree Engine verified successfully!")

if __name__ == "__main__":
    main()
