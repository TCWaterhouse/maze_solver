from graphics import Window, Point, Line


def main():
    win = Window(800, 600)

    start = Point(0, 0)
    middle = Point(200, 200)
    end = Point(400, 400)


    test_line = Line(start, middle)
    test_line_2 = Line(middle, end)

    win.draw_line(test_line, "black")
    win.draw_line(test_line_2, "red")

    win.wait_for_close()


main()
